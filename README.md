# 2022_IBM_Code_Challenge_Travelogue_Divination
Travelogue divination is a location prediction system for predicting the location providing the expected time we need and current location.

## The Problem

We all have experienced situations like where could we reach by this time while travelling. So that we can plan accordingly like cancel future tickets,  change schedule etc. Most of the ticket booking applications doesn’t include live tracking, time prediction and other facilities. Hence, there are hardships to locate the live status of a booked entity (Bus, Train, Flight).

## How can we solve this?

We came up with a solution for this. A location prediction system, which is capable of predicting the future location based on the historical data table of other travellers in same route. Each travellers location and time they reached are stored in the database table and from this, location is predicted. By giving currrent location and current time, system will  search for the delay in that location and delay is added to the expected time and the max count is taken to get predicted location.

## Code Flow and System Users

![Flow Diagram](https://github.com/abasith99/2022_IBM_Code_Challenge_Travelogue/blob/main/images/Architecture.jpg)
## How to use

### Pre-requisites
- Download Python from [here](https://www.python.org/downloads/)
- Code Editor of your choice. (Eg. VSCode, Sublime Text, Atom, etc.)
Clone or download the repository from the main page and navigate into the root directory.

The repository is split into two segment:

-'bin' folder contains the core python scripts used in prediction part and database .
-'src' folder contains a Flask application which can be used to demonstrate the interaction of web UI and backend processing.

'Step 1' : Excute command '''pip install requirments.txt'''. This will install all the libraries needed to run the program.

'Step 2' : Navigate into 'src' folder and execute the command 'py app.py'

'Step 3' : The application will now be running on local host. i.e. 'https://127.0.0.5000/'

'Step 4' : Provide details in respective fields and submit the form. The predicted location will be displayed on the screen.

## Problems faced during development

- Less accurate as dataset is small
- Need to give time, locations in dataset
- Time may vary according to the traffic and block

## Future plans

- Inclusion of optimisation to already made travel plans.
- Time prediction based on traffic blocks in the passenger routes.
- A facility for the passengers to add the experience so that others get an idea about the route.
- An online chat support to the passengers

## Contributors

- Abdul basith, *NSS College of Engineering, Palakkad*
- Swathy S, *NSS College of Engineering, Palakkad*
- Devanand NS, *NSS College of Engineering, Palakkad*
- Sandra T, *NSS College of Engineering, Palakkad*
- Harikrishnan G, *NSS College of Engineering, Palakkad*

## License

This repository is licensed under Apache License, v2.0. See [LICENSE]() for full licensing text.
