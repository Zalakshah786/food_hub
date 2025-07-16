#!/usr/bin/env python3
"""
Script to verify Django settings configuration
Run this to check if DEBUG and security settings are correct
"""

import os
import sys
import django
from pathlib import Path

# Add the project root to the Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from django.conf import settings

def check_settings():
    print("=== Django Settings Check ===")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    if settings.DEBUG:
        print("⚠️  WARNING: DEBUG is True - This should be False for production!")
        print("   For local development, this is OK")
        print("   For production deployment, ensure DEBUG=False")
    else:
        print("✅ DEBUG is False - Good for production")
        print("   Security settings are active:")
        print(f"   - SECURE_SSL_REDIRECT: {getattr(settings, 'SECURE_SSL_REDIRECT', 'Not set')}")
        print(f"   - SECURE_HSTS_SECONDS: {getattr(settings, 'SECURE_HSTS_SECONDS', 'Not set')}")
        print(f"   - SESSION_COOKIE_SECURE: {getattr(settings, 'SESSION_COOKIE_SECURE', 'Not set')}")
        print(f"   - CSRF_COOKIE_SECURE: {getattr(settings, 'CSRF_COOKIE_SECURE', 'Not set')}")
    
    print(f"\nSECRET_KEY: {'Set' if settings.SECRET_KEY else 'Not set'}")
    print(f"DATABASE_URL: {'Set' if os.getenv('DATABASE_URL') else 'Not set'}")
    
    # Check for local_settings.py
    local_settings_path = BASE_DIR / 'local_settings.py'
    if local_settings_path.exists():
        print("\n📝 local_settings.py found - Development mode detected")
        print("   This file should NOT be committed to git")
        print("   It's used for local development only")
    else:
        print("\n📁 local_settings.py not found - Production mode")
        print("   This is normal for production deployment")
    
    print("\n=== Environment Variables ===")
    debug_env = os.getenv('DEBUG', 'Not set')
    print(f"DEBUG environment variable: {debug_env}")
    
    if debug_env.lower() == 'true' and not settings.DEBUG:
        print("⚠️  Note: DEBUG env var is True but settings.DEBUG is False")
        print("   This might indicate an issue with settings loading")

if __name__ == "__main__":
    check_settings()