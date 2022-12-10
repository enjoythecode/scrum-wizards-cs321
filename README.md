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


<div align="center"><img width="622" alt="Screen Shot 2022-12-09 at 9 22 26 PM" src="https://user-images.githubusercontent.com/92835209/206824124-62e81020-7699-4872-a523-36a85924930a.png">
<div align="center">Fig 1: Data entries received from the Hawkins Dynamics API. First 10 out of 100+ Hawkins Dynamics stats for the tennis team, displayed on the coach and admin view of the Tennis team (scrambled data for anonymity). 
</div>
<div align="center"><img width="625" alt="Screen Shot 2022-12-09 at 9 24 53 PM" src="https://user-images.githubusercontent.com/92835209/206824221-797302c2-f8e8-4237-bf3d-095d2bfb3482.png"></div>

<div align="center">Fig. 2: All users we have entered in the database displayed (with randomized clearance for now) on the super-admin dashboard.

<div align="center"><img width="626" alt="Screen Shot 2022-12-09 at 9 26 04 PM" src="https://user-images.githubusercontent.com/92835209/206824268-baa017e4-456d-49f5-9714-33ba409e2dab.png"></div>
	<div align="center">Fig. 3: The same page as above after using the search bar, to demonstrate functionality

		


<div align="center"><img width="623" alt="Screen Shot 2022-12-09 at 9 28 55 PM" src="https://user-images.githubusercontent.com/92835209/206824356-3f7ca3c1-3113-45a3-8f57-231127e27532.png"></div>
		<div align="center">Fig. 4: The athlete dashboard, showing the button we added to sync with Google Drive in the case we end up using Google Fit
			
<div align="center"><img width="626" alt="Screen Shot 2022-12-09 at 9 29 39 PM" src="https://user-images.githubusercontent.com/92835209/206824384-42191894-b6e7-4734-b485-9b7bee7025c4.png"></div>
			<div align="center">Fig. 5: After pressing the Sync with Google Drive button, the window that pops up (obviously if I was the current athlete, the accounts would match up and I could log in)
<div align="center"><img width="619" alt="Screen Shot 2022-12-09 at 9 30 50 PM" src="https://user-images.githubusercontent.com/92835209/206824436-7de2c25b-8a5c-4b42-800b-cfe4da6b88bf.png"></div>
<div align="center">Fig. 6: Issues closed in this milestone.

<br>

<h2 align ="left">Team Reflection</h2>
<div align="left">
This task was very difficult and was probably the most enlightening as to the real Software Engineering process. Accessing the API tokens was near impossible for many of the APIs, connecting to Google Drive was difficult, and going through documentation for each API especially could be very confusing. However, going through difficult documentation in order to implement what is arguably the most crucial part of this software (the athlete/team information and data) is what being a software engineer is all about. We also had to have a lot of conversations as a team about how best to display the data, which we didn’t even think about when we were busy focusing on connecting the data and actually getting it. Furthermore, going through the entire website also showed us how many other issues needed to be resolved; it was very hard to focus on one thing when we realized that our website also needed other functions that were less crucial than APIs, but still important to the client. However difficult this milestone was, it was easily the most rewarding when we finally received the Colby athlete data from Hawkins Dynamics after a lot of hard work from the back end team. 

<br>
	
<h2 align ="left">Burndown Chart</h2>
<div align="center"><img width="593" alt="Screen Shot 2022-12-09 at 9 32 57 PM" src="https://user-images.githubusercontent.com/92835209/206824537-de445135-a3f5-4d87-b69d-436433426969.png">
	
As you can see, the burndown chart was not a straight line down with perfectly distributed pull requests throughout time. However, the nature of this milestone was basically a lot of work beforehand (getting the API tokens, formatting the data), so it was very frontloaded. We also couldn’t make the table and display the data until we had achieved it, so the frontend work was also forced to the end after the bigger issues. However, it is still important to note that we need to work on having smaller pull requests, and much more of them, so we can distribute our work over time. 


<h2 align="left">Contributions</h3>

**List of all group members contributions**

_Chandra Gowda_

* Added user-interface integration between Google Drive API and our application
* Setup Google Fit API implementation on the backend
* Created the readcsv.py file for interpreting csv files for reading in data into the users database
* Connected my Apple Watch to Google Fit and setup test data to be imported and integrated with the Google Drive

_Zehra_

* Created the use-case diagram for our current version of the Colby Athlete Data Management system.
* Worked on the redirectings of buttons on the super admin edit permissions page.


_Sinan_

* Worked with Ghailan on understanding and attempting to connect to the MyFitnessPal API
* Wrote data download automation from the Hawkins API from scratch under time pressure
* Unblocked teammates by debugging git and Flask issues


_Jasper Loverude_

* Pair programmed with Kelly to give admin page a real-time and accurate display of users, with links to their permissions pages
* Worked with Chandra to add user-interface integration between the Google Drive API and our application
* Served as scrum master for Milestone 7
	- Provided assistance unblocking people with git/merge issues


_Kelly Putnam_

* Helped on the front end for users to be able to have access to their API data as well as for the athletes to be able to import it
	- Created the buttons to access the data
	- Helped with displaying the data in a readable way
* Fine-tuned adding real users to the database
* Connected the database of athletes and coaches to a real list of Colby athletes and coaches
	- To display them on the Super Admin page, so they can be accessed
	- To display the athletes of a single team on the coach page, so that the coach can access real Colby athletes
* Worked on report 
* Connected the .csv file we created from Hawkins Dynamics data and used Flask, Python, and HTML to display it as a table on the website


_Ghailan Fadah_

* Worked on understanding and adding the myfitnesspal API to our application with sinan 
* Worked on implanting and understanding the hawking dynamics with sinan
* Peer programming with Sinan, Kelly, and Jasper
* Looked at and tried to understand the documentation for Flask dance.

_Emmanuel Assumang_
	
* Made the search bars active in the super admin page. 
* Enables the super admin search for athlete names and coach names in the search bars easily.
* Made a new file named api.py to handle the backend side and the logic to fetch the athletes/coaches database based on the search query. I updated home.html with a search input and search button id for both coaches and athletes.
* Created a searchathletecoach.js file which contained the fetch coach and athlete functions that handled the on-click events on the button. Added this in the assets/js folder.
* Partially worked with Chandra and Jasper to add user-interface integration between the Google Drive API and the application.


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
