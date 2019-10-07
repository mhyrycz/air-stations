## About

Connect raspberry pi with react js to display air params for defined stations. Backend folder running a flask microservice in the raspberry pi using airly API to get air parameters. Frontend folder contains react app.

## Credential setup

Please provide airly and xiaomi (device) credentials like in `.example.py` files. You may use files by deleting `.example` from name.

## Backend setup

Backend using python flask framework.

### Install

```
git clone url
cd backend
pip install flask
```

Go to https://python-miio.readthedocs.io/en/latest/discovery.html and install python-miio.

## Run

```
FLASK_APP=serve.py flask run --host=0.0.0.0
```

## Frontend Setup

Frontend is using reactJS.

### Install

Install node modules.

```
npm install
```

Go to `frontend/src/config.js`

Change the url of your raspberry pi.

## Run

```
npm start
```

Access the panel from `http://localhost:3000`
