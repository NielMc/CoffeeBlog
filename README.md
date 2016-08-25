# CoffeeBlog
****
## A forum and blog for coffee lovers with user authentication

####Framework
>This app is written using a Django framework.

####User Authentication
>This app uses email/password authentication from a custom User model. An app called accounts hosts the authentication code. The custom authentication uses Django AbstractUser for basic attributes and the class UserManager for basic registration. The create_user method in UserManager is overridden and a new one equating user with email is created. This new class is added to settings so it will be used on startup. In backends.py the email authorisation is done and an additional user active test is done. These backends are referenced in settings to override the standard procedure. A UserRegistrationForm in forms.py collects the data required from the user. First and last name are collected but are not used for authentication. Rather they are used to identify posts in the blog/forum thus avoiding email addresses being made public in the app. The app django_forms_bootstrap is used to render the form on the register webpage. When a user successfully registers the profile webpage is displayed. Within the views.py the actions for login, logout, register and profile are coded. This data is rendered on html templates. A login required attribute is used to show pages that should only be viewed by the user who is logged in. 

####Stripe one off payment
>Stripe is used to take a one off payment from the user when they register. A stripe app is installed and the publishable/secret keys are stored on the server. The user's credit card information is input through the registation form. The user's stripe_id is retained although not displayed to verify that a payment has been made successfully. Credit card validation is done through Stripe's JavaScript API. The script is only linked on the register html page using a {{block head_js}} section. 

####Forum
>The forum allows threads and posts to be created for discussions between users. 
* django-emoticons plugin is used for animated emoticons
+ django-tinymce plugin is a text editor allowing formatting by the user
- arrow plugin replaces computer timestamps with descriptions like "just now"
>The tinymce requires JavaScript libraries to be stored in the static folders. hFont-awesome css files in the static folders enable the use of icons for edit/delete rather than buttons. The threads app contains all the forum code. Only the admin can create a subject but users can add threads and posts. Users are identified in the thread app by using accounts.User as a ForeignKey. This establishes the one to many relationship between threads and users. There are many threads but each one is owned by one user. In models.py the subject, thread and post are defined. HTMLField is what triggers the use off tinymce text editor. The views.py defines what the user can do and renders to html. In threads_extras.py the code counts the posts by user and does statistics on votes cast. The poll itself is a separate app with its own model and form. However the poll is accessed from the thread views where a formset is set for 3 poll subjects. A user can choose to add a poll when creating a thread by checking a checkbox. A script then shows or hides the poll form based on the checkbox status. 

####Blog
>The blog is a seperate app. A blogpost consists of a title, content, image and tag which the user enters with a form. As with the forum the author is liked to the accounts user by a ForeignKey. Views are set up to show the blogposts in truncated form by time, views or tag. Django paginator is used so that the number of posts per page can be limited. Views also exist to view a blogpost in detail and if logged in create/edit a blogpost. User added images are uploaded to a media directory. Within models.py the number of views and post creation time are available for display in the html page. 
*django-disqus plug in is used to manage comments on blogposts with Disqus
-Pillow plugin facilitates upload of images
+django-gravatar shows images of users who use Gravatar.com globally recognised avatars