## About

Connect raspberry pi with react js to turn on, off a led bulb. Backend folder running a flask microservice in the raspberry pi. Frontend folder is a simple react app with two buttons, calls to the microservice.

You can find the blog post [here](http://chamoda.com), expains all the details from configuring circuit to setting up the microservice

## Backend setup

Backend using python flask framework.

### Install

```
git clone url
cd backend
pip install flask
```

## Run

```
FLASK_APP=serve.py flask run --host=0.0.0.0
```

## Frontend Setup

Frontend is using react

### Install

```
npm install
```

Go to `frontend/src/config.js`

Change the url to your IP of raspberry pi

## Run

```
npm start
```

Access the panel from `http://rpi-address:3000`


