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
- *submit* my own **feature requests** for *a small fee*.
- *edit* my own **tickets** *(bugs and features)*. :white_check_mark:
- *delete* my own **tickets** *(bugs and features)*. :white_check_mark:
- be able to **log out**. :white_check_mark:
- be able to **change my password**. :white_check_mark:
- *see* the **total views** of each *bug and feature*. :white_check_mark:
- *comment* on **bugs and features** that I relate to.
- *upvote* **bugs** for *free* that I relate to.
- *pay a nominal fee to upvote* **features** that I support.
- *view* **statistics** of tickets such as "*highest-grossed features*" and "*most upvoted bugs*".
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

In keeping with the overall *rainbow / unicorn* theme, I have opted for a bright and colorful scheme.

**Ticket Type Color Scheme**

| Bug | Feature |
| --- | --- |
| ![#FD8D14](https://placehold.it/15/FD8D14/FD8D14) | ![#1484FC](https://placehold.it/15/1484FC/1484FC) |
| **#FD8D14** | **#1484FC** |

**Ticket Status Color Scheme**

| Open | In Progress | Closed |
| --- | --- | --- |
| ![#F44336](https://placehold.it/15/F44336/F44336) | ![#FFC107](https://placehold.it/15/FFC107/FFC107) | ![#4CAF50](https://placehold.it/15/4CAF50/4CAF50) |
| **#F44336** | **#FFC107** | **#4CAF50** |

**Top Supports / Donors**

| Gold | Silver | Bronze |
| --- | --- | --- |
| ![#D6AF36](https://placehold.it/15/D6AF36/D6AF36) | ![#A7A7AD](https://placehold.it/15/A7A7AD/A7A7AD) | ![#A77044](https://placehold.it/15/A77044/A77044) |
| **#D6AF36** | **#A7A7AD** | **#A77044** |

**Rainbow Color Scheme**

| Red | Orange | Yellow | Green | Blue | Indigo | Purple |
| --- | --- | --- | --- | --- | --- | --- |
| ![#F44336](https://placehold.it/15/F44336/F44336) | ![#FF9800](https://placehold.it/15/FF9800/FF9800) | ![#FFEB3B](https://placehold.it/15/FFEB3B/FFEB3B) | ![#4CAF50](https://placehold.it/15/4CAF50/4CAF50) | ![#2196F3](https://placehold.it/15/2196F3/2196F3) | ![#3F51B5](https://placehold.it/15/3F51B5/3F51B5) | ![#9C27B0](https://placehold.it/15/9C27B0/9C27B0) |
| **#F44336** | **#FF9800** | **#FFEB3B** | **#4CAF50** | **#2196F3** | **#3F51B5** | **#9C27B0** |

#### Icons

*pending*

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

pending

### Features Left to Implement

pending

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
- [jQuery 3.4.0](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.

### Back-End Technologies

- **Django**
    - *pending* 
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.

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