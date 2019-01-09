# Concert Tracking Web Application
Django application built using SQLlite and MongoDB to store profile and Geojson Concert data. The application allows users to share concerts or look for concerts close to them to attend.

## Frontend:
HTML and CSS using Bootstrap. This includes some JavaScript to access the Mapbox Api to display a map with concerts that users can choose from. Python is used with the Django framework to pass variables from the databases to the HTML and JavaScript.

## Backend:
Django is a web framework that eases many backend tasks by incorporating them in the frontend with models. I used Djangos built in SQLlite database for user profiles and authentication. This is one of Django's best features. I also used MongoDB for Geojson data on users shared concerts because of MongoDB's great location query capabilities and support.

## App Sample Screen Shots

| ![Alt text](/project/appScreenShots/Home.png?raw=true) | 
|:--:|
| *Home Page: Search for concerts near you* |

| ![Alt text](/project/appScreenShots/Profile.png?raw=true) |
|:--:|
| *Profile* |
