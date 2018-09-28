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
8. **Upvotes** - Add a feature to include a tye of upvote for each invidiaul recipe.

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






1. **Recipes.html**
    1. **Bug/Expected Output** - Application not rendering in browser. **Issue** - spelled {{ endfor }}. **Fix** - Scanned code. Updated jinja code to {% endfor %}.
    2. **Bug/Expected Output** - Application not rendering in browser. **Issue** - app.py '@app.route('add_recipe')'. **Fix** - Added missing '/', to '@app.route('/add_recipe')'.
    3. **Bug/Expected Output** - Date posted not appearing after selecting edit. **Issue** - Wording for key value within mongoDB not in line with application. **Fix** Updated from 'posted_date' to 'date_posted' to correctly align all code.
2. **Addrecipe.html**
    1. **Bug/Expected Output** - Date posted populating on form but not showing when recipe added. **Issue** - Spelled {{recipe.posted_date}} **Fix** - {{recipe.date_posted}}, words wrong way around.
3. **Editrecipe.html**
    1. **Bug/Expected Output** - Application not rendering in browser. **Issue** - spelled @app.route('/eit_recipe/<recipe_id>') **Fix** - spelled @app.route('/edit_recipe/<recipe_id>').
    2. **Bug/Expected Output** - Date posted not appearing. **Issue** - Script bug, written as #Date_posted. **Fix** - Updated to #date_posted.
4. **Responsive Testing**: Used Chrome Dev tools to inspect application on various device sizes.
    1. **Bug/Expected Output** - Background image not responsive. **Issue** - Included as a div with static width and height html. **Fix** - Updated as div with css 'bg' class. Added css styling for responsive image.
5. **Heroku Testing**: Tested to ensure application successfully hosted.
    1. **Bug/Expected Output** - Application error, not rendering in browser. **Issue** - Requirements.txt not updated posted pymongo installation. **Fix** - Checked app log within Heroku for error messages. Ran sudo pip3 freeze --local > requirements.txt and pushed to Heroku. 



1. **Recipes (homepage)**
    * **Recipes**: User selects the drop-down arrow, which displays recipe details in an accordion popout style.
    * **Edit Button**: User selects the edit button to update/make changes to the recipe. The recipe with all details opens in an edit recipe page and includes the recipe details. The user make changes and adds a new version of the recipe by selecting the edit recipe button.
    * **Delete Button:** User selects the delete button to remove a recipe.
2. **New Recipes**
    * **New Recipes**: User selects new recipes on the navbar to open the new recipe page. User inputs recipe details and selects add recipe button to add the recipe.



1. **Navbar - Contact**:
    1. Select 'Contact' on the navbar and verify that the user is moved to the contact page.
    2. Complete all user details within the contact form and verify that all fields accept relevant inputs.
    3. Select 'Send' to submit the user’s details and verify that the user is brought to a thank you message and that the form input fields are cleared.
        - **Bug 1** - Code not initially rendering in browser.
            - **Issue** - Jinja code at end of the html files spelled {% end block %}, in error.
            - **Fix** - Scanned all html code. Updated with relevant jinja code, with no space i.e. {% endblock %}.
        - **Bug 2** - 'Contact Developer' heading missing.
            - **Issue** - Jinja typo in {{ page_heading }} on `contact.html` and code not reading from `run.py` file.
            - **Fix** - Checked relevant code and updated typo to ensure {{ page_heading }} spelled the same as code on `run.py` file.
        - **Bug 3** - After updating commentary within html files, error in browser pointing to {{curly brackets.
            - **Issue** - Updated commentary to state that the code within {{ }}, is flask code. The browser tried to read this as code.
            - **Fix** - Updated {{ }} to the words, 'curly brackets'.
2. **Navbar - Riddle Game**
    1. Select 'Riddle Game' on the navbar and verify that the user is moved to the landing page.
    2. Verify that the landing page user name textarea is blank and the page is ready to start a new game.
3. **Navbar - Game**
    1. Select 'Game' on the navbar and verify that the user is moved to the landing page.
    2. Verify that the landing page user name textarea is blank and the page is ready to start a new game.
4. **Enter user Name and Start Game**
    1. Enter a user name into the blank text area.
    2. Select 'Start Game' and verify that the user is moved to the start game page, is greeted by their user name with instructions on answering the riddle, is presented with the first riddle and their name is displayed in a list of user names.
    3. When the list is longer than the box, verify that the scrolling bar appears on the user name list.
        - **Bug 1** - After entering user name and selecting start game, browser error 'Method Not Allowed'.
            - **Issue** - `run.py` not updated with the relevant code to write a user name to the `users.txt` file.
            - **Fix** - Updated `run.py` to write to the `users.txt` file.
        - **Bug 2** - user name is appearing duplicated on the list of user names.
            - **Issue** - user name is being stored in the user name list, with every correct and incorrect answer that is entered.
            - **Fix** - Updated `run.py` as it contained duplicated code causing this bug.
5. **Enter Correct Answer**
    1. Enter an answer into the blank text area.
    2. Select 'Submit' to be redirected to the next riddle if the answer is correct.
        - **Bug 1** - After entering correct answer, browser error 'ValueError' appeared.
            - **Issue** - JSON data is not reading from `riddles.json` file.
            - **Fix** - Scanned `riddles.json` for to identify the issue. Removed comma at the end of last closing curly bracket.
6. **Enter Incorrect Answer**
    1. Enter an answer into the blank text area.
    2. Select 'Submit' to be redirected to answer the riddle again if the answer is incorrect.
    3. Verify that incorrect answers are displayed with a list of incorrect answers.
    4. When the list is longer than the box, verify that the scrolling bar appears on the incorrect answer list.
7. **Answer all Riddles Correctly**
    1. Enter the correct answer for all riddles.
    2. Verify that the user is brought to an end of game message.
8. **Responsive Testing**:
    1. In Chrome, right click on the site and select 'inspect', to open the Chrome Dev tools.
    2. Select the toggle device icon at the top of the window, to open the responsive testing window.
    3. Test/walk through how all features and pages are rendering on each device size from Galaxy S5 to iPad Pro.
        - **Bug 1** - Terminal displaying error 'socket.error: [Errno 98] Address already in use [closed]'.
            - **Issue** - Did not select `ctrl+c` to stop `run.py` running prior to closing workspace, the following day encountered this error. 
            - **Fix** - Researched solutions online and located fix via stack overflow. In terminal, ran `lsof -i :8080` to locate port ID. Then ran `sudo kill -9 <process_id>` to kill the process and allow the application to run.
        - **Bug 2** - Application not responsive on various device sizes.
            - **Issue** - Bootstrap grid layout required changing.
            - **Fix** - Updated bootstrap `<div>` tags with various classes and styling within the `html files` and retested until application fully responsive on all device sizes.

Bug
Not Found - The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
When card recipe data populated from Mlab, cards not aligning horizonatally, but vertically. Added <div style="text-align: center">.
No spacing between cards. Added bootstrap spacing class = mt-5 mb-5. OPEN = MAKE ALL CARDS SAME SIZE, NO MATTER WHAT TEXT IN DESCRIPTION.
Cards not all same height. Added 'd-flex align-items-stretch' to div.
Card buttons - displaying randomly and not at bottom of cards. Moved <a href="{{url_for('view_recipe', recipe_id=recipe._id)}}" class="btn btn-primary">View Recipe</a> down a div.
Nav bar not highlighting when selecting page - overwrote bootstrap nav tags with index.html, updated as per bootstrap template. 'active' class highlight nav menu item.


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
- The photo on the about text section of this website was copied from [About photo](https://www.pexels.com/search/chocolate/).
- The health benefits text on the about text section of this website was copied from [About health benefits](https://www.webmd.com/diet/a-z/raw-foods-diet).
- The photo on the recipes page of this website was copied from [Recipes photo](https://image.freepik.com/free-photo/melted-chocolate-bowl-and-crushed-bar-on-chopping-board-with-wooden-spoon_23-2147867190.jpg0).
- The Recipes for this website were copied from [Recipes](http://rawfoodrecipes.com/).
- 
- Card Title image: https://www.freepik.com/free-photo/melted-chocolate-bowl-and-crushed-bar-on-chopping-board-with-wooden-spoon_2698076.htm#term=chocolate&page=1&position=33

Bootsnipp form - https://bootsnipp.com/snippets/featured/simple-contact-form

### Media
- The video used in this site was copied from [Background Video](https://www.youtube.com/watch?v=1hQ6pJ6bPik).

### Acknowledgements
- I received inspiration for this project from my interest in Health, [Materlize](https://materializecss.com/) and ongoing research online. I also used knowledge gained from the [Code Institute - Diploma in Software Development](https://www.codeinstitute.net/), [Stack Overflow](https://stackoverflow.com/) and [W3 Schools](https://www.w3schools.com/).