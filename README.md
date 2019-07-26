[![Build Status](https://travis-ci.org/TravelTimN/ci-milestone05-fsfw.svg?branch=master)](https://travis-ci.org/TravelTimN/ci-milestone05-fsfw)

# [Unicorn Attractor](#)

Welcome to the new and exciting Augmented Reality (AR) app - **Unicorn Attractor**!

**Unicorn Attractor** allows players to explore the world while on the search for magical Unicorns. Once you've downloaded the app (*available on Android and iOS devices*), you'll be able to use your mobile phone's GPS to locate, snatch, and train virtual Unicorns! As you build your Unicorn herd with your fellow Bronies, you'll earn more XP.

This exciting app helps to promote physical activity in the outdoors, combined with the virtual world of *Equestria* through your mobile phone. If you're extremely lucky, perhaps you'll have what it takes to find and snatch the elusive Alicorn! (*Alicorns are winged Unicorns; they have wings like a Pegasus, and a horn like a Unicorn*)

The best part? **Unicorn Attractor** is absolutely free to enjoy with your friends and Bronies!

If you have any issues or requests regarding the the app, please head over to our support page: [Unicorn Attractor Support Page](#). You'll be able to open two different types of Tickets; *Bugs* and *Features*.

- **BUGS** - If you have any problems or issues using the app, please open a new *Bug* Ticket.
- **FEATURES** - If you think we've missed something, or you'd like to see something added to the app, please open a new *Feature* Ticket. (***NOTE**: Features require a small donation, and can gain more donations if others support your Feature.*)

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)
    - [**Automated Testing**](#automated-testing)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, specifically the **Full Stack Frameworks** module. The objective for this milestone project is to "*Create a web application that allows users to submit tickets to an online issue tracker called the **Unicorn Attractor**, where bugs can be submitted for free, but feature requests require a nominal fee*".

*DISCLAIMER: The Unicorn Attractor 'app' does not actually exist for download. The 'app' itself is part of the project concept, whereby the project itself is what I've developed. As exciting as the Unicorn Attractor 'app' sounds, you'll just have to check out these two actual augmented reality apps instead, where my inspiration came from.*

- **[Harry Potter - Wizards Unite](https://www.harrypotterwizardsunite.com)**
- **[Pokémon GO](https://www.pokemongo.com)**

### User Stories

"**_As a user, I would like to_** _____________________________"

- *view the site* from **any device** *(mobile, tablet, desktop)*. :white_check_mark:
- *view all tickets (bugs/features)* as a **Guest**. :white_check_mark:
- *create* my own **profile**. :white_check_mark:
- *update* my **profile**, including *uploading* a **photo**. :white_check_mark:
- *log* my own **bug tickets** for *free*. :white_check_mark:
- *submit* my own **feature requests** for *a small fee*. :white_check_mark:
- *edit* my own **tickets** *(bugs and features)*. :white_check_mark:
- *delete* my own **tickets** *(bugs and features)*. :white_check_mark:
- be able to **log out**. :white_check_mark:
- be able to **change my password**. :white_check_mark:
- *see* the **total views** of each *bug and feature*. :white_check_mark:
- *comment* on **bugs and features** that I relate to. :white_check_mark:
- *upvote* **bugs** for *free* that I relate to. :white_check_mark:
- *pay a nominal fee to upvote* **features** that I support. :white_check_mark:
- *view* **statistics** of tickets such as "*most upvotes received*". :white_check_mark:
- *earn* various **badges** for *active participation* using the app. :x:

:white_check_mark: *denotes items that have been successfully implemented*

:x: *denotes items that have not been implemented yet*

### Design

Since the app is called **Unicorn Attractor**, I figured *cute* and *full of colorful rainbows* would match the overall theme. In addition, there are plenty of *unicorns* across the site.

#### Framework

- [Materialize 1.0.0](https://materializecss.com/)
    - I really like the modern and clean layout of Materialize as a framework, with its simple-to-understand documentation.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 1.11.22](https://www.djangoproject.com/download/)
    - Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Materialize.

#### Color Scheme

*Color Scheme* - **Ticket Type**

| Bugs | Features |
| :---: | :---: |
| ![#FD8D14](https://placehold.it/15/FD8D14/FD8D14) | ![#1484FC](https://placehold.it/15/1484FC/1484FC) |
| #FD8D14 | #1484FC |

*Color Scheme* - **Ticket Status**

| Open | In Progress | Closed |
| :---: | :---: | :---: |
| ![#F44336](https://placehold.it/15/F44336/F44336) | ![#FFC107](https://placehold.it/15/FFC107/FFC107) | ![#4CAF50](https://placehold.it/15/4CAF50/4CAF50) |
| #F44336 | #FFC107 | #4CAF50 |

*Color Scheme* - **Top Supports / Donors**

| Gold | Silver | Bronze |
| :---: | :---: | :---: |
| ![#D6AF36](https://placehold.it/15/D6AF36/D6AF36) | ![#A7A7AD](https://placehold.it/15/A7A7AD/A7A7AD) | ![#A77044](https://placehold.it/15/A77044/A77044) |
| #D6AF36 | #A7A7AD | #A77044 |

*Color Scheme* - **Rainbow**

| Red | Orange | Yellow | Green | Blue | Indigo | Purple |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ![#F44336](https://placehold.it/15/F44336/F44336) | ![#FF9800](https://placehold.it/15/FF9800/FF9800) | ![#FFEB3B](https://placehold.it/15/FFEB3B/FFEB3B) | ![#4CAF50](https://placehold.it/15/4CAF50/4CAF50) | ![#2196F3](https://placehold.it/15/2196F3/2196F3) | ![#3F51B5](https://placehold.it/15/3F51B5/3F51B5) | ![#9C27B0](https://placehold.it/15/9C27B0/9C27B0) |
| #F44336 | #FF9800 | #FFEB3B | #4CAF50 | #2196F3 | #3F51B5 | #9C27B0 |

All of these colors (plus a few others) are set at `:root` level within my *CSS file*. This also allows me to reuse my colors as classes across the site, instead of having to assign the colors each and every time.

#### Icons

- [Font Awesome 5.8.2](https://fontawesome.com/)
    - Although *Materialize Icons* have nearly 1,000 free-to-use icons, I prefer the look of the *Font Awesome* icons, and they significantly more icons to use. They aren't displayed using *text*, but rather *classes*, so use on mobile devices isn't affected.

#### Typography

*pending*

### Wireframes

For my wireframes, I started with simple pencil and paper sketches. Once satisfied with the initial sketches, I built mockup concept wireframes using [Balsamiq Wireframes](https://balsamiq.com/) for a couple reasons:
- Code Institute have provided all students with free access until the end of 2019.
- The simplicity and ease of use in a quick and effective manner.

All of my wireframes for this project can be found [here](https://github.com/TravelTimN/ci-milestone05-fsfw/tree/master/wireframes) in the *sketches* and *balsamiq* sub-directories respectively.

##### back to [top](#table-of-contents)

---

## Features

*pending*

### Existing Features

**Register Account**
- Anybody can register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes!

**Change Password**
- Users can update their passwords from their profile page. They will receive an email with instructions on how to reset the password.

**Add Profile Picture**
- In addition to updating their profile, users can upload a photo to use as their avatar. All images are cropped and resized to a 300px square in order to minimize file size being stored on AWS, since avatars are displayed small anyway.

**View All Tickets**
- On the *tickets* page, all Tickets are initially displayed in a 'last edit date' order, with a standard 8-items per page using pagination.

**Filtering Tickets**
- If a user would like to narrow-down the number of tickets displayed, they can easily filter tickets using a few different options. Filter can by done by ticket type (bug vs feature), by ticket status (open, in progress, closed), or by minimum/maximum number of upvotes received.

**Add a Ticket**
- Opening a new ticket comes in two varieties; Bugs and Tickets. Both require two minimal items: a Ticket Title and Description. For Features, however, there is a minimum donation required which allows users to slide the donation amount with a minimum of €5 and maximum of €100. The secure Stripe API allows users to pay for these donations.

**View a Ticket**
- Whether it's a Bug or a Feature, users can view all tickets individually, regardless of their ticket status. All ticket details are displayed, including a list of other users who have upvoted/supported the ticket. In addition, any existing comments on the ticket will be displayed to the user.

**Update a Ticket**
- Only the user that created a ticket, can edit the ticket. Exception: the admin (superuser) can also edit any ticket in the database.

**Delete a Ticket**
- Similar to editing tickets, only the user that creates a ticket can edit the ticket. Exception: the admin (superuser) can also delete any ticket in the database, should they be inappropriate and/or offensive.

**Upvote a Ticket**
- If the ticket is a Bug, then anybody can upvote the ticket free of charge. If the ticket is a Feature, then in order to upvote the ticket, a small donation is required. The user can decide how much to donate by using a slider, with a minimum donation required of €5. Payment of the donation is done using the secure Stripe API. If the Feature ticket has met its goal of €100, then any additional upvote henceforth is free of charge.

**Downvote a Ticket**
- If a user no longer supports a ticket, they can downvote it to remove their name from the list of supporters. This is only allowed for tickets that are Bugs, since donations on Features are non-refundable.

**Comment on a Ticket**
- Users can add comments on tickets that they relate to. This is also where they would see updates from the Admin related to the ticket, to offer transparency to users.

**View Statistics**
- On the *statistics* page, a number of lists and charts can be viewed. This includes: a leader board outlining the top 3 supporters, the top 10 most upvoted bugs and features (5 of each), a bar chart showing the number of bugs/features based on ticket status, a pie chart showing the total number of bugs vs features, and a bar chart showing the average number of bugs/features that are created on a monthly/weekly/daily basis. In addition to the *statistics* page, the *footer* also displays the 5 most recent tickets that have been opened.

### Features Left to Implement

**Badge Achievements**
- Ideally, I would've loved to implement a badge system for unlocking different achievements. These would've included awarding a badge for new members, creating your 1st/10th/25th ticket, having a feature reach full donation goal, adding an avatar to your profile, etc.

**Additional Stats**
- I think another statistic that would be great to display would've been *most popular tickets*, which would list the top 5 tickets with the most comments.

**Delete Account**
- Users should be given the opportunity to delete their account entirely. Currently they can register and edit their data, but not remove it from the database.

##### back to [top](#table-of-contents)

---

## Technologies Used

- [VS Code](https://code.visualstudio.com/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Photoshop CS6](https://www.adobe.com/Photoshop) - Used for editing images.
- [TinyPNG](https://tinypng.com/) - Used to compress images for faster loading.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Materialize 1.0.0](https://materializecss.com/) - Used as the front-end framework for layout and design.

### Back-End Technologies

- **Django**
    - 
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.

<details>
<summary>Click to expand the full <b>requirements.txt</b></summary>

| Package | Version | Description |
| :--- | :--- | :--- |
| boto3 | 1.9.179 | The AWS SDK for Python |
| botocore | 1.12.179 | Foundation for AWS-CLI command line utilities |
| certifi | 2019.3.9 | Collection of Root Certificates for validating the trustworthiness of SSL |
| chardet | 3.0.4 | Universal Character Encoding Detector |
| colorama | 0.2.7 | Cross-platform API to print colored terminal text from Python apps) |
| coverage | 4.5.3 | Tool for measuring code coverage of Python programs |
| dj-database-url | 0.4.2 | Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps |
| django-cleanup | 3.2.0 | Automatically deletes old files/images to replace with updated versions |
| django-materializecss-form | 1.1.14 | Django form template tags to work with Materialize CSS |
| django-storages | 1.7.1 | Connects Django to S3 Buckets |
| docutils | 0.14 | Modular system for processing documentation into useful formats |
| gunicorn | 19.7.1 | A Python WSGI HTTP Server for UNIX |
| html5lib | 0.999999999 | A pure-Python library for parsing HTML |
| idna | 2.8 | Suitable replacement for the “encodings.idna” module that comes with the standard Python library |
| jmespath | 0.9.4 | Allows you to declaratively specify how to extract elements from a JSON document |
| olefile | 0.46 | Python package to parse, read and write Microsoft OLE2 files |
| Pillow | 5.3.0 | Adds support for opening, manipulating, and saving many different image file formats |
| postgres | 2.2.2 | High-value abstraction over psycopg2 |
| psycopg2 | 2.7.3.2 | Most popular PostgreSQL database adapter for Python |
| psycopg2-binary | 2.8.3 | Python-PostgreSQL Database Adapter |
| pycurl | 7.43.0.2 | Used to fetch objects identified by a URL from a Python program |
| python-dateutil | 2.6.1 | Provides powerful extensions to the standard datetime module |
| pytz | 2018.9 | Brings the Olson tz database into Python |
| requests | 2.22.0 | Makes HTTP requests simpler and more human-friendly |
| s3transfer | 0.2.1 | Python library for managing Amazon S3 transfers |
| six | 1.12.0 | A Python 2 and 3 compatibility library |
| stripe | 2.29.4 | Python library for Stripe’s API |
| urllib3 | 1.25.3 | Powerful, sanity-friendly HTTP client for Python |
| webencodings | 0.5.1 | Character encoding aliases for legacy web content |
| whitenoise | 3.3.1 | Simplifies static file serving for WSGI applications with Django |

</details>

##### back to [top](#table-of-contents)

---

## Testing

*pending*

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - *pending*

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - *pending*

**JavaScript**
- [JShint](https://jshint.com/)
    - *pending*
- [JSesprima](http://esprima.org/demo/validate.html)
    - *pending*
- [Beautify Tools](http://beautifytools.com/javascript-validator.php)
    - *pending*

**Python**
- [PEP8 Online](http://pep8online.com/)
    - *pending*

### Compatibility

*pending*

### Known Issues

*pending*

### Automated Testing

*pending*

##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

*pending*

### Remote Deployment

*pending*

##### back to [top](#table-of-contents)

---

## Credits

### Content

*pending*

### Media

*pending*

### Code

*pending*

### Acknowledgements

- [Ignatius Ukwuoma](https://github.com/ignatiusukwuoma)
    - My Code Institute mentor.
- [Chris Quinn](https://github.com/10xOXR)
    - My accountability partner on all projects.

##### back to [top](#table-of-contents)