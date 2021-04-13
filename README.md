# Reciprocate

Welcome to **Reciprocate** - share your favourite recipes!

**Reciprocate** is a community-based website designed to allow users to share and contribute recipes ideas with each other. Users utilise the website to share their own data with the community, and benefit from having convenient access to the data provided by all other members. 

In preparation for this project, I conducted research on friends, colleagues and family members to identify the kind of recipes in demand. The three main recipes types we are focusing on are smoothies, cocktails and snacks. The most popular recipes will be compiled in a cookbook which can be published.

The website was designed using CRUD functionality. Create, Read, Update, and Delete (CRUD) are the four basic functions available to users of the website. 

Create — A function we can call when a new recipe is being added to the database. The user can supply the values for  `“category_name”`,  `“recipe_name”`,  `“recipe_ingredients”` and `"recipe_instructions"`. Additionally, a similar process can be followed if a user wishes to add a new recipe type to the database. The new entry is assigned a unique  `id`, which can be used to access the resource later.

Read — A function we can call to see all of the recipes currently in the database. This function does not alter the recipes in the catalog - it would simply retrieve the resource and display the results. Again, a similar process can be followed if a user wishes to display the types of recipes contained in the database. 

Update — A function we can call when information about a particular recipe must be changed. The user can supply the values for  `“category_name”`,  `“recipe_name”`,  `“recipe_ingredients”` and `"recipe_instructions"`.  After the function call, the corresponding entry in the  `recipes`  database would contain the new fields supplied. These steps can be followed if a user wishes to edit an existing category in the database. 

Delete — A function we can call to remove a particular recipe from the catalog. After this function is called, the  `recipe`  resource should contain all of the books it had before, except for the one recipe we just deleted. A similar process can be followed if a user wishes to remove a category from the database. 

## Table of Contents

1.  [**UX**]()
    
2.  [**Scope**]()
    
3.  [**Structure**]()
    
4.  [**Wireframe Mockups**]()
    
5.  [**Technologies**]()
    
6.  [**Features**]()
    
7.  [**Testing**]()
    
8.  [**Bugs**]()
    
9.  [**Deployment**]()
    
10.  [**Credits**]()
    
11.  [**Acknowledgements**]()
    

----------

## User Experience (UX)

The website was designed with a community-based approach in mind. It was created with three main objectives in mind:

-   To encourage people to share their favourite recipes with all other members
    
-   To allow convenient access to the recipes provided by all other members
    
-   To compiled the most popular recipes in a cookbook for publishing
    

As mentioned, 

**Smoothies:** are becoming more popular each year. Many people are opting for smoothies made up of fruit and vegetables as part of their daily intake. Our smoothie recipes provides users with choice while keeping up a healthy diet.

**Cocktails:** are also becoming increasingly popular among adults. People have grown to appreciate the variety of taste and beauty of these artisan drinks. Our cocktail recipes allows users to create popular drinks themselves without having to rely solely on bartenders.

**Snacks:** have also been a significant part of our diet. People have become more creative and adventurous with their snacking habits in recent years. Our snack recipes offer choice for people constantly on-the-go.


### User Stories

### Users:

-   As a proponent of health-living, I would like to share recipes for others to enjoy. 
    
-   As a health-conscious individual, I would like easy access to recipes provided by other members.
    
    

### Owner:

-   As the owner of this website, I would like to foster a community-based environment allowing users to share and contribute recipe ideas.
    
-  As the owner of this website, I would like to compile the most popular recipes in order to publish a cookbook.
    

### Design

-   #### Colour Scheme
    

-   #### Typography
    


-   #### Imagery
    
## Scope 

The minimum features to be included in this project are as follows:

-   **Home page** attracts first-time visitors and presents the purpose of the website. The two call-to-action buttons invite users to either log in or register. All recipes are displayed below.
-   **Recipe Types** allows users to manage the categories of recipes. Users can add or delete categories.
-   **Register** invites visitors to create an account in order to create new recipes as well as edit or delete recipes they have shared.
-   **Login** invites users to log in to their account. This allows users to edit or delete recipes they have shared.
-   **Logout** allows users to log out of their account.
-   **Profile** can be accessed by users when they have successfully logged in. Users can view all recipes they have shared. users can also edit or delete their recipes.
-   **Create Recipe** encourages users to share their new recipes with the community.
-   **Edit Recipe** allows users to edit their own recipes.
-   **Delete Recipe** function that users can delete their recipes.
-   **Search function** allows users to search for specific recipes using keywords.



## Structure



#### Wireframe Mockups


## Languages used

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    
-   [CSS](https://en.wikipedia.org/wiki/CSS)
    
-   [JavaScript](https://www.javascript.com/)

-   [Python](https://www.python.org/)
    

## Technologies

-   [MongoDB](https://www.mongodb.com//)  MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

-  [Heroku](https://dashboard.heroku.com/apps) Heroku is a cloud platform as a service supporting several programming languages.

-   [jQuery](https://code.jquery.com/)  JQuery is a JavaScript library which I found to be a good resource.

-   [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))  is a web framework written in Python.

-  [Materialize](https://materializecss.com/getting-started.html) is a modern responsive front-end framework based on Material Design.
    
-   [GitHub](https://github.com/)  GitHub was used for hosting for software development and version control using Git.
    
-   [Slack](https://slack.com/intl/en-ie/)  Slack was used for motivation and to ask questions to peers.
    
-   [W3 Validator](https://validator.w3.org/)  W3 Validator was used to validate the HTML code.
    
-   [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)  W3 CSS Validator was used to validate the CSS code.
    
-   [JS Hint](https://jshint.com/)  JS Hint was used for ensuring JavaScript code complies with coding rules.
    
-   [Favicon.io](https://favicon.io/)  Favicon was used to choose an emoji to use as my favicon.
    
-   [Gmail](https://www.gmail.com/)  Gmail was used as my inbox and for signing into different accounts.
    
-   [Bootstrap:](https://getbootstrap.com/)  Bootstrap was used to assist with the responsiveness and styling of the website.
    
-   [Google Fonts](https://fonts.google.com/)  Google Fonts was used in making the website more beautiful, fast, and open through great typography.
    
-   [StackEdit](https://fonts.google.com/)  StackEdit is a free, open-source Markdown editor used to create my README file.
    
-   [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)  A Google Chrome extension to show multiple screens in one view.
    
-   [QuickTime Player](https://support.apple.com/downloads/quicktime)  QuickTime Player is an extensible multimedia framework developed by Apple Inc., capable of handling various formats of digital video, picture, sound, panoramic images, and interactivity.
    

## Features


### Features to Implement in the Future


## Testing

### Feature Testing Table

### Testing - User Stories

### Further Testing


### Devices Tested



## Bugs

### Known Bugs

- Input fields are not populating on the edit_recipe page.


## Credits

- [MongoDB](https://www.mongodb.com//)  for providing a scalable and flexible database system.

-  [Heroku](https://dashboard.heroku.com/apps) for supplying a platform for deploying my website.

-  [Materialize](https://materializecss.com/getting-started.html) for offering a modern responsive front-end framework.

- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) for providing a framework including components like Jinja and Werkzeug. It was used for rendering templates, URI's, redirects, requests and flash messages.
    
- [BSON](https://en.wikipedia.org/wiki/BSON) was used to access the data in MongoDB and to access ID's
Werkzeug

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) was user to hash password entry when registering to the site and encrypting on MongoDB.

-   [W3Schools](https://www.w3schools.com/) for providing a wealth of information about HTML, CSS and JavaScript. It was a very informative and beneficial resource.
    
-   [GitHub](https://github.com/)  for hosting for software development and version control.
    
-   [Google Fonts](https://fonts.google.com/)  for making the web more beautiful, fast, and open through great typography. A resource that is very easy to use.
    
-   [Slack](https://app.slack.com/client/T0L30B202/C016NG69WG3)  community is always helpful and motivating. It is great for asking questions and discussing challenges.
    
-   [Pixabay](https://pixabay.com/)  for providing a large collection of high quality images.
    
-   [Pexels](https://www.pexels.com/)  for providing striking, high resolution images.
    
-   [Stack Overflow](https://stackoverflow.com/)  for providing a platform for questions and answers by professional and enthusiast programmers.
    

### Acknowledgements


Input Fields: https://materializecss.com/text-inputs.html
Buttons: https://materializecss.com/buttons.html