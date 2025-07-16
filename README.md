# Food Hub

<a href="https://github.com/user-attachments/assets/35397cfd-f83a-4831-b465-cbb60f10b627" target="_blank">
<img src="https://github.com/user-attachments/assets/35397cfd-f83a-4831-b465-cbb60f10b627" alt="mainpage">
</a>

## 🔐 ASSESSOR INFORMATION

### Admin Credentials:
- **Username**: `assessor`
- **Password**: `assessor123`
- **Admin Panel**: [https://food-hub-0b5046e8acf1.herokuapp.com/admin/](https://food-hub-0b5046e8acf1.herokuapp.com/admin/)

### Test User Credentials:
- **User 1**: `testuser` / `testpass123`
- **User 2**: `demouser` / `demopass123`

### 📋 Assessment Documentation:
- **Assessor Guide**: [ASSESSOR_CREDENTIALS.md](ASSESSOR_CREDENTIALS.md)
- **Security Compliance**: [SECURITY_COMPLIANCE.md](SECURITY_COMPLIANCE.md)
- **Resubmission Summary**: [RESUBMISSION_SUMMARY.md](RESUBMISSION_SUMMARY.md)

---



### Overview 
Food Hub is a web application designed to be the ultimate platform for discovering and sharing delicious Gujarati recipes. Whether you are a seasoned chef or a home cook, Food Hub provides a rich collection of authentic Gujarati recipes, cooking tips, and culinary delights to explore and enjoy.

**Purpose**
  -  The primary purpose of Food Hub is to create a community-driven platform where users can find, share, and collaborate on Gujarati recipes. The application aims to preserve and promote the rich culinary 
    heritage of Gujarat by providing a space for users to share their favorite recipes, discover new dishes, and connect with other food enthusiasts.

**Recipe Discovery:** 
  - Finding authentic Gujarati recipes can be challenging, especially for those who are not familiar with the cuisine. Food Hub solves this problem by providing a curated collection of recipes that are easy to 
   search and browse.

**Community Engagement:**

  - Many cooking enthusiasts lack a platform to share their recipes and connect with like-minded individuals. Food Hub fosters a sense of community by allowing users to submit their recipes, leave comments, and 
  rate dishes.

**Collaboration:**

  - Collaborating on recipes and cooking projects can be difficult without a dedicated platform. Food Hub offers features that enable users to collaborate with others, share cooking tips, and improve their 
   culinary skills.By joining Food Hub, users become part of a supportive community of food enthusiasts who share a passion for Gujarati cuisine. They can receive feedback on their recipes, discover new cooking 
    techniques, and build connections with other users.
    
**Value to Users**

  - Authentic Recipes: Users gain access to a wide variety of authentic Gujarati recipes, ensuring they can recreate traditional dishes with confidence.
    
**User-Friendly Interface:**

  - The application is designed with a user-friendly interface, making it easy for users to search for recipes, submit their own, and interact with the community.
    
**Conclusion**

  - Food Hub is more than just a recipe website; it is a vibrant community dedicated to celebrating and preserving the rich culinary traditions of Gujarat. By providing a platform for recipe discovery, community 
    engagement, and collaboration, Food Hub offers immense value to users who are passionate about Gujarati cuisine.
    

[Live View](https://food-hub-0b5046e8acf1.herokuapp.com/)

## Table of Contents

- [Food Hub](#food-hub)
  - [Overview](#overview)
- [UX Design Process](#ux-design-process)
  - [Logo](#logo)
  - [Color Palette](#color-palette)
  - [Typography](#typography)
  - [Wireframe](#wireframe)
  - [Design Rationale](#design-rationale)
- [Key Features](#key-features)
- [Additional Features](#additional-features)
- [Future Expansion](#future-expansion)
- [Usage Application](#usage-application)
- [Verification and Validation](#verification-and-validation)
  - [User Authentication (Login, Logout, Register)](#user-authentication-login-logout-register)
  - [Chef Profile Management](#chef-profile-management)
  - [Dish Listings Management](#dish-listings-management)
  - [Reviews and Comments on Chef's Kitchen Profile](#reviews-and-comments-on-chefs-kitchen-profile)
  - [Menu Management](#menu-management)
  - [Collaboration Requests (Contact Us Feature)](#collaboration-requests-contact-us-feature)
  - [Navbar and Page Navigation](#navbar-and-page-navigation)
- [Security Measures](#security-measures)
- [Responsive](#responsive)
- [Database](#database)
  - [Creating a Database](#creating-a-database)
- [Deployment](#deployment)
- [Validators for All HTML, CSS, JavaScript, Python Files](#validators-for-all-html-css-javascript-python-files)
- [Food Hub - Manual Testing Documentation](#food-hub---manual-testing-documentation)
  - [Testing Summary](#testing-summary)
- [AI Assistance in Development](#ai-assistance-in-development)
- [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Credits](#credits)
  - [External Libraries and Tools](#external-libraries-and-tools)
  - [Inspiration and References](#inspiration-and-references)
  - [Acknowledgements](#acknowledgements)



## UX Design Process:
**Agile Methodology**
- Agile methodology was adopted for the Food Hub project to ensure a flexible, collaborative, and iterative approach to development.
- I have used the MoSCoW technique to prioritize and complete my project requirements effectively. This technique helped me to categorize the features into Must-Have, Should-Have, and Could-Have, ensuring that the most critical functionalities were implemented first, while also considering additional enhancements for future development.
  
## MoSCoW Prioritization

### Must-Have
1. **User Authentication (Login, Logout, Register)**
   - Users must be able to register, log in, and log out.
   - Only registered users can comment and rate dishes.

2. **Recipe Discovery**
   - Users must be able to search and browse a curated collection of authentic Gujarati recipes.

3. **Chef Profile Management**
   - Chefs must be able to create, edit, and delete their profiles.
   - Profiles must include details such as name, description, specialty, and images.

4. **Dish Listings Management**
   - Chefs must be able to add, view, edit, and delete dishes.
   - Dishes must be displayed with images and categorized appropriately.

5. **Interactive Comments & Ratings System**
   - Users must be able to leave reviews and ratings for chefs.
   - Edit & Delete options must be available for authorized users.

6. **Responsive & Intuitive Layout**
   - The website must be fully responsive and adapt seamlessly across different screen sizes (desktop, tablet, mobile).

7. **Secure & User-Friendly Authentication**
   - Session-based authentication must keep users logged in while ensuring data security.

### Should-Have
1. **Collaboration Requests (Contact Us Feature)**
   - Users should be able to submit collaboration requests through a form.
   - Admins should be able to view and manage these requests in the admin panel.

2. **Menu Management**
   - Chefs should be able to create, view, edit, and delete menu items.
   - Menu items should be categorized and displayed correctly under the appropriate categories.

3. **Social Media Links**
   - Chef profiles should include social media links (YouTube, Facebook, Instagram).

4. **Accessibility Enhancements**
   - Keyboard navigation support and ARIA attributes should be implemented to ensure accessibility for all users.

### Could-Have
1. **Weekly Recipe Recommendations**
   - Offer users personalized weekly recipe recommendations based on their preferences.

2. **Place an Order for Dishes**
   - Allow users to place orders for dishes directly through the platform.

3. **Chef Dashboard for Managing Orders**
   - Provide chefs with a dashboard to manage orders and track their status.

4. **Online Payment Integrations**
   - Integrate online payment gateways for seamless transactions.

5. **Parallax & Effects Optimization**
   - Implement parallax effects and other visual enhancements for a more engaging user experience.

     
**Link to User Stories in GitHub Projects:**

- <a href="https://github.com/user-attachments/assets/e969ecb8-ade7-4595-9e6e-c092b1b70e6a" target="_blank">Moscow</a>
- [Project Board](https://github.com/users/Zalakshah786/projects/10)
- 

### logo:
  <a href="https://github.com/user-attachments/assets/8ba80947-02cf-4416-a75b-bc4dd46dcd33" target="_blank">logo</a>

### Color Palette:
  <a href="https://github.com/user-attachments/assets/ce863301-2bfb-4e43-b573-36fe09bf5629" target="_blank">color Palette link</a>

Detailed breakdown of the color palette:
* Olive Green:
  -  Hex: #656C12
  -  RGB: 101, 108, 18
  - A deep, earthy green reminiscent of olive leaves
* Mustard Yellow:
  - Hex: #D79A1F
  - RGB: 215, 154, 31
  - Warm, rich yellow typical of Indian spices like turmeric
* Deep Burgundy:
  - Hex: #900533
  - RGB: 144, 5, 51
  - A deep, wine-like red with rich intensity
* Brown:
  - Hex: #94571D
  - RGB: 148, 87, 29
  - Warm, earthy brown similar to roasted spices
* Dark Red:
  - Hex: #731314
  - RGB: 115, 19, 20
  - Deep, dark red reminiscent of chili peppers
* Golden Yellow:
  - Hex: #B18620
  - RGB: 177, 134, 32
  - A rich, warm golden tone
This palette beautifully captures the essence of Indian spicy food, with colors that evoke spices, warmth, and traditional cuisine. The combination suggests richness, depth, and the vibrant culinary culture of India.

### Typography:
<a href="https://github.com/user-attachments/assets/ff604833-0a9d-445e-a0ed-5d5f3012ab90" target="_blank">Embedded code for google fonts</a>

### Wireframe:
  - **Note**: The original Balsamiq wireframe link may require authentication to access
  - **Alternative**: Individual wireframe images are embedded below for full accessibility and easy viewing
    
**1. Main Page (Homepage)**
 
 * Displays dish images and names to grab user attention.
 * Users can click on a dish image or name to navigate to the detailed Dish Page.
 * Includes a section for chefs and their kitchens, where users can click to explore further
 * Navigation bar has clear categories (Food Hub, Recipes, Discover Us) with Login and Sign-up options.

<a href="https://github.com/user-attachments/assets/d8c2dca7-9b78-4878-8361-1dd4b6164fd6" target="_blank">Wireframe for main landing page</a>

   
**Usability & Accessibility:**
* Large images and clickable elements ensure easy navigation.
* Descriptive labels and buttons improve clarity for users, including those with screen readers.
* Consistent layout across pages enhances familiarity and ease of use

  
**2. Dish Page**
* Displays a larger dish image, name, and step-by-step preparation method.
* Ensures users can easily read and follow recipes.
* Header and footer remain the same across pages for consistency.
* Usability & Accessibility:
* Simple and structured layout with clear separation between image and text.
* Text-based instructions allow compatibility with screen readers.

  <a href="https://github.com/user-attachments/assets/d3e36b4a-d615-4eb7-8a0c-030c028f49e2" target="_blank">Wireframe for Dish Image</a>



**3. Chef's Kitchen Page**
* Shows chef’s name, specialty, and social media links (YouTube, Facebook, Instagram).
* Users can leave comments and ratings (Login required).
* Display user comments with username, date, time, and rating.
* Edit and Delete options for authorized users.


<a href="https://github.com/user-attachments/assets/25b0b609-0db5-4af8-bc92-0a947f6c8c7b" target="_blank">wireframe for Chef's kitchen page</a>

**Usability & Accessibility:**
* Clickable social media links allow users to explore the chef’s content externally.
* Comments section promotes interaction while maintaining moderation control.
* Login requirement for commenting prevents spam and ensures engagement from real users.

  <a href="https://github.com/user-attachments/assets/28e352ec-7ce8-4b2f-9b8f-90ccbec19fb0" target="_blank">login</a>

  <a href="https://github.com/user-attachments/assets/d31095d3-77a7-46fe-8f98-c28450ec3686" target="_blank">signout page</a>

  
**Navigation Between Pages**
* Clicking on a dish on the homepage redirects to the Dish Page for full details.
* Clicking on a chef's name or kitchen redirects to the Chef's Kitchen Page.
* Consistent navigation and visual hierarchy help users understand where they are in the site.

### Design Rationale:


**1. Clear Visual Hierarchy & Navigation**

* The layout is designed with a clear visual hierarchy, ensuring users can quickly locate important sections such as dishes, chef details, and user comments.
Sticky navbar with clear labels enhances usability and helps users navigate easily.
* Large clickable areas for dishes and chefs improve interaction, especially for mobile users.

  
**2. Accessibility Enhancements**

* Keyboard navigation support ensures that all interactive elements (links, buttons, forms) are accessible via the Tab key.
* ARIA labels and roles for images, buttons, and forms help screen readers convey information to visually impaired users.
* Contrast-optimized color scheme (using your preferred colors #900533 and #731314) ensures readability and adheres to WCAG contrast guidelines.
* Alt text for images ensures users with visual impairments can understand content.
  
**3. Responsive & Mobile-Friendly Design**
* Bootstrap 5 grid system ensures the website adapts to different screen sizes.
* Cards and images scale dynamically, preventing content from breaking on smaller screens.
* Collapsible menu for mobile devices improves accessibility and usability.
  <a href="https://github.com/user-attachments/assets/d2712591-64d1-41dd-871f-c2d46e14e478" target="_blank">Am I responsive</a>
  
**4. User Engagement & Feedback**
Comment section with ratings allows users to share their experiences with a chef’s kitchen.
Login prompts for commenting ensure only registered users can interact, reducing spam.
Feedback mechanism (e.g., “Like” or “Helpful” buttons) to engage users further.


**5. Performance & Loading Optimization**
* Lazy loading for images ensures that only visible content loads initially, improving speed.
* Optimized font choices to enhance readability and reduce loading time.
  
**6. Inclusive Language & Readability**

* Ensuring concise and readable content with simple instructions for recipes and chef details.
* Font choices (like sans-serif fonts) make reading easier, even for users with dyslexia.


## Key Features:
**1. Responsive & Intuitive Layout**

* The website is designed using Bootstrap 5, ensuring a fully responsive interface that adapts seamlessly across different screen sizes (desktop, tablet, mobile).
* A sticky navbar provides easy navigation, helping users quickly access key sections like recipes, chefs, and reviews.
* Large buttons and clear labels ensure easy interaction, benefiting users with motor impairments.
  [Am I responsive ?](https://github.com/user-attachments/assets/952ff6b2-dfb1-4ea0-87e2-3c06667480eb)
  
**2. Recipe & Chef Pages with Interactive Features**

* The homepage displays a preview of dishes and chefs, allowing users to explore details by clicking on an image or name.
* The recipe page provides a step-by-step guide for preparing Gujarati dishes, ensuring clarity for all users, including those with cognitive impairments.
* Each chef’s page includes social media links (YouTube, Facebook, Instagram) and a comment section for user engagement.
  
  <a href="https://github.com/user-attachments/assets/50724d34-e09a-4200-bd83-8f8d45e94c85" target="_blank">
  <img src="https://github.com/user-attachments/assets/50724d34-e09a-4200-bd83-8f8d45e94c85" alt="dish page">
  </a>
  <a href="https://github.com/user-attachments/assets/7d608059-b4f2-4d40-b22f-21c777c05472" target="_blank">
  <img src="https://github.com/user-attachments/assets/7d608059-b4f2-4d40-b22f-21c777c05472" alt="chef's kitchen page">
  </a>
  
![social accout excess](https://github.com/user-attachments/assets/13147f72-37fc-46f1-bdf6-1f6f4fdae516)
![required to login](https://github.com/user-attachments/assets/6f211881-dbbd-4ba9-a560-79dd76af4512)



**3. Accessible Design for Diverse Users**

* Keyboard navigation support: Users can navigate all elements using the Tab key without needing a mouse.
* ARIA attributes & screen reader support: Elements like buttons, images, and forms include ARIA roles and labels, making the website readable for visually impaired users.
* High contrast and accessible fonts: The color scheme follows WCAG contrast guidelines, and fonts are chosen for readability, benefiting users with dyslexia.
* Alt text for images: Ensures that visually impaired users can understand images through screen readers.

**4. Secure & User-Friendly Authentication**

* Login & Registration System: Only registered users can comment, ensuring a secure and spam-free environment.
* Login prompts are clearly displayed when users try to interact with restricted features.
* Session-based authentication keeps users logged in while ensuring data security.
  
   ![login](https://github.com/user-attachments/assets/28e352ec-7ce8-4b2f-9b8f-90ccbec19fb0)

  ![signout page](https://github.com/user-attachments/assets/d31095d3-77a7-46fe-8f98-c28450ec3686)

  ![register user ](https://github.com/user-attachments/assets/c29e6add-4bc7-4446-8c68-a0b20908f779)

  ![user already exit ](https://github.com/user-attachments/assets/6531bbd8-c7a3-4962-ad35-35916bc7691c)

**5. Interactive Comments & Ratings System**
* Users can leave reviews and ratings for chefs, helping others make informed decisions.
* Edit & Delete options are available for authorized users, maintaining content quality.
* Clear timestamp and username display enhance credibility and transparency.

<a href="https://github.com/user-attachments/assets/f6262a83-82bd-4772-87d6-bad51f78d79c" target="_blank">
<img src="https://github.com/user-attachments/assets/f6262a83-82bd-4772-87d6-bad51f78d79c" alt="login required to comment">
</a>

<a href="https://github.com/user-attachments/assets/d7ca02b2-61cc-4f08-b633-487ab253a712" target="_blank">
<img src="https://github.com/user-attachments/assets/d7ca02b2-61cc-4f08-b633-487ab253a712" alt="approve comment">
</a>

<a href="https://github.com/user-attachments/assets/8e61b460-514b-47a1-9247-f999e2772cf5" target="_blank">
<img src="https://github.com/user-attachments/assets/8e61b460-514b-47a1-9247-f999e2772cf5" alt="admin can approve comment">
</a>

<a href="https://github.com/user-attachments/assets/7a807771-d9e5-47b9-a875-34f1149c858e" target="_blank">
<img src="https://github.com/user-attachments/assets/7a807771-d9e5-47b9-a875-34f1149c858e" alt="edit and delete comment">
</a>

![comment added in chefs profile page ](https://github.com/user-attachments/assets/43c11962-249b-485a-94d2-7a3c664828e9)

![edit comment sucessfully added](https://github.com/user-attachments/assets/f6eae0b0-297e-4d5f-a7bc-d2b588407b75)

![sucessfully delete comment](https://github.com/user-attachments/assets/34f24b41-54b6-4de3-a087-55b014625cdb)


**6. Performance & Optimization**
* Lazy loading for images to improve page speed.
* Efficient database queries to minimize loading times.
* Optimized font and CSS choices for a lightweight experience.


  ![desktop lighthouse Report](https://github.com/user-attachments/assets/bd53468b-6b8f-4a92-95da-10dfb7f76f38)

  ![mobile lighthouse report](https://github.com/user-attachments/assets/9f3ccc3c-63e5-497a-86e3-4027643d37be)

  ![chefpage performance](https://github.com/user-attachments/assets/4702d37c-c005-40ad-9091-8e035e540e33)

  ![dishpage performance](https://github.com/user-attachments/assets/2ce732b1-f98e-46aa-aa97-c957117553b5)
  ![menulist performance](https://github.com/user-attachments/assets/abefe40e-7fe3-4fc9-9749-9883f375df7a)

  



## Additional Features
1.**Collaboration Requests (Contact Us Feature)**

- Users can submit collaboration requests through a form.
- Admins can view and manage these requests in the admin panel.
  
2.**Menu Management**

- Chefs can create, view, edit, and delete menu items.
- Menu items are categorized and displayed correctly under the appropriate categories.
  
3.**Dish Listings Management**

- Chefs can add, view, edit, and delete dishes.
- Dishes are displayed with images and categorized appropriately.
  
4.**Chef Profile Management**

- Chefs can create, edit, and delete their profiles.
- Profiles include details such as name, description, specialty, and images.
- Social media links are included in the profiles.

5.**User Authentication (Login, Logout, Register)**

- Users can register, log in, and log out.
- Only registered users can comment and rate dishes.
  
6.**Dynamic Navbar**

- The navbar changes based on the user's login status.
- Guests see Login and Register links, while logged-in users see Dashboard and Logout links.

### Future Expansion:
1.**Place an Order for Dishes**
   - Allow users to place orders for dishes directly through the platform.

2. **Chef Dashboard for Managing Orders**
   - Provide chefs with a dashboard to manage orders and track their status.

3. **Online Payment Integrations**
   - Integrate online payment gateways for seamless transactions.

4. **Weekly Recipe Recommendations**
   - Offer users personalized weekly recipe recommendations based on their preferences. 

### Usage Application:
1. **Register and Login**
   - Register a new account or log in with an existing account.

2. **Explore Recipes and Chefs**
   - Browse through the available recipes and chef profiles.

3. **Leave Comments and Ratings**
   - Leave comments and ratings on chef profiles.

4. **Manage Chef Profiles and Dishes**
   - Chefs can create, edit, and delete their profiles and dishes.

5. **Submit Collaboration Requests**
   - Users can submit collaboration requests through the contact form.
   - 
# Verification and Validation

### Steps to Verify the Deployed Version Matches the Development Version

 **Test Core Features:** Verify key functionality like user registration, login/logout, and the ability to create and manage content (e.g., notices, dishes, chefs)
 
 ## 1.User Authentication (Login, Logout, Register):
  ✅1. **Sign Up Functinality:**
   - Tests to Perform: User Registration
   - Test user registration and ensure the system successfully creates an account.
  -  [Sign Up ](https://food-hub-0b5046e8acf1.herokuapp.com/accounts/signup/)
  - Try registering a new user and check if the system successfully creates an account.
     [Register user with name xyz](https://github.com/user-attachments/assets/eb54341d-6403-40ae-a9a4-3daf7fb9284c)  
  - Confirm that an already registered email cannot be used again.
    [confirm that user already register](https://github.com/user-attachments/assets/7b048ccd-2154-4aa2-aef2-9ee3f19f733c)

✅2. **Login Functinality:**
Log in with valid credentials and ensure access to restricted pages.

 - [Login Page](https://github.com/user-attachments/assets/33181e7b-5534-4363-a14a-635251a19479)

 - [Login page ](https://food-hub-0b5046e8acf1.herokuapp.com/accounts/login/)

- Test invalid credentials (wrong password, non-existent email) and check if error messages are displayed.
     
- [Test with wrong password](https://food-hub-0b5046e8acf1.herokuapp.com/accounts/login/)

It's not showing any message because I didn't set 
- Add site ID
-  SITE_ID = 1
  
   `` Allauth settings
     ACCOUNT_EMAIL_REQUIRED = True
     ACCOUNT_USERNAME_REQUIRED = False
     ACCOUNT_AUTHENTICATION_METHOD = 'email'
     ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
     LOGIN_REDIRECT_URL = '/'
     LOGOUT_REDIRECT_URL = '/' ``
   
 - Email backend configuration
   
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@example.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    DEFAULT_FROM_EMAIL = 'webmaster@example.com'`
  

✅ 3.**Logout Functionality:**

  - Ensure users can log out successfully.

  - [logout](https://food-hub-0b5046e8acf1.herokuapp.com/accounts/logout/)
    
## Chef Profile Management (Tests to Perform):

✅**Tests to Perform:**

✅ **Creating a Chef Profile**:

  - Verify that a logged-in user can create a chef profile with details such as name, description, specialty, and images.
  - Check that required fields cannot be left blank.
  - Confirm that image uploads (via Cloudinary) work properly.
    
✅ **Editing and Updating Profile**

   - Ensure that chefs can edit and update their details (e.g., change profile image, update description).
     
✅ **Deleting Profile**
   -  Confirm that a chef can delete their profile, and the associated data (e.g., dishes) is handled correctly.
     
✅ **Social Media Links**

  -  Test if the YouTube, Instagram, and Facebook links added in the chef profile open correctly.
  -  [Create chef's kitchen profile Management](http://127.0.0.1:8000/admin/foodhub/post/add/)
    
         
## Dish Listings Management**

✅ **Tests to Perform:**

✅ Adding a New Dish
  -  Ensure that chefs can successfully add dishes with names, descriptions, images, and categories.
  -  Verify that a chef can assign a dish to a category (Snacks, Breakfast, Lunch, Dinner).
    
✅ Viewing Dishes
   - check if all dishes are displayed correctly on the menu page.
   - Ensure images load correctly via Cloudinary.
     
✅ Editing and Deleting Dishes
    -  [Adding new Dishes](http://127.0.0.1:8000/admin/foodhub/dish_receipe/add/)
    -  [Adding New Dishes](https://github.com/user-attachments/assets/fc673e9c-1d14-46a9-8732-8a7f35985213)
     
**future Expantion User Stories:**
✔ Searching and Filtering:
  - Test if users can filter dishes based on categories.
  - Verify if the search functionality works correctly when searching for a dish.


## Reviews and Comments on Chef's Kitchen Profile:**

✅**3.Tests to Perform:**

 ✅ Adding a Comment and Rating
   -  [login required to comment](https://github.com/user-attachments/assets/398f872e-c76d-4556-bd95-934d5883a3e5)

      -  Log in as a user and submit a comment on a chef’s profile.
      -  Ensure the comment appears under the chef’s profile with a rating.
      -  [required to login](https://github.com/user-attachments/assets/b541714c-0ea2-438f-a4be-c089c42266ca)

   
✅ Approving Comments:
    
 - Log in as an admin and approve/unapprove comments.
 - Confirm that unapproved comments are not visible on the website.
   - [approve comment](https://github.com/user-attachments/assets/d8200198-b932-44c2-acfb-6b67af272600)
   - [Approving Comment](https://food-hub-0b5046e8acf1.herokuapp.com/post_detail/7/)
      
✅ Editing and Deleting Comments:

  - Test if authorized users (Test and Zalak) can edit and delete comments.
  - Verify that regular users can only delete their own comments.
    - [Admin can approve comment](https://github.com/user-attachments/assets/28e7c503-debc-4d65-9bd7-957b9487870c)
    - [Admin can approve comment](https://github.com/user-attachments/assets/3762dbcf-dbc5-40da-973a-147c7e9bdc6c)
    - [edit and delete comment](https://github.com/user-attachments/assets/bdf75773-6f05-4853-be29-4b83869681d6)

## Menu Management
  ✅**Tests to Perform:**
  ✅ Creating a Menu Item
    - Check that a menu item can be created with a name, description, chef name, image, and category.
    
  ✅ Viewing the Menu
    - Ensure that menu items display correctly under the correct categories.
    
  ✅ Editing and Deleting Menu Items and only authorized users (admin or chef) can modify or remove menu items.
  
    - [Menu Listing](https://github.com/user-attachments/assets/f4d32519-b91f-4c4b-bc44-daa8d23b16e5)
    - [Editing and Deleting Menu Items](http://127.0.0.1:8000/admin/foodhub/menuitem/add/)


## Collaboration Requests (Contact Us Feature)

  ✅**Tests to Perform**:
  
  ✅ **Submitting a Collaboration Request**
  
  [Collobration Form](https://food-hub-0b5046e8acf1.herokuapp.com/collaborate_request/)

  ![Collobration form Image](https://github.com/user-attachments/assets/5b6000ff-db91-4e9b-881a-7321b9f816ec)

  - Fill out the collaboration request form with a name, email, and message.

  ![collobration request submit Message](https://github.com/user-attachments/assets/64cf0215-c6ed-4d89-8094-c00667f17144)

  Check if the request is successfully stored in the database.
  - ![Collobration request can view in database](https://github.com/user-attachments/assets/bd719f93-40ff-4387-99ac-a3cace3bf7c8)

✅**Viewing and Managing Requests**
  - Log in as an admin and check if collaboration requests appear in the admin panel.
  - Ensure that can be updated to "Read" when viewed.
    ![collobration request can view in database](https://github.com/user-attachments/assets/63a7fc54-f8bb-4964-9c55-31d8f51d910c)

   ![collobration request edit and delet](https://github.com/user-attachments/assets/7c1df680-18ce-41cc-9e0f-fae3f26033a7)

    

    
### Navbar and Page Navigation
  ✅Tests to Perform:
  
  ✅ Dynamic Navbar for Logged-in Users vs. Guests
  
     - Ensure the navbar changes based on login status.
     -  Guests should see Login and Register links, while logged-in users see Dashboard and Logout.
     
  ✅ Navigation Links
     - Click on Home, Recipes, Menu, and Chefs to check if pages load correctly.
     
     ![Navbar ](https://github.com/user-attachments/assets/ec11a305-6f02-49d3-8300-02edad4d3619)


## Security Measures

1. **Environment Variables for Sensitive Data**
   - Use environment variables to store sensitive data such as `SECRET_KEY`, database credentials, and API keys.

2. **Disable DEBUG Mode in Production**
   - Ensure `DEBUG` is set to `False` in production to prevent the display of detailed error messages.

3. **Allowed Hosts**
   - Set `ALLOWED_HOSTS` to include only the domains that should be allowed to serve your application.

4. **Secure Authentication**
   - Use secure authentication methods and ensure that user passwords are hashed and stored securely.

5. **HTTPS**
   - Ensure that your application is served over HTTPS to encrypt data transmitted between the server and clients.

6. **CSRF Protection**
   - Enable Cross-Site Request Forgery (CSRF) protection to prevent unauthorized actions on behalf of authenticated users.


## Responsive:
The Gujarati Food Hub project is fully responsive, ensuring a seamless experience across various devices, including desktops, tablets, and mobile phones. The following features have been implemented to enhance responsiveness:

✅ Mobile-Friendly Layout
- The website adjusts dynamically to different screen sizes using Bootstrap 5.3 grid system and CSS media queries.
- Elements such as images, text, and buttons resize and reposition appropriately for smaller screens.
  
✅ Navigation Adaptation
- A dynamic navbar automatically collapses into a mobile-friendly hamburger menu on smaller screens.
- The navigation bar is sticky to improve accessibility and user experience.

  
✅ Scalable Images & Fonts
- High-quality responsive images and SVG icons are used to prevent distortion on different screen sizes.
- Font sizes adjust dynamically using relative units (em, rem, %) for better readability.

  
✅ Touch-Friendly Interactions
- Buttons, links, and interactive elements are optimized for touchscreens with adequate spacing.
- Hover effects gracefully transition into tap-friendly actions on mobile.

  
✅ Parallax & Effects Optimization
- The Parallax effect on the landing page is optimized for desktops but gracefully deactivates on mobile to ensure smooth scrolling.
- Animations and overlays scale efficiently to avoid performance issues on low-end devices.

  
✅ Testing & Cross-Browser Compatibility
- The website has been tested across major browsers (Chrome, Firefox, Edge, Safari) to ensure consistent performance.
- Developer tools and mobile emulators were used to verify responsiveness.

![Am I responsive ](https://github.com/user-attachments/assets/d2712591-64d1-41dd-871f-c2d46e14e478)

## Database
### Creating a database
  - Navigate to PostgreSQL from Code Institute.
  - Enter your student email address in the input field provided.
  - Click Submit.
  - Wait while the database is created.
  - Check your email.
  -You now have a URL you can use to connect your app to your database.
      - I used Code Institute's PostgreSQL database.
      - here is the link to view Database

  [ERD Diagram](https://github.com/user-attachments/assets/1b815370-9b00-4cbe-ab17-b8532057475e)

  ![admin database](https://github.com/user-attachments/assets/8a0818fb-92d5-4313-9748-2bb4a6f8ffd0)


# Deployment:
## 🚀 Step-by-Step Guide to Deploy Django Project on Heroku

This guide will walk you through the steps to deploy your Django project on Heroku. Follow these steps carefully to get your project live.

### Prerequisites
Before you start, ensure you have the following:
- A Heroku account: [Create a Heroku account](https://signup.heroku.com/)
- Installed [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Python 3.x and Django installed on your local machine
- Git installed on your local machine

### Step 1: Prepare Your Django Project

1. **Install Dependencies**  
   Ensure you have the following dependencies installed in your Django project:
   - `gunicorn` for serving the application
   - `psycopg2` for PostgreSQL database support (or any database you're using)

        Install them using pip:
          `pip install gunicorn psycopg2`

2.**Create a requirements.txt file**
         Run the following command to generate the requirements.txt file which lists all 
   
         dependencies:
         `pip freeze > requirements.txt`
3.**Create a Procfile**
        In the root directory of your project, create a Procfile to tell Heroku how to run the application. 
        The content of this file should be:
    
          ```web: gunicorn <your_project_name>.wsgi```
           Replace <your_project_name> with the actual name of your Django project.
           [live view](https://food-hub-0b5046e8acf1.herokuapp.com/)

4.**Setup Database Configuration (Optional)**
         If you are using PostgreSQL or another database, make sure your project is configured to work with it. For PostgreSQL, update the DATABASES setting in 
           settings.py:

        ```DATABASES = {
                  'default': {
                  'ENGINE': 'django.db.backends.postgresql',
                  'NAME': os.environ.get('DB_NAME'),
                  'USER': os.environ.get('DB_USER'),
                  'PASSWORD': os.environ.get('DB_PASSWORD'),
                  'HOST': os.environ.get('DB_HOST'),
                  'PORT': '5432',
                          }
                    }``
### Step 2: Set Up Heroku

1. Log in to Heroku CLI
     Open your terminal and run the following command:

          ```heroku login```

2. Create a Heroku App
      Run the following command to create a new app on Heroku:

         ```heroku create <your-app-name>```
   
3. Set Environment Variables

          Set the required environment variables for your project, such as SECRET_KEY, DEBUG, and ALLOWED_HOSTS:

          ```heroku config:set SECRET_KEY=<your-secret-key> DEBUG=False ALLOWED_HOSTS=<your-app-name>.herokuapp.com```



### Step 3: Deploy the Project

 1. Initialize Git Repository (if not already initialized)
           If your project is not already a git repository, run:

                ```git init```


2.Commit Your Changes
           Add all the files to Git and commit them:
              ```git add .
                 git commit -m "Initial commit"```

3.Push to Heroku
          Push your project to Heroku:

              ```git push heroku master ```
4.Migrate Database
          Once the project is deployed, run database migrations:

            ```heroku run python manage.py migrate```

5.Open Your App
          Finally, open your app in the browser:

            ```heroku open```



# Validators for All Html,css, java script,python files:

  ![html validations](https://github.com/user-attachments/assets/5c640ba0-d47b-4228-b10a-434e23fe69e9)

  ![login page validator](https://github.com/user-attachments/assets/ca04bc87-81f8-41e9-a048-6bd2b98965a7)
  ![menulist html validator ](https://github.com/user-attachments/assets/719005d5-eb5f-478d-8987-391dec251de8)
  ![dish detail html page validator](https://github.com/user-attachments/assets/0374fd96-e296-421f-964f-e0dd04a3dea1)
  ![colobratations request form validators](https://github.com/user-attachments/assets/a9563da8-f094-4693-8d0e-73a562b0c666)
  ![chef's kitchen html validator](https://github.com/user-attachments/assets/1e6b4d55-7c8c-49df-a07b-cc6993932628)
  ![css validator](https://github.com/user-attachments/assets/3d6e8088-33af-4667-ab23-353ece013420)
  ![forms py-validator](https://github.com/user-attachments/assets/b937ea0c-f3ed-4e4f-baf0-cd7587f6a312)
  ![admin py-validator](https://github.com/user-attachments/assets/2fd2754e-1003-4daa-8be3-afee611d7d50)

  ![models py-validator](https://github.com/user-attachments/assets/58b59697-6fd5-4211-9d36-a01b809afec0)
  ![urls py-validator](https://github.com/user-attachments/assets/d7f98d65-3231-4227-8f3c-8cd19c5a521e)
  ![views py-validator png-orig](https://github.com/user-attachments/assets/2bbdafcf-44e8-4771-99cd-40d9d753c408)
  ![admin py-validator](https://github.com/user-attachments/assets/14bdb77d-d50a-4bf1-bf41-f84f908b4846)
  ![js file validator](https://github.com/user-attachments/assets/4b098f75-9151-472c-ba1e-09355e8b7655)




# Food Hub - Manual Testing Documentation
## Testing Summary

## 1. User Authentication Testing

The detailed manual test cases are available in the following file:

📄 [View Manual Test Cases](test.md)

![Ai testcase done](https://github.com/user-attachments/assets/7b9daf4e-66a5-4f18-959c-68ff522253dd)



## AI Assistance in Development

- During the development of food Hub , I strategically used GitHub Copilot to assist in various aspects of the code creation process. They were utilized to enhance productivity and code quality:
**Code Suggestions**:
 -  Copilot helped in writing efficient and error-free code by suggesting relevant code snippets and functions. It also assisted in refining classes and optimizing the CSS for better organization.


**Debugging:**
- I encountered several bugs in the code, which were identified and corrected with the help of AI. Copilot played crucial role to identify and fix issues and semantic errors quickly, ensuring a smooth 
   development process.

**AI Assistance in Development**
- During the development of Food Hub, I strategically used GitHub Copilot to assist in various aspects of the code creation process. They were utilized to enhance productivity and code quality:

**Code Suggestions:**
- Copilot helped in writing efficient and error-free code by suggesting relevant code snippets and functions. It also assisted in refining classes and optimizing the CSS for better organization.

**Debugging:**
- I encountered several bugs in the code, which were identified and corrected with the help of AI. Copilot played crucial role to identify and fix issues and semantic errors quickly, ensuring a smooth development process.

**Documentation:**
- AI tools facilitated the creation of comprehensive documentation by generating markdown templates and content suggestions for the website.

**Design:**
- AI-based design tools provided inspiration and suggestions for UI/UX improvements, contributing to a more polished and user-friendly application.

**Productivity**
- Copilot significantly boosted productivity by automating repetitive tasks and providing intelligent code completions. This allowed me to focus more on the core functionality and design aspects of the application, ultimately leading to a more robust and feature-rich product.

**Reflection:**
- One of my proudest moments came when I used Copilot to refine the Bootstrap styling. I wasn’t very confident in front-end design, but the AI helped bridge that gap. It suggested small, impactful changes, like 
   improving button alignment and tweaking breakpoints, that made the application feel polished and professional. These adjustments also ensured that the app was truly responsive, which was a priority for me.

**Overall Impact:**
- Working with Copilot transformed my workflow. It allowed me to focus on higher-level decisions while handling repetitive tasks efficiently. However, it wasn’t always perfect—some suggestions required 
   significant tweaking to fit my specific needs. Those moments were valuable reminders that the AI wasn’t a replacement for my skills but a tool to enhance them.

- Looking back, I feel this experience not only improved my technical abilities but also my problem-solving skills. It pushed me to articulate my ideas clearly (both to the AI and myself) and made me more 
  mindful of inclusivity and accessibility in software design. Above all, it taught me the importance of embracing new technologies as partners in the creative process.

## Frameworks, Libraries & Programs Used
- HTML5: The standard markup language for creating web pages, providing the structure and content of the site.

- CSS3: A style sheet language used for describing the presentation of a document written in HTML, enabling responsive and visually appealing designs.

- JavaScript: A programming language that enables interactive web pages, enhancing user experience with dynamic content and features.

- GitHub: A platform for version control and collaboration, allowing multiple developers to work on projects simultaneously and manage code changes.

- Heroku: A cloud platform as a service (PaaS) supporting several programming languages, used for deploying, managing, and scaling web applications.

- Pexels: A free stock photo and video website, providing high-quality images used within the application for visual enhancement.

- Cloudinary: Media management service that allows uploading, storing, manipulating, and delivering images and videos.

- Crispy-bootstrap5: Django package that integrates Django forms with Bootstrap 5, allowing for easy and consistent form rendering.

-  Dj-database-url: Utility for configuring database URLs in Django.

- Dj3-cloudinary-storage: Django package that integrates Django media storage with the Cloudinary service.

- Django: High-level web framework for Python that enables rapid and clean development of web applications.

- Django-summernote: WYSIWYG editor based on Summernote for integration with Django. summernote==0.8.20.0
- Django-allauth: Django application for authentication, registration, and account management. allauth==0.57.2
- Django-crispy-forms: Django package that makes it easy to create elegant and reusable forms. crispy-forms==2.3
- Gunicorn: WSGI HTTP server for Python applications, used to deploy Django applications.

- Pillow: Image processing library for Python.

- Psycopg2: PostgreSQL database adapter for Python.

- Python3-openid: Library for supporting the OpenID protocol.

- Tzdata: Time zone database.

- Whitenoise: Library for serving static files in Django applications.

- Python
asgiref==3.8.1
bleach==6.2.0
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
cloudinary==1.42.2
crispy-bootstrap5==0.7
cryptography==44.0.0
defusedxml==0.7.1
dj-database-url==0.5.0
Django==4.2.18
django-allauth==0.57.2
django-cloudinary-storage==0.3.0
django-crispy-forms==2.3
django-heroku==0.3.1
django-storages==1.14.4
django-summernote==0.8.20.0
gunicorn==20.1.0
idna==3.10
oauthlib==3.2.2
pillow==11.1.0
psycopg2==2.9.10
pycparser==2.22
PyJWT==2.10.1
python3-openid==3.2.0
requests==2.32.3
requests-oauthlib==2.0.0
setuptools==75.8.0
six==1.17.0
sqlparse==0.5.3
typing_extensions==4.12.2
tzdata==2025.1
urllib3==2.3.0
webencodings==0.5.1
whitenoise==6.8.2

### Tools

- **Visual Studio Code:** For code editing and development.
- **Git and GitHub**: For version control and repository management.
  
## Credits:
### External Libraries and Tools
- [Django](https://www.djangoproject.com/) - The web framework used for the project.
- [Bootstrap](https://getbootstrap.com/) - For responsive design and styling.
- [Cloudinary](https://cloudinary.com/) - For image storage and management.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - For better form rendering.
- [Font Awesome](https://fontawesome.com/) - For icons.
- [Google Fonts](https://fonts.google.com/) - For typography.
- [ChatGPT](https://openai.com/chatgpt) - For AI assistance and content generation.
- [Gemini](https://gemini.com/) - For cryptocurrency tools and resources.
- [Claude AI](https://claude.ai/) - For AI assistance and content generation.
- Copilot- For search and AI tools.
- Balsamiq was used to create the design wireframe.

### Inspiration and References
- [Django Documentation](https://docs.djangoproject.com/en/stable/) - For comprehensive guides and references.
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - For design and layout inspiration.
- [Real Python](https://realpython.com/) - For tutorials and articles on Django and Python.

### Acknowledgements:

- Through the exhilarating world of hackathons, I've discovered more than just code – I've found true friendship. These amazing individuals have become my anchors during challenging times, turning stress into      smiles with every conversation. A special heartfelt thank you goes to Nrupay Shah, whose invaluable guidance and unwavering support have been the cornerstone of this project. His mentorship and expertise have     not only shaped this project but have also helped me grow as a developer. Their collective support and understanding remind me that I can overcome any obstacle. Because when my friends say "You can do it,        Zalak," those words carry the weight of genuine belief and heartfelt encouragement, making every challenge feel conquerable.

- Thanks to the [**Code Institute Team **]**Emma_lamont_ci**,**Roo**,**Spencer** thank you so much for providing valuable resources and support.


























