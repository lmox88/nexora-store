from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings

from django.urls import reverse
from django.core.mail import send_mail
from orders.models import Order, OrderItem
stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    for product_id, qty in cart.items():

        product = Product.objects.get(id=product_id)

        items.append({
            'product': product,
            'qty': qty,
            'subtotal': product.price * qty
        })

        total += product.price * qty

    return render(request, 'cart/checkout.html', {
        'items': items,
        'total': total
    })
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('/cart/')

def cart_detail(request):
    cart = request.session.get('cart', {})

    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)

        items.append({
            'product': product,
            'qty': qty,
            'subtotal': product.price * qty
        })

        total += product.price * qty

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1

    request.session['cart'] = cart

    return redirect('cart')   # 👈 بدل products
def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')
def update_cart(request, product_id):
    cart = request.session.get('cart', {})

    qty = int(request.POST.get('qty', 1))
    cart[str(product_id)] = qty

    request.session['cart'] = cart
    return redirect('cart')




@login_required
def create_checkout_session(request):

    cart = request.session.get('cart', {})

    line_items = []

    for product_id, qty in cart.items():

        product = Product.objects.get(id=product_id)

        line_items.append({
            'price_data': {
                'currency': 'sar',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': qty,
        })

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',

        success_url=request.build_absolute_uri(
            reverse('payment_success')
        ),

        cancel_url=request.build_absolute_uri(
            reverse('checkout')
        ),
    )

    return redirect(checkout_session.url)

@login_required
def payment_success(request):

    cart = request.session.get('cart', {})

    items_text = ""
    total = 0

    # 1️⃣ إنشاء الطلب أولاً
    order = Order.objects.create(
        user=request.user,
        total=0
    )

    # 2️⃣ إنشاء المنتجات داخل الطلب
    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)

        subtotal = product.price * qty
        total += subtotal

        OrderItem.objects.create(
            order=order,
            product_name=product.name,
            price=product.price,
            quantity=qty
        )

        items_text += f"- {product.name} x {qty} = {subtotal} SAR\n"

    # 3️⃣ تحديث إجمالي الطلب
    order.total = total
    order.save()

    # 4️⃣ إرسال الإيميل
    send_mail(
        subject="🧾 Order Confirmation - Nexora",
        message=f"""
Thank you for your order 🎉

Items:
{items_text}

Total: {total} SAR

We are processing your order now.
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False,
    )

    # 5️⃣ تفريغ السلة
    request.session['cart'] = {}

    return render(request, 'cart/payment_success.html')