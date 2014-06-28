from flask import Flask
from flaskapp import settings


app = Flask(__name__)
app.config.from_object(settings)

#import views so that it binds the controllers to the views
from flaskapp import views



