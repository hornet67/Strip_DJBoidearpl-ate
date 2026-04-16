#### Django Boilerplate with Stripe Subscriptions   ####

I build(trying to) a django boilerplate with stripe for the purpose of helping fellow developer to intregate them without any hassel and problem.

#### Features  ####

- ✅ User authentication (email + password)
- ✅ Google OAuth login
- ✅ Stripe subscription payments (monthly)
- ✅ Webhook for automatic premium activation
- ✅ Premium content restriction
- ✅ User dashboard with subscription status
- ✅ Pricing page (Free vs Premium)
- ✅ Responsive design with Tailwind CSS

#### Prerequisites ####

- Python 3.10 or higher
- Stripe account (free)
- Google Cloud account (for OAuth)

*** if anyone dont know how to create stripe account free or create google cloud account the guideline will be shared below after the whole cocumentation  ***

#### Installation  ####

1. **Clone the repository**
  
   git clone https://github.com/hornet67/Strip_DJBoidearpl-ate.git
   cd Strip_DJBoidearpl-ate

2. **create virtual env and installation of dependencys**

    python -m venv venv
    source venv/bin/activate  

    pip install -r req.txt

3. **Secret key**

    create a file named local_settings.py in your project folder and add your STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY in their.For example

    STRIPE_PUBLISHABLE_KEY = 'pk_tes*************************************************************************************************'
    STRIPE_SECRET_KEY = ' sk_tes*****************************************************************************************************' 

    *** you can get your both key and seret key from your stripe account dashboard (creating of stripe account and will be shown at later part of the project) ***

4. **running of the project**

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver



5. **Testing Payments**
    
    Use Stripe test cards (no real money):

    Card Number	Purpose
    4242 4242 4242 4242	          Successful payment
    4000 0025 0000 3155	3D        Secure authentication
    4000 0000 0000 9995           Declined (insufficient funds)
    
    Use any future expiry date (e.g., 12/34) and any CVC (e.g., 123).



#### pROJECT STRUCTURE ####

            djangoBoilerplate/
            ├── core/                  # Project settings
            ├── accounts/              # User authentication
            ├── payments/              # Stripe integration
            ├── templates/             # HTML templates
            │   ├── base.html
            │   ├── dashboard.html
            │   ├── premium_content.html
            │   └── payments/
            │       ├── pricing.html
            │       ├── success.html
            │       └── error.html
            ├── local_settings.py      # Your secrets (gitignored)
            ├── manage.py
            └── req.txt



#### Common Windows Issues & Solutions ####


    Issue	Solution
    'python' is not recognized	     Reinstall Python and check "Add Python to PATH"
    venv\Scripts\activate  fails	 Run Set-ExecutionPolicy Unrestricted -Scope Process in PowerShell
    Port 8000 already in use	     Run python manage.py runserver 8001

    Migrations fail	Delete db.sqlite3 and run python manage.py migrate again




