## User stories
 
 
**Consistency**
 
 
This website was designed to remain consistent wherever possible across the various pages:
 
 
- The Navigation Bar and Footer are the same across all pages, including both error handling pages.
 
- All headings are clear and consistent on each page.
 
- Recipe cards follow a uniform size and structure.
 
- Buttons are standardised throughout the website using either small or large buttons with the same styling.
 
 
**Easy navigation**
 
 
Designing a platform with easy navigation was front of mind during the development of this project:
 
 
- The Navigation Bar and Footer contain links for easily navigating to other pages.
 
- Headings are clear and descriptive of the content displayed below.
 
- When a search finds no results, the user is prompted to try different search words or to clear the search.
 
- Most views or actions can be reached within four clicks or taps.
 
 
**Intuitive design**
 
 
- In the Navigation Bar, the Reciprocate logo returns users to the homepage displaying all recipes.
 
- Familiar icons are used throughout the website for typical actions e.g. add, edit, delete, search, logout.
 
- Flash messages notify users on screen when they perform meaningful actions e.g. adding a new recipe or logging in.
 
- A modal pops up to confirm deletion of recipes or categories of recipe.
 
 
**Responsiveness**
 
 
- All pages respond to a variety of different screen sizes with help from the Materialize elements.
 
- Different sized screens were tested extensively using Chrome Dev Tools.
 
- I added the`loading="lazy"`attribute to recipe images to keep loading time down as the number of images on the website increases.
 
 
**Security**
 
 
- Passwords are hashed using Werkzeug Security to ensure they are not visible to the owner of the database or anyone else.
 
 
**Visually appealing**
 
 
- Design using cards focus on the images uploaded by users.
 
- Striking images were used to attract users to the website.
 
- Bright colours used for headings grabs the attention of the user towards the content.
 
 ### Testing - User Stories
 
**User Story 1:**  As an individual who likes to keep a healthy lifestyle, I want to find tasty food and drink recipes to try at home.
 
I can open the main homepage and scroll down to quickly view all recipes that have been shared by other members of the community.
 
In order for this user to browse all recipes:
 
-   Open homepage of website.
  
-   Scroll down slightly to view ‘Our Favourite Recipes'.
  
-   Click on any selection to view additional information about the recipe.
  
 
**User Story 2:**  As a food lover, I would like to share recipe ideas for healthy snacks and smoothies with other people with similar interests.
 
When I am logged into my profile, I can add a new recipe in just a few steps.
 
In order for this user to share recipe ideas:
 
-   Open homepage of website.
  
-   Click on the 'Log In' button.
  
-   Enter 'Username' and 'Password' and click the 'Log In' button.
  
-   Navigate to the 'Add New Recipe' tab in the Navigation Bar.
  
-   Input details such as 'Recipe Type', 'Name of Recipe', 'Ingredients' and 'Instructions'.
  
-   Click the 'Add New Recipe' button.
  
 
**User Story 3:**  As an individual looking to improve their health and fitness, I want to easily browse through healthy recipes and try different ones.
 
I can open the main homepage and scroll down to quickly view all recipes that have been shared by other members of the community.
 
In order for this user to browse all recipes:
 
-   Open homepage of website.
  
-   Scroll down slightly to view ‘Our Favourite Recipes'.
  
-   Click on any selection to view additional information about the recipe.
 
## Manual testing
 
 
The following tests have been carried out manually without raising an issue:
 
 
**Navigation Bar**
 
 
- Navbar is visible at the top of the screen displaying:
 
- **Users not logged in**: Home, Log In & Register.
 
- **Users logged in**: Home, Profile, New Recipe & Log Out.
 
- **Admin logged in**: Home, Profile, New Recipe, Recipe Types & Log Out.
 
- Clicking on the Reciprocate logo takes users to the homepage displaying all recipes.
 
- Clicking on each link takes the user to the relevant page.
 
- If the user is logged in, clicking 'Log Out' will remove the user from a session by logging them out.
 
 
Mobile Device:
 
 
- The hamburger menu replaces the names of each tab.
 
- All available menu options appear in the Side Navigation Bar when the hamburger icon is tapped.
 
 
**Footer**
 
 
- The footer appears at the bottom of each tab and remains consistent.
 
- Clicking on each link takes the user to the relevant page.
 
- If the user is logged in, clicking 'Log Out' will remove the user from a session by logging them out.
 
 
**Home page**
 
 
- Call-to-action buttons for 'Log In' or 'Register' redirect users to the appropriate form to enter their username and password.
 
- The search bar returns results relevant to the key words entered.
 
- Clicking on a card reveals more information about the recipe.
 
 
**Register page**
 
 
- Entering a unique username and password creates a profile for the user.
 
- When the 'Register' button is clicked after inputting valid details, the user is redirected to their unique 'Profile' page.
 
- If an existing username is submitted, a flash message will notify the user: 'Unfortunately, this username already exists!'
 
- A flash message notifies the user: 'You have successfully registered!'
 
- Upon successful registration, the new username and password are added to the Users collection in the MongoDB database.
 
- - Clicking on the link below the form reading 'Already registered? Log in now' redirects the user to the Log In page.
 
 
**Log In page**
 
 
- When the 'Log In' button is clicked after inputting valid details, the user is redirected to their unique 'Profile' page.
 
- If the username and password are not matching, a flash message will notify the user: 'Incorrect Username and/or Password Entered!'
 
- A flash message notifies the user: 'Welcome to your profile, <username>!'
 
- Clicking on the link below the form reading 'Not registered yet? Register now' redirects the user to the 'Register' page.
 
 
**Profile page**
 
 
Search function:
 
 
- After entering a term in the search field and either tapping/clicking the search icon or pressing Enter, the correct results are displayed from the fields `recipe_name` and `recipe_ingredients`.
 
- Clicking on the 'Clear' button reloads the page without a query.
 
 
Recipe Cards:
 
 
- All recipes in the collection are displayed with the correct name, image, ingredients, instructions and the username of the person who shared the recipe.
 
- Clicking on 'Edit' allows users to edit recipes submitted by them. The input fields are already populating with the current content.
 
- Clicking on a card reveals more information about the recipe.
 
-
 
**New Recipe page**
 
 
- A user who is logged in can add a new recipe by entering the required field in the form.
 
- Input field validation functions correctly.
 
- Clicking the 'Add New Recipe' button:
 
- Adds the recipe to the 'Recipes' collection.
 
- Refreshes the page to allow users to easily create another recipe
 
- A flash message notifies the user: 'New recipe was successfully added!'
 
 
**Edit Recipe page**
 
 
- A user who is logged in can edit recipes by clicking 'Edit' on any recipe card they have created
 
- Fields are populated correctly with current information.
 
- Clicking the 'Edit Recipe' button:
 
- Adds the recipe to the 'Recipes' collection.
 
- Refreshes the page to allow users to easily create another recipe
 
 
**Recipe Types page**
 
 
- A link to "Recipe Types' is only accessible to the admin of the website.
 
- All recipe types from the categories collection are displayed on an individual card.
 
- The 'Edit' button allows the admin to edit the name of each recipe type.
 
- The 'Delete' button allows the admin to delete each recipe type. A modal pops up to confirm before deleting category.
 
 
**404 page**
 
 
- The '404 Page Not Found' error handling page displays if users end up on an invalid page.
 
- The prominent 'Return to Home' button redirects users back to the homepage.
 
 
**500 page**
 
 
- The '500 Page Not Found' error handling page displays if the server encountered an unexpected condition that prevented it from fulfilling the request.
 
- The prominent 'Return to Home' button redirects users back to the homepage.
 
 
## Version Control
 
Throughout the production of this application, I used  [Gitpod](https://gitpod.io/)  as a local repository and  [GitHub](https://github.com/)  as a remote repository.
 
--  **Creating a Repository**  --
 
1.  Create a repository in GitHub by clicking 'New repository' in the top right corner of the main page.
2.  Select the Code Institute Template from drop-down options, enter the repository name (and description).
3.  Select 'Public' and then click 'Create Repository'.
4.  Open the repository on Gitpod.
 
—  **Commits**  — Commits were made frequently and consistently throughout the course of this project. It is important to commit often to ensure no work is lost during production. The work is saved securely in GitHub.
 
-   **git status**  checks the current status of new or modified files and folders
-   **git add - A**  adds files to the staging area before committing.
-   **git commit -m "initial commit"**  commits the work on the stage before pushing it to GitHub.
-   **git push**  updates the repository in GitHub to include new or modified files and folders.
 
## Deployment
 
The application was deployed using  [Heroku](https://www.heroku.com/). Heroku is a cloud platform with a service supporting several programming languages including Python. GitHub can host a static websites but this particular project requires back-end technology such as a server and a database. I connected the GitHub repository with Heroku.
 
Before deploying the website to Heroku, please follow the necessary steps outlined below:
 
1.  Create a  `requirements.txt`  file containing the name of packages being used in Python. The file is updated whenever new packages or modules are installed during the project.
2.  Create a  `Procfile`  containing the name of the application file. Procfile may have a blank line when it is created so remove it as it may cause problems
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
10.  Click 'View'.

