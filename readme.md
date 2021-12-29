# Firebase + Cloudrun + Machine learning

A simple loan eligibility decision system developed with fastapi and scikit learn for the server side and HTML, CSS and Javascript for the client side

The Backend is deployed on google cloud run while the static frontend is served with firebase hosting.

# How to serve the frontend locally
- install firebase tools
~~~
npm install -g firebase-tools
~~~

- serve on localhost
~~~
firebase serve
~~~

# How to serve the backend locally [Docker]

- navigate to the server folder and create a .env file and enter the following values

~~~
IS_DEBUG = False
API_KEY = <ENTER AN API KEY OF YOUR CHOICE>
DEFAULT_MODEL_PATH=./assets/finalized_model.sav
~~~

you can simply generate an api key using the python repl as follows:

~~~python
import uuid
print(str(uuid.uuid4()))
~~~

- run the shell scripts as follows:
~~~
chmod +x run.sh
chmod +x build.sh
~~~

- build the image
~~~
./build.sh
~~~

- serve the api
~~~
./run.sh
~~~

- navigate to the api documentation on localhost:8000/docs


