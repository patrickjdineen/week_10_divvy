import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
        Set Config variables for the flask app.
        using environment variables where available,
        otherwise create the config variable if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'new Secret Key'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Fifty5050!@127.0.0.1:5432/divvy"
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off notification messages from the sqlalchemy db
    