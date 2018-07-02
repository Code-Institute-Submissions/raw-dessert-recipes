![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### Cookbook
A web application that allows users to store and easily access coking recipies.

### Project Requirements
1. Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data																					
2. Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course).																					
3. Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation																		
4. Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large.																					
5. Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions																					
6. Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.																					
7. Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure).																					
8. The website must be data-driven and can rely on structured data, unstructured data or a mix of structured and unstructured data. 																					
9. Share details of how you created your database schema in your README. Consider sharing working drafts or finalised versions of your database schema in a 'Database Schema' folder in your repo. Provide a link to this folder in your README.																					
10. CRUD operations can be carried out using either SQL (e.g. MySQL/SQLite/Postgres) or NoSQL (e.g. MongoDB).	

### Technologies
1. **Cloud 9**: IDE `Integrated Development Environment` used to build project end to end.
2. **Bootstrap**: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) used as boilerplate design.
    * **Static folder**: Contains Bootstrap files (no other files stored within this folder).
    * **`base.html` and `contact.html`** - most of this html code was copied from the bootstrap `index.html` and `contact.html` files, then amended to suit this project.
    * **All other code**: Compiled by developer from knowledge gained and online researching - frequently using stack overflow, W3 Schools and YouTube videos.
3. **Flask**: A python microframework used to build and run the application. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
4. **Python code**: Written within `run.py`. Used to write the logic of the game.
5. **HTML files**: Used to build the structure of each application page.
6. **JSON file**: Used as a database to retrieve riddle question and answers.
7. **Text files**: Used to write to and read from via python back end code e.g. write player name to `players.txt` when player inputs name on form and selects start game.
8. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
9. **Git and GitHub**: Used for version control and to deploy a backup of the project.
10. **Heroku**: Used to deploy and host final project.

### Development Process
1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project and developed as project progressed.
3. **Folders and files**: Created in line with wireframe and developed as project progressed.
4. **Bootstrap**: [Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded to static folder and used as boilerplate for design.
5. **HTML files**: Developed with own code/commentary on top of bootstrap template code, e.g. overwriting photo and renaming nav bar to align with this project design. 
6. **Run.py**: Flask and python back end code developed to render application in web browser and execute functionality.
7. **Commentary**: Developed throughout files to provide code guidance.
8. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality coded, checked application operating as expected in web browser by walking through each functionality. Testing included the following:

### Deploy via Heroku
1. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Cookbook]().