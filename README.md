# scrum-wizards-cs321
Athlete Data Management System for CS321 (Fall 2022) at Colby College, ME

<br>


<h1 align="center">Milestone 4 Report</h1>
<h3 align="center">Flask Web App</h3>

<br><br>


<h2 align="left">Abstract</h3>
<p>In Milestone 4, we came together as a team to create a Flask web application that used the highest priority issues that we had created on GitHub. We used our static website from the previous milestone as a starting point, then edited the HTML in order to add more of what our application required. We also created Python files that implemented flask, and connected them to our HTML files with inputs. We split the work into backend (authorization, database) and frontend (superadmin, team, and individual athlete dashboards), which really immersed us in github remote programming and merging the two groups together at the end. We also split up the backend work, and the front end work, so that we could form smaller groups and practice pair programming. This functional web application showed us how to work as a team, even when we are not physically together, using GitHub, as well as showing us how to use Flask. 
</p>

<br><br>

<h2 align="left">Results</h2>
<p>After the group work and pair programming mentioned above, we basically had four branches: one for database and authorization, one for super admin adding and editing users, one for team and athlete dashboards, and another for login. Once we had all completed our individual branches, we came together and made pull requests to merge everything onto our develop remote branch. We used code reviews, and fixed merge conflicts together to avoid any important code being overwritten, in order to create the web application shown below.</p>

<br>

<p align="center">
    <div>
</p>

<div align="center"><a href="https://github.com/enjoythecode/scrum-wizards-cs321">
Our GitHub Repository</a> </div>

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

<h2 align="left">Team Reflection:</h2>
<p>This milestone was definitely the most complicated yet, as it forced us to work with tools that we had, for the most part, never used before (Flask and its many capabilities, GitHub and working remotely as a group) and other tools, such as implementing HTML with Python files. Working remotely was definitely challenging, and we had to practice a lot with GitHub in order to combine all our ideas effectively. We made many mistakes with GitHub, but facing these challenges with the help of our Scrum Master, and fixing merge conflicts all together definitely made us stronger as a team. Code reviews were done extremely effectively and respectfully, and we all learned so much from this incredibly immersive milestone. We are now definitely much more prepared for the remote group work that is ahead of us, and are all the more ready for more learning challenges. </p>

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

* Adapted the HTML from the Corona template to create the following pages / features:
	- Created the Athlete Breakdown board on the PEAK/ Coach dashboard index.html.
	- Created the main admin dashboard index.html, added:
	- The charts presenting team results
	- A list of users and a search bar for users.
	- Buttons to download reports / edit user permissions.
* Participated in pair-programming with Sinan.
* Practiced the GitHub workflow, created and reviewed pull requests, merged branches

_Sinan_

* Served the team as the Scrum Master
* Lead pair programming to teach all teammates about Git and HTML, oversaw branching strategy, helped debug various issues to unblock individual work
* Created GitHub repository, configured Netlify with automated deploys of all branches (Previews for PRs and production deploys on the main branch)
* Created GitHub issues
* Polished folder structure after teammates pushed their commits
* Created Login HTML mock with links to individual mocks for superadmin, admin, and athlete

_Jasper Loverude_

* Pair programmed with Kelly on Athletepermissions.html and Coachpermissions.html
* Added custom HTML element (toggle) for disabling coach view out-of-season
* Added appropriate CSS to core css file for animation, styling of out-of-season toggle
* Helped resolved Git problems related to branching and managing remote/local branches
* Helped team navigate commits and merging
	- Connected PRs to issues on Github project so that work is tracked and efficiency can be recorded
* Added Anne Beethe profile photo
* Worked on Extension 3: Worked on adding milestone 3 report to markdown on the README.md file on the github repository.

_Kelly Putnam_

* Adapted the HTML from the Corona template to create the following pages: 
	-Permissions.html, which is essentially where PEAK admin can choose a team, coach, or athlete and choose to adjust their permissions. They can also choose to add a user here.
	- Athletepermissions.html, which adjusts athlete permissions
	- Coachpermissions.html, which adjusts coach permissions
	- Addcoach.html, which adds a coach
	- Addathlete.html which adds an athlete and adds personal information about the athlete
	- Addpeak.html, which adds an admin
* Focused on design elements for the above pages and created a baseline for the rest of the group to approve, improve, and adapt
* Extension 1: adding a bit of functionality so that the navigation buttons on the side of the permissions website actually leads to add a user, and clicking on a user leads to their permissions

_Ghailan Fadah_

* Used the Corona template to create part of the coaches dashboard
* Created the bar graph in the coaches view
* Created the dropdown bottom on the coaches team selection
* Created the download and time selection buttons
* Took part in pair programming sessions with Sinan
* Used the github flow  to push and pull template with teammates



<h2 align="left">Extensions</h3>



