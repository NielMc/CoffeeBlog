# CoffeeBlog
****
## A forum and blog for coffee lovers with user authentication

####Framework
>This app is written using a Django framework.

####Project level
>The settings files are split into base, dev and prod. This allows different options on the hosted site versus development. For example the debug_toolbar package is used when running locally for development. The url.py gives the url patterns routes to views. As the accounts and blog apps have their own url.py the include function is used to import them. 

####Templates
>The base.html template is the basis for all the pages in the app. It uses a bootstrap blog theme which makes the app fully responsive across all screen sizes. The nav bar is transparent and collapses down to an icon on small screen sizes. A black and white photo suitable to the site's purpose is used as the banner background for high contrast with the text. Social media links are in the footer. Django expressions show where the JavaScript and html content will be injected. All the other templates extend from the base template. 

####User Authentication
>This app uses email/password authentication from a custom User model. An app called accounts hosts the authentication code. The custom authentication uses Django AbstractUser for basic attributes and the class UserManager for basic registration. The create_user method in UserManager is overridden and a new one equating user with email is created. This new class is added to settings so it will be used on startup. In backends.py the email authorisation is done and an additional user active test is done. These backends are referenced in settings to override the standard procedure. A UserRegistrationForm in forms.py collects the data required from the user. First and last name are collected but are not used for authentication. Rather they are used to identify posts in the blog/forum thus avoiding email addresses being made public in the app. The app django_forms_bootstrap is used to render the form on the register webpage. When a user successfully registers the profile webpage is displayed. Within the views.py the actions for login, logout, register and profile are coded. This data is rendered on html templates. A login required attribute is used to show pages that should only be viewed by the user who is logged in. 

####Stripe one off payment
>Stripe is used to take a one off payment from the user when they register. A stripe app is installed and the publishable/secret keys are stored on the server. The user's credit card information is input through the registation form. The user's stripe_id is retained although not displayed to verify that a payment has been made successfully. Credit card validation is done through Stripe's JavaScript API. The script is only linked on the register html page using a {{block head_js}} section. 

####Forum
>The forum allows threads and posts to be created for discussions between users. 
* django-emoticons plugin is used for animated emoticons
+ django-tinymce plugin is a text editor allowing formatting by the user
- arrow plugin replaces computer timestamps with descriptions like "just now"

>The tinymce requires JavaScript libraries to be stored in the static folders. Font-awesome css files in the static folders enable the use of icons for edit/delete rather than buttons. The threads app contains all the forum code. Only the admin can create a subject but users can add threads and posts. Users are identified in the thread app by using accounts.User as a ForeignKey. This establishes the one to many relationship between threads and users. There are many threads but each one is owned by one user. In models.py the subject, thread and post are defined. HTMLField is what triggers the use off tinymce text editor. The views.py defines what the user can do and renders to html. In threads_extras.py the code counts the posts by user and does statistics on votes cast. The poll itself is a separate app with its own model and form. However the poll is accessed from the thread views where a formset is set for 3 poll subjects. A user can choose to add a poll when creating a thread by checking a checkbox. A script then shows or hides the poll form based on the checkbox status. 

####Blog
>The blog is a separate app. A blogpost consists of a title, content, image and tag which the user enters with a form. As with the forum the author is liked to the accounts user by a ForeignKey. Views are set up to show the blogposts in truncated form by time, views or tag. Django paginator is used so that the number of posts per page can be limited. Views also exist to view a blogpost in detail and if logged in create/edit a blogpost. User added images are uploaded to a media directory. Within models.py the number of views and post creation time are available for display in the html page.  
* django-disqus plug in is used to manage comments on blogposts with Disqus
- Pillow plugin facilitates upload of images
+ django-gravatar2 shows images of users who use Gravatar.com globally recognised avatars

####hello app
>This app contains the views to render the index, contact, about, login and profile pages. Login only is visible if you are not logged in.

####Databases
>SQLite is used for the locally hosted development of this app. ClearDB MySQL is used for the hosted version of the app. 

####aws/s3
>For performance reasons the static and media files are hosted on Amazon S3. A static and a media bucket were set up in S3 and a AWS user was set up to manage the resources. A STATIC_URL and MEDIA_URL are required in settings so that the load static (or media) in the html templates points to AWS. Cross-origin resource sharing (CORS) defines how the web client app interacts with resources in AWS. 
* django-storages python package used to enable collectstatic to copy to S3
+ boto python package is an AWS library for django
- django-cors-headers is a django app to handle server headers for CORS

#### tests
>The blog app contains examples in tests.py of automated testing using django. 
 The built in Django class TestCase is used to create classes containing methods starting test_ which test aspects of the code. A test of the Post model uses the example of a title and checks it is equal to the string posted to the database. A temporary copy of the database is made for the test then is destroyed. The url is tested to see if the correct page is resolved, the correct status code obtained and the correct post id given. The inbuilt setUp method is used to test logging in. 

 ####Hosting
>This app is hosted on Heroku. The python package gunicorn is required as well as a Procfile. Automatic deploy from GitHub has been set up. The python package dj-database-url is required to connect to the ClearDB database. 