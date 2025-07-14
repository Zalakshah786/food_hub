from django.core.management.utils import get_random_secret_key

# Generate a new secret key for production
production_secret_key = get_random_secret_key()
print("=== PRODUCTION SECRET KEY ===")
print(production_secret_key)
print("=== COPY THIS TO HEROKU CONFIG VARS ===")