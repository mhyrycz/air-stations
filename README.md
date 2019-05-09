## About

Connect raspberry pi with react js to display air params for neareast stations. Backend folder running a flask microservice in the raspberry pi. Frontend folder is a simple react app with two buttons, calls to the microservice.

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


