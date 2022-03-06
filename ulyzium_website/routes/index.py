from ulyzium_website.core.website import WebsiteCore

from flask import request, redirect

def setup(core:WebsiteCore):
    def index():
        scope = request.args.get(
            'scope',
            'identify bot connections guilds guilds.join guilds.members.read')
        discord = core.make_session(scope=scope.split(' '))
        authorization_url, state = discord.authorization_url(core.AUTHORIZATION_BASE_URL)
        core.session['oauth2_state'] = state
        return redirect(authorization_url)
    core.website.add_url_rule("/", view_func=index)