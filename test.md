# Test Results 2.1 Profile Creation
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Create Basic Profile | 1. Navigate to profile creation<br>2. Fill mandatory fields:<br>   - Name<br>   - Description<br>   - Specialty<br>3. Upload profile image<br>4. Submit | • Profile created successfully<br>• Redirect to profile view<br>• Success message displayed | pass |
| Social Media Links | 1. Add valid social media URLs:<br>   - YouTube<br>   - Instagram<br>   - Facebook<br>2. Save profile | • Links saved correctly<br>• Links open in new tab<br>• Valid URLs validated |  pass|

### 2.2 Profile Editing
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Update Profile Info | 1. Navigate to edit profile<br>2. Modify fields<br>3. Save changes | • Changes saved successfully<br>• Updated info displayed correctly | pass |
| Change Profile Image | 1. Click change image<br>2. Upload new image<br>3. Save | • New image uploaded<br>• Old image replaced<br>• Image displayed correctly | pass |

## 3. Dish Management

### 3.1 Dish Creation
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Add New Dish | 1. Navigate to dish creation<br>2. Enter:<br>   - Name<br>   - Description<br>   - Category<br>3. Upload image<br>4. Submit | • Dish created successfully<br>• Appears in menu listing<br>• Success message displayed | pass |
| Required Fields | 1. Submit without required fields | • Form validation errors<br>• Clear error messages<br>• Form not submitted | pass |

### 3.2 Dish Management
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Edit Dish | 1. Select dish to edit<br>2. Modify fields<br>3. Save changes | • Changes saved successfully<br>• Updated in menu listing | pass |
| Delete Dish | 1. Select dish to delete<br>2. Confirm deletion | • Dish removed from listing<br>• Success message displayed | pass |

## 4. Review System

### 4.1 Comment Management
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Add Comment | 1. Navigate to chef profile<br>2. Enter comment<br>3. Select rating<br>4. Submit | • Comment pending approval<br>• Success message displayed |  pass|
| Admin Approval | 1. Login as admin<br>2. View pending comments<br>3. Approve/reject | • Comment status updated<br>• Appears/hidden on profile |  pass|

## 5. Menu Management

### 5.1 Menu Operations
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Create Menu Item | 1. Add new menu item<br>2. Fill all fields<br>3. Select category<br>4. Submit | • Item created successfully<br>• Appears in correct category | pass |
| Category Display | 1. View menu page<br>2. Check category sections | • Items grouped by category<br>• Correct sorting/display |  pass|

## 6. Collaboration Requests

### 6.1 Request Submission
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Submit Request | 1. Fill contact form<br>2. Submit request | • Request stored in database<br>• Confirmation message shown | pass|
| Admin View | 1. Login as admin<br>2. Check requests panel | • All requests listed<br>• Details correctly displayed | pass |

## 7. Navigation Testing

### 7.1 Navbar Functionality
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Guest View | 1. Access site as guest<br>2. Check navbar options | • Show: Home, Login, Register<br>• Hide: Profile, Admin | pass |
| Logged-in View | 1. Login<br>2. Check navbar options | • Show: Profile, Logout<br>• Hide: Login, Register | pass|

## Browser Compatibility
Test on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS/Android)

## Testing Notes
- Test both positive and negative scenarios
- Verify all success/error messages
- Check responsive design on different screen sizes
- Test with different user roles (Guest, User, Chef, Admin)
- Document any unexpected behavior


