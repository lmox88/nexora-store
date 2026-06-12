# 🛍️ SoftPalm Store

A full-stack Django e-commerce web application built as part of a technical assessment.  
The platform allows users to browse products, manage a cart, complete payments via Stripe (test mode), and receive automated email notifications.

---

## 🚀 Features

- 🔐 User authentication (Register / Login / Logout)
- 📧 Email verification after registration
- 🛒 Session-based shopping cart
- 💳 Stripe payment integration (Test Mode)
- 📦 Order creation after payment
- 📧 Order confirmation email after successful purchase
- 👤 User profile with order history
- 🧾 Order detail tracking

---

## 🏗️ Tech Stack

- Django (Python)
- SQLite
- HTML / CSS / Bootstrap
- Stripe API
- SMTP Email (Gmail)
- Git & GitHub

---

## 🔑 Demo Accounts

### 👤 Test User
- **Username:** testuser  
- **Password:** test123456  

### 💳 Stripe Test Card
- **Card Number:** 4242 4242 4242 4242  
- **Expiry:** Any future date  
- **CVC:** Any 3 digits  

### 📧 Email System
- Email verification sent after registration  
- Order confirmation sent after successful payment  

---

## 📦 Project Apps

- **accounts** → authentication + email verification  
- **products** → product catalog  
- **cart** → shopping cart (session-based)  
- **orders** → order management  
- **payments** → Stripe integration  

---

## 🔐 Security Notes

- Secret keys stored in `.env` (not pushed to GitHub)  
- Stripe runs in Test Mode  
- CSRF protection enabled  
- Login required for checkout  

---

## 👨‍💻 Project Purpose

Built for a technical assessment focusing on:

- Authentication system  
- Secure checkout flow  
- Payment integration  
- Order management system  
- Real-world e-commerce architecture  

---

## 📌 Author

**Developed by:** Laila Albusayr
