from flask import Flask, g, session, redirect, request, url_for, jsonify
import mysql.connector, os
import importlib

from requests_oauthlib import OAuth2Session

from typing import (
    Tuple
)

routes: Tuple[str] =(
    "ulyzium_website.routes.callback",
    "ulyzium_website.routes.index",
    "ulyzium_website.routes.me"
)

class WebsiteCore:
    def __init__(self, debug:bool=False):
        self.instance = " Azure Staff "

        self.db = mysql.connector.connect(
            database=os.getenv("ULY_DB"),
            host=os.getenv("ULY_HOST"),
            user=os.getenv("ULY_DBUSER"),
            password=os.getenv("ULY_PASSWORD")
        )

        self.OAUTH2_CLIENT_ID = os.getenv("OAUTH2_CLIENT_ID")
        self.OAUTH2_CLIENT_SECRET = os.getenv("OAUTH2_CLIENT_SECRET")
        self.OAUTH2_REDIRECT_URI = os.getenv("OAUTH2_REDIRECT_URI")
        self.TOKEN_URL = 'https://discordapp.com/api/oauth2/token'
        self.AUTHORIZATION_BASE_URL = 'https://discordapp.com/api/oauth2/authorize'

        if 'http://' in self.OAUTH2_REDIRECT_URI:
            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'

        self.website = Flask(__name__)
        self.website.config['SECRET_KEY'] = self.OAUTH2_CLIENT_SECRET
        self.debug = debug
        self.website.debug = True
        self.session = session
    
    def readAllRoutes(self):
        for route in routes:
            spec = importlib.util.find_spec(route)
            lib = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(lib)

            try:
                setup = getattr(lib, "setup")
                setup(self)
            except Exception as e:
                print(e.args)
        return

    def token_updater(self, token):
        self.session['oauth2_token'] = token

    def make_session(self, token=None, state=None, scope=None):
        return OAuth2Session(
            client_id=self.OAUTH2_CLIENT_ID,
            token=token,
            state=state,
            scope=scope,
            redirect_uri=self.OAUTH2_REDIRECT_URI,
            auto_refresh_kwargs={
                'client_id': self.OAUTH2_CLIENT_ID,
                'client_secret': self.OAUTH2_CLIENT_SECRET,
            },
            auto_refresh_url=self.TOKEN_URL,
            token_updater=self.token_updater)
    def start(self):
        self.website.run()
        return
    