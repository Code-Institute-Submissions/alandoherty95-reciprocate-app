# TESTING.md

Welcome to **[Reciprocate](https://reciprocate-application.herokuapp.com/)** - a community for sharing and discovering recipes!

![Reciprocate Logo](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/images/reciprocate-logo.png?raw=true)

View [README](README.md) file.

View [Reciprocate](https://reciprocate-application.herokuapp.com/) application.

## Table of Contents

1. <a href="#overview">Overview</a>

2. <a href="#user-stories">User Stories</a>

3. <a href="#manual">Manual Testing</a>

4. <a href="#auto">Automated Testing</a>

5. <a href="#version-control">Version Control</a>

6. <a href="#responsive">Responsiveness</a>

7. <a href="#resolved-bugs">Resolved Bugs</a>

8. <a href="#unresolved-bugs">Unresolved Bugs</a>

---

<span id="overview"></span>

## 1. Overview

**Consistent design**

This website was designed to remain consistent wherever possible across the various pages:

- The Navigation Bar and Footer are the same on all pages, including both error handling pages.

- All headings are clear and concise with additional info below.

- Recipe cards follow a uniform size and structure.

- Buttons are standardised throughout the website using either small or large buttons with varying colours depending on the actions.

**Easy navigation**

Designing a platform with easy navigation was front of mind during the development of this project:

- The Navigation Bar and Footer contain links for easily navigating to other pages.

- Headings are clear and descriptive of the content displayed below.

- When a search finds no results, the user is prompted to try different search words.

- Most views or actions can be reached within four clicks or taps.

**Visually appealing**

- Recipe cards focus on the images uploaded by users.

- Striking images encourage users to find out more info about the recipes.

- Bright colours used for headings grabs the attention of the user.

**Intuitive design**

- In the Navigation Bar, the Reciprocate logo returns users to the homepage displaying all recipes.

- Familiar icons are used throughout the website for typical actions e.g. delete, search.

- Flash messages notify users on screen when they perform meaningful actions e.g. sharing a new recipe or logging in.

- A modal pops up to confirm deletion of recipes or categories of recipe.

- A modal reveals more info about how to upload an image if the icon is clicked while filling out form.

**Responsiveness**

- All pages respond to a variety of different screen sizes with help from the Materialize elements.

- Different sized screens were tested extensively using [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/).

- I added the`loading="lazy"`attribute to recipe images to keep loading time down as the number of images on the website increases.

**Security**

- Passwords are hashed using Werkzeug Security to ensure they are not visible to the owner of the database or anyone else.
- Users can create a secure password of between 4 and 30 characters when creating their account. Both numbers and letters can be used.

<span id="user-stories"></span>

## 2. User stories

**User Story 1:** As an individual who likes to keep a healthy lifestyle, I want to find tasty food and drink recipes to try at home.

I can open the main homepage and scroll down to quickly view all recipes that have been shared by other members of the community.

In order for this user to browse all recipes:

- Open homepage of website.

- Scroll down slightly to view ‘Our Favourite Recipes'.

- Click on any selection to view additional information about the recipe.
  ![User Story 1 Demo](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/demos/user-stories-1.gif?raw=true)

**User Story 2:** As a food lover, I would like to share recipe ideas for snacks and smoothies with other people with similar interests.

When I am logged into my profile, I can add a new recipe in just a few steps.

In order for this user to share recipe ideas:

- Open homepage of website.

- Click on the 'Log In' button.

- Enter 'Username' and 'Password' and click the 'Log In' button.

- Navigate to the 'Add New Recipe' tab in the Navigation Bar.

- Input details such as 'Recipe Type', 'Name of Recipe', 'Ingredients' and 'Instructions'.

- Click the 'Add New Recipe' button.
  ![User Story 2 Demo](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/demos/user-stories-2.gif?raw=true)

**User Story 3:** As an individual looking to improve their health and fitness, I want to easily browse through healthy recipes and try different ones.

I can open the main homepage and search using keywords to quickly view all relevant recipes.

In order for this user to browse all recipes:

- Open homepage of website.

- Enter keywords into the search bar in Navigation Bar.
- Submit search
- View recipes relating to the keywords entered.

- Click on any selection to view additional information about the recipe.
  ![User Story 3 Demo](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/demos/user-stories-3.gif?raw=true)

<span id="manual"></span>

## 3. Manual Testing

The following tests have been carried out manually without raising an issue:

**Navigation Bar**

- Navbar is visible at the top of the screen displaying:

- **Users not logged in**: Home, Log In & Register.

- **Users logged in**: Home, Profile, New Recipe & Log Out.

- **Admin logged in**: Home, Profile, New Recipe, Categories & Log Out.

- Clicking on the Reciprocate logo takes users to the homepage displaying all recipes.

- Clicking on each link takes the user to the relevant page.

- If the user is logged in, clicking 'Log Out' will remove the user from a session by logging them out.

Mobile Device:

- The hamburger menu replaces the names of each tab.

- All available menu options appear in the Side Navigation Bar when the hamburger icon is tapped.

**Footer**

- The footer appears at the bottom of each tab and remains consistent.

- Clicking on each link takes the user to the relevant page.

- Clicking on the GitPod icon will open GitPod profile in new tab.

- Clicking on the LinkedIn icon will open LinkedIn profile in new tab.

- If the user is logged in, clicking 'Log Out' will remove the user from a session by logging them out.

- An 'About' page was added to the Footer towards the end of development. This gives users more information about the application and listing frequently asked questions.

**Home page**

- Call-to-action buttons for 'Log In' or 'Register' redirect users to the appropriate form to enter their username and password.

- The search bar returns results relevant to the key words entered.

- Clicking on a card reveals more information about the recipe.

**Register page**

![Invalid Registration Form](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/invalid-register-form.png?raw=true)

- Entering a unique username and password creates a profile for the user.

- When the 'Register' button is clicked after inputting valid details, the user is redirected to their unique 'Profile' page.

- If an existing username is submitted, a flash message will notify the user: 'Unfortunately, this username already exists!'

- A flash message notifies the user: 'Registration complete!'

- Upon successful registration, the new username and password are added to the Users collection in the MongoDB database.

- Clicking on the link below the form reading 'Already registered? Log in now' redirects the user to the Log In page.

**Log In page**

![Valid Log In Form](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/valid-login-form.png?raw=true)

- When the 'Log In' button is clicked after inputting valid details, the user is redirected to their unique 'Profile' page.

- If the username and password are not matching, a flash message will notify the user: 'Incorrect Username and/or Password'

- A flash message notifies the user: 'Good to see you again, <username>!'

![Flash Message](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/flash-message.png?raw=true)

- Clicking on the link below the form reading 'Not registered yet? Register now' redirects the user to the 'Register' page.

**Profile page**

Search Function:

- After entering a term in the search field and either tapping/clicking the search icon or pressing Enter, the correct results are displayed from the fields `recipe_name` and `recipe_ingredients`.

- Clicking on the 'Clear' button reloads the page without a query.

Recipe Cards:

- All recipes in the collection are displayed with the correct name, image, ingredients, instructions and the username of the person who shared the recipe.

- Clicking on 'Edit' allows users to edit recipes submitted by them. The input fields are already populating with the current content.

- Clicking on a card reveals more information about the recipe.

**New Recipe page**

![Share New Recipe Form](https://github.com/alandoherty95/reciprocate-app/blob/master/resources/screenshots/share-new-recipe-form.png?raw=true)

- A user who is logged in can add a new recipe by entering the required field in the form.

- Input field validation functions correctly.

- Clicking the 'Add New Recipe' button:

- Adds the recipe to the 'Recipes' collection.

- Refreshes the page to allow users to easily create another recipe

- A flash message notifies the user: 'Thank you for contributing!'

**Edit Recipe page**

- A user who is logged in can edit recipes by clicking 'Edit' on any recipe card they have created

- Fields are populated correctly with current information.

- Clicking the 'Edit Recipe' button:

- Adds the recipe to the 'Recipes' collection.

- Refreshes the page to allow users to easily create another recipe

**Categories page**

- A link to "Categories' is only accessible to the admin of the website.

- All categories from the categories collection are displayed on an individual card.

- The 'Edit' button allows the admin to edit the name of each recipe type.

- The 'Delete' button allows the admin to delete each recipe type. A modal pops up to confirm before deleting category.

**About page**

- The 'About' page provides more information about the application.

- It contains a list frequently asked questions.

**404 page**

- The '404 Page Not Found' error handling page displays if users end up on an invalid page.

- The prominent 'Return to Home' button redirects users back to the homepage.

**500 page**

- The '500 Page Not Found' error handling page displays if the server encountered an unexpected condition that prevented it from fulfilling the request.

- The prominent 'Return to Home' button redirects users back to the homepage.

<span id="auto"></span>

## 4. Automated Testing

![Desktop Report]()

![Mobile Report]()

<span id="version-control"></span>

### Lighthouse Opportunities

- Properly size images: Serve images that are appropriately-sized to save cellular data and improve load time

- Defer offscreen images: Consider lazy-loading offscreen and hidden images after all critical resources have finished loading to lower time to interactive.

- Eliminate render-blocking resources: Resources are blocking the first paint of your page. Consider delivering critical JS/CSS inline and deferring all non-critical JS/styles.

- Remove unused JavaScript: Remove unused JavaScript to reduce bytes consumed by network activity

- Remove unused CSS: Remove dead rules from stylesheets and defer the loading of CSS not used for above-the-fold content to reduce unnecessary bytes consumed by network activity

- Image elements do not have explicit `width` and `height`

- Set an explicit width and height on image elements to reduce layout shifts and improve CLS.

- Displays images with incorrect aspect ratio: Image display dimensions should match natural aspect ratio.

- Document does not have a meta description: Meta descriptions may be included in search results to concisely summarise page content.

## 5. Version Control

Throughout the production of this application, I used [Gitpod](https://gitpod.io/) as a local repository and [GitHub](https://github.com/) as a remote repository.

-- **Creating a Repository** --

1. Create a repository in GitHub by clicking 'New repository' in the top right corner of the main page.

2. Select the Code Institute Template from drop-down options, enter the repository name (and description).

3. Select 'Public' and then click 'Create Repository'.

4. Open the repository on Git Pod.

— **Commits** — Commits were made frequently and consistently throughout the course of this project. It is important to commit often to ensure no work is lost during production. The work is saved securely in GitHub.

- **git status** checks the current status of new or modified files and folders

- **git add - A** adds files to the staging area before committing.

- **git commit -m "commit description"** commits the work on the stage before pushing it to GitHub.

- **git push** updates the repository in GitHub to include new or modified files and folders.

<span id="deployment"></span>

## 6. Deployment

The application was deployed using [Heroku](https://www.heroku.com/). Heroku is a cloud platform with a service supporting several programming languages including Python. GitHub can host static websites but this particular project requires back-end technology such as a server and a database. I connected the GitHub repository with Heroku.

Before deploying the website to Heroku, please follow the necessary steps outlined below:

1. Create a `requirements.txt` file containing the name of packages being used in Python. The file is updated whenever new packages or modules are installed during the project.

2. Create a `Procfile` containing the name of the application file. Procfile may have a blank line when it is created so remove it as it may cause problems

3. Push the two files above to GitHub to save.

Once those steps are done, the website can be deployed and below are the steps of the deployment in Heroku.

1. Create an account in Heroku.

2. Click 'New' and then 'Create new app' to get started.

3. Enter a unique 'App name' and 'Choose a region'. Then click 'Create app'.

4. Navigate to the 'Deploy' tab and click 'Connect to Github'.

5. Search for the name of the repository and click 'Connect'.

6. Navigate to the 'Settings' tab, click 'Reveal Config Vars' and enter the necessary keys and values.

7. Navigate back to the 'Deploy' tab and click 'Enable Automatic Deploys'

8. Click 'Deploy Branch'.

9. A message will appear saying 'Your app was successfully deployed.'

10. Click 'View'.

<span id="resolved"></span>

## 7. Resolved Bugs

- Deletion modal was not functioning, the modal used for confirming an action before deleting was not popping up and the selection was deleted without confirmation: the class `modal-trigger` was added to the modal function to trigger to pop up window before deleting the record.

- Background and foreground colours do not have a sufficient contrast ratio. Low-contrast text is difficult or impossible for many users to read: Colour scheme was altered to be more visually pleasing.

- Favicon not displaying: graphic image displayed correctly after changing the file path. Favicon is visible on desktop and mobile devices.

- Form fields not populating when editing a recipe, the existing information was not displayed in each of the fields to allow editing: tweaked input to `value="{{ recipe.recipe_name }}"`. The fields are populating automatically now based on the `recipe_id`.

- Search feature was functioning but it did not display the search words that were inputted after submitting. The `{page_heading}` variable was added to display the missing information. e.g. `"Showing results for: banana"`

- Search feature was displaying results based on the `recipe_name` and `recipe_ingredients`. The `category_name` was added to the index to ensure these results were also returned.

- The recipe images did not fit well within the card. The `-o-object-fit: contain;`styling was added so the image will keep its aspect ratio, but is resized to fit within the given dimension.

- The homepage was loading slowly due to the large number of images. I changed the number of recipes displayed per page from 9 to 6 using pagination. This improved the loading speed of the site and gave more attention to the 6 recipes displayed on each tab.

- Lighthouse identified buttons with an icon but no label and advised using the `aria-label` attribute. This attribute is used to provide the label to any assistive technologies.

- The drop-down field in the add recipe form changed colour back to red after selecting next field. The colour was corrected to green in the JS code and resolved this minor issue.

- Added `input type="url"` to the add recipe form to allow users to input the full image url when sharing a recipe. The image will be displayed on the recipe card.

<span id="unresolved"></span>

## 8. Unresolved Bugs

- Materialize select dropdown does not function correctly on iOS: known bug with Materialize meaning either the dropdown does not appear or selects the wrong item when tapped/clicked. I read more information about this possible bug on [Stack Overflow](https://stackoverflow.com/questions/52850091/materialize-select-and-dropdown-touch-event-selecting-wrong-item)

- Warning reported by Chrome console, `[DOM] Input elements should have autocomplete attributes`: Resolution: added `autocomplete` to Register and Log In inputs.

**Issues reported by GitPod**

Special characters must be escaped : [ > ] [Jinja documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping) suggested escaping the `>` character, this warning persists in the console.

Doctype must be declared first: This issue relates to GitPod's inability to recognise the `!DOCTYPE html` in the base.html, is being passed through to all other HTML templates.

<a href="#top">Return to Top</a>
