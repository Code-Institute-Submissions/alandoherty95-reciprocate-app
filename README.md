**[Reciprocate](https://reciprocate-application.herokuapp.com/)**

Welcome to **[Reciprocate](https://reciprocate-application.herokuapp.com/)** - a community for sharing and discovering recipes!

![Website Mockup](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/images/responsive-mockup.png?raw=true)

<span id="top"></span>

![Reciprocate Logo](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/images/reciprocate-logo.png?raw=true)

**[Reciprocate](https://reciprocate-application.herokuapp.com/)** is a community-based application created for anyone who enjoys trying new recipes or sharing their favourites recipes with others. It was designed to allow users to freely share recipes with each other. Users can share their own food and drink recipes with the community and conveniently access the recipes provided by all other members. The website was designed with simplicity and ease-of-use in mind, encouraging users to recreate recipes at home with family and friends. Users will have the option of setting up an account to create, locate, display, edit and delete records from the collection of recipes.

## Table of Contents

1. <a href="#context">**Context**</a>

2. <a href="#ux">**User Experience (UX)**</a>

3. <a href="#scope">**Scope**</a>

4. <a href="#structure">**Structure**</a>

5. <a href="#wireframes">**Wireframes**</a>

6. <a href="#technologies">**Technologies**</a>

7. <a href="#database">**Database**</a>

8. <a href="#features">**Features**</a>

9. <a href="#testing">**Testing**</a>

10. <a href="#deployment">**Deployment**</a>

11. <a href="#credits">**Credits**</a>

12. <a href="#acknowledgements">**Acknowledgements**</a>

<span id="context"></span>

## 1. Context

In preparation for this project, I conducted research on friends, colleagues and family members to identify the kind of recipes in demand at this time. The website currently focuses on three main categories of recipe: smoothies, cocktails and snacks. The website admin has the capability to add additional recipes types for selection by other users in future development.

The application was designed using CRUD functionality. Create, Read, Update, and Delete are the four primary functions available to users of the website. Any user who creates an account will have the ability to create, read, edit and delete records from the recipe collection.

Create — A function we can call when a new recipe is being added to the database. The user can supply the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The new entry is assigned a unique `id`, which can be used to access the resource later. The website admin has the capability to create new recipes types for selection.

Read — A function we can call to see all of the recipes currently in our database. This function does not alter the recipes in the catalog - it simply retrieves the information and displays the results. Again, a similar process can be followed if the website admin wishes to view the categories contained in the database. All visitors to the website can browse all recipes without having to create an account.

Update — A function we can call when information about a particular recipe must be changed. The user can edit the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. After the function is called, the corresponding entry in the `recipes` database will contain the new fields provided. This option is only available to the creator of each recipe. These steps can be followed if the website admin wishes to edit an existing category in the database.

Delete — A function we can call to remove a particular recipe from the catalog. After this function is called, the `recipe` resource should contain all of the recipes it had before, except for the one recipe we just deleted. This option is only available to the creator of the recipe. A similar process can be followed if the website admin wishes to remove a category from the database.

<span id="ux"></span>

## 2. User Experience (UX)

### Overview

The website was designed with a community-based approach in mind. It was created with three main objectives:

- To encourage people to share their favourite recipes with other members

- To allow convenient access to the recipes provided by all other members

- To promote a local catering supplies company

The website focuses on the following three types of recipes but it is not limited. The admin has the capability to add a new category for different categories.

**Smoothies:** are becoming increasingly more popular each year. Many people are opting for smoothies made up of fruit and vegetables as part of their daily calorie intake. Our smoothie recipes provide users with real choice while keeping up a healthy diet.

**Cocktails:** are also becoming increasingly popular among adults. People have grown to appreciate the variety of taste and beauty of these artisan drinks. Our cocktail recipes allow users to create popular drinks themselves without having to rely solely on bartenders.

**Snacks:** have always been a significant part of our diet. People have become more creative and adventurous with their snacking habits in recent years. Our snack recipes offer variety for people constantly on-the-go who need a quick source of energy.

### User Stories

#### As a first-time visitor, I want to:

- Immediately understand the purpose of the website

- Easily create an account

- Browse all recipes without having to register

- Find specific recipes by searching for keywords

#### As a returning visitor, I want to:

- Log in and out easily

- Add new recipes quickly and conveniently

- Edit or delete recipes I have already shared

- View all recipes I have shared on my profile

### Users:

- As an individual who likes to keep a healthy lifestyle, I want to find tasty food and drink recipes to try at home.

- As a food lover, I would like to share recipe ideas for snacks and smoothies with other people with similar interests.

- As an individual looking to improve their health and fitness, I want to easily browse through healthy recipes and try different ones.

### Owner:

- As the owner of this website I would like to provide a platform to encourage users to share their favourite recipes with other members of the community.

- As the owner, I want users to browse and find recipes that suit their tastes.

- As the owner, I want to allow users to create additional categories if they would like.

- As the owner, I want to promote a local catering supplies company.

### Design

#2632A6 - Blue

#FFFFFF - White

#A62632 - Crimson

#32A626 - Green

#000000 - Black

![Colour Scheme](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/my-color-scheme.png?raw=true)

The colour scheme chosen for this project was inspired by bright colours to give the website an attractive, vibrant look. While Crimson and Persian Green complement each other nicely, the white background gives a sleek, neutral look to the application.

- **#A62632 Crimson** is used for all headings, giving a clean, consistent feel throughout the website. Crimson on a white background draws attention to the headings.

- **#FFFFFF White** is the backdrop of all headings and text on the website. The bright colour emphasises clarity and removes visual clutter. The black text is easily readable on the white background.

- **#2632A6 Blue** is used for some buttons such as the log in button.

- **32A626 Green** is used for buttons such as the register button.

- **#26A69A Persian Green** is used for neutral buttons. This allows users to easily identify buttons on the screen. It is also used as the button hover colour.

#### Typography

[Merienda One](https://fonts.google.com/specimen/Merienda+One) was used for the main headings and navigation links on the website to grab the users attention. 'Merienda' is a Spanish term for "afternoon snack", which seems fitting for the purpose of this application. Merienda has soft shapes, is slightly condensed, and has a rhythm which is an invitation to read short pieces of text.

![Merienda One](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/merienda-one.png?raw=true)

[Oswald](https://fonts.google.com/specimen/Oswald) was used for the primary text because it is easy to read. Oswald is designed to be used freely across the internet by web browsers on desktop computers, laptops and mobile devices.

![Oswald](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/oswald.png?raw=true)

- #### Imagery

Images used in the development of this website were selected from [Pexels](https://www.pexels.com/). Users are encouraged to add the full image URL if they would like to include a picture with their recipe.

<span id="scope"></span>

## 3. Scope

The minimum features to be included in this project are as follows:

- **Home Page** attracts first-time visitors and clearly presents the purpose of the website. The two prominent call-to-action buttons encourage users to either log in or register if they do not have an account yet. The log in and register buttons will redirect users to the respective form. The search bar is also a prominent feature on the homepage with all recipes in our collection displayed below. The search bar can be used to find specific recipes based on keywords.

- **Categories** allows the website admin to manage the categories of recipe available for selection by other users. The admin can add, edit or delete categories. This function allows for expansion into different types of recipes in future development.

- **Register** invites visitors to create an account if they have not set one up yet. New users can simply enter a unique username and password to create an account. Users with an account have the ability to add new recipes as well as edit or delete recipes they have already shared. Users can access their own profile page which displays all recipes shared by them.

- **Log In** invites users to log in to their account. Returning users can simply enter their username and password to sign in. This allows users to view, edit or delete recipes they have already shared as well as adding new recipe ideas. Users can access their own profile page which displays all recipes shared by them.

- **Log Out** allows users to log out of their account with one click of a button. The log out function removes the user from the session. This button is available in the navigation bar and footer of all pages when a user is logged in.

- **Profile** can be accessed by users when they have successfully logged in. Users can view all recipes they have shared. Users can also edit or delete recipes they have already shared with the community. The profile page also promotes a local catering company where users can shop for any supplies needed.

- **Create Recipe** encourages users to share new recipes with the community. Users must be logged in to their account in order to share recipes. A new recipe can be submitted by filling out a simple form. The user will enter the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The new recipe is displayed on the homepage and the user's profile page.

- **Edit Recipe** allows users to edit their own recipes. Users can edit their existing recipes by selecting the 'Edit' button. The user can update the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The updated recipe is displayed on the homepage and the user's profile page.

- **Delete Recipe** function that users can delete their recipes. A modal pop up will ask the user to confirm their action before deleting. This provides an extra layer of protection against accidental deletion of records. Once deleted, the recipe will be permanently removed from the collection.

- **Search Function** allows users to search for specific recipes using keywords. The search function targets the `“recipe_name”` and `“recipe_ingredients”` fields in each recipe. The search will return results based on the keyword inputted.

<span id="structure"></span>

## 4. Structure

### Structure Plane

**Front-End**

- **Home** (`recipes.html`)

The welcome page clearly outlines the main purpose of the website. In the top navigation bar, there is a logo and tabs for the _Home_, _Register_ and _Login_ pages. There are two prominent call-to-action buttons encouraging users to either log in or register if they do not have an account yet. By scrolling down, users can browse all recipes in our database and search for specific recipes using keywords.

- **Log In** (`login.html`)

The log in page allows users who already have an account to log in to their profile. Both the username and password must be 4-20 characters long, containing only numbers and letters. When users log in successfully, they are redirected to their unique _Profile_ page where they can view, edit and delete their existing recipes. Additional tabs are visible to the user after logging in.

- **Register** (`register.html`)

The registration page allows users to create an account by entering a distinct username and password. Both the username and password must be 4-20 characters long, containing only numbers and letters. When users register successfully, they are redirected to their unique _Profile_ page. Additional tabs are visible to the user after logging in.

- **Profile** (`profile/<username>.html`)

The profile page is unique to each user of the application. When users register successfully, they are redirected to their unique _Profile_ page where they can view, edit and delete their existing recipes. The profile page also promotes a local catering company where users can shop for any supplies needed.

- **New Recipe** (`add_recipe.html`)

The recipe page allows users to add a new recipe by submitting a form. The user will enter the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The new recipe is displayed on the homepage and the profile page.

- **Categories** (`get_categories.html`)

The categories page can be accessed by the website admin to view existing types of recipe. There is also the option to edit or delete categories. The categories currently available on this website are cocktails, smoothies and snacks. New categories can also be created by the admin and will be available for selection by other users. This function allows for expansion into different types of recipes in future development.

- **Edit Recipe** (`edit_recipe.html`)

The edit recipe page allows users to edit a new recipe by editing a form. The user will update the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. Existing recipes can also be deleted by the user who created them. The updated recipe will be contained in the collection.

- **Add Categories** (`add_category.html`)

The add categories page allows the website admin to add a new category. All categories can be selected from the drop-down in the recipe form. The primary categories on this website are cocktails, smoothies and snacks. New categories can be created by the admin. This function allows for expansion into different types of recipes in future development.

- **Edit Categories** (`edit_category.html`)

The add categories page allows the website admin to edit an existing category. All categories can be selected from the drop-down in the recipe form. The name of the category will be updated in the collection.

<span id="wireframes"></span>

## 5. Wireframes

Wireframe mockups for both desktop and mobile devices can be found in this [folder](https://github.com/alandoherty95/reciprocate-app/tree/master/resources/wireframes)

## Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://www.javascript.com/)

- [Python](https://www.python.org/)

<span id="technologies"></span>

## 6. Technologies

- [MongoDB](https://www.mongodb.com//) MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

- [Heroku](https://dashboard.heroku.com/apps) Heroku is a cloud platform as a service supporting several programming languages.

- [jQuery](https://code.jquery.com/) JQuery is a JavaScript library which I found to be a good resource.

- [Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>) is a web framework written in Python.

- [Materialize](https://materializecss.com/getting-started.html) is a modern responsive front-end framework based on Material Design.

- [GitHub](https://github.com/) GitHub was used for hosting for software development and version control using Git.

- [Coolors](https://coolors.co/) Coolors was used to generate the colour scheme.

- [Slack](https://slack.com/intl/en-ie/) Slack was used for motivation and to ask questions to peers.

- [W3 Validator](https://validator.w3.org/) W3 Validator was used to validate the HTML code.

- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) W3 CSS Validator was used to validate the CSS code.

- [JS Hint](https://jshint.com/) JS Hint was used for ensuring JavaScript code complies with coding rules.

- [Favicon.io](https://favicon.io/) Favicon was used to choose an emoji to use as my favicon.

- [Gmail](https://www.gmail.com/) Gmail was used as my inbox and for signing into different accounts.

- [Bootstrap:](https://getbootstrap.com/) Bootstrap was used to assist with the responsiveness and styling of the website.

- [Google Fonts](https://fonts.google.com/) Google Fonts was used in making the website more beautiful, fast, and open through great typography.

- [StackEdit](https://fonts.google.com/) StackEdit is a free, open-source Markdown editor used to create my README file.

- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) A Google Chrome extension to show multiple screens in one view.

- [QuickTime Player](https://support.apple.com/downloads/quicktime) QuickTime Player is an extensible multimedia framework developed by Apple Inc., capable of handling various formats of digital video, picture, sound, panoramic images, and interactivity.

- [Wireframes.cc](https://wireframe.cc/) for designing simple black and white layouts providing structure for the website.

<span id="database"></span>

## 7. Database

MongoDB was chosen as the database program for this application. It is a source-available cross-platform document-oriented database program. MongoDB's non-relational database structure was suitable because the number of collections is small as well as the relationships between them

![Overview of MongoDB Collections](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/mongodb-collections-overview.png?raw=true)

![MongoDB Record](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/mongodb-collection.png?raw=true)

| Categories | | |

| -------------------------------------------------------------------------------------------------------------------------- |

| Key | Type | Notes |

| \_id | ObjectId |

| category_name | string | The admin can add, edit or delete categories from the Categories page. |

| -------------------------------------------------------------------------------------------------------------------------- |

| Recipes | | |

| -------------------------------------------------------------------------------------------------------------------------- |

| Key | Type | Notes |

| \_id | ObjectId |

| category_name | string | Category name is selected from a drop-down list when adding a new recipe |

| created_by | string | The username of the person who shared the recipe is automatically filled. |

| image_url | string | The full image URL is entered to display a picture of the finished recipe. |

| recipe_ingredients | string | Ingredients needed for the recipe are entered in the form. |

| recipe_instructions | string | Instructions to follow when creating the recipe are entered in the form. |

| recipe_name | string | Name of the recipe is entered in the form. |

| -------------------------------------------------------------------------------------------------------------------------- |

| Users |

| -------------------------------------------------------------------------------------------------------------------------- |

| Key | Type | Notes |

| \_id | ObjectId |

| password | string | A password is chosen when registering and it is hashed using Werkzeug. |

| username | string | A unique username is chosen when registering. |

<span id="features"></span>

## 8. Features

**CRUD Functionality**

**New visitors** have the ability to:

- View all recipes shared by other members.

**Users with an account** have the ability to:

- Share their own recipes.

- View all recipes shared by other members.

- Edit their own recipes.

- Delete their own recipes.

**The admin** has the ability to:

- Share their own recipes.

- View all recipes shared by other members.

- Edit their own recipes.

- Delete their own recipes.

- Add a new category.

- Edit an existing category.

- Delete an existing category.

**Materialize CSS**:

- [Cards](https://materializecss.com/cards.html)

- [Forms](https://materializecss.com/text-inputs.html)

- [Menu dropdown](https://materializecss.com/dropdown.html)

- [Modals](https://materializecss.com/modals.html)

- [Sidenav](https://materializecss.com/sidenav.html)

**Secure Registration**

In order to register an account, the user must enter a unique username and a password. The password is hashed so it is not visible to the owner of the database. Werkzeug was used to hash the password entry when registering to the site and encrypting on MongoDB. Both the username and password must be between 4 and 20 characters, containing only numbers and letters using`a-zA-Z0-9`.

**Discover new recipes**

The homepage displays all recipes that have been shared on the application. Each selection shows the category, the recipe name and an image. Users can reveal more information about the recipe by hovering over or clicking on each selection. Users can view the suggested ingredients, instructions and the username of the person who shared the idea. Users can attempt to recreate recipes with their friends and family at home.

**Share your favourite recipes**

The application encourages all users to share their own favourite recipes with the rest of the community. The user can input the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. Users must create an account before they can share recipes.

**Edit your recipes**

In addition to adding new recipes, users can also edit recipes they have already shared with the community. The user can update the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The updated record will be contained within the collection.

**Delete your recipes**

Users have the option to delete recipes they have shared with the community. Users must confirm if they would like to delete a selection before it is removed permanently from the database. This adds an extra layer of protection to prevent records being deleted accidentally.

**Register an account**

The application encourages users to register an account for a better experience. Users are required to enter a unique `"username"` and `"password"` when registering. Username must be 4-20 characters long, containing only numbers and letters. There is a large call-to-action button on the homepage attracting users to either log in or register. Users can view all recipes without logging in. However, users are required to log in in order to share a new recipe and edit or delete an existing recipe.

**Search all recipes**

The application has a search feature allowing users to search using keywords within the `“recipe_name”`and `“recipe_ingredients”` fields. A message will display if no results are found. The search function will display results based on the keywords inputted. All users have access to the search bar without having to register.

**Error handling**

Additional pages were created to handle 404 and 500 errors on the website. Both pages will redirect users back to the homepage. These pages allow the website to handle errors gracefully.

### Features to Implement in the Future

- **Like your favourite recipes** Users will be able to like their favourite recipe ideas. Recipes with the most votes or likes will be promoted more favourably than the rest.

- **Up Vote/Down Vote** Users could have the option of voting in favour of or against certain recipes. This feature could be considered instead of a 'like' feature.

- **Share your recipes** Users could have the option of sharing their favourite recipes via email or on social media.

- **View other profiles** Users could have the option to view the profile page of other users. This would be a beneficial feature, adding to the communal feel of the application.

- **Forgot Password:** The primary design goals were to make the website easy-to-use and intuitive for users. An e-mail address will be required when creating an account for this feature to be implemented. It could be considered in future development.

- **Uploading Images:** The application is currently using full image URLs to display pictures of recipes. This is because databases store image locations as a URL and the file itself is located elsewhere. Uploading images directly could be considered in future development.

**Site Map**

![Site Map](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/site-map.png?raw=true)

- The 'About' page was created towards the end of development. This page provides more detailed information about the purpose of the application and the different components involved. It also lists frequently asked questions.

<span id="testing"></span>

## 9. Testing

Please see [TESTING.md](https://github.com/alandoherty95/reciprocate-app/blob/master/TESTING.md) file for more details.

### Version Control

Throughout the production of this application, I used [Gitpod](https://gitpod.io/) as a local repository and [GitHub](https://github.com/) as a remote repository.

**Creating a Repository**

1. Create a repository in GitHub by clicking 'New repository' in the top right corner of the main page.

2. Select the Code Institute Template from drop-down options, enter the repository name (and description).

3. Select 'Public' and then click 'Create Repository'.

4. Open the repository on Git Pod.

**Commits**

Commits were made frequently and consistently throughout the course of this project. It is important to commit often to ensure no work is lost during production. The work is saved securely in GitHub.

- **git status** checks the current status of new or modified files and folders

- **git add - A** adds files to the staging area before committing.

- **git commit -m "initial commit"** commits the work on the stage before pushing it to GitHub.

- **git push** updates the repository in GitHub to include new or modified files and folders.

<span id="deployment"></span>

## 10. Deployment

The application was deployed using [Heroku](https://www.heroku.com/). Heroku is a cloud platform with a service supporting several programming languages including Python. GitHub can host static websites but this particular project requires back-end technology such as a server and a database. I connected the GitHub repository with Heroku.

Before deploying the application to Heroku, please follow the necessary steps outlined below:

1. Create a `requirements.txt` file containing the name of packages being used in Python. The file is updated whenever new packages or modules are installed during the project.

2. Create a `Procfile` containing the name of the application file. Procfile may have a blank line when it is created so remove it as it may cause problems. The Procfile tells Heroku what to run.

3. Push the two files above to GitHub to save.

Once those steps have been completed, the application can be deployed. Please follow the necessary steps in Heroku outlined below:

1. Create an account in Heroku.

2. Click 'New' and then 'Create new app' to get started.

3. Enter a unique 'App name' and 'Choose a region'. Then click 'Create app'.

4. Navigate to the 'Deploy' tab and click 'Connect to Github'.

5. Search for the name of the repository and click 'Connect'.

6. Navigate to the 'Settings' tab, click 'Reveal Config Vars' and enter the necessary keys and values.

![Heroku Config Vars](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/heroku-config-vars.png?raw=true)

7. Navigate back to the 'Deploy' tab and click 'Enable Automatic Deploys'

8. Click 'Deploy Branch'.

9. A message will appear saying 'Your app was successfully deployed.'

10. Click 'View'.

## Code

**HTML5**

**CSS3**

**JavaScript**

**Python**

<span id="credits"></span>

## 11. Credits

- [MongoDB](https://www.mongodb.com//) for providing a scalable and flexible database system.

- [Heroku](https://dashboard.heroku.com/apps) for supplying a platform for deploying my website.

- [Materialize](https://materializecss.com/getting-started.html) for offering a modern responsive front-end framework.

- [Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>) for providing a framework including components like Jinja and Werkzeug. It was used for rendering templates, URI's, redirects, requests and flash messages.

- [BSON](https://en.wikipedia.org/wiki/BSON) was used to access the data in MongoDB and to access ID's.

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) was used to hash password entry when registering to the site and encrypting on MongoDB.

- [W3Schools](https://www.w3schools.com/) for providing a wealth of information about HTML, CSS and JavaScript. It was a very informative and beneficial resource.

- [GitHub](https://github.com/) for hosting for software development and version control.

- [Google Fonts](https://fonts.google.com/) for making the web more beautiful, fast, and open through great typography. A resource that is very easy to use.

- [Slack](https://app.slack.com/client/T0L30B202/C016NG69WG3) community is always helpful and motivating. It is great for asking questions and discussing challenges.

- [Pixabay](https://pixabay.com/) for providing a large collection of high quality images.

- [Pexels](https://www.pexels.com/) for providing striking, high resolution images.

- [Stack Overflow](https://stackoverflow.com/) for providing a platform for questions and answers by professional and enthusiast programmers.

### General Resources

- [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/) Course Material

- [Stack Overflow](https://stackoverflow.com/)

- [YouTube](https://www.youtube.com/)

- [W3schools](https://www.w3schools.com/)

- [Google](https://www.google.com/)

<span id="acknowledgements"></span>

## 12. Acknowledgements

- My Code Institute Mentor [Nishant Kumar](https://github.com/nishant8BITS/) for his continuous help and guidance.

- The Code Institute team for being available to answer any questions or queries I may have.

- My friends lent me their time to demonstrate the website while offering proposals and constructive feedback.

- My family for putting up with me during this project and for providing ideas and feedback along the way.

### Disclaimer

This website was developed for educational purposes.

<a href="#top">Return to Top</a>
