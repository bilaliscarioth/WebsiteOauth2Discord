from ulyzium_website.core.website import (
    WebsiteCore
)

def run():
    website = WebsiteCore()

    website.readAllRoutes()
    print()    
    website.start()