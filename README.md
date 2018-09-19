# Raw Dessert Recipes

A data-driven web application that allows users to easily access, add new and edit recipes.

This a raw dessert Recipes website, built using **Flask**, a Python micro-framework. It is a data-driven application, and the target audience is any user who wants to easily access, add new and edit Recipes.

## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed the Code Institute learnings to date and Bootstrap themes to extract design ideas.
2. **player Stories** - Walked through player stories.
    1. **Header Call-to-action** - As a player, I want to understand the purpose of this website and intuitively understand how to use it.
    2. **Navbar - Contact** - As a player, I want to be able to contact the developers to offer feedback and suggestions.
    3. **Navbar - Riddle Game** - As a player, I want to be able to, go to the landing page from anywhere, and be presented with a blank player name textarea.
    4. **Navbar - Game** - As a player, I want to be able to restart the game from anywhere and be presented with a blank player name textarea.
    5. **Enter Player Name** - As a player, I want to be able to enter a player name into a textarea and start the game.
    6. **Start Game** - As a player, once I select start game, I want to be greeted with my player name, to be presented with the first riddle and view player names in a list.
    7. **Enter Correct Answer** - As a player, I want to be able to enter an answer into a blank textarea, submit an answer and if I provide the correct answer, be redirected to the next riddle.
    8. **Enter Incorrect Answer** - As a player, I want to be able to enter an answer into a blank textarea, submit an answer and if I provide an incorrect answer, I am redirected to a blank textarea to guess again, with answers are displayed in a list.
    9. **Answer all Riddles Correctly** - As a player, when I have answered all riddles correctly, I want to be redirected to an end of game message.
3. **Wireframe** - Sketched the wireframe on paper, to include the features for each player story.

## Features

### Existing Features
The following section describes all the front-end features in this project.

1. **Header Call-to-action** - Provides players with a website title and brief description of what to do next.
2. **Navbar - Contact** - Provides players with a navbar menu, bringing players to a form, to contact developers.
3. **Navbar - Riddle Game** - Provides players with a navbar menu, bringing players, to the landing page.
4. **Navbar - Game** - Provides players with a navbar menu, bringing players to restart the game.
5. **Enter Player Name** - Provides players with a blank text area, to input a player name.
6. **Start Game** - Provides players with a 'Start Game' button, bringing players to a new page, which greets them by their player name, displays a riddle one by one, and displays their player name in a list of player names.
7. **Enter Correct Answer** - Provides players with a blank text area, to enter their answer and select submit to be redirected to the next riddle if the answer is correct.
8. **Enter Incorrect Answer** - Provides players with a blank text area, to enter their answer and select submit to be redirected to answer this riddle again if the answer is incorrect. Players incorrect answers are also displayed in a list.
9. **Answer all Riddles Correctly** - Provides players with an end of game message when they have answered all riddles correctly.

### Features to Implement
1. **Leader board** - Add a feature to include a scoring system that ranks all players.
2. **Incorrect Answers - Show Riddle or Riddle Number** - Consider adding a feature to indicate which incorrect answer is related to which riddle but ensure not to make the game too simple for players.

## Technologies Used
The following section describes all technologies and tools used to construct this project.


Bootsnipp form - https://bootsnipp.com/snippets/featured/simple-contact-form

1. **Cloud 9**: IDE `Integrated Development Environment` used to build project end to end.
2. **Materialize**: A web design library created by Google. Used for styling and interactive design, e.g. Buttons, Forms, Icons.
3. **mLab**: Cloud database service that hosts MongoDB databases. Used for creating and storing recipe data.
4. **Flask**: A python microframework used to build and run the application. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
5. **Python code**: Written within `app.py`. Used to write the logic of creating, reading, updating and deleting recipes.
6. **HTML files**: Used to build the structure of each application page.
7. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
8. **Git and GitHub**: Used for version control and to deploy a backup of the project.
9. **Heroku**: Used to deploy and host the project.

1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project. Developed and finalised as project progressed.
3. **Files & Folders**: Created in line with wireframe and developed as project progressed.
4. **mLab**: Before building Cloud 9 code, first created the MongoDB database.
    * **New DB:** Created new database, selecting AWS Sandbox with 0.5GB free storage.
    * **DB Schema:** Created new collection i.e. document, which represents a recipe. Within each document created key value pairs per wireframe, e.g. "recipe_title": "Raw Chocolate Buttons". Saved a couple of new recipes to link flask to whilst building project. Each new recipe created on the front end would then save as a document under collections.
    * **User:** Create admin user and added relevant mongoDB code to app.py to connect application with database.
5. **Flask**: Installed Flask via sudo pip3 install flask command.
6. **App.py**: Developed code to run flask and added code throughout build to render html files in browser.
7. **Materialize**: Developed code to include relevant Materialize links within html files to import library.
8. **Font Awesome**: Develoepd code to include relevant Font Awesome links within html files to import library.
8. **HTML files**: Developed HTML code to build structure of each web application page.
9. **CSS file**: Developed CSS code to add own custom styling.
10. **Commentary**: Developed commentary throughout to provide code guidance.
11. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

Share details of how you created your database schema in your README. Consider sharing working drafts or finalised versions of your database schema in a 'Database Schema' folder in your repo. Provide a link to this folder in your README.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - The project used **Cloud 9**, online integrated development environment, to construct the code end to end.
- [Bootstrap](https://getbootstrap.com/)
    - This project uses **Bootstrap**, a library of website themes. The [Business Casual Template](https://startbootstrap.com/template-overviews/business-casual/), was used for this project.
        - **Static folder**: Contains Bootstrap files ONLY (no other files stored within this folder).
        - **`base.html` and `contact.html`** - Boiler plate html was copied from the bootstrap `index.html` and `contact.html` files, then amended to suit this project.
        - **All Other Code**: Compiled by the project developer.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask**, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %}`, `{% block content %}`, and ` {% endblock %}` jinja code.
- [Jinga](http://jinja.pocoo.org/)
    - This project uses **Jinja**, a template engine for Python, which is included with the curly brackets.
- [Python](https://www.python.org/)
    - This project uses **Python**, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which was written in this project within the `.html` files.
- [JSON](https://json.org/)
    - This project uses **JSON** (JavaScript Object Notation), which is a text-based data interchange format designed for transmitting structured data. It is most commonly used for transferring data between web applications and web servers. A JSON file was used as a database in this project to retrieve the riddle information.
- [.txt files](https://en.wikipedia.org/wiki/Text_file)
    - This project uses **.txt files**, to store text and was used in this project to write data to and read data from.
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


Bugs
Nav bar not highlighting when selecting page - overwrote bootstrap nav tags with index.html, updated as per bootstrap template. 'active' class highlight nav menu item.



1. **Navbar - Contact**:
    1. Select 'Contact' on the navbar and verify that the player is moved to the contact page.
    2. Complete all player details within the contact form and verify that all fields accept relevant inputs.
    3. Select 'Send' to submit the player’s details and verify that the player is brought to a thank you message and that the form input fields are cleared.
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
    1. Select 'Riddle Game' on the navbar and verify that the player is moved to the landing page.
    2. Verify that the landing page player name textarea is blank and the page is ready to start a new game.
3. **Navbar - Game**
    1. Select 'Game' on the navbar and verify that the player is moved to the landing page.
    2. Verify that the landing page player name textarea is blank and the page is ready to start a new game.
4. **Enter Player Name and Start Game**
    1. Enter a player name into the blank text area.
    2. Select 'Start Game' and verify that the player is moved to the start game page, is greeted by their player name with instructions on answering the riddle, is presented with the first riddle and their name is displayed in a list of player names.
    3. When the list is longer than the box, verify that the scrolling bar appears on the player name list.
        - **Bug 1** - After entering player name and selecting start game, browser error 'Method Not Allowed'.
            - **Issue** - `run.py` not updated with the relevant code to write a player name to the `players.txt` file.
            - **Fix** - Updated `run.py` to write to the `players.txt` file.
        - **Bug 2** - Player name is appearing duplicated on the list of player names.
            - **Issue** - Player name is being stored in the player name list, with every correct and incorrect answer that is entered.
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
    2. Verify that the player is brought to an end of game message.
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

### Media
- The video used in this site was copied from [Background Video](https://www.youtube.com/watch?v=1hQ6pJ6bPik).

### Acknowledgements
- I received inspiration for this project from my interest in Health, [Materlize](https://materializecss.com/) and ongoing research online. I also used knowledge gained from the [Code Institute - Diploma in Software Development](https://www.codeinstitute.net/), [Stack Overflow](https://stackoverflow.com/) and [W3 Schools](https://www.w3schools.com/).