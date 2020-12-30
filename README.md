# College Messaging Micro-Service 
This Repository is the Backend Micro-Service that handles Messaging Part of the College Application. Built Using Python ❤️


## Setup
make sure you have python 3.6+ installed and virtualenv. If you do not have virtualenv installed, run

```
$ pip install virtualenv
```

To setup the environment, run

```
$ virtualenv venv
```

to create the virtual environment (there will be a new folder called `venv`). To install the dependencies, run:

Windows:
```
$ .\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Linux:
```
$ ./venv/bin/python -m pip install -r requirements.txt
```

## Run

To run the app, first activate the environment (if not activated already. To know if the environment is activated, you should be able to see a `(venv)` prefix in the command line prompt.)

Windows:
```
$ .\venv\Scripts\activate
```

Linux:
```
$ ./venv/bin/activate
```

And you can run the server using
```
$ python start.py
```

you can also run the server using `uvicorn`.
```
$ uvicorn app.main:app --reload
```

## Development

If you want to install any extra dependencies, **first activate the environment** and then run `pip`.

> Don't forget to add the dependency in `requirements.txt` after you install it!

## Production

Build a docker image by using,
```
$ docker build -t cynergyruas/ruas-app:messaging-service-0.0.1 .
```

and run the image using,
```
$ docker run -p 8000:8000 \
     -e MONGODB_URI=<MONGODB_URI> \
     -e COLLECTION_NAME=<Message_Collection_Name>\
     -e DB_NAME=<Database_Name> \
     -e cynergyruas/ruas-app:message-service-0.0.1  
```
## Testing it 

You may run the server using docker image file 
```
$ docker run -p 8000:8000 \
     -e MONGODB_URI=<MONGODB_URI> \
     -e COLLECTION_NAME=<Message_Collection_Name>\
     -e DB_NAME=<Database_Name> \
     -e cynergyruas/ruas-app:message-service-0.0.1  
```
or you can run the server using 

.env file will contains 

```
MONGODB_URI 
DB_NAME
COLLECTION_NAME
```

Linux:

To export the local environment varibles 
```
$ export $(cat .env | xargs)
```
And you can run the server using
```
$ python start.py
``` 

Windows:
```
$env:MONGODB_URI=<MONGODB_URI>
$env:DB_NAME=<Database_Name>
$env:COLLECTION_NAME=<Message_Collection_Name>
```
Activating the environment 

```
./venv/Scripts/activate 
```
To run 
```
python start.py
```

After you run the server you can reach this URL to test it out 

```
http://localhost:8000/<channel_name>/<user_name>
```
