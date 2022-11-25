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

<div align="center"><img width="565" alt="Unit-test" src="https://user-images.githubusercontent.com/92835209/203896563-9f22d838-8fe2-4e6c-939e-68864aab523e.png"></div>
<div align="center">Fig 1: A unit test, complete with proper GIVEN, WHEN, THEN documentation.
</div>

<div align="center"><img width="565" alt="Unit-test" src="https://user-images.githubusercontent.com/92835209/203896698-ae72eaf8-9b06-4f7a-aafd-2ac89a70a1a1.png"></div>
<div align="center">Fig 2: Test coverage report
</div>

<br>

<h2 align ="left">Team Reflection</h2>
<p>All in all, we are very grateful to this milestone because we learned about all the mistakes we had made in our code that we never would have otherwise run into. We went into this milestone thinking that our code was perfect because, whenever we ran the website through the server, everything was working perfectly and we thought that was a complete test of everything. However, when we wrote our own tests, we realized exactly how many things we needed to test in order to simulate everything a user might run into. For example, we had to make so many tests that redirected pages to other ones, and while most of them worked like we expected, some of them (that we had never tested before) resulted in errors and we were able to fix that so clicking on certain buttons led exactly to the page we wanted. We also practiced so much with functional v. unit testing that we definitely have a much better grasp on the differences between them, especially when it comes to testing with Flask. Without testing, we could have given faulty software to our clients.</p>

<br>

<h2 align="left">Contributions</h3>	

**List of all group members contributions**

_Chandra Gowda_

* Setup the testing environments/functions in conftest.py and __init__.py
* Added tests for “get” functions in helper_db.py
* Helped resolve git-workflow related issues during pair-programming sessions


_Zehra_ 

* Worked on testing views.py
* Wrote test functions for redirecting to the athlete home page and the individual dashboards
* Wrote test functions for redirecting to the coach home page and the team dashboards
* Wrote a test function for the mock database function in views.py that we used in the earlier stages of development 

_Sinan_

* Set up pytest for automated testing
* Set up the "coverage" tool for automated code coverage reporting on top of pytest, including Makefile aliases
* Set up pre-commit configuration for automated testing and code quality checking.
* Assisted teammates with resolving git branching situations such that it fit proper git flow branching structure.

_Jasper Loverude_

* Added unit tests for “update” functions in helper_db.py
* Utilized HTML inheritance to remove hundreds of lines of <head> html code, (did not get to all files)
* Added documentation for all backend db-related tests in GIVEN, WHEN, THEN format
* Added new background for login, and new browser tab image
* Added generic rerouting so all uncaught paths go to /login
* Helped resolve git-workflow related issues during pair-programming sessions

_Kelly Putnam_

* Fixed an issue with the delete and save forms for user permissions (on the super admin side) 
 	- Now, there is a different form for delete and another one for save, so they can do two different actions
* Testing
	- Wrote superadmin tests in views.py for test_views.py
	- Wrote tests for addathlete, adduser, addadmin in test_adduser.py
* Served as Scrum Master and organized meetings, assigned tasks

_Ghailan Fadah_

* Developed testing for views.py
* Helped with git-flow 
* Did pair-programming with zehra
* Developed testing for auth.py; in particular log in and log out structure. 
* Developed additional testing for coach page 
* Developed additional testing for athlete page
* Made sure Jasper got his sleep!

_Emmanuel Assumang_	
	
<br><br>

<h2 align="left">Extensions</h3>

<h3 align="left">Extension 1: Use Precommit for CI</h4>
	
<p>For this milestone, we chose to achieve CI capabilites with Precommit, a library that performs automatic testing on all commits before they can be made. Using precommit, we reduced the complexity and time required to ensure that all code is tested, because precommit runs tests before changes are committed, rather than during the PR process like most CI features. Additionally, pre-commit hooks allow for further linting and code quality standardization, which leaves room to expand upon our current CI capabilites.</p>

<div align="center"><img width="638" alt="Screen Shot 2022-10-28 at 1 35 18 AM" src="https://user-images.githubusercontent.com/92835209/198514024-17d83fae-96c7-4ad5-a50b-a0de076be41e.png"></div>

<h3 align="left">Extension 2: Write your report in Markdown as a readme file in your repository, including table images and appropriate tags and content..</h4> 

<p>We recreated this exact interactive report on the GitHub repository in the README.md file. The link to the README.md file (i.e. on the main repository) is this.</p>

<h3 align="left">Extension 3: Use a makefile to streamline development.</h4> 
	
<p>We employed a Makefile (see 'Makefile') to encode common development tasks with easy-to-understand aliases. This allowed us to get team members up to speed on how to get productive with the codebase fast. Several of our Makefile aliases included 'make test', to run pytest, 'make coverage', to run pytest with coverage, and 'make coverage-open', to make run test coverage and open the test-coverage report in a browser. </p>

<h2 align="left">References/Acknowledgements</h3>

Pre-commit: https://pre-commit.com/

Burndown Chart: http://radekstepan.com/burnchart/#!/enjoythecode/scrum-wizards-cs321
