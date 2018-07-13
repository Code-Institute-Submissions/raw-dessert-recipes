### Raw Dessert Recipes
A data-driven web application that allows users to easily access, add new and edit recipes.

### Functionalities
1. **Recipes (homepage)**
    * **Recipes**: User selects the drop-down arrow, which displays recipe details in an accordion popout style.
    * **Edit Button**: User selects the edit button to update/make changes to the recipe. The recipe with all details opens in an edit recipe page and includes the recipe details. The user make changes and adds a new version of the recipe by selecting the edit recipe button.
    * **Delete Button:** User selects the delete button to remove a recipe.
2. **New Recipes**
    * **New Recipes**: User selects new recipes on the navbar to open the new recipe page. User inputs recipe details and selects add recipe button to add the recipe.

### Technologies
1. **Cloud 9**: IDE `Integrated Development Environment` used to build project end to end.
2. **Materialize**: A web design library created by Google. Used for styling and interactive design, e.g. Buttons, Forms, Icons.
3. **mLab**: Cloud database service that hosts MongoDB databases. Used for creating and storing recipe data.
4. **Flask**: A python microframework used to build and run the application. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
5. **Python code**: Written within `app.py`. Used to write the logic of creating, reading, updating and deleting recipes.
6. **HTML files**: Used to build the structure of each application page.
7. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
8. **Git and GitHub**: Used for version control and to deploy a backup of the project.
9. **Heroku**: Used to deploy and host the project.

### Other Resources
1. **Recipe details**: For the purpose of populating this project used this [Recipe Website](http://rawfoodrecipes.com/).

### Development Process
1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project. Developed and finalised as project progressed.
3. **Files & Folders**: Created in line with wireframe and developed as project progressed.
4. **mLab**: Before building Cloud 9 code, first created the MongoDB database.
    * **New DB:** Created new database, selecting AWS Sandbox with 0.5GB free storage.
    * **DB Schema:** Created new collection i.e. document, which represents a recipe. Within each document created key value pairs per wireframe, e.g. "recipe_title": "Raw Chocolate Buttons". Saved a couple of new recipes to link flask to whilst building project. Each new recipe created on the front end would then save as a document under collections,
    * **User:** Create admin user and added relevant mongoDB code to app.py to connect application with database.
5. **Flask**: Installed Flask via sudo pip3 install flask command.
6. **App.py**: Developed code to run flask and added code throughout build to render html files in browser.
7. **Materialize**: Developed code to include relevant Materialize links within html files to import libraries.
8. **HTML files**: Developed HTML code to build structure of each web application page.
9. **CSS file**: Developed CSS code to add own custom styling.
10. **Commentary**: Developed commentary throughout to provide code guidance.
11. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality code developed, checked operated as expected in the web browser by walking through each functionality. The following bugs were encountered:

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
    1. **Bug/Expected Output** - Background image not responsive. **Issue** - Included as a div with static width and height html. **Fix ** - Updated as div with css 'bg' class. Added css styling for responsive image.
5. **Heroku Testing**: Tested to ensure application successfully hosted.
    1. **Bug/Expected Output** - Application error, not rendering in browser. **Issue** - Requirements.txt not updated posted pymongo installation. **Fix** - Checked app log within Heroku for error messages. Ran sudo pip3 freeze --local > requirements.txt and pushed to Heroku. 

### Deploy via Heroku
1. Via Linux Terminal, login to Heroku, using 'Heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Raw Dessert Recipes](https://cookbook-mongodb.herokuapp.com/).
