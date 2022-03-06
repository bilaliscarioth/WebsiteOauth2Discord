from ulyzium_website.core.website import (
    WebsiteCore
)
from ulyzium_website.core.html.html import (
    HtmlPage
)

card_player = """
<link rel="stylesheet" href="../css/materialize.min.css">

<div class="row">
    <div class="col s6 m2">
        <div class="card">
            <div class="card-image">
                <img src="{0}">
                <span class="card-title">{1}</span>
            </div>
            <div class="card-content">
                <p> Ziums : {2} /  </p>
            </div>
            <div class="card-action">
                <p>Bienvenue Parmis nous {3}</p>
            </div>
        </div>
    </div> 
</div>"""

def setup(core:WebsiteCore):
    def me():
        cursor = core.db.cursor()
        cursor.execute("SELECT * FROM player")

        result = cursor.fetchall()
        print(result)

        API_BASE_URL = 'https://discord.com/api'
        discord = core.make_session(token=core.session.get('oauth2_token'))
        user = discord.get(API_BASE_URL + '/users/@me').json()
        guilds = discord.get(API_BASE_URL + '/users/@me/guilds').json()
        connections = discord.get(API_BASE_URL + '/users/@me/connections').json()

        servers = []

        for server in guilds:
            if "ULYZIUM" in server['name']:
                servers.append(server)

        if not len(servers):    
            return "You don't have permission to connect here."

        uly = discord.get(API_BASE_URL + f'/users/@me/guilds/{servers[0]["id"]}/member').json()
        print(uly)

        page =  HtmlPage()
        card_player_str  =card_player.format(
            f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png", 
            f"{user['username']}", 
            "120", 
            f"{user['username']}"
        )
        page.addLine(page.top)
        page.addLine(card_player_str)
        return str(page)

    core.website.add_url_rule("/me", view_func=me)

