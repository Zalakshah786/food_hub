# Assessor Testing Credentials & Information

## 🔐 ADMIN/SUPERUSER CREDENTIALS

### Django Admin Panel Access
- **URL**: [https://food-hub-0b5046e8acf1.herokuapp.com/admin/](https://food-hub-0b5046e8acf1.herokuapp.com/admin/)
- **Username**: `assessor`
- **Password**: `assessor123`

### Alternative Admin Accounts (if needed):
- **Username**: `zalak` (original developer account)
- **Username**: `test` (testing account)
- **Username**: `shah` (backup admin account)

### Admin Panel Features Available:
- ✅ **User Management**: View/edit registered users
- ✅ **Post Management**: Create/edit/delete chef posts
- ✅ **Comment Moderation**: Approve/reject user comments
- ✅ **Dish Management**: Add/edit recipe dishes
- ✅ **Menu Management**: Manage restaurant menu items
- ✅ **Collaboration Requests**: View user collaboration requests

## 👤 TEST USER ACCOUNTS

### Regular User Account #1
- **Username**: `testuser`
- **Password**: `testpass123`
- **Email**: `testuser@example.com`
- **Purpose**: Testing comment functionality, user authentication

### Regular User Account #2
- **Username**: `demouser`
- **Password**: `demopass123`
- **Email**: `demouser@example.com`
- **Purpose**: Testing multi-user interactions

## 🧪 TESTING SCENARIOS FOR ASSESSORS

### 1. Authentication Testing
```
Login URL: https://food-hub-0b5046e8acf1.herokuapp.com/accounts/login/
Register URL: https://food-hub-0b5046e8acf1.herokuapp.com/accounts/signup/
```

**Test Cases:**
- ✅ Login with admin credentials
- ✅ Login with regular user credentials
- ✅ Register new user account
- ✅ Logout functionality
- ✅ Access restrictions (try accessing admin without login)

### 2. Comment System Testing
**Steps to test:**
1. Navigate to any chef's profile page
2. Try commenting without login (should prompt for login)
3. Login with `testuser` credentials
4. Add a comment with rating (1-5 stars)
5. Login as admin and approve the comment
6. Edit the comment as testuser (should require re-approval)
7. Delete the comment (should show confirmation dialog)

### 3. Admin Panel Testing
**Login as admin and test:**
1. **Comments Moderation**: `/admin/foodhub/chef_comment/`
   - View pending comments
   - Approve/reject comments
   - Bulk actions

2. **User Management**: `/admin/auth/user/`
   - View registered users
   - Edit user permissions
   - Deactivate users

3. **Content Management**: `/admin/foodhub/post/`
   - Create new chef posts
   - Edit existing posts
   - Change post status (draft/published)

### 4. Security Testing
**Verify these security measures:**
- ✅ DEBUG=False in production (no debug information on errors)
- ✅ HTTPS redirect working
- ✅ CSRF protection active
- ✅ User ownership verification (users can only edit their own comments)
- ✅ Admin-only access to sensitive areas

## 📱 RESPONSIVE TESTING

### Test on Different Devices:
- **Desktop**: Full functionality
- **Tablet**: Responsive layout
- **Mobile**: Touch-friendly interface

### Key Pages to Test:
1. **Homepage**: `https://food-hub-0b5046e8acf1.herokuapp.com/`
2. **Chef Profile**: Click on any chef image
3. **Dish Details**: Click on any dish
4. **Menu List**: Navigation → Recipes
5. **Login Page**: `/accounts/login/`
6. **Admin Panel**: `/admin/`

## 🔍 FUNCTIONALITY CHECKLIST

### Core Features to Verify:
- [ ] **User Registration/Login**: Working correctly
- [ ] **Comment System**: Add, edit, delete with proper permissions
- [ ] **Rating System**: 1-5 star ratings functional
- [ ] **Admin Approval**: Comments require approval after editing
- [ ] **Social Media Links**: Links to chef social profiles
- [ ] **Responsive Design**: Works on all device sizes
- [ ] **Search/Navigation**: Easy to find content
- [ ] **Security**: No sensitive data exposed

### Database Content Available:
- ✅ **3 Chef Profiles** with social media links
- ✅ **Multiple Dishes** with detailed recipes
- ✅ **Menu Items** categorized by meal type
- ✅ **Sample Comments** for testing
- ✅ **User Accounts** pre-configured

## 🚨 IMPORTANT SECURITY NOTES

### What You Should NOT See:
- ❌ Django debug pages (DEBUG=False in production)
- ❌ Database credentials in source code
- ❌ Secret keys in repository
- ❌ Stack traces on errors

### What You SHOULD See:
- ✅ Custom error pages (404, 500)
- ✅ HTTPS redirection
- ✅ Secure headers in browser dev tools
- ✅ User authentication required for restricted actions

## 📞 ASSESSMENT SUPPORT

### If You Encounter Issues:
1. **Login Problems**: Try the credentials exactly as provided
2. **Admin Access**: Ensure you're using `/admin/` URL
3. **Comments Not Showing**: Check if they need admin approval
4. **Security Questions**: Refer to SECURITY_COMPLIANCE.md

### Quick Testing Commands:
```bash
# To verify DEBUG=False in production
curl -I https://food-hub-0b5046e8acf1.herokuapp.com/

# Should show secure headers and no debug info
```

## 📋 ASSESSMENT CRITERIA VERIFICATION

### LO2 - Data Model & Business Logic
- ✅ Comment system with user ownership
- ✅ Rating system (1-5 stars)
- ✅ Admin approval workflow
- ✅ CRUD operations for authorized users

### LO3 - Authentication & Authorization
- ✅ Clear difference between visitors and logged-in users
- ✅ User registration and login
- ✅ Admin panel access restricted
- ✅ Comment edit/delete restricted to owners

### LO6 - Security & Deployment
- ✅ DEBUG=False in production
- ✅ HTTPS enforcement
- ✅ No sensitive data in codebase
- ✅ Proper environment variable usage

---

**Ready for assessment!** All credentials are active and the application is fully functional for testing all required features.