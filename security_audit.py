#!/usr/bin/env python3
"""
Security Audit Script for Django Project
=========================================

This script checks for potential security issues in your Django project
before committing to git or deploying to production.

Run this script before every commit to ensure no sensitive data is exposed.
"""

import os
import subprocess
import sys
import re
from pathlib import Path

def run_command(cmd):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return "", str(e)

def check_git_status():
    """Check what files are being tracked by git"""
    print("🔍 Checking git status...")
    
    # Check if sensitive files are tracked
    sensitive_patterns = [
        'env.py',
        'local_settings.py',
        '.env',
        'config.py',
        'secrets.py'
    ]
    
    stdout, stderr = run_command('git ls-files')
    tracked_files = stdout.split('\n') if stdout else []
    
    issues = []
    for pattern in sensitive_patterns:
        matching_files = [f for f in tracked_files if pattern in f]
        if matching_files:
            issues.append(f"❌ Sensitive file tracked by git: {matching_files}")
    
    return issues

def check_hardcoded_secrets():
    """Check for hardcoded secrets in Python files"""
    print("🔍 Checking for hardcoded secrets...")
    
    issues = []
    
    # Patterns to look for
    secret_patterns = [
        (r'SECRET_KEY\s*=\s*["\'][^"\']+["\']', 'Hardcoded SECRET_KEY'),
        (r'django-insecure-[a-zA-Z0-9@#$%^&*()_+=-]+', 'Django insecure secret key'),
        (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
        (r'api_key\s*=\s*["\'][^"\']+["\']', 'Hardcoded API key'),
        (r'sk-[a-zA-Z0-9]+', 'Possible API key'),
    ]
    
    # Check all Python files (excluding venv, __pycache__, test files, and other directories)
    exclude_dirs = {'venv', 'env', '__pycache__', '.git', 'staticfiles', 'node_modules', 'migrations'}
    exclude_files = {'test_', 'tests.py', 'test.py', 'env.py', 'local_settings.py', 'conftest.py'}
    
    for py_file in Path('.').rglob('*.py'):
        # Skip if file is in excluded directories
        if any(excluded in str(py_file) for excluded in exclude_dirs):
            continue
            
        # Skip if file is a test file or ignored file
        if any(excluded in str(py_file) for excluded in exclude_files):
            continue
            
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern, description in secret_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    issues.append(f"❌ {description} found in {py_file}")
        except Exception as e:
            continue
    
    return issues

def check_debug_setting():
    """Check if DEBUG is properly configured"""
    print("🔍 Checking DEBUG setting...")
    
    issues = []
    
    # Check settings.py for hardcoded DEBUG=True
    settings_file = Path('my_project/settings.py')
    if settings_file.exists():
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for hardcoded DEBUG=True (not using environment variables)
            if re.search(r'DEBUG\s*=\s*True\s*(?!.*getenv|.*environ)', content):
                issues.append("❌ Hardcoded DEBUG=True found in settings.py")
        except Exception as e:
            issues.append(f"❌ Could not read settings.py: {e}")
    
    return issues

def check_gitignore():
    """Check if .gitignore includes all sensitive files"""
    print("🔍 Checking .gitignore...")
    
    issues = []
    required_entries = [
        'env.py',
        'local_settings.py',
        '.env',
        '*.log',
        '__pycache__/',
        'db.sqlite3'
    ]
    
    gitignore_file = Path('.gitignore')
    if not gitignore_file.exists():
        issues.append("❌ .gitignore file not found")
        return issues
    
    try:
        with open(gitignore_file, 'r', encoding='utf-8') as f:
            gitignore_content = f.read()
            
        for entry in required_entries:
            if entry not in gitignore_content:
                issues.append(f"❌ {entry} not in .gitignore")
    except Exception as e:
        issues.append(f"❌ Could not read .gitignore: {e}")
    
    return issues

def main():
    """Main security audit function"""
    print("🔒 SECURITY AUDIT STARTING...")
    print("=" * 50)
    
    all_issues = []
    
    # Run all checks
    all_issues.extend(check_git_status())
    all_issues.extend(check_hardcoded_secrets())
    all_issues.extend(check_debug_setting())
    all_issues.extend(check_gitignore())
    
    print("\n" + "=" * 50)
    print("🔒 SECURITY AUDIT RESULTS")
    print("=" * 50)
    
    if all_issues:
        print("❌ SECURITY ISSUES FOUND:")
        for issue in all_issues:
            print(f"  {issue}")
        print("\n⚠️  PLEASE FIX THESE ISSUES BEFORE DEPLOYMENT!")
        sys.exit(1)
    else:
        print("✅ NO SECURITY ISSUES FOUND!")
        print("✅ Safe to commit and deploy")
        
    print("\n💡 RECOMMENDATIONS:")
    print("  - Run this script before every commit")
    print("  - Use environment variables for all sensitive data")
    print("  - Never commit env.py or local_settings.py")
    print("  - Set DEBUG=False in production")
    print("  - Use different credentials for dev/prod")

if __name__ == "__main__":
    main()