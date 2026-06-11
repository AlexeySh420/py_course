import os
from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask
from board import pages, tweets, database, api

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    rest_api = Api(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(tweets.bp)

    rest_api.add_resource(api.Tweet, "/api/<tweet_id>/")
    rest_api.add_resource(api.Tweets, "/api/")

    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    return app 
