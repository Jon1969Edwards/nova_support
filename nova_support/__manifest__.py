{
    "name": "Nova Support",
    "version": "17.0.1.0.0",
    "summary": "Customer portal to submit and track support tickets",
    "category": "Website/Customer Support",
    "depends": [
        "base",
        "mail",
        "portal",
        "website",
        "web"
    ],
    "data": [
        "security/nova_support_security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/mail_template.xml",
        "views/support_ticket_views.xml",
        "views/portal_templates.xml",
        "views/portal_menu.xml"
    ],
    "assets": {
        "web.assets_frontend": [
        ]
    },
    "application": true,
    "license": "LGPL-3"
}
