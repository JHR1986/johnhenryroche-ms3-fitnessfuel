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
- [Database Design](#database-design)
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

## Database Design

- I used MongoDB as the database for this project, and the plan of the database (which I named task_manager) is detailed below;

![database](https://user-images.githubusercontent.com/71781554/121535833-68ab5d00-c9fa-11eb-9975-c53963210520.png)

I also created an Index relating to searches for English and Korean phrases in the Phrases html page.

The code for this project relating to interaction with the MongoDB database is outlined below;
1. Getting the list of phrases saved to database:
```
# App route for phrases page
@app.route("/get_phrases")
def get_phrases():
    phrases = list(mongo.db.phrases.find())
    return render_template("phrases.html", phrases=phrases, page="get_phrases")
```
2. Searching for English or Korean phrase:
![mongo1](https://user-images.githubusercontent.com/71781554/121538485-ba54e700-c9fc-11eb-92c5-930016ab485d.png)
3. Checking if username already exists in database:
![mongo2](https://user-images.githubusercontent.com/71781554/121538631-d8224c00-c9fc-11eb-93fc-bb148ee9465e.png)
4. Checking if username already exists in respect of login page:
![mongo3](https://user-images.githubusercontent.com/71781554/121539015-2e8f8a80-c9fd-11eb-9440-974379f4f6ad.png)
5. Grabbing username from database for login to profile page:
![mongo4](https://user-images.githubusercontent.com/71781554/121539238-64cd0a00-c9fd-11eb-91bd-1512f5106a80.png)
6. Adding new phrase to database:
![mongo5](https://user-images.githubusercontent.com/71781554/121539449-9940c600-c9fd-11eb-9863-b83052ed2561.png)
7. Editing phrase in database:
![mongo6](https://user-images.githubusercontent.com/71781554/121539562-afe71d00-c9fd-11eb-8470-622997a2bdd8.png)
8. Deleting phrase from database:
![mongo7](https://user-images.githubusercontent.com/71781554/121539654-c55c4700-c9fd-11eb-9bc7-9513ce878aef.png)

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
### Database Deployment
### Application Hosting
### Heroku

The website is hosted using Heroku and is deployed directly from the master branch of GitHub. The deployed site updates automatically as new commits are pushed to the master branch.

Creating a Heroku app:
- From the Heroku dashboard select "New" and then select "Create new app"

- Add new app details to form:
  - Add an app name (this name must be unique)
  - Select your region
  - Click "Create App"

Setting Environmental Variables:
- From the Heroku dashboard:
  - Select your newly created app from the list
- Select "Settings" from the top menu:
  - Under 'Config Vars', select "Reveal Config Vars"
  - Add your environment variables in key-value pairs, and then click "Add" to add additional pairings.

Deployment:
- Create the following required deployment files in the repository:
  - requirements.txt: This file lists the required python modules for Heroku to install. In order to create this file, type: pip freeze > requirements.txt in your IDE terminal.
  - Procfile: This file tells Heroku the command to launch the app. In order to create this file, type: python app.py > Procfile in your IDE terminal. 
  - .gitignore (this file is optional): This tells git which files (or patterns) it should ignores. To create this file, type: touch .gitignore in your IDE terminal type. This lists the files and directories to be excluded from live deployment, within the .gitignore file. Save this file to your repository root directory.

From the application top menu:
  - Select 'Deploy'
  - Choose your Deployment method:
    - Github: Select the correct Github account. Type in the repository name that you wish to deploy. Choose the correct repository from search results and then select "Connect".
    - Manual Deployment: Choose the correct branch you wish to deploy from the drop-down. Select "Deploy Branch" and Heroku will then return "Your App has successfully deployed". 

Automatic Deployment
  - From the application top menu, select 'Deploy' and ensure that the app is connected to the correct repository. Under the 'Automatic Deployment' section, select 'Enable Automatic Deployment". 

### GitHub and GitPod Repository Management

### How to clone 'Handy Korean Phrases' in GitHub, GitPod and setup on Heroku.

To run a version of the site locally, you can clone this repository using the following steps;

In a code editor of your choice;

1. Go to GitHub.com
2. Click on 'Repositories'
3. Click on 'Handy Korean Phrases'
4. Click on the 'Code' button.
5. Under 'HTTPS' click the clipboard icon to the right of the URL.
6. In your IDE of choice, open a repository or create a new repository.
7. Open Terminal ('Terminal' then 'New Terminal' from the top ribbon menu in GitPod.)
8. Type 'git clone', paste the URL link and press enter.

Additional information around these cloning steps can be found on GitHub Pages Help Page.  

### Installing Requirements

- Install all requirements modules to your local IDE with the following CL:

`pip3 install -r requirements.txt`

### Create Collections in MongoDB

- Login to your MongoDB account
- Create a Cluster and then create a database using the information contained in the Database Design section of this Readme file.

### Setup Environmental Variables

- Create a '.gitignore' file in the root directoy.
- Add 'env.py' and 'pycache/' to the file list within the gitignore file. 
- Create an 'env.py' file and in the 'env.py' file write the following code lines;

```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "[UNIQUE ID]")
os.environ.setdefault("MONGO_URI", "[UNIQUE ID]") 
os.environ.setdefault("MONGO_DBNAME", "[UNIQUE ID]")
```

Note: For each section noted as [UNIQUE ID], you will need to provide your own unique identifier. These must also be aligned to Heroku environmental variables.

### Setup Unique Identifies / Environment Variables

#### SECRET_KEY
This is required when using flash() and session() functions in flask. The key can be whatever you want, but it is generally advisable to use a randomly generated secure key.

#### MONGO_URI
The Mongo URI is used to connect your application to your MongoDB cluster.

- Click the 'Overview' tab from your Cluster, followed by 'Connect'.
- Select 'Connect your application'.
- Select your correct version of Python and copy the connection string.
- Replace the 'username' and 'password' text, with the relevant criteria you setup in 'Database Access'.

#### MONGO_DBNAME
This is the name of your database in MongoDB. This can be foung under the 'Collections' tab, which is located under your cluster.

Running Development Server

To launch a Http server using the development mode code for the application, use the following command in your IDE:

`python3 app.py http.server`

The IDE will then open a port for you to access the site.

## Credits
### Code
- [Change input field to green when correct number of characters entered](https://stackoverflow.com/questions/39540302/how-to-change-the-background-color-of-an-input-field-when-text-is-entered): I studied this post in order to fully understand how to change the input field green when a correct number of characters had been entered, to assist with the validation process.
- [Validation system for form entries](https://mdbootstrap.com/docs/b4/jquery/forms/validation/): I studied this validation feature from mdbootstrap (including a JS file) and applied it to my project. 
- [Show active page when using Flask and Jinja](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2): I wished to ensure that the page currently clicked on was underlined as active in the Navbar. To achieve this while using flask, I followed the instructions listed in this Stackoverflow post. 
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
