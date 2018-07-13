### Raw Dessert Recipes
A data-driven web application that allows users to easily access, add new and edit recipes.

### Functionalities
1. **Recipes (homepage)**
    * **Recipes**: User selects the drop down arrow, which displays recipe details in an accordion popout style.
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
1. **Recipie details**: For purpose of populating this project used this [Recipe Website](http://rawfoodrecipes.com/).

### Development Process
1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project. Developed and finalised as project progressed.
3. **Files & Folders**: Created in line with wireframe and developed as project progressed.
4. **mLab**: Before building Cloud 9 code, first created the MongoDB database.
    * **New DB:** Created new database, selecting AWS Sandbox with 0.5GB free storage.
    * **DB Schema:** Created new collection i.e. document, which represents a recipe. Within each document created key value pairs per wireframe, e.g. "recipe_title": "Raw Chocolate Buttons". Saved a couple of new recipes to link flask to whilst building project. Each new recipe created on the front end would then save as a document under collections,
    * **User:** Create admin user and added relevant mongodb code to app.py to connect application with database.
5. **Flask**: Installed Flask via sudo pip3 install flask command.
6. **App.py**: Developed code to run flask and added code throughout build to render html files in browser.
7. **Materialize**: Developed relevant links within html files to import libraries.
8. **HTML files**: Developed code to build structure of each web application page.
9. **CSS file**: Developed code to add own custom styling.
10. **Commentary**: Developed throughout to provide code guidance.
11. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality coded, checked application operating as expected in web browser by walking through each functionality. Testing included the following:

 recipies.html - jinja error rendering {{ endfor }}, should be  {% endfor %}.
 app.py - application not rendering in browser. @app.route('add_recipe') should be @app.route('/add_recipe') '/' missing.
 jinja error - (edit_recipe spelled incorrectly).
 Add Recipie/Edit Recipe - Date being input into field but not posted to front end. {{recipe.posted_date}} should have been {{recipe.date_posted}}.
 MongoDB manually input recipies, date blank - after previous bug was fixed, wording on MOngo DB has to be updated fom posted_date to date_posted to correctly align all code.
 DAte Posted not appearing under edit task - added sript to editrecipe.html. #Date, bug - should be #date_posted.

Responsive

### Deploy via Heroku
1. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Raw Chocolate Recipes]().