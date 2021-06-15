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
  * [How to run this project locally](#how-to-run-this-project-locally)
  * [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Language Phrases Website - Milestone Project 3

[View the Live Website Here](https://jhroche-handy-korean-phrases.herokuapp.com/)

This project comprises the development of a Korean phrases resource website, where English speakers who are visiting South Korea as tourists can learn key phrases in this language in order to assist them with communication when they are in the country. The website also allows visitors to the site to register an account and create their own profile, from which they can then create, read, update and delete phrases themselves when they are logged in. 

In respect of the overall construction of this website, it has been designed to be fully responsive, intuitive and accessible on a range of media devices (e.g. mobile, tablet & desktop), in order to make it as easy as possible for users of the website to navigate it and source the information that they require.

Photo of Site Represented on Various Media to highlight responsive design:

![responsive](https://user-images.githubusercontent.com/71781554/121665154-23416b00-caa0-11eb-9bec-1a12e464fbfd.png)

## User Experience 

### User Stories

### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly establish what information the website contains in respect of English speakers learning easy to use Korean phrases.
2.  As a First Time Visitor, I want to be able to easily navigate throughout the site pages and be able to find and search for Korean phrases to use when I visit the country.
3.  As a First Time Visitor, I want to be able to go to the Register page and create my own account.

### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able to login, see phrases that have been added by other users and have the option to add my own phrases.
2.  As a Returning Visitor, I want to be able to easily access the key information in respect of contacting the site owners (info contained in footer) if I have any queries in respect of the website itself.

### Frequent Visitor Goals
1.  As a Frequent/Returning Visitor, I want to be able to login to my account and create, read, update and delete my own phrases. 
2.  As a Frequent/Returning Visitor, I want to be able to see which new phrases have been added by users to the site since my last visit.

## Design

### Colour Scheme
- In line with the Bootstrap Light theme that I used for the Navbar and Footer, I used various green and blue colours to match the design of the logo that I created for the site, while also using grey and white background colours to match the overall bootstrap theme. I also used a dark red colour for the Reset and Cancel buttons (see colour chart below). I ensured that these colours contrasted well and would result in good readability and accessibility for the user, which I confirmed was in order through completing detailed testing on Google Lighthouse.

- The colours that I used for the website are detailed in the colour chart below which I prepared on coolors.co;

![coolors](https://user-images.githubusercontent.com/71781554/121667498-3fdea280-caa2-11eb-8fde-d9c1e6fc474c.png)

### Typography
- The PT Sans font (which I downloaded from Google Fonts) is the main font used throughout the whole website, with Sans Serif as the fallback font in case for any reason the PT Sans font fails to be imported correctly.
- As per its description on the Google Fonts website, PT Sans is based on Russian sans serif types of the second part of the 20th century, but at the same time has distinctive features of contemporary humanistic designs. It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov and released by ParaType in 2009.

### Imagery
- The imagery within the website is utilised as a means to highlight the culture of Korea, as well as the beautiful architecture and scenic views that the country has to offer. I used large detailed background hero images for the login, registration, error (404 & 500) and profile pages to add more colour to the site, while the home page has images of books and a person typing to highlight the educational aspect of the site, and an image of an iphone to represent the users ability to login and register to the site. Examples of the images used in the site are detailed below; 

![homepageimages](https://user-images.githubusercontent.com/71781554/121673393-bd0d1600-caa8-11eb-8270-5b0d042b07ad.png)

![homepageimages2](https://user-images.githubusercontent.com/71781554/121673457-cc8c5f00-caa8-11eb-8ac2-4f4b4243b739.png)

![loginimage](https://user-images.githubusercontent.com/71781554/121863517-d9e95980-ccf3-11eb-9bc1-35499af51e20.jpg)

### Wireframes
- My general site map and wireframes are saved to PDF and can be found [here](static/images/wireframes.pdf). I designed them at the start of the project and they served as the basis for this project. 
- In review, the wireframes stayed generally consistent with the finished design (in respect of the Home page, Phrases page, Login page and Register page). While completing the wireframes at the start of the project, I was not aware that my project would also require additional html pages in respect of the CRUD features (Profile, Add Phrase, Edit Phrase) and errors (404, 500) so these pages were not included in the original wireframes. I queried this point on the Slack channel and was advised to keep the original wireframes as they are (as they are a reflection of what my original design plan was), while optionally creating a 2nd wireframes file relating to the additional html pages. I took this advice and the wireframes for the additional 5 html pages are located [here](static/images/wireframes2.pdf).

## Features
- The website is responsive on all device sizes (and has been tested through Chrome Dev Tools on various devices including iPhone 6, iPhone X, Galaxy S5, iPad and Desktop).
- The website has several interactive elements, including three Bootstrap buttons on the home page which can be clicked to navigate to the Phrases, Login and Register pages, while there are further call to action buttons in the Add Phrase, Edit Phrase, Profile, Login, Register and Error pages. 
- Each page in the website features a responsive Bootstrap navigation bar with the site logo featured to the left and the four page links to the right (with the active page highlighted), and these pages also each contain a 3 column Bootstrap footer with a copyright message, address and contact information (email and phone). 

The pages contain the following features on various pages:
    - Home Page: A main jumbotron introductory section, three images relating to links to the Phrases, Login and Register pages, and two images of Korean culture and architecture. 
    - Phrases Page: A main search box at the top of the page with two buttons (reset and search), and the list of phrases below them. When logged in, the user has access to edit and delete buttons in respect of phrases which they have added.
    - Login Page: Main background hero image with a login box in the centre where users can enter their username and password, and press a login button below, as well as a link to the Register page. 
    - Register Page: Main background hero image with a registration box in the centre where users can enter their username and passeword, and press a register button below, as well as a link to the Login page for current users. 
    - Profile Page: A main jumbotron section, with two cards below with links to the Phrases and Add Phrase pages, as well as a background hero image.
    - Add Task Page: Main background hero image with an add phrase box in the centre where users can enter their phrase category, English phrase, Korean phrase and fun fact about Korean, and press an add phrase button below.
    - Edit Task Page: Main background hero image with an edit phrase box in the centre where users can edit their phrase category, English phrase, Korean phrase and fun fact about Korea, and press either the edit phrase or cancel buttons below.
    - 404 Error Page: A page with a heading "404 Error", a confirmation statement "Something went wrong" and link back to the homepage, as well as a hero image below this text. 
    - 500 Error Page: A page with a heading "500 Error", a confirmation statement "Something went wrong" and link back to the homepage, as well as a hero image below this text. 

## Database Design

- I used MongoDB as the database program for this project, and the plan of the database (which I named task_manager) is detailed below;

![database](https://user-images.githubusercontent.com/71781554/121675310-268e2400-caab-11eb-9767-8b6aa37303f8.png)

There are three collections titled "Categories", "Phrases" and "Users", and I also created an Index relating to the search function for English and Korean phrases in the phrases page.

The code for this project relating to interaction with the MongoDB database is outlined below;
1. Getting the list of phrases saved to database:
```
# App route for Phrases page
@app.route("/get_phrases")
def get_phrases():
    phrases = list(mongo.db.phrases.find())
    return render_template("phrases.html", phrases=phrases, page="get_phrases")
```
2. Searching for English or Korean phrases:
```
# App route for search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    phrases = list(mongo.db.phrases.find({"$text": {"$search": query}}))
    return render_template("phrases.html", phrases=phrases)
```
3. Checking if username already exists in respect of Register page:
```
# App route for register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
```
4. Checking if username already exists in respect of Login page:
```
# App route for login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
```
5. Grabbing username from database for login to Profile page:
```
# App route for profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, page="profile")

    return redirect(url_for("login"))
```
6. Adding new phrase to database:
```
# App route for add phrase page
@app.route("/add_phrase", methods=["GET", "POST"])
def add_phrase():
    if request.method == "POST":
        phrase = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.insert_one(phrase)
        flash("Phrase Successfully Added!")
        return redirect(url_for("get_phrases"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_phrase.html", categories=categories, page="add_phrase")
```
7. Editing phrase in database:
```
# App route for edit phrase page
@app.route("/edit_phrase/<phrase_id>", methods=["GET", "POST"])
def edit_phrase(phrase_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.update({"_id": ObjectId(phrase_id)}, submit)
        flash("Phrase Successfully Updated!")

    phrase = mongo.db.phrases.find_one({"_id": ObjectId(phrase_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_phrase.html", phrase=phrase, categories=categories)
```
8. Deleting phrase from database:
```
# App route for delete phrase function
@app.route("/delete_phrase/<phrase_id>")
def delete_phrase(phrase_id):
    mongo.db.phrases.remove({"_id": ObjectId(phrase_id)})
    flash("Phrase Successfully Deleted!")
    return redirect(url_for("get_phrases"))
```
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
4. [PyMongo](https://pypi.org/project/pymongo/): PyMongo was used to serve the communication between Python and MongoDB.
5. [Visual Studio Code](https://code.visualstudio.com/): Visual Studio Code was the IDE used for developing this project.
6. [Heroku](https://www.heroku.com/): Heroku was utilised to host and deploy my website.
7. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/): Jinja was utilised to simplify displaying data from the backend of this project smoothly and effectively.
8. [Flask](https://flask.palletsprojects.com/en/2.0.x/): Flask was utilised to construct and render pages for the project.
9. [Google Fonts](https://fonts.google.com/): Google fonts was utilised to import the 'PT Sans' font into the style.css file and this font is used on all pages throughout the website.
10. [Font Awesome](https://fontawesome.com/): Font Awesome was utilised in the Phrases, Login, Register, Add Phrase and Edit Phrases pages, as well as in the footer, for aesthetic and UX purposes. I matched the icons with the activity or place that they most closely represented.
11. [Git](https://git-scm.com/): Git was used for version control throughout the project by utilizing the Gitpod terminal to Commit to git and Push to the GitHub repository.
12. [GitHub](https://github.com/): GitHub was used to store the code for the project after being pushed from Gitpod.
13. [FreeLogoDesign](https://www.freelogodesign.org/): FreeLogoDesign was used to create the Handy Korean Phrases logo.
14. [Lets Enhance](https://letsenhance.io/): Lets Enhance was used to enhance the logo in order that the png file size would pass Google Lighthouse requirements.
15. [Favicon](https://en.wikipedia.org/wiki/Favicon): I used a Favicon image of the logo and added it to all of the pages.
16. [Free Image Optimiser](http://www.imageoptimizer.net/Pages/Home.aspx): I utilised a photo optimiser to ensure that the high quality images that I used from the Unsplash website would load quicker.
17. [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAnKeCBhDPARIsAFDTLTJ5qmGTj2XQK_FoiFP6eKlzn-5oxqsh5N5hjjYKaGvx1AKPc1wb48EaAoSYEALw_wcB): Balsamiq was used to create the wireframes during the initial design phase.
18. [Coolors](https://coolors.co/): I prepared the screenshot (included in this Readme) of the colours I had selected for this project using the Coolors template.

## Testing

- Testing information for this project can be found in the separate Testing File [here](testing.md). 

## Deployment

### How to run this project locally

In order to run this project on your own IDE, follow the instructions detailed below:

Ensure that you have the following tool:
- An IDE such as Visual Studio Code (which was used to create the Handy Korean Phrases site).

Please note that the following items must be installed on your machine in order to run this project:

- PIP (used for installation of tools)
- Python 3 (programming language)
- Git (used to handle version control)
- An account at MongoDB (database for this project) which is running locally on your machine.

#### Instructions
1. Save a copy of the Github repository located at https://github.com/JHR1986/johnhenryroche-ms3-handykoreanphrases by clicking the Code dropdown button and then pressing "download zip" and extracting the zip file to your chosen folder. If you have already have Git installed on your system, you can clone the repository with the following command;

``git clone https://github.com/JHR1986/johnhenryroche-ms3-handykoreanphrases``

2. If possible open a terminal session in the unzip folder or change directory to the correct location.

3. A virtual environment is recommended for the Python interpreter, and on this basis it is suggested that the user use Python's built in virtual environment by entering the following command:

``python -m .venv venv``

NOTE: It should be noted that your Python command may differ (e.g. such as python3 or py). The venv command creates a lightweight “virtual environment” with its own site directory, optionally isolated from system site directories.

4. Activate the .venv with the following command:

``.venv\Scripts\activate`` 

Note: Again this command may differ depending on your operating system.

5. If required, upgrade pip locally with the following command:

``pip install --upgrade pip.``

6.Install all required modules with the command:

``pip -r requirements.txt.``

7. In your local IDE, create a file called ``.flaskenv``.

8. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI in order to link to your own database. In line with my project, please make sure to call your Database ``task_manager``, with 3 Collections called ``users``, ``phrases`` and ``categories``. The structure of these collections are fully outlined above in the Database section of the Readme. 

9. You can now run the application by entering the following command:

``python app.py``

You can visit the website at the following address: ``http://127.0.0.1:5000``

### Heroku Deployment

In order to deploy the Handy Korean Phrases website to Heroku (which is a cloud platform service which supports several programming languages), you are required to complete the following steps:

1. Create a ``requirements.txt`` file using the terminal command ``pip freeze > requirements.txt``.

2. Create a ``Procfile`` with the terminal command ``echo web: python app.py > Procfile``.

3. ``git add`` and ``git commit`` the new requirements.txt file and Procfile, and then ``git push`` the newly created project to GitHub.

4. Create a new app on the Heroku website by clicking the "New" button which is located at the top right corner of the Heroku dashboard. Provide a name for the project and set the region to Europe (this is required for users based in Ireland).

5. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and then select GitHub.

6. Confirm that the Heroku app has correctly linked to the correct GitHub repository.

7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars" and then set the following config vars detailed below:

![deployment](https://user-images.githubusercontent.com/71781554/121898137-fb117080-cd1a-11eb-9a36-0f1e9dbbbc4e.png)

- In order to get your MONGO_URI (which is a required step), read the official documentation relating to connecting to MongoDB [here](https://docs.mongodb.com/guides/server/drivers/).

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, make sure that the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed!

## Credits
### Code
- [Change input field to green when correct number of characters entered](https://stackoverflow.com/questions/39540302/how-to-change-the-background-color-of-an-input-field-when-text-is-entered): I studied this post in order to fully understand how to change the input field green when a correct number of valid characters had been entered, to assist with the overall validation process for my form sections.
- [Validation system for form entries](https://mdbootstrap.com/docs/b4/jquery/forms/validation/): I studied this validation feature from mdbootstrap (including a JS file) and amended it for use in my project in respect of the form sections in the Phrases, Add Phrase, Edit Phrase, Login and Register pages. 
- [Show active page when using Flask and Jinja](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2): I wished to ensure that the page currently clicked on was underlined as active in the Navbar. To achieve this while using flask, I followed the instructions listed in this Stackoverflow post. 
- I studied a comment by Ed Bradley (Ed B) on Code Institute's Slack channel in respect of how to correctly set up the 404 & 500 error pages for Python and Flask.
- I used the Bootstrap Library throughout the project to make the site more responsive through using the Bootstrap Grid System and employing Bootstrap elements for the Navbar, Footer, Jumbotron, Cards and Forms.
- I studied in detail the videos for the Code Institute mini project presented by Tim Nelson prior to starting my website, in order to get a clear understanding of how both Flask and MongoDB operate, and how to implement a fully functioning CRUD system.

### Content
- All content within this project was written by the developer.

### Media
- The images used in this project have all been sourced from Unsplash, which is a stock photography site which contains a large catalogue of high-quality free to use images which are not the subject of copyright. The attributions for these images are listed below;
    - [Background Image Profile Page – Minseok Kwak](https://unsplash.com/photos/_1qQSgLoYKg)
    - [Background Image Edit Phrase Page - Timothy Ries](https://unsplash.com/photos/S5XsDlChGAQ)
    - [Background Image Add Phrase Page - Marcus Winkler](https://unsplash.com/photos/fxZihI5e6BI)
    - [Background Image Login Page - Jongsun Lee](https://unsplash.com/photos/t-klL0oHX8Y)
    - [Image of Laptop Home Page - Mark Wong](https://unsplash.com/photos/bvGgYoW97tk)
    - [Image of Korean Woman Home Page - Johen Redman](https://unsplash.com/photos/gUcrrDxJ5SQ)
    - [Image of Korean Temple Home Page - Brady Bellini](https://unsplash.com/photos/t5dGNNQVwg8)
    - [Image of Books Home Page - Hope House Press](https://unsplash.com/photos/IOzk8YKDhYg)
    - [Image of Iphone Home Page - Rahul Chakraborty](https://unsplash.com/photos/xsGxhtAsfSA)
    - [Image of Cityscape Register Page - Farrel Nobel](https://unsplash.com/photos/vw_XqUC1ORQ)

- The icon images used for the headings (Categories, English Phrase, Korean Phrase & Fun Fact) in the Phrases page were sourced from Flaticon, an image database website with free icons available in PNG, SVG, EPS, PSD and BASE 64 formats.
- The logo for Handy Korean Phrases was created using a template which I made on a design website called FreeLogoDesign, and which I amended in respect of colour scheme and design to match the proposed styling of my site. FreeLogoDeisgn is a website which allows people to make brand logos for free and download them to their own media. I also enhanced the logo using a website called Lets Enhance. 

### Acknowledgements
- I wish to thank my Mentor, Maranatha Ilesanmi, for providing me with excellent feedback and support during the various processes of competing this project.
- I also wish to thank Tutor Support and Student Care at Code Institute for their support and advice during my third term and while working on my MS3 project.
