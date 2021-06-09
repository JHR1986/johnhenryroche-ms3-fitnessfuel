# Handy Korean Phrases

- [Language Phrases Website - Milestone Project 3](#language-phrases-website---milestone-project-3)
- [User Experience](#user-experience)
  * [User Stories](#user-stories)
  * [First Time Visitor Goals](#first-time-visitor-goals)
  * [Returning Visitor Goals](#returning-visitor-goals)
  * [Frequent Visitor Goals](#frequent-visitor-goals)
- [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
- [Features](#features)
- [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks and Libraries and Programs Used](#frameworks-and-libraries-and-programs-used)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Heroku Deployment](#heroku-deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)
- [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Language Phrases Website - Milestone Project 3

[View the Live Website Here](https://jhroche-handy-korean-phrases.herokuapp.com/)

This project comprises the development of a Korean phrases resource website, where English speakers who are visiting Korea as tourists can learn key phrases in this language in order to assist them with communication when they are in the country. The website also allows visitors to the site to register an account and create their own profile, from which they can then create, read, update and delete phrases themselves when they are logged in. 

In respect of the overall construction of this website, it has been designed to be fully responsive, intuitive and accessible on a range of media devices (e.g. mobile, tablet & desktop), in order to make it as easy as possible for users of the website to navigate it and source the information that they require.

Photo of Site Represented on Various Media to highlight responsive design:

![responsivephoto](https://user-images.githubusercontent.com/71781554/121212704-7e434a00-c875-11eb-991b-1672243efc7c.png)

## User Experience 

### User Stories

### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly establish what information the website contains in respect of English speakers learning easy to use Korean phrases.
2.  As a First Time Visitor, I want to be able to easily navigate throughout the site pages and be able to find and search for Korean phrases for use when I visit the country.
3.  As a First Time Visitor, I want to be able to go to the register page and create my own account.

### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able to login, see phrases that have been added by other users and have the option to add my own phrases.
2.  As a Returning Visitor, I want to be able to easily access the key information in respect of contacting the site owners (info contained in footer) if I have any queries in respect of the website itself.

### Frequent Visitor Goals
1.  As a Frequent/Returning Visitor, I want to be able to login to my account and create, read, update and delete my own phrases. 
2.  As a Frequent/Returning Visitor, I want to be able to see which new phrases have been added by users to the site since my last visit.

## Design

### Colour Scheme
- In line with the Bootstrap Light theme that I used for the Navbar and Footer, I used various green and blue colours to match the design of the logo that I created for the site, while also using grey and white background colours to match the overall bootstrap theme. I ensured that these colours contrasted well and would result in good readability and accessibility for the user, which I checked was in order on Google Lighthouse. 
- The colours that I used for the website are detailed in the colour chart below which I prepared on coolors.co;

![colorpalette](https://user-images.githubusercontent.com/71781554/121214408-037b2e80-c877-11eb-8dd1-3b4e8f136ef6.png)

### Typography
- The PT Sans font (which I downloaded from Google Fonts) is the main font used throughout the whole website, with Sans Serif as the fallback font in case for any reason the PT Sans font fails to be imported correctly.
- As per its description on the Google Fonts website, PT Sans is based on Russian sans serif types of the second part of the 20th century, but at the same time has distinctive features of contemporary humanistic designs. It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov and released by ParaType in 2009.

### Imagery
- The imagery within the website is utilised as a means to highlight the culture of Korea, as well as the beautiful architecture and scenic views that the country has to offer. I used large detailed hero images for the login and registration pages to add more colour to the site, while the home page has images of books and a person typing to highlight the educational aspect of the site, and an image of an iphone to represent the users ability to login and register to the site. 

![homeimages](https://user-images.githubusercontent.com/71781554/121215760-3245d480-c878-11eb-8b8a-db0fb4cb1818.png)

### Wireframes
- My general site map and wireframes are saved to PDF and can be found [here](static/images/wireframes.pdf). I designed them at the start of the project and they served as the basis for this project. 
- In review, the wireframes stayed generally consistent with the finished design (in respect of the home page, phrases page, login page and register page). While completing the wireframes at the start of the project, I was not aware that my project would also require additional html pages in respect of the CRUD features (profile, add task, edit task) and errors (404, 500) so these pages were not included in the original wireframes. I queried this point on the Slack channel and was advised to keep the original wireframes as they are (as they are a reflection of what my original design plan was), while optionally creating a 2nd wireframes file relating to the additional html pages. I took this advice and the wireframes for the additional 5 html pages are located [here](static/images/wireframes2.pdf).

## Features
- The website is responsive on all device sizes (and has been tested through Chrome Dev Tools on various devices including iPhone 6, iPhone X, Galaxy S5, iPad and Desktop).
- The website has several interactive elements, including three Bootstrap buttons on the Home page which can be clicked to navigate to the Phrases, Login and Register Pages, while there are further buttons in the add phrase, edit phrase, profile, login and register pages. 
- Each page in the website features a responsive Bootstrap navigation bar with the site logo featured to the left and the four page links to the right (with the active page highlighted), and these pages also each contain a 3 column Bootstrap footer with a copyright message, address and contact information (email and phone). The pages contain the following features on various pages:
    - Home Page: A main Jumbotron introductory section, three images relating to links to the phrases, login and register pages and two images of Korean culture and architecture. 
    - Phrases Page: A main search box at the top with two buttons (reset and search), and the list of phrases below them.
    - Login Page: Main background hero image with a login box in the centre where users can enter their username and passeword, and press a login button below, as well as a link to the register page. 
    - Register Page: Main background hero image with a registration box in the centre where users can enter their username and passeword, and press a register button below, as well as a link to the login page for current users. 
    - Profile Page: A main jumbotron section, with two cards below with links to the phrases and add phrase pages, as well as a background hero image.
    - Add Task Page: Main background hero image with an add phrase box in the centre where users can enter their phrase category, english phrase, Korean phrase and fun fact about Korean, and press an add phrase button below.
    - Edit Task Page: Main background hero image with an edit phrase box in the centre where users can edit their phrase category, english phrase, Korean phrase and fun fact about Korea, and press either the edit phrase or cancel buttons below.

## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries and Programs Used

1. [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/): Bootstrap was utilised to assist with the responsiveness and styling of the website, specifically in respect of the Navigation and Footer Sections and various jumbtron, cards and rows/columns features used.
2. [MongoDB](https://www.mongodb.com/): MongoDB Atlas was used as the database for this project.
3. [PIP](https://pypi.org/project/pip/): PIP was used to install the tools needed in this project.
4. [Pymongo](https://pypi.org/project/pymongo/): PyMongo was used to serve the communication between Python and MongoDB.
5. [Visual Studio Code](https://code.visualstudio.com/): Visual Studio Code was the IDE used for developing this project.
6. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/): Jinja was utilised to simplify displaying data from the backend of this project smoothly and effectively.
7. [Flask](https://flask.palletsprojects.com/en/2.0.x/): Flask was utilised to construct and render pages for the project.
8. [Google Fonts](https://fonts.google.com/): Google fonts was utilised to import the 'PT Sans' font into the style.css file and this font is used on all pages throughout the website.
9. [Font Awesome](https://fontawesome.com/): Font awesome was utilised in the phrases, login, register, add phrase and edit phrases pages, as well as in the Footer, for aesthetic and UX purposes. I matched the icons with the activity or place that they most closely represented.
10. [Git](https://git-scm.com/): Git was used for version control throughout the project by utilizing the Gitpod terminal to Commit to git and Push to the GitHub repository.
11. [GitHub](https://github.com/): GitHub was used to store the code for the project after being pushed from Gitpod.
12. [FreeLogoDesign](https://www.freelogodesign.org/): FreeLogoDesign was used to create the Handy Korean Phrases logo.
13. [Lets Enhance](https://letsenhance.io/): Lets Enhance was used to enhance the logo in order that the png file size would pass Google Lighthouse.
13. [Favicon](https://en.wikipedia.org/wiki/Favicon): I used a Favicon image of the logo and added it to all of the pages.
14. [Free Image Optimiser](http://www.imageoptimizer.net/Pages/Home.aspx): I utilised a photo optimiser to ensure that the high quality images that I used from the Unsplash website would load quickly.
15. [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAnKeCBhDPARIsAFDTLTJ5qmGTj2XQK_FoiFP6eKlzn-5oxqsh5N5hjjYKaGvx1AKPc1wb48EaAoSYEALw_wcB): Balsamiq was used to create the wireframes during the initial design phase.
16. [Coolors](https://coolors.co/): I prepared the screenshot (included in this Readme) of the colours I had selected for this project using the Coolors template.

## Testing

- Testing information for this project can be found in the separate Testing File [here](testing.md). 

## Deployment
### How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

- An IDE such as Visual Studio Code

The following must be installed on your machine:

- PIP
- Python 3
- Git
- An account at MongoDB Atlas or MongoDB running locally on your machine.
    - How to set up your Mongo Atlas account [here](https://docs.mongodb.com/manual/tutorial/getting-started/).

#### Instructions
1. Save a copy of the github repository located at https://github.com/JHR1986/johnhenryroche-ms3-handykoreanphrases by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

`git clone https://github.com/JHR1986/johnhenryroche-ms3-handykoreanphrases`

2. If possible open a terminal session in the unzip folder or cd to the correct location.
3. A virtual environment is recommended for the Python interpreter. I recommend using Pythons built in virtual environment. Enter the command:

`python -m .venv venv`

NOTE: Your Python command may differ, such as python3 or py.

4. Activate the .venv with the command:
`.venv\Scripts\activate`

Again this command may differ depending on your operating system, please check the Python Documentation on virtual environments for further instructions.

5. If needed, Upgrade pip locally with

`pip install --upgrade pip.`

6. Install all required modules with the command

`pip -r requirements.txt.`

7. In your local IDE create a file called `.flaskenv.`

Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database task_manager, with 3 collections called users, phrases and categories. You will find the structures of these collections in the features section above.

You can now run the application with the command

`python app.py`

You can visit the website at http://127.0.0.1:5000

### Heroku Deployment
To deploy Handy Korean Phrases to Heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile.`
3. `git add` and `git commit` the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
6. Confirm the linking of the heroku app to the correct GitHub repository.
7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars:
![heroku](https://user-images.githubusercontent.com/71781554/121223709-b8194e00-c87f-11eb-8ce4-b2f348c1dedc.png)

To get your MONGO_URI read the MongoDB Atlas documentation [here](https://docs.mongodb.com/manual/reference/connection-string/)

8. In the heroku dashboard, click "Deploy".
9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".
10. The site is now successfully deployed.

### Forking the GitHub Repository
By forking the GitHub Repository, this enables you to make a copy of the original Repository on the GitHub account to view and/or make changes without affecting the original repository;
1.  Log in to GitHub and locate the GitHub Repository which contains the project.
2.  At the top of the Repository (as opposed to the top of page) just above the "Settings" Button on the menu, locate and then select the "Fork" Button.
3.  You should now have a copy of the original Repository in your GitHub account which you can inspect.

### Making a Local Clone
1.  Log in to your GitHub account and locate the GitHub Repository which contains the project.
2.  Under the Repository name, click "Clone or download".
3.  If you wish to clone the Repository using HTTPS, you should copy the link under "Clone with HTTPS".
4.  Proceed to open your preferred terminal.
5.  Change the current working directory to the location where you want the cloned directory to be made.
6.  Type git clone, and then paste the URL you copied from the link that is detailed in Step 3 above.
7.  ```$ git clone https://github.com/USERNAME/REPOSITORY```
8.  Press Enter and your local clone will then be created and available to be inspected and reviewed.

## Credits
### Code
- [Change input field to green when correct number of characters entered](https://stackoverflow.com/questions/39540302/how-to-change-the-background-color-of-an-input-field-when-text-is-entered): I studied this post in order to fully understand how to change the input field green when a correct number of characters had been entered, to assist with the validation process.
- [Validation system for form entries](https://mdbootstrap.com/docs/b4/jquery/forms/validation/): I studied this validation feature from mdbootstrap (including a JS file) and applied it to my project. 
- [Show active page when using Flask and Jinja](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2) I wished to ensure that the page currently clicked on was underlined as active in the Navbar. To achieve this while using flask, I followed the instructions listed in this Stackoverflow post. 
- I studied a comment by Ed Bradley (Ed B) on Code Institute's Slack channel in respect of how to correctly set up the 404 & 500 error pages for Python and Flask.
- I used the Bootstrap Library throughout the project to make the site more responsive through using the Bootstrap Grid System and employing Bootstrap elements for the Navbar, Footer, Jumbotron, Cards and Forms.
- I studied the videos for the Code Institute mini project presented by Tim Nelson prior to starting my website, in order to get a good understanding of how both Flask and MongoDB operate, and how to implement a CRUD system.

### Content
- All content within this project was written by the developer.

### Media
- The images used in this project have all been sourced from Unsplash, which is a stock photography site which contains a large catalogue of high-quality free to use images which are not the subject of copyright. The attributions for these images are listed below;
    - [Image Title Page – Photographer](link)

- The logo for Handy Korean Phrases was created using a template which I made on a design website called FreeLogoDesign, and which I amended in respect of colour scheme and design to match the proposed styling of my site. FreeLogoDeisgn is a website which allows people to make brand logos for free and download them to their own media. I also enhanced the logo using a website called https://letsenhance.io/. 

### Acknowledgements
- I wish to thank my Mentor, Maranatha Ilesanmi, for providing me with excellent feedback and support during the various processes of competing this project.
- I also wish to thank Tutor Support and Student Care at Code Institute for their support and advice during my third term and while working on my MS3 project.
