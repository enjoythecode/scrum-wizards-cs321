# scrum-wizards-cs321

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/enjoythecode/scrum-wizards-cs321/main.svg)](https://results.pre-commit.ci/latest/github/enjoythecode/scrum-wizards-cs321/main)

Athlete Data Management System for CS321 (Fall 2022) at Colby College, ME

<br>


<h1 align="center">Milestone 7 Report</h1>
<h3 align="center">Flask Web App</h3>


<h2 align="left">Abstract</h3>
In Milestone 7, we were tasked with implementing APIs, such as MyFitnessPal, Hawkins Dynamics, and wearable devices such as Apple Watch. We also needed to use these to display the information on each athlete to our website. Since the API tokens were very difficult to access, we finally decided to stick to Hawkins Dynamics, something that the Colby College Athletic Department uses all the time and has a good understanding of. We also knew that, since all Colby students are familiar with Google Drive, we would be able to use Google Fit (which the Athletic Department may or may not use now or in the future) by connecting the accounts of the users of our websites (the athletes, specifically) to their Google drive account. We also used this time to finetune our website, such as fully integrating our database into the entries displayed on the frontend side.

<br><br>

<h2 align="left">Results</h2>
Connecting Google Drive accounts to the CAMS accounts (our software), as well as implementing the Hawkins API, proved to be very difficult. The official API for pulling nutrition data from MyFitnessPal turned out to be falsely-advertised as available freely to developers, which was a misunderstanding that wasted a few days of effort. However, we’ve had better luck with the Hawkins API thanks to access information that we were provided two days before the deadline. Thanks to our efforts with the MyFitnessPal API, we had the code scaffolding to quickly take advantage of the API and successfully import and display Hawkins data for the Tennis team. 
As for cleaning up the website other than the APIs, there was quite a lot of work to be done. Adding a user technically created one, but never added one to the database, so we worked on that and eventually created a lot of users of different roles and added them to the database. Using this expanded database, we made use of the extremely helpful helper_db.py file, which essentially had a bunch of different functions which could query users by all of their attributes. These were helpful, as we also spent this milestone replacing the mock database that we had created and were displaying as the athletes/coaches for the admin, with the real database that we created. This was further expanded when we successfully implemented the Hawkins API, since we were able to add real Colby athletes to the database with their real data (scrambled, as to keep their anonymity). Therefore, real athletes from a team were really displayed on our website, which made all the hard work worth it, since this felt like something the client could really use. 
<div align="center"><img width="565" alt="Unit-test" src="https://user-images.githubusercontent.com/92835209/203896563-9f22d838-8fe2-4e6c-939e-68864aab523e.png"></div>
<div align="center">Fig 1: A unit test, complete with proper GIVEN, WHEN, THEN documentation.
</div>

<div align="center"><img width="825" alt="Screen Shot 2022-11-24 at 10 38 48 PM" src="https://user-images.githubusercontent.com/92835209/203896788-fcf8874a-530e-4cf6-8a26-0ca57b5fac39.png"></div>
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

<h3 align="left">Extension 1: Burndown chart to reflect on our efficiency.</h4>

<p>The Burndown Chart that we generated offers us the ability to reflect on how we worked. While it doesn’t reflect exactly how we worked over time, since we made very big pull requests at the very end and merged it all instead of doing smaller pull requests over time. Therefore, we can definitely look at this graph and see that we need to do smaller pull requests for our next sprint. </p>

<div align="center"><img width="638" alt="Screen Shot 2022-10-28 at 1 35 18 AM" src="https://user-images.githubusercontent.com/92835209/198514024-17d83fae-96c7-4ad5-a50b-a0de076be41e.png"></div>

<h3 align="left">Extension 2: Write your report in Markdown as a readme file in your repository, including table images and appropriate tags and content..</h4>

<p>We recreated this exact interactive report on the GitHub repository in the README.md file. The link to the README.md file (i.e. on the main repository) is this.</p>

<h3 align="left">Extension 3: Use a makefile to streamline development.</h4>

<p>We employed a Makefile (see 'Makefile') to encode common development tasks with easy-to-understand aliases. This allowed us to get team members up to speed on how to get productive with the codebase fast. Several of our Makefile aliases included 'make test', to run pytest, 'make coverage', to run pytest with coverage, and 'make coverage-open', to make run test coverage and open the test-coverage report in a browser. </p>

<h2 align="left">References/Acknowledgements</h3>

Pre-commit: https://pre-commit.com/

Burndown Chart: http://radekstepan.com/burnchart/#!/enjoythecode/scrum-wizards-cs321

Database Block-Diagram Creator: https://nulab.com/cacoo/examples/database-diagrams-er-diagram-tool/

Osascript open new Terminal tab (Shell): https://stackoverflow.com/questions/7171725/open-new-terminal-tab-from-command-line-mac-os-x
