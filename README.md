# Snappy - Chat Application 
Snappy is a chat application build with the power of MERN (MongoDB, Express, React, Node.js) Stack. 

![login page](./images/snappy_login.png)

![home page](./images/snappy.png)

## Install and Run Snappy App

### Requirements
- [Nodejs](https://nodejs.org/en/download)
- [Mongodb](https://www.mongodb.com/docs/manual/administration/install-community/)

Both should be installed. You can also use a container running MongoDB on Docker.

This repository provides example environment (.env.example) files which you can use. To use them you need to rename them from ``.env.example`` to ``.env``
```shell
cd website
mv .env.example .env
cd ..
cd backend-server
mv .env.example .env
cd ..
```

Now install the dependencies for backend and frontend.
```shell
cd backend-server
pip install -r requirements.txt
cd ..
cd website
npm i
```

### Run a MongoDB instance
Start a mongoDB instance, either installing it on your pc or using the docker platform to run a MongoDB image/container.

>Note: **Update the MONGO_URL inside ``/server/.env`` accordingly, if necessary!**

### Run the Backend Server and Website
To run the backend (Flask) app:


```shell
cd backend-server
python index.py
```

For Frontend:
```shell
cd website
npm start
```

Done! Now open localhost:3000 in your browser and test the app.
