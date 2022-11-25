# scrum-wizards-cs321
Athlete Data Management System for CS321 (Fall 2022) at Colby College, ME

<br>


<h1 align="center">Milestone 6 Report</h1>
<h3 align="center">Flask Web App</h3>


<h2 align="left">Abstract</h3>
<p>In Milestone 6, we used this sprint to implement a CI/CD pipeline to lint, test, and deploy a web app to the cloud using Azure. Essentially, this checked over our code for us so we didn’t have any errors that we might have missed. The goal of this task, using Pytest to improve code quality, was to simulate everything a potential user might run into, and making sure there are no errors in the code that would confuse the user or render the software unusable. We had to write our own tests, with the aim of full coverage (meaning we tested all of our functions used in the software), and then used Pytest to see what went wrong. We learned a lot about Flask testing as well in homework and quiz videos, as well as in lecture, and also had to do a lot of outside research to figure out how to test functions that are specific to our software. 
</p>

<br><br>

<h2 align="left">Results</h2>
<p>Our focus for this milestone was deploying our testing, with the aim of 100% coverage. While this was not realized, we went through the testing of the functions we deemed the most important. To test views.py, we implemented test_views.py, which essentially just tested all the redirecting of the urls that we implemented in that file, for athletes, coaches, and the superadmin. We also created a test app using create_test_app, which created a new test app to run our tests and made it a lot easier instead of manually creating a new app every time we created a new test function. For testing addathlete, addadmin, and addcoach, we made a test_adduser.py file that tested out the forms that we put in those html files, essentially all the info needed to create a new user. We did the same strategy for testing out the forms for test_userpermissions.py, which tested coachpermissions and athletepermissions, seeing if we could successfully switch a role or team of a user. We also created tests for the login and authorization functions, which can all be seen in the github repository. 
The backend database testing was by far the most involved, found in the test_helper_db.py file. This file tested creating a new user, a new team, a new entry, a new permissions, and the get functions for all of the above as well. We also implemented tests for the helper functions, such as filtering users by their emails, names, IDs, etc. We also tested out filtering permissions, teams, entries, and users, by each other. 
</p>

<br>

<h2 align ="left>Team Reflect</h2>
<p>All in all, we are very grateful to this milestone because we learned about all the mistakes we had made in our code that we never would have otherwise run into. We went into this milestone thinking that our code was perfect because, whenever we ran the website through the server, everything was working perfectly and we thought that was a complete test of everything. However, when we wrote our own tests, we realized exactly how many things we needed to test in order to simulate everything a user might run into. For example, we had to make so many tests that redirected pages to other ones, and while most of them worked like we expected, some of them (that we had never tested before) resulted in errors and we were able to fix that so clicking on certain buttons led exactly to the page we wanted. We also practiced so much with functional v. unit testing that we definitely have a much better grasp on the differences between them, especially when it comes to testing with Flask. Without testing, we could have given faulty software to our clients.
<p>

<br>

<div align="center"><img width="718" alt="Screen Shot 2022-10-27 at 12 15 41 PM" src="https://user-images.githubusercontent.com/35567444/198343906-da68e9af-9307-4f0c-bf5b-12ea04123412.png"></div>
<div align="center">Fig 1: First page; login page.</div>

<br><br>

<div align="center"><img width="717" alt="Screen Shot 2022-10-27 at 12 16 26 PM" src="https://user-images.githubusercontent.com/35567444/198344087-c31d0db8-1bfc-4ccc-bb10-3a26842508a8.png"></div>
<div align="center">Fig 2: Login page when incorrect password for user is entered.</div>

<br><br>

<div align="center"><img width="715" alt="Screen Shot 2022-10-27 at 12 17 09 PM" src="https://user-images.githubusercontent.com/35567444/198344248-33dbe398-cb39-4211-9ecd-562096386a13.png"></div>
<div align="center">Fig 3: Login page when a nonexistent user is entered</div>

<br><br>

<div align="center"><img width="715" alt="Screen Shot 2022-10-27 at 12 17 46 PM" src="https://user-images.githubusercontent.com/35567444/198344374-3da741f1-75e1-4113-88ed-4f5cb9c6a0c6.png"></div>
<div align="center">Fig 4: Coach Dashboard (as well as Admin dashboard, when they click on a specific team)</div>

<br><br>

<div align="center"><img width="716" alt="Screen Shot 2022-10-27 at 12 18 16 PM" src="https://user-images.githubusercontent.com/35567444/198344491-c7d1a416-7369-432a-966d-eadc1f2d8acc.png"></div>
<div align="center">Fig 5: Athlete Dashboard</div>

<br><br>

<div align="center"><img width="717" alt="Screen Shot 2022-10-27 at 12 18 45 PM" src="https://user-images.githubusercontent.com/35567444/198344604-afa9c933-cefd-4960-8e8b-dbaa5142c0e2.png"></div>
<div align="center">Fig 6: Super admin home (when you first log in as Super Admin)</div>

<br><br>

<div align="center"><img width="712" alt="Screen Shot 2022-10-27 at 12 19 11 PM" src="https://user-images.githubusercontent.com/35567444/198344705-77d157a2-e227-48c8-9d24-f54e4cc52dbf.png"></div>
<div align="center">Fig 7: Editing (When you click on a specific Athlete) </div>

<br><br>

<div align="center"><img width="614" alt="Screen Shot 2022-10-27 at 12 19 54 PM" src="https://user-images.githubusercontent.com/35567444/198344864-988d9ace-b171-4fdc-8cc7-d7996444a220.png"></div>
<div align="center"><img width="322" alt="Screen Shot 2022-10-27 at 12 20 12 PM" src="https://user-images.githubusercontent.com/35567444/198344958-43cff1f0-297d-46e6-bf77-8c8110302760.png"></div>
<div align="center">Fig 8, 9, 10: Add Athlete, Admin, and Coach (in order)
</div>

<br><br>

<h2 align="left">Backend Logic</h3>
<p>The Backend, built in Flask, drove the functionality, connectivity, and security that tied the front end together. For this sprint, we made a database, described it in models.py with 4 different tables, and used some supporting objects to smooth out the database logic. Below is a wireframe mockup to visualize our relational database.</p>



<div align="center"><img width="985" alt="Screen Shot 2022-10-28 at 1 33 38 AM" src="https://user-images.githubusercontent.com/92835209/198510893-ee86a8ee-b0d2-408b-9f70-84f021f6de82.png"></div>

<p>The four tables of our database, which we settled on after several iterations- ‘User’, ‘Entry’, ‘Team’, and ‘Permission’. We initially had more than four tables, but found it difficult to work with and realized we were duplicating some logic- our team agreed that four tables would remove complexity for our project going forward, even if the logic took more work upfront. 
Also seen here is the ‘Category’ enum and an association table between ‘User’ and ‘Team’. Because ‘User’ and ‘Team’ is a many-to-many relationship, an association table was needed to facilitate this using left and right keys for the user and team id.
Also unique about our backend logic was the implementation for ‘Entry’ which represents an individual data entry into the system about an athlete. 
</p>
    
<div align="center"><img width="166" alt="Screen Shot 2022-10-28 at 1 34 22 AM" src="https://user-images.githubusercontent.com/92835209/198511298-c23d4dd8-1acd-4be9-933a-f7f286a4df09.png"><img width="166" alt="Screen Shot 2022-10-28 at 1 34 22 AM" src="https://user-images.githubusercontent.com/92835209/198511467-2ba727b0-895e-47df-9369-2da5e48da77d.png">
</div>
<p>Above are two examples of a possible entry of type ‘Entry’. An entry contains a category, which can only be one of 5 types. Depending on the type, it might be null for the notes field (in the case of category sleep) or null in the value field (in the case of the psychology category). Every entry, of course, is attached to a time/date and a user id.</p>

<br><br>

<h2 align="left">Team Reflection:</h2>
<p>This milestone was definitely the most complicated yet, as it forced us to work with tools that we had, for the most part, never used before (Flask and its many capabilities, GitHub and working remotely as a group) and other tools, such as implementing HTML with Python files. Working remotely was definitely challenging, and we had to practice a lot with GitHub in order to combine all our ideas effectively. We made many mistakes with GitHub, but facing these challenges with the help of our Scrum Master, and fixing merge conflicts all together definitely made us stronger as a team. Code reviews were done extremely effectively and respectfully, and we all learned so much from this incredibly immersive milestone. We are now definitely much more prepared for the remote group work that is ahead of us, and are all the more ready for more learning challenges. </p>

<br><br>

<h2 align="left">Contributions</h3>	

**List of all group members contributions**

_Chandra Gowda_


Worked on the backend for the Flask app:
* Created the User, Entry, Permission, and Teams models and schema in the models.py
* Created helper_db.py file with database access and query functions for all possible query options for the 4 model classes. 
* Created a demo database in the __init__.py file, and wrote test functions for the database additions/queries/listing/deletion and validated the tests through the sqlliteviewer.app file. 
* Created GitHub issues labeled under “BACKEND” for Milestone 1.
* Worked with the frontend team regarding implementing the database data to input sample data in fields in the Flask App UI. 
* Assisted in handling merge conflicts in the models.py, auth.py, and __init__.py backend files while merging the db-and-auth and frontend branches into our streamlined develop branch.
Extensions:
* Did the README.md extension in the GitHub develop repository.

_Zehra_ 

* Developed the front-end of the project by working on views.py, individual_dashboard, team_dashboard, athlete_permissions.html, and the index.html of the super admin for creating the following elements:
* Created the dynamic notes section of the individual dashboard used for the athlete dashboard
* Created the dynamic team search list on the coach / admin dashboard
* Created the dynamic lists displaying the names and profile pictures of the coaches and athletes on the super admin home page.
* Pair-programmed a mock database for athlete names and ids with Sinan.
* Edited the super admin athlete permissions html file and used the mock database for displaying the specific athlete names on the edit athlete permissions page.  
* Worked on resolving merge conflicts when merging the front-end branches to develop.



_Sinan_

As the Scrum leader for this sprint, I was responsible for;
* Teaching teammates about HTML, CSS, Flask
* I organized two meetings in the beginning of the sprint with interactive exercises where we built the barebones version of the website
* Organizing GitHub repository; issues, PRs, milestones
* I upheld proper practice of Git flow; coordinating branches and advising teammates on correct git branching.
* Deciding on an architecture for the website
* Unblocking teammates

In addition to all of these duties, I also had the following contributions:
* Created and educated teammates about Makefiles to streamline development on the project
* Created and educated teammates about Python virtual environments to explicitly document dependencies and prevent productivity-killing environment-specific issues
* Modified the login page from our static template to be fitting, including “flashing” messages in Python


_Jasper Loverude_

* Worked on backend for the application, using Flask to create the database schema and authentication logic
* Worked on User, Entry, Permission, and Teams tables for describing the database schema in models.py
* Created Python enum representing 5 possible types for ‘Entry’, to standardize data better than a 'string' field
* Created bi-directional association table for the many-to-many relationship of users and teams
* Helped manage teams Git workflow; assisted teammates with getting unblocked with Git
* Implemented backend authentication on auth.py
* Created visual mockup of database schema
* Made Google slides presentation with Chandra
* Added a make command ‘make rmdb’ to remove the database in instance
* Added a make command ‘make new’ that ran a series of other 'make' commands.
	- I used osascript in the make command to open a new terminal tab and make it run commands when the 'python3.10...' terminal hung


_Kelly Putnam_

* Created the SuperAdmin permissions dashboard
* Created the Add Coach, Add Athlete, and Add PEAK Admin pages and made sure they redirected from their respective sidebar buttons correctly
* Redirected clicking on a certain athlete or coach to the Edit Permissions for the specific role
* Added permissions toggles to the Edit Coach Permissions file so that the super admin can control their viewing permissions
* Created Python Flask files for Add Coach, Add Athlete, and Add Admin that added the users to the database with their respective attributes, including role and permissions
* Added forms and inputs to html code to connect the html to the flask tools
* Created Python Flask files for Coach and Athlete Permissions that changed the role and permissions based off of how the super admin edited it
* Added forms and inputs to html code to connect the html to the flask tools

_Ghailan Fadah_

* Worked on the front-end of the project:
* Made the Sleep circle graph dynamic 
* Made the Calorie circle graph dynamic
* Made the Readiness graph dynamic
* Made the progression graph over time dynamic. 
* Helped with making the tables dynamic
* Coordinated with the back-end to make sure our vision aligns in terms of how data will be stream-lined to the front-end.
* Made sure the page was visually pleasing but simple  
* Made sure Jasper got his sleep!

<br><br>

<h2 align="left">Extensions</h3>

<h3 align="left">Extension 1: Burndown chart to reflect on our efficiency.</h4>
	
<p>The Burndown Chart that we generated offers us the ability to reflect on how we worked. While it doesn’t reflect exactly how we worked over time, since we made very big pull requests at the very end and merged it all instead of doing smaller pull requests over time. Therefore, we can definitely look at this graph and see that we need to do smaller pull requests for our next sprint. </p>

<div align="center"><img width="638" alt="Screen Shot 2022-10-28 at 1 35 18 AM" src="https://user-images.githubusercontent.com/92835209/198514024-17d83fae-96c7-4ad5-a50b-a0de076be41e.png"></div>

<h3 align="left">Extension 2: Write your report in Markdown as a readme file in your repository, including table images and appropriate tags and content..</h4> 

<p>We recreated this exact interactive report on the GitHub repository in the README.md file. The link to the README.md file (i.e. on the main repository) is this.</p>

<h3 align="left">Extension 3: Use a makefile to streamline development.</h4> 
	
<p>We employed a Makefile (see 'Makefile') to encode common development tasks with easy-to-understand aliases. This allowed us to get team members up to speed on how to get productive with the codebase fast. </p>

<h3 align="left">Extension 4: Using the python virtual environment.</h4> 

<p>We used the venv package that comes with Python to manage and document our dependencies for this project. Virtual environments allow us to standardize computing environments across developers and help prevent issues from mismatching library versions. By committing the versions of Python libraries we used in requirements.txt (see on GitHub), we made sure that our software is easier to reproduce. This extension goes along with Extension 3; for example, make dependencies will automatically install Python dependencies from the requirements.txt file in the currently checked out branch.</p>


<h2 align="left">References/Acknowledgements</h3>


Burndown Chart: http://radekstepan.com/burnchart/#!/enjoythecode/scrum-wizards-cs321

Database Block-Diagram Creator: https://nulab.com/cacoo/examples/database-diagrams-er-diagram-tool/

Osascript open new Terminal tab (Shell): https://stackoverflow.com/questions/7171725/open-new-terminal-tab-from-command-line-mac-os-x





