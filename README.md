# packhacks2021
Project for PackHacks2021 - "High School Headaches" track

Main idea was that while we hear that there are tutors, there aren't many widely available resources as to where to find them and most people don't want to take too much time emailing the wrong people to find information. I was inspired by that to build a website as a sort of middle man. It has the data for the tutors, what they tutor, and their free times and allows the user to register for a session automatically. Obviously, this isn't ready for widespread use. Most of the api calls are not working and the pages are a bit generic but the foundation is there. I think that with a bit more time, I could probably get the javascript api calls working and once that's done, it's relatively smooth sailing. Just have it make a POST to the api for a session at said time, confirmation email to both tutor and student (tutoree?), force page reload so that it doesn't display false positives for open times. 

The website is currently hosted on Netlify [here](https://upbeat-mcclintock-02a53e.netlify.app) and the api is hosted on Heroku (although it's a bit broken at the moment)
