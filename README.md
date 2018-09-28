# Raw Dessert Recipes

This a Raw Dessert Recipes website, built using **Flask**, a Python micro-framework. This is a data-driven application, and the target audience is any user who would like to easily access, add new, update and delete recipes.

## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed the Code Institute learnings to date and Bootstrap themes to extract design ideas.
2. **User Stories** - Walked through user stories.
    1. **Navbar - Home** - As a user, I want to be able to understand the health benefits of raw desserts and the functionality of this website.
    2. **Navbar - Recipes** - As a user, I want to be able to easily access, update and delete recipes.
    3. **Navbar - New Recipes** - As a user, I want to be able to add new recipes, to the website for other users to access.
    4. **Navbar - Contact** - As a user, I want to be able to contact the webite developers to offer feedback and suggestions.
    5. **Footer - Social Links** - As a user, I want to be able to follow the Raw Dessert Recipes on social media, to be a part of the raw community and interact with this community online.
3. **Wireframe** - Sketched the wireframe on paper, to include the features for each user story.

## Features

### Existing Features
The following section describes all the front-end features in this project.

1. **Navbar - Home** - Provide users with a navbar menu, which brings users to the home page. The home page includes a summary on the health benefits of raw food and a brief description about the website.
2. **Navbar - Recipes** - Provides users with a navbar menu, which brings users to the recipes page. Recipe details can be viewed by selecting 'View Recipe'. The recipe selected is then displayed, which contains a recipe title, description, ingredients, instructions, author and date posted. Users are also provided with an 'Update Recipe' and 'Delete Forever' button, which allows them to update all areas of a recipe or delete a recipe from the website. Both buttons have Javascript alerts to ensure the user is provided with an opportunity to change their mind before applying changes.
3. **Navbar - New Recipes** - Provides users with a navbar menu, which brings users to the new recipes page and form. This page allows users to add brand new recipes, which are displayed on the recipes page.
4. **Navbar - Contact** - Provides users with a navbar manu item, which brings users to the contact page form, which allows users to contact the website developers to offer feedback and suggestions (not wired up to an email address as this is not a real business).
5. **Footer - Social Links** - Provides users with links to the website social media pages (no links for this project as its not a real business).

### Features to Implement
1. **Recipe Authors** - Add a feature to include user registration and a seperate page showing all recie authors.
2. **Blog** - Add a feature to include a blog page.
3. **Recipe Image** - Add a feature to build in a feature to upload an image related to the recipe.
4. **Recipe Details** - Add a feature to display recipe ingredients and instructions as lists, displaying information on seperate lines.
5. **Datepicker** - Add a date picker into the Date Posted field to maintain the same date format throughout.
6. **Search, Sort, Filter, Pagination** - Add these type of features to facilitate the recipe page growing.
7. **Prep Time** - Add a feature to include prep time.

## Technologies Used
The following section describes all technologies and tools used to construct this project.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - This project used **Cloud 9**, online integrated development environment, to construct the code end to end.
- [Bootstrap](https://getbootstrap.com/)
    - This project used **Bootstrap**, a library of website themes. The [Business Casual Template](https://startbootstrap.com/template-overviews/business-casual/), was used for this project.
        - **Static folder**: All files except `custom.css`, `custom.js`, `bg.jpg`,`intro.jpg`, were copied from the bootstrap template.
        - **.html files**: All `.html` files used the bootstrap `.html` files as boiler plate code. The project developer then amended and built upon each of these files to suit this project.
        - **gilpfile.js, package-lock.json, package.json**: Each of these files were included with the boostrap template.
        - **All Other Code**: Compiled by the project developer.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask**, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.
- [mLab](https://mlab.com/)
    - This project uses **mLab**, a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. The developer used an mLab sandbox DB, which is for learning and prototyping. Json value pairs were added into the mLab document to align with the recipe wireframe. For example, Recipe_Title: Title.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **mongoDB**, a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata. 
- [MongoDB](https://www.mongodb.com/)
    - This project uses **mongoDB**, a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata. 
- [Jinga](http://jinja.pocoo.org/)
    - This project uses **Jinja**, a template engine for Python, which is included within the curly brackets.
- [Python](https://www.python.org/)
    - This project uses **Python**, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which was written in this project within the `.html` files.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - This project uses **JavaScript**, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project backup.
- [Heroku](https://www.heroku.com/home)
    - This project uses **Heroku**, a web hosting service that supports Python applications, for final project deployment.
- [All Other Technologies](https://startbootstrap.com/template-overviews/clean-blog/)
    - All other technologies within this project were included with the Bootstrap template.

## Testing
The following is an overview of testing to ensure all functionality works as intended in this project.

1. **Navbar - Home**:
    1. Select 'Contact' on the navbar and move the user away from the home page.
    2. Select 'Home' on the navbar.
    3. Verify that 'Home' is highlighted on the navbar and that the user is moved to the home page.
    4. Verify that the page header, footer, social links, image and text are displayed.
        - **Bug 1** - Application not rednering in browser.
            - **Issue** - app.py `'@app.route('add_recipe')`.
            - **Fix** - Added missing `/`, to `@app.route('/add_recipe')`.
        - **Bug 2** - Application not rednering in browser.
            - **Issue** - Incorrectly spelled code as `{{ endfor }}`.
            - **Fix** - Scanned all code. Updated jinja code to `{% endfor %}`. 
        - **Bug 3** - Home is not highlighted on the navar.
            - **Issue** - Overwrote bootstrap nav html tags, losing bootstrap div styling classes.
            - **Fix** - Added `active` class to 'Home' navbar menu. Corrected on all navbar menu items.
2. **Navbar - Recipes**:
    1. Select 'Recipes' on the navbar.
    2. Verify that 'Recipes' is highlighted on the navbar and that the user is moved to the recipes page.
    3. Verify that the page header, footer, social links and all recipes are displayed as intended.
    4. Select 'View Recipe' and verify that all the recipe details are displayed as intended.
    5. Select 'Update Recipe' and verify that a form is displayed, containing the recipe details, which can be updated and over-written.
    6. Once the Recipe has been updated, select 'Update Recipe' and verify that an alert box appears.
    7. Select X and verify that the user is brought back to the recipe to continue editing it.
    8. Select 'Update Recipe' again, and select 'OK' on the alert box. Verify that the user is brought to the recipe page and that the updated recipe is added.
    9. Verify that the old recipe is still on the recipes page for the user to refer back to if required and for the user to delete once satisfied with their updated recipe.
    10. Select 'View Recipe' again. Once a recipe is displayed, select 'Delete Forever'. Verify that an alert box appears.
    11. Select X and verify that the user is brought back to the recipe to continue editing it.
    12. Select 'Delete Forever' again, and select 'OK' on the alert box. Verify that the user is brought to the recipe page and that the recipe is deleted.
        - **Bug 1** - Cards not alignings vertically.
            - **Issue** - Html divs require adjusting.
            - **Fix** - Added `<div style="text-align: center">`.
            - **Bug 2** - No spacing between cards.
            - **Issue** - Margins require styling.
            - **Fix** - Added Bootstrap spacing classes i.e. mt and mb.
        - **Bug 3** - Cards are not all the same height.
            - **Issue** - Card sizes only stretching as far as the reipe description text, rather than aligning with the design of that div row.
            - **Fix** - Added `d-flex align-items-stretch` to div.
        - **Bug 4** - Cards buttons displaying randomly, rather than in each card footer.
            - **Issue** - Card sizes only stretching as far as the reipe description text, rather than aligning with the design of that div row.
            - **Fix** - Moved `<a href="{{url_for('view_recipe', recipe_id=recipe._id)}}" class="btn btn-primary">View Recipe</a>` down a div.
3. **Navbar - New Recipes**:
    1. Select 'New Recipes' on the navbar.
    2. Verify that 'New Recipes' is highlighted on the navbar and that the user is moved to the new recipes page.
    3. Verify that the page header, footer, social links and all recipes are displayed as intended.
    4. Verify that a blank form is displayed.
    5. Leave all form fields, blank and select 'Add Recipe'. Verify that the user is required to populate all fields before a new recipe can be added.
    6. Input dummy data into each form field. Select 'Add Recipe'. Verify that the user is brought to the recipes page and that the new recipe is added.
        - **Bug 1** - Date posted field is populating but not displaying when the recipe is added to the recipes page.
            - **Issue** - Incorrectly spelled `{{recipe.posted_date}}`.
            - **Fix** - Updated to `{{recipe.date_posted}}`, the words were the incorrect way around.
4. **Navbar - Contact**:
    1. Select 'Contact' on the navbar.
    2. Verify that 'Contact' is highlighted on the navbar and that the user is moved to the contact page.
    3. Verify that the page header, footer, social links and all recipes are displayed as intended.
    4. Verify that a blank form is displayed.
    5. Input dummy data into each form field. This contact page is currently not wired up to an email account. Select Submit, button highlighted but no further action happens.

## Deployment
The following section describes the process to deploy this project to Heroku.

1. Via Linux Terminal, login to Heroku, using 'Heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Raw Dessert Recipes](https://cookbook-mongodb.herokuapp.com/).

## Credits

### Content

- The background photo on all pages of this website was copied from [Background photo](https://image.freepik.com/foto-gratis/barras-de-chocolate-oscuro-con-granos-de-cacao-en-la-mesa-de-madera_23-2147873730.jpg).
- The photo on the home text section of this website was copied from [Home photo](https://image.freepik.com/free-photo/fresh-chocolate-mini-cakes_23-2147896378.jpg).
- The health benefits text on the home page text section of this website was copied from [About health benefits](https://www.webmd.com/diet/a-z/raw-foods-diet).
- The photo on the recipes page of this website was copied from [Recipes photo](https://image.freepik.com/free-photo/melted-chocolate-bowl-and-crushed-bar-on-chopping-board-with-wooden-spoon_23-2147867190.jpg0).
- The Recipes for this website were copied from [Recipes](http://rawfoodrecipes.com/).

### Acknowledgements
- I received inspiration for this project from my interest with using food for health, reading books, online videos and experience. [Mark Sisson](https://www.marksdailyapple.com/) a Paelo and Ketogenic expert, has in particular opened me up to an interest in food for health.
- For the technical skills used in this project, I harnessed the knowledge gained from the [Code Institute - Diploma in Software Development](https://www.codeinstitute.net/), [Stack Overflow](https://stackoverflow.com/), [W3 Schools](https://www.w3schools.com/), [Bootstrap](http://getbootstrap.com/) and [Bootsnipp](https://bootsnipp.com/).