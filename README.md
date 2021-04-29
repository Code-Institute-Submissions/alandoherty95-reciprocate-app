[Reciprocate](https://reciprocate-application.herokuapp.com/)

Welcome to **Reciprocate** - a community for sharing your favourite recipes!

@@ Insert mockups
@@ Insert live demo

<span id="top"></span>

**Reciprocate** is a community-based website aimed at anyone who enjoys trying new recipe ideas or sharing their favourites recipes with the world. It is designed to allow users to share and contribute recipes with each other. Users can share their own food and drink ideas with the community and conveniently access the recipes provided by all other members. The website was designed with simplicity and ease-of-use in mind so people of all ages can get involved.

## [Table of Contents]()

1.  <a href="#context">**Context**</a>
2.  <a href="#ux">**User Experience (UX)**</a>
3.  <a href="#scope">**Scope**</a>
4.  <a href="#structure">**Structure**</a>
5.  <a href="#wireframes">**Wireframes**</a>
6.  <a href="#technologies">**Technologies**</a>
7.  <a href="#database">**Database**</a>
8.  <a href="#features">**Features**</a>
9.  <a href="#testing">**Testing**</a>
10. <a href="#deployment">**Deployment**</a>
11. <a href="#credits">**Credits**</a>
12. <a href="#acknowledgments">**Acknowledgements**</a>

<span id="context"></span>

## Context

In preparation for this project, I conducted research on friends, colleagues and family members to identify the kind of recipes in demand. The three main recipes types we are focusing on are smoothies, cocktails and healthy snacks. The website admin has the capability to add additional recipes types for selection.

The website was designed using CRUD functionality. Create, Read, Update, and Delete are the four primary functions available to users of the website.

Create — A function we can call when a new recipe is being added to the database. The user can supply the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The new entry is assigned a unique `id`, which can be used to access the resource later. The website admin has the capability to create new recipes types for selection.

Read — A function we can call to see all of the recipes currently in our database. This function does not alter the recipes in the catalog - it simply retrieves the information and displays the results. Again, a similar process can be followed if the website admin wishes to view the recipes types contained in the database.

Update — A function we can call when information about a particular recipe must be changed. The user can edit the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. After the function is called, the corresponding entry in the `recipes` database would contain the new fields provided. This option is only available to the creator of the recipe. These steps can be followed if the website admin wishes to edit an existing recipe type in the database.

Delete — A function we can call to remove a particular recipe from the catalog. After this function is called, the `recipe` resource should contain all of the books it had before, except for the one recipe we just deleted. This option is only available to the creator of the recipe. A similar process can be followed if the website admin wishes to remove a recipe type from the database.

<span id="ux"></span>

## User Experience (UX)

### Overview

The website was designed with a community-based approach in mind. It was created with three main objectives in mind:

- To encourage people to share their favourite recipes with all other members
- To allow convenient access to the recipes provided by all other members
- To promote a local catering supplier

The website focuses on the following three types of recipes but it is not limited. Users can choose to add a new category for different recipe types.

**Smoothies:** are becoming more popular each year. Many people are opting for smoothies made up of fruit and vegetables as part of their daily intake. Our smoothie recipes provide users with choice while keeping up a healthy diet.

**Cocktails:** are also becoming increasingly popular among adults. People have grown to appreciate the variety of taste and beauty of these artisan drinks. Our cocktail recipes allow users to create popular drinks themselves without having to rely solely on bartenders.

**Healthy Snacks:** have also been a significant part of our diet. People have become more creative and adventurous with their snacking habits in recent years. Our snack recipes offer choice for people constantly on-the-go.

### User Stories

#### As a first-time visitor, I want to:

- Immediately understand the purpose of the website
- Easily create an account
- Browse all recipes without having to register
- Be able to search for keywords

#### As a returning visitor, I want to:

- Log in and out easily
- Add new recipes quickly and easily
- Edit or delete recipes I have already shared
- View all recipes I have shared on my profile

### Users:

- As an individual who likes to keep a healthy lifestyle, I want to find tasty food and drink recipes to try at home.
- As a food lover, I would like to share recipe ideas for healthy snacks and smoothies with other people with similar interests.
- As an individual looking to improve their health and fitness, I want to easily browse through healthy recipes and try different ones.

### Owner:

- As the owner of this website I would like to provide a platform to encourage users to share their favourite recipes with other members of the community.
- As the owner, I want users to browse and find recipes that suit their tastes.
- As the owner, I want to allow users to create additional recipe types if they would like.
- As the owner, I want to promote a local catering supplies company.

### Design

- #### Colour Scheme

  The colour scheme chosen for this project was inspired by natural colours found in fruit and vegetables. These colours give the website an attractive, vibrant look.

@@ Insert colour scheme

- #### Typography
- #### Imagery
  Images used on this website were chosen from [Pexels](https://www.pexels.com/).

<span id="scope"></span>

## Scope

The minimum features to be included in this project are as follows:

- **Home page** attracts first-time visitors and presents the purpose of the website. The two call-to-action buttons invite users to either log in or register. All recipes in our database are displayed below.
- **Recipe Types** allows the website admin to manage the categories of recipe. The admin can add or delete categories. Users can select from any recipe type in the database when creating a new recipe.
- **Register** invites visitors to create an account in order to share new recipes as well as edit or delete recipes they have already shared.
- **Login** invites users to log in to their account. This allows users to view, edit or delete recipes they have already shared as well as sharing new recipe ideas.
- **Logout** allows users to log out of their account with one click of a button.
- **Profile** can be accessed by users when they have successfully logged in. Users can view all recipes they have shared. Users can also edit or delete their recipes.
- **Create Recipe** encourages users to share their new recipes with the community.
- **Edit Recipe** allows users to edit their own recipes.
- **Delete Recipe** function that users can delete their recipes. A modal pop up will ask the user to confirm action before deleting.
- **Search function** allows users to search for specific recipes using keywords.

<span id="structure"></span>

## Structure

### Structure Plane

**Front-End**

- **Home** (`recipes.html`)  
  The welcome page outlines the main purpose of the website. In the top navigation bar, there is a logo and tabs for the _Home_, _Login_ and _Register_ pages. There are two call-to-action buttons encouraging users to either log in or register. By scrolling down, users can browse all recipes in our database and search using keywords.
- **Log In** (`login.html`)  
  The log in page allows users who already have an account to log in to their profile. When users log in successfully, they are redirected to their unique _Profile_ page. Additional tabs are visible to the user after logging in.
- **Register** (`register.html`)  
  The registration page allows users to create an account by entering a distinct username and password. When users register successfully, they are redirected to their unique _Profile_ page. Additional tabs are visible to the user after logging in.
- **Profile** (`profile/<username>.html`)  
  The profile page is unique to each user of the application. When users register successfully, they are redirected to their unique _Profile_ page. All recipes shared by the user are displayed on their profile page.
- **New Recipe** (`add_recipe.html`)  
  The recipe page allows users to add a new recipe by submitting a form. The user will enter the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. The new recipe is displayed on the homepage and the profile page.
- **Recipe Types** (`get_categories.html`)  
  The recipe types page can be used by the website admin to view existing types of recipe. There is also the option to edit or delete recipe types. New categories can also be created by the admin.
- **Edit Recipe** (`edit_recipe.html`)  
  The edit recipe page allows users to edit a new recipe by editing a form. The user will update the fields for`“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. Existing recipes can also be deleted by the user who created them.
- **Add Recipe Types** (`add_category.html`)  
  The add recipe types page allows the website admin to add a new recipe type. All categories can be selected from the drop-down in the recipe form.
- **Edit Recipe Types** (`edit_category.html`)  
  The add recipe types page allows the website admin to edit an existing category. All categories can be selected from the drop-down in the recipe form.

<span id="wireframes"></span>

## Wireframes

Wireframe mockups can be found in this [folder](https://github.com/alandoherty95/reciprocate-app/tree/master/resources)

## Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

<span id="technologies"></span>

## Technologies

- [MongoDB](https://www.mongodb.com//) MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.
- [Heroku](https://dashboard.heroku.com/apps) Heroku is a cloud platform as a service supporting several programming languages.
- [jQuery](https://code.jquery.com/) JQuery is a JavaScript library which I found to be a good resource.
- [Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>) is a web framework written in Python.
- [Materialize](https://materializecss.com/getting-started.html) is a modern responsive front-end framework based on Material Design.
- [GitHub](https://github.com/) GitHub was used for hosting for software development and version control using Git.
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

## Database

MongoDB was chosen as the database program for this application. It is a source-available cross-platform document-oriented database program. MongoDB's non-relational database structure was suitable because the number of collections is small as well as the relationships between them.

| Categories    |          |                                                                                                                |
| ------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| Key           | Type     | Notes                                                                                                          |
| \_id          | ObjectId |                                                                                                                |
| category_name | string   | Category name is also called recipe types. The admin can add, edit or delete recipe types from the Types page. |

| Recipes             |          |                                                                          |
| ------------------- | -------- | ------------------------------------------------------------------------ |
| Key                 | Type     | Notes                                                                    |
| \_id                | ObjectId |                                                                          |
| category_name       | string   | Category name is selected from a drop-down list when add a new recipe    |
| created_by          | string   | The username of the person who shared the recipe.                        |
| image_url           | string   | The full image URL is entered to display a picture of the finished good. |
| recipe_ingredients  | string   | Ingredients needed for the recipe are entered in the form.               |
| recipe_instructions | string   | Instructions to follow when creating the recipe are entered in the form. |
| recipe_name         | string   | Name of the recipe is entered in the form.                               |

| Users    |          |                                                                        |
| -------- | -------- | ---------------------------------------------------------------------- |
| Key      | Type     | Notes                                                                  |
| \_id     | ObjectId |                                                                        |
| password | string   | A password is chosen when registering and it is hashed using Werkzeug. |
| username | string   | A unique username is chosen when registering.                          |

<span id="features"></span>

## Features

**Materialize CSS**:

- [Cards](https://materializecss.com/cards.html)
- [Forms](https://materializecss.com/text-inputs.html)
- [Menu dropdown](https://materializecss.com/dropdown.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)

**Secure Registration**

In order to register an account, the user must enter a unique username and a password. The password is hashed so it is not visible to the owner of the database. Werkzeug was used to hash the password entry when registering to the site and encrypting on MongoDB.

**CRUD functionality**

New visitors have the ability to:

- View all recipes shared by other members.

Users with an account have the ability to:

- Share their own recipes.
- View all recipes shared by other members.
- Edit their own recipes.
- Delete their own activities.

The admin has the ability to:

- Share their own recipes.
- View all recipes shared by other members.
- Edit their own recipes.
- Delete their own activities.
- Add a new recipe type.
- Edit an existing recipes type.
- Delete an existing recipes type.

---

- **Discover new recipes**  
  The homepage displays all recipes that have been shared on the application. Each selection shows the recipe type, the recipe name and an image. Users can reveal more information about the recipe by clicking on each selection. Users can view the suggested ingredients, instructions and the username of the person who shared the idea.
- **Share your favourite recipes**  
  The application encourages all users to share their own favourite recipes with the rest of the community. The user can input the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. Additionally, a similar process can be followed if a user wishes to add a new recipe type to the database.
- **Edit your recipes**  
  In addition to adding new recipes, users can also edit recipes they have already submitted. The user can update the values for `“category_name”`, `“recipe_name”`, `“recipe_ingredients”`, `"recipe_instructions"` and `"image_url"`. Similar steps can be followed if a user wishes to add a new recipe type to the database.
- **Delete your recipes**  
  Users have the option to delete recipes they have submitted. Users must confirm they would like to delete a selection before it is removed from the database.
- **Register an account**  
  The application encourages users to register an account for a better experience. Users are required to enter a unique `"username"` and `"password"` when registering. There is a large call-to-action button on the homepage attracting users to either log in or register. Users can view all recipes without logging in. However, users are required to log in in order to share a new recipe and edit or delete an existing recipe.

### Features to Implement in the Future

- **Like your favourite recipes**  
  Users will be able to like their favourite recipe ideas. Recipes with the most votes or likes will be promoted more favourably than the rest.
- **Up Vote/Down Vote** Users could have the option of voting in favour of or against certain recipes. This feature could be considered instead of a 'like' feature.
- **Share your recipes** Users could have the option of sharing their favourite recipes via email or on social media.

<span id="testing"></span>

## Testing

Please see [TESTING.md](https://github.com/alandoherty95/reciprocate-app/blob/master/TESTING.md) file for more details.

### Version Control

Throughout the production of this application, I used [Gitpod](https://gitpod.io/) as a local repository and [GitHub](https://github.com/) as a remote repository.

**Creating a Repository**

1.  Create a repository in GitHub by clicking 'New repository' in the top right corner of the main page.
2.  Select the Code Institute Template from drop-down options, enter the repository name (and description).
3.  Select 'Public' and then click 'Create Repository'.
4.  Open the repository on Git Pod.

**Commits**
Commits were made frequently and consistently throughout the course of this project. It is important to commit often to ensure no work is lost during production. The work is saved securely in GitHub.

- **git status** checks the current status of new or modified files and folders
- **git add - A** adds files to the staging area before committing.
- **git commit -m "initial commit"** commits the work on the stage before pushing it to GitHub.
- **git push** updates the repository in GitHub to include new or modified files and folders.

<span id="deployment"></span>

## Deployment

The application was deployed using [Heroku](https://www.heroku.com/). Heroku is a cloud platform with a service supporting several programming languages including Python. GitHub can host static websites but this particular project requires back-end technology such as a server and a database. I connected the GitHub repository with Heroku.

Before deploying the website to Heroku, please follow the necessary steps outlined below:

1.  Create a `requirements.txt` file containing the name of packages being used in Python. The file is updated whenever new packages or modules are installed during the project.
2.  Create a `Procfile` containing the name of the application file. Procfile may have a blank line when it is created so remove it as it may cause problems
3.  Push the two files above to GitHub to save.

Once those steps are done, the website can be deployed and below are the steps of the deployment in Heroku.

1.  Create an account in Heroku.
2.  Click 'New' and then 'Create new app' to get started.
3.  Enter a unique 'App name' and 'Choose a region'. Then click 'Create app'.
4.  Navigate to the 'Deploy' tab and click 'Connect to Github'.
5.  Search for the name of the repository and click 'Connect'.
6.  Navigate to the 'Settings' tab, click 'Reveal Config Vars' and enter the necessary keys and values.
7.  Navigate back to the 'Deploy' tab and click 'Enable Automatic Deploys'
8.  Click 'Deploy Branch'.
9.  A message will appear saying 'Your app was successfully deployed.'
10. Click 'View'.

## Code

**HTML5**

**CSS3**

**JavaScript**

**Python**

### Contents

### Media

### Images

- Images for recipes were found in [Pexels](https://www.pexels.com/)

## Bugs

### Known Bugs

- Edit Recipe form fields not populating: when editing a recipe, the existing information was not displayed in each of the fields to allow editing.
- Deletion modal not functioning: The modal used for confirming an action before deleting was not popping up and the selection was deleted without confirmation
- Error in console due to one or more images not displaying.
- Website is loading slowly due to large number of images, compress images?
- Recipe Types page is not displaying, only accessible for admin, enable admin function for username: aland

<span id="credits"></span>

## Credits

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

- Code Institute Course Material
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

<span id="acknowledgements"></span>

## Acknowledgements

- My Code Institute Mentor [Nishant Kumar](https://github.com/nishant8BITS/) for his continuous help and guidance.
- The Code Institute team for being available to answer any questions or queries I may have.
- My friends lent me their time to demonstrate the website while offering proposals and constructive feedback.
- My family for putting up with me during this project and for providing ideas and feedback along the way.

<a href="#top">Return to Top</a>
