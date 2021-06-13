# Handy Korean Phrases Website - Testing details

## [Main Readme File](README.md).

[View the Live Website Here](https://jhroche-handy-korean-phrases.herokuapp.com/)

- [Testing](#testing)
  * [Client Stories Testing](#client-stories-testing)
  * [Testing Client Stories from UX Section of Main Readme File](#testing-client-stories-from-ux-section-of-main-readme-file)
    + [First Time Visitor Goals](#first-time-visitor-goals)
    + [Returning Visitor Goals](#returning-visitor-goals)
    + [Frequent Visitor Goals](#frequent-visitor-goals)
  * [Manual Logical Testing of all Elements and Functionality on every Page](#manual-logical-testing-of-all-elements-and-functionality-on-every-page)
    + [Home Page](#home-page)
    + [Phrases Page](#phrases-page)
    + [Login Page](#login-page)
    + [Register Page](#register-page)
    + [Profile Page](#profile-page)
    + [Add Phrase Page](#add-phrase-page)
    + [Edit Phrase Page](#edit-phrase-page)
    + [Additional HTML Pages](#additional-html-pages)
- [Further Testing](#further-testing)
  * [Further Testing Details](#further-testing-details)
  * [Known Bugs](#known-bugs)

## Testing
- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project (10 html pages and 1 css page) in order to ensure that there were no syntax errors in the project (e.g. the code was fully accurate and correctly structured throughout).
The results that I received for the HTML and CSS pages are shown below;

![htmlvalidation](https://user-images.githubusercontent.com/71781554/121773988-789c7b80-cb77-11eb-86f4-d2e8e6a71d9e.png)
![cssvalidation](https://user-images.githubusercontent.com/71781554/121773997-85b96a80-cb77-11eb-8fef-484355ca170d.png)

- The JavaScript file was also tested in JSHint and no errors were recorded (as well as no errors being recorded in DevTools). An image of the result is listed below;
![jsvalidation](https://user-images.githubusercontent.com/71781554/121774014-b3061880-cb77-11eb-91bb-e9183ecd325b.png)

- I tested the Python file for PEP8 compliance at Pep8Online and it was fully compliant (see image below);
![pythonvalidator](https://user-images.githubusercontent.com/71781554/121774027-ce712380-cb77-11eb-8046-a92883bebaab.png)

- I ensured that alt tags were added to all images and that aria labels were added to all background images for accessibility purposes. 

### Client Stories Testing
The most direct path through the website is as follows:
- Home – Phrases – Login (if a user) or Register (if not a user)
- On the Home page, the user is presented with the options of going to the Phrases, Login or Register pages through three call to action buttons (as detailed below); 
    1. "Go To Phrases": From Home – Phrases
    2. "Go To Login": From Home - Login
    2. "Go To Register": From Home – Register
- On the Phrases page, the user can search the phrases and use the Navbar to go to different pages.
- On the Login and Register pages, the user goes to the Profile page when they login or register.
- On the Profile page, the user is presented with the options of going to the Phrases or New Phrase pages through two call to action buttons (as detailed below);
    1. "Go To Phrases": From Profile - Phrases
    2. "Go To New Phrase": From Profile - New Phrase
- On the New Phrase page, the user goes back to the Phrases page when a new phrase is added. There they have the option of clicking an edit or delete button in respect of their phrases. Clicking the Edit button brings them to the Edit Phrase page.
    1. "Edit": From Phrases - Edit Phrase
- On the Edit Phrase page, the user goes back to the Phrases page when a phrase is edited. They have the option to continue using the Navbar or to click the Logout link to return to the Login page.
- When the Logout button in the Navbar is clicked the user returns to the Login page and is no longer logged in.

The Home page provides a brief overview of the purpose of the site, while the Profile page confirms what the user can do in respect of CRUD functionality, and the information is kept very concise and to the point in order that the user does not feel overwhelmed with information.

### Testing Client Stories from UX Section of Main Readme File

#### First Time Visitor Goals
As a First Time Visitor, I want to quickly establish what information the website contains in respect of English speakers learning easy to use Korean phrases:
- The Home page has a general synopsis of the purpose of the website and several striking images of Korean culture and scenery, and there is a prominent navigation bar for clicking to the Phrases, Login and Register pages. 

As a First Time Visitor, I want to be able to easily navigate throughout the site pages and be able to find and search for Korean phrases for use when I visit the country:
- The Home page has three prominent call to action buttons in the middle of the page which leads to the Phrases, Login and Register pages. The Phrases page lists the main reference information, while the register page enables the user to create an account from which they can add their own phrases.  

As a First Time Visitor, I want to be able to go to the register page and create my own account:
- The call to action button on the Home page brings the visitor to the register page which contains a form, which when filled out results in a new account being created for the user, and they are directed to their Profile page.

#### Returning Visitor Goals
 As a Returning Visitor, I want to be able to login, see phrases that have been added by other users and have the option to add my own phrases:
- When a user logs in to their account, they are directed to their profile page, which has two call to action buttons to either go to the Phrases page (where they can see all of the phrases added by users) or to add a New Phrase. 

As a Returning Visitor, I want to be able to easily access the key information in respect of contacting the site owners (info contained in footer) if I have any queries in respect of the website itself:
- The footer to each of the html pages lists the site's address in Dublin, their opening hours and phone/email address, so that any subsequent queries can be addressed to the site owners.

#### Frequent Visitor Goals
As a Frequent/Returning Visitor, I want to be able to login to my account and create, read, update and delete my own phrases:
- As highlighted in the frequent visitor section, when logged in the user has access to CRUD functionality in respect of the phrases that they create that are listed on the Phrases page.

As a Frequent/Returning Visitor, I want to be able to see which new phrases have been added to the site since my last visit:
- With the site being updated on a regular basis, the Phrases page will list more and more phrases, so that the user can improve their language skills when they return to the site on a regular basis. The search functionality also enables the user to find phrases easily when they begin to increase significantly in number. 

### Manual Logical Testing of all Elements and Functionality on every Page

This is a complete account of the testing process for the site from start to finish which I completed when the site had been ready for submission.

#### Home Page
1.  Navigation bar:
    - Go to the "Home" page from a desktop.
    - Amend the screen size from desktop to tablet (e.g. iPad) to verify that the navigation bar is fully responsive and switches from the inline menu to the hamburger icon dropdown menu at the appropriate place on the right of the navbar.
    - When checking the responsiveness of navbar, verify that there is no overflow and that all of the items are in their correct places. 
    - Click on the Handy Korean Phrases logo in the left section of the navigation bar and verify that it links correctly to the Home page.
    - Click on every navigation menu item (Home, Phrases, Log In & Register) and verify that they link to the correct page and that the active page is correctly highlighted.
    - Hover over the "Phrases", "Login" and “Register” links and verify the hover colour change features work as expected.
    - Click on the "Phrases", "Login and “Register” links and verify that they go correctly to the Phrases, Login and Register pages.
    - Change the screen size to mobile and click the hamburger icon in order to verify that the menu drops down correctly and that the menu items are fully visible.
    - Conclude by verifying that functionality and responsiveness is all working correctly on mobile and tablet view.

2.  Introduction Text:
    - Go to "Home" page from a desktop.
    - Confirm that the jumbotron text section is correctly appearing on screen and is fully responsive when the width of the window is reduced to tablet and mobile size.
    
3. Three Cards & Two Images:
    - Confirm that the three cards are correctly spaced on screen and are fully responsive.
    - Confirm that the five images on the page (three images above cards and two below) are correctly aligned.
    - Reduce and expand the width of the window to verify that the text and images respond as expected, and that they fit appropriately on all device widths.
    - Confirm that the alt text is correctly inputted for all five images in order to confirm readability.
    
4. Footer:
    - Confirm that the Font Awesome icons in the footer are visible and correctly formatted and that all text is spaced and clearly visible.
    - Reduce and expand the width of window to verify that the Footer is responsive and looks as it should on all devices, in line with the Bootstrap grid system.
    - Confirm that Footer items are correctly stacked on top of one another in tablet and mobile view.

5.  Review all functionality and responsiveness on mobile and tablet for the Home Page and confirm that everything on this page is correct.

#### Phrases Page
1.  Navigation bar:
    - Repeat the verification steps that I completed for the Navbar on the Home page.
    - Confirm that the Navbar is appearing as identical on all html pages.

2.  Search Box:
    - Reduce and expand the width of the window to verify that the search box behaves and centres the way expected, that it looks good on all device widths and that the font color and size is appropriate.
    - Confirm validation is working correctly for search input field.
    - Search all of the phrases by the entry to (i) English Phrase or (ii) Korean Phrase that are currrently in the phrases list and confirm that they appear correctly when searched for. 
    - Ensure that No Results statement appears if search is not found in MongoDB database. 
    - Confirm that Reset button works correctly.

3.  Phrases:
    - Confirm that the phrases are listed correctly below the search box.
    - When not logged in, confirm that no phrases added by registered users can be either edited or deleted.
    - When logged in, confirm that edit and delete buttons work as expected.
    - Reduce and expand the width of the window to verify that the phrases section responds as expected, and that it reacts appropriately on all device widths.

5.  Footer:
    - Repeat the verification steps completed for the footer on the Home page.
    - Confirm that the appearance of the Footer is identical on all html pages.

6.  Review all functionality and responsiveness on my mobile phone and tablet for the Phrases Page and confirm that everything on this page is correct.

#### Login Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home & Phrases page.
    - Confirm that the Navbar is identical on all html pages.

2.  Bootstrap Form for Login:
    - Click login with no details entered and confirm that validation is working correctly.
    - Click login with only Username or Password entered and confirm that validation is working correctly (e.g. login wont progress).
    - Enter incorrect login details to confirm that flash message ("An incorrect Username and/or Password was entered!") is shown.
    - Confirm that input fields turn green when correct number of characters is entered.
    - When correct user details are entered, click Login button and confirm that user is directed to Profile page.
    - Reduce and expand width of window to verify that the form responds as expected, and that it fits correctly on all device widths from mobile to tablet to desktop.

3.  Image:
    - Confirm that the background image for the page is correctly visible.

4.  Footer:
    - Repeat verification steps completed for the Footer on Home and Phrases page.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Login Page and confirm that everything on this page is correct.

#### Register Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home, Phrases and Login page.
    - Confirm that the Navbar is identical on all html pages.

2.  Bootstrap Form for Register:
    - Click register with no details entered and confirm that validation is working correctly.
    - Click register with only Username or Password entered and confirm that validation is working correctly (e.g. registration won't progress).
    - Confirm that input fields turn green when correct number of characters is entered.
    - When correct user details are entered, click Register button and confirm that user is directed to Profile page.
    - Reduce and expand width of window to verify that the form responds as expected, and that it fits correctly on all device widths from mobile to tablet to desktop.

3.  Image:
    - Confirm that the background image for the page is correctly visible.

4.  Footer:
    - Repeat verification steps completed for the Footer on Home, Phrases and Login page.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Enquiries Page and confirm that everything on this page is correct.

#### Profile Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home, Phrases, Login and Register page.
    - Confirm that the Navbar is identical on all html pages.

2. Introduction Text:
    - Confirm that the jumbotron text section is correctly appearing on screen and is fully responsive when the width of the window is reduced to mobile size.
    
3. Two Cards:
    - Confirm that the two cards are correctly spaced on screen and are fully responsive.
    - Confirm that the two call to action buttons in the cards ("Go To Phrases", "Go To New Phrase") are working correctly.

4.  Footer:
    - Repeat verification steps completed for the Footer on Home, Phrases, Login and Register page.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Profile Page and confirm that everything on this page is correct.

#### Add Phrase Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on the previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2.  Bootstrap Form for Add Phrase:
    - Click Add Phrase with no details entered and confirm that validation is working correctly (form not submitted).
    - Click Add Phrase with one of the fields not completed (in turn) and confirm that validation is working correctly.
    - Confirm that input fields turn green when correct number of characters is entered.
    - When correct information is entered, click Add Phrase button and confirm that user is directed to Phrases page.
    - Confirm that new phrase has been added, and that buttons to Edit or Delete phrase are listed below phrase.
    - Reduce and expand width of window to verify that the form responds as expected, and that it fits correctly on all device widths from mobile to tablet to desktop.

3.  Image:
    - Confirm that the background image for the page is correctly visible.

4.  Footer:
    - Repeat verification steps completed for the Footer on previous html pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Add Phrase Page and confirm that everything on this page is correct.

#### Edit Phrase Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on the previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2.  Bootstrap Form for Edit Phrase:
    - Confirm that data from the added phrase to be edited is listed correctly and that the fields are currently green (as the information that was previously added was valid).
    - Confirm that all fields (Phrase Category, English Phrase, Korean Phrase & Fun Fact) can be edited by the user and that form will only submit when all fields are filled correctly (e.g. validation is working as intended). 
    - When correct information is present, click Cancel button and confirm that user is directed to Phrases page and that phrase has not been edited.
    - When correct information is present, click Edit Phrase button and confirm that user is directed to Phrases page.
    - Confirm that phrase has been edited, and that buttons to Edit or Delete phrase are listed below phrase.
    - Reduce and expand width of window to verify that the form responds as expected, and that it fits correctly on all device widths from mobile to tablet to desktop.

3.  Image:
    - Confirm that the background image for the page is correctly visible.

4.  Footer:
    - Repeat verification steps completed for the Footer on previous html pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Edit Phrase Page and confirm that everything on this page is correct.

#### Additional HTML Pages

- Logout: Confirm that clicking the Logout link works and that when clicked the user is returned to the Login page and sees confirmation flash message.
- Error Pages: Confirm that 404 and 500 error html pages are correctly set up (html has been validated). When user reaches the 404 and 500 page they see the heading "Something went wrong" and can click the Return to Home Page button as an option. Confirm that images below "Something went wrong" text are responsive and that alt tags are attached.
- Review all functionality and responsiveness on my mobile phone and tablet for the 404 page and confirm that everything on this page is correct.  

## Further Testing

### Further Testing Details

- The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers, and was found to operate satisfactorily on all of these.
- I also tested the website in Google Lighthouse, which returned the following scores; (i) Performance: 98, (ii) Accessibility: 100, (iii) Best Practices: 100 & (iv) SEO: 100. The result image is detailed below;

![lighthouse](https://user-images.githubusercontent.com/71781554/121774293-c74b1500-cb79-11eb-8b27-f6a1590f5923.png)

- The website was viewed on a variety of devices such as Desktop, iPad, iPhone 6 & iPhone X. All formats were in order with no sections out of line or overlapping.

- I completed a large amount of detailed testing to ensure that all links were working correctly and that external links opened (as detailed in Manual Testing section above), and was happy that there were no broken links. This involved going into every page of the site and clicking every link/button that is available to a user (as part of their journey through the site) to ensure that everything was fully functional. 

- I checked the console in Devtools and confirmed that there were no error reports in respect of any of the pages.

- As part of the testing process, my family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- N/A - No bugs were found during the testing completed before submission. 
