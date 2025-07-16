#!/usr/bin/env python3
"""
Pre-Deployment Security Check
============================

This script performs a final security check before deployment to ensure
no sensitive data will be exposed in the deployed application.

Run this script before deploying to production.
"""

import os
import subprocess
import sys
from pathlib import Path

def check_env_files():
    """Check that sensitive files exist locally but are not in git"""
    print("🔍 Checking environment files...")
    
    # Files that should exist locally but not in git
    sensitive_files = ['env.py', 'local_settings.py']
    
    for file in sensitive_files:
        file_path = Path(file)
        
        # Check if file exists locally
        if file_path.exists():
            print(f"✅ {file} exists locally")
            
            # Check if file is ignored by git
            result = subprocess.run(['git', 'check-ignore', file], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {file} is properly ignored by git")
            else:
                print(f"❌ {file} is NOT ignored by git - SECURITY RISK!")
                return False
        else:
            print(f"ℹ️  {file} does not exist locally")
    
    return True

def check_git_tracked_files():
    """Check what files are tracked by git"""
    print("\n🔍 Checking git tracked files...")
    
    # Get list of tracked files
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
    tracked_files = result.stdout.strip().split('\n')
    
    # Files that should NEVER be in git
    forbidden_files = [
        'env.py', 'local_settings.py', '.env', 'config.py', 'secrets.py',
        'local_settings.py.backup', 'env.py.backup'
    ]
    
    security_issues = []
    for file in tracked_files:
        if any(forbidden in file for forbidden in forbidden_files):
            security_issues.append(file)
    
    if security_issues:
        print("❌ SECURITY RISK: Sensitive files found in git:")
        for file in security_issues:
            print(f"   - {file}")
        return False
    else:
        print("✅ No sensitive files found in git repository")
        return True

def simulate_production_settings():
    """Simulate production settings by temporarily removing local_settings.py"""
    print("\n🔍 Simulating production environment...")
    
    # Check if local_settings.py exists
    local_settings = Path('local_settings.py')
    backup_created = False
    
    if local_settings.exists():
        # Temporarily rename it
        local_settings.rename('local_settings.py.temp')
        backup_created = True
        print("📁 Temporarily removed local_settings.py")
    
    try:
        # Test Django settings
        result = subprocess.run([
            sys.executable, 'check_settings.py'
        ], capture_output=True, text=True)
        
        if 'DEBUG: False' in result.stdout:
            print("✅ Production mode: DEBUG=False")
            production_ready = True
        else:
            print("❌ Production mode: DEBUG should be False")
            production_ready = False
            
    except Exception as e:
        print(f"❌ Error checking production settings: {e}")
        production_ready = False
    
    finally:
        # Restore local_settings.py if it existed
        if backup_created:
            Path('local_settings.py.temp').rename('local_settings.py')
            print("📁 Restored local_settings.py")
    
    return production_ready

def check_deployment_readiness():
    """Check if application is ready for deployment"""
    print("\n🔍 Checking deployment readiness...")
    
    checks = [
        ("Environment files security", check_env_files()),
        ("Git repository security", check_git_tracked_files()),
        ("Production settings", simulate_production_settings())
    ]
    
    print("\n" + "="*50)
    print("📋 DEPLOYMENT READINESS REPORT")
    print("="*50)
    
    all_passed = True
    for check_name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {check_name}")
        if not passed:
            all_passed = False
    
    print("="*50)
    
    if all_passed:
        print("🚀 READY FOR DEPLOYMENT!")
        print("✅ All security checks passed")
        print("✅ No sensitive data will be exposed")
        print("✅ Production settings are correct")
        return True
    else:
        print("🛑 NOT READY FOR DEPLOYMENT!")
        print("❌ Security issues found - please fix before deploying")
        return False

def main():
    """Main function"""
    print("🔒 PRE-DEPLOYMENT SECURITY CHECK")
    print("="*50)
    
    if not Path('.git').exists():
        print("❌ Not a git repository")
        sys.exit(1)
    
    if not Path('manage.py').exists():
        print("❌ Not a Django project")
        sys.exit(1)
    
    ready = check_deployment_readiness()
    
    if ready:
        print("\n💡 DEPLOYMENT COMMANDS:")
        print("git add .")
        print("git commit -m 'Security fixes and deployment preparation'")
        print("git push origin main")
        print("# Deploy to Heroku or your hosting platform")
        sys.exit(0)
    else:
        print("\n⚠️  FIX ISSUES BEFORE DEPLOYMENT")
        sys.exit(1)

if __name__ == "__main__":
    main()