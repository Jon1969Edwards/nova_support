{
    "name": "Nova Support",
    "version": "17.0.1.0.0",
    "category": "Helpdesk",
    "summary": "Public ticket form + Helpdesk extensions for Nova Tile and Stone",
    "author": "Nova Tile and Stone",
    "website": "",
    "license": "LGPL-3",
    "depends": ["helpdesk", "website", "portal", "mail"],
    "data": [
        "security/security.xml",
        "views/templates.xml",
        "data/website_menu.xml",
        # "data/mail_templates.xml",  # add back later if you like
        # "views/helpdesk_views.xml", # add back later
    ],
    "installable": True,
    "application": True,
}
