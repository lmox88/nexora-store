from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from products.models import Product
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from orders.models import Order

def home(request):
    products = Product.objects.exclude(id__isnull=True)

    return render(request, 'home.html', {
        'products': products
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is None:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

        if not user.is_active:
            return render(request, 'accounts/login.html', {
                'error': 'Please verify your email before login'
            })

        # ✅ نجاح
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    request.session.flush() 
    return redirect('home')


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'accounts/register.html',
                {'error': 'Username already exists'}
            )

        # User.objects.create_user(
        #     username=username,
        #     email=email,
        #     password=password
        # )
        # send_mail(
        # subject='Welcome to Sysora',
        # message='Your account was created successfully.',
        # from_email=settings.EMAIL_HOST_USER,
        # recipient_list=[email],
        # fail_silently=False,
        # )
        

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        verify_link = request.build_absolute_uri(
            reverse('verify_email', args=[uid, token])
        )

        send_mail(
            subject='Verify your email - SoftPalm',
            message=f"""
        Hi {username},

        Please verify your account:

        {verify_link}
        """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return render(request, 'accounts/verification_sent.html', {
            'email': email
        })

    return render(request, 'accounts/register.html')



def verify_email(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        return redirect('home')

    return render(request, 'invalid_token.html')
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'accounts/profile.html', {
        'orders': orders
    })