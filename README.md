# Fishing Predictor App

A web app that can predict fishing activity of 'Pole and Line' vessels
## Installation

Download the repo and navigate there from the command line:

```sh
git clone https://github.com/Ekram49/gfw.git
cd gfw
```

## Setup

Setup a virtual environment and install required packages

```sh
pipenv --python 3.7
pipenv shell
pipenv install Flask pandas numpy scikit-learn python-dotenv gunicorn category_encoders

```



## Run the Flask app locally

```sh
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
```

## Deploy the app to Heroku

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```sh
 $ heroku login 
 ```

Create a new Git repository
Initialize a git repository in a new or existing directory

```sh
$ cd my-project/
$ git init
```

```sh
$ heroku git:remote -a fishing_predictor
```
Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.

```sh
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
Existing Git repository
For existing repositories, simply add the heroku remote

```sh
$ heroku git:remote -a fishing_predictor
```

