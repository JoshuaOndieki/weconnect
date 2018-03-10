# WeConnect
This repo contains(currently) non-functional UI templates and a Flask API for the WeConnect project. A platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.  

[![Maintainability](https://api.codeclimate.com/v1/badges/fd1b6c22bebb59492101/maintainability)](https://codeclimate.com/github/JoshuaOndieki/weconnect/maintainability) [![Coverage Status](https://coveralls.io/repos/github/JoshuaOndieki/weconnect/badge.svg?branch=master)](https://coveralls.io/github/JoshuaOndieki/weconnect?branch=master) [![Build Status](https://travis-ci.org/JoshuaOndieki/weconnect.svg?branch=master)](https://travis-ci.org/JoshuaOndieki/weconnect) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1cdd8a328b3a4ae3ab03854da7521aa9)](https://www.codacy.com/app/JoshuaOndieki/weconnect?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JoshuaOndieki/weconnect&amp;utm_campaign=Badge_Grade)


## Motivation

This is an [Andela](https://www.andela.com) bootcamp project aimed at facilitating developers to learn in a more fun and productive way. I.e. doing real world projects while learning the concepts of programming.
The project defination can be found [here](https://docs.google.com/document/d/1iJrCZKiHl-9bIqsTinHmipI_ItYZgrPHT2ZzO3W7ACg/edit#)

## Installation

To test the UIs install a browser of your choice.
The UIs can be viewed and manually tested at [joshuaondieki.github.io](https://joshuaondieki.github.io/)
Alternatively, clone this repo and test the UIs locally.

### Flask API
1. Install Python 3.6.4
2. Git clone this repo.
3. cd to the root dir of this repo.
4. Create a virtual env and `pip install -r requirements.txt`
5. Run the app with `python app.py` or `python3 app.py`
6. Checkout the endpoints and test them with a tool like [POSTMAN](https://www.getpostman.com)

#### Heroku
This Flask API has been hosted to heroku at [Wecon](https://wecon.herokuapp.com)

## API ENDPOINTS


EndPoint | Functionality
-- | --
POST `/api/v1/auth/register` | Creates a user account
POST `/api/v1/auth/login` | Logs in a user
POST `/api/v1/auth/logout` | Logs out a user
POST `/api/v1/auth/reset-password` | Password reset
POST  `/api/v1/businesses` | Register a business
PUT `/api/v1/businesses/<businessId>` | Updates a business profile
DELETE `/api/v1//businesses/<businessId>` | Remove a business
GET  `/api/v1/businesses` | Retrieves all businesses
GET  `/api/v1/businesses/<businessId>` | Get a business
POST  `/api/v1/businesses/<businessId>/reviews` | Add a review for a business
GET  `/api/v1/businesses/<businessId>/reviews` | Get all reviews for a business


## Contributors
- [Joshua Ondieki](https://www.github.com/JoshuaOndieki/)
- Some credits go to fellow bootcampers, LFAs and Andela for the support and assistance.

A Pivotal tracker board was used in planning and managing this project. The board is publicly available [here](https://www.pivotaltracker.com/n/projects/2153376)

## License : MIT
