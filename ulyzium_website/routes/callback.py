from flask import Flask, g, session, redirect, request, url_for, jsonify

from ulyzium_website.core.website import (
    WebsiteCore
)

def setup(core:WebsiteCore):
    def callback():
        if request.values.get('error'):
            return request.values['error']
        discord = core.make_session(state=core.session.get('oauth2_state'))
        print(core.session)
        token = discord.fetch_token(
            core.TOKEN_URL,
            client_secret=core.OAUTH2_CLIENT_SECRET,
            authorization_response=request.url)
        core.session['oauth2_token'] = token
        return redirect(url_for('.me'))
    core.website.add_url_rule("/callback", view_func=callback)