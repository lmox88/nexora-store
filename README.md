🛍️ Nexora Store
Nexora Store is a modern, full-stack Django e-commerce web application. The platform provides a seamless shopping experience, including product browsing, shopping cart management, secure checkout, and automated email notifications.

🔗 Live Demo
You can visit the live version of the project here:
👉 Click here to visit Nexora Store (Note: Please use the test credentials below for demo purposes)

📧 Email Verification Proof
The system uses Mailtrap for email testing. Below is the screenshots :

verification email for registration:
<img width="1905" height="862" alt="لقطة شاشة 2026-06-13 083200" src="https://github.com/user-attachments/assets/44390dd0-9430-4fc5-89a1-b6db97687807" />

verification email for order completion:
<img width="1911" height="857" alt="لقطة شاشة 2026-06-13 085048" src="https://github.com/user-attachments/assets/959e98c0-fb72-4ca6-84b0-6e537c18b396" />

🚀 Features
🔐 User Authentication: Secure registration, login, and email verification.

🛒 Shopping Cart: Session-based cart for a smooth shopping experience.

💳 Stripe Integration: Secure payment processing (Test Mode).

📦 Order Management: Automated order creation and history tracking.

📧 Notification System: Automated emails for verification and order confirmation.

👤 User Dashboard: Profile management and order history tracking.

🛠 Tech Stack
Framework: Django (Python)

Database: PostgreSQL (on Render)

Media Storage: Cloudinary

Payment Gateway: Stripe API (Test Mode)

Email Testing: Mailtrap (SMTP Sandbox)

Deployment: Render & WhiteNoise

🔑 Demo Accounts
👤 Test User
Username: testuser

Password: test123456

💳 Stripe Test Card
Card Number: 4242 4242 4242 4242

Expiry: 12/30

CVC: 123

📦 Project Structure
accounts: User registration, login, and email verification logic.

products: Product catalog and browsing functionality.

cart: Shopping cart management using session data.

orders: Order processing and history tracking.

🔐 Security & Deployment
Environment Variables: All sensitive keys (Stripe, Cloudinary, Email) are secured using .env files.

Static Files: Compressed and served using WhiteNoise.

Media Hosting: Files are stored in the cloud using Cloudinary.

👨‍💻 Author
Developed by: Laila Albusayr
