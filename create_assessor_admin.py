#!/usr/bin/env python3
"""
Create Admin User for Assessors
===============================

This script creates a dedicated admin user account for assessors to test the application.
Run this script to ensure assessors have proper admin access.
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

from django.contrib.auth.models import User
from django.core.management.utils import get_random_secret_key

def create_assessor_admin():
    """Create admin user for assessors"""
    
    # Admin credentials for assessors
    admin_username = 'assessor'
    admin_password = 'assessor123'
    admin_email = 'assessor@foodhub.com'
    
    # Check if admin user already exists
    if User.objects.filter(username=admin_username).exists():
        print(f"✅ Admin user '{admin_username}' already exists")
        admin_user = User.objects.get(username=admin_username)
        
        # Update password in case it was changed
        admin_user.set_password(admin_password)
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print(f"✅ Admin password updated for '{admin_username}'")
    else:
        # Create new admin user
        admin_user = User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        print(f"✅ Created new admin user: '{admin_username}'")
    
    return admin_user

def create_test_users():
    """Create test users for assessors"""
    
    test_users = [
        {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        },
        {
            'username': 'demouser',
            'password': 'demopass123',
            'email': 'demouser@example.com',
            'first_name': 'Demo',
            'last_name': 'User'
        }
    ]
    
    for user_data in test_users:
        username = user_data['username']
        
        if User.objects.filter(username=username).exists():
            print(f"✅ Test user '{username}' already exists")
            user = User.objects.get(username=username)
            
            # Update password and details
            user.set_password(user_data['password'])
            user.email = user_data['email']
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            user.save()
            print(f"✅ Updated test user '{username}'")
        else:
            user = User.objects.create_user(
                username=username,
                password=user_data['password'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            print(f"✅ Created new test user: '{username}'")

def display_credentials():
    """Display all credentials for assessors"""
    print("\n" + "="*60)
    print("🔐 ASSESSOR CREDENTIALS SUMMARY")
    print("="*60)
    
    print("\n📋 ADMIN ACCESS:")
    print("Username: assessor")
    print("Password: assessor123")
    print("URL: https://food-hub-0b5046e8acf1.herokuapp.com/admin/")
    
    print("\n👤 TEST USERS:")
    print("User 1 - Username: testuser, Password: testpass123")
    print("User 2 - Username: demouser, Password: demopass123")
    
    print("\n🌐 APPLICATION URLs:")
    print("Homepage: https://food-hub-0b5046e8acf1.herokuapp.com/")
    print("Login: https://food-hub-0b5046e8acf1.herokuapp.com/accounts/login/")
    print("Admin: https://food-hub-0b5046e8acf1.herokuapp.com/admin/")
    
    print("\n📊 DATABASE SUMMARY:")
    total_users = User.objects.count()
    superusers = User.objects.filter(is_superuser=True).count()
    regular_users = total_users - superusers
    
    print(f"Total Users: {total_users}")
    print(f"Admin Users: {superusers}")
    print(f"Regular Users: {regular_users}")
    
    print("\n✅ ALL CREDENTIALS READY FOR ASSESSMENT!")

def main():
    """Main function"""
    print("🚀 Setting up assessor credentials...")
    
    try:
        # Create admin user
        create_assessor_admin()
        
        # Create test users
        create_test_users()
        
        # Display summary
        display_credentials()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎯 Ready for assessment submission!")
    else:
        print("\n❌ Please fix errors before submission")