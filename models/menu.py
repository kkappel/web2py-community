# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Klaus kappel <kkappel@jugendhilfe-wuemmetal.de'
response.meta.description = 'Wümmebook'
response.meta.keywords = 'web2py, Wümmebook'
response.meta.generator = 'Web2py Wümmebook'
response.meta.copyright = 'Copyright 2015'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'home')),
    (T('Wall'), False, URL('default', 'wall')),
    (T('Friends'), False, URL('default', 'friends')),
    (T('Search'), False, URL('default', 'search')),
    ]

response.vmenu = [
    (T('Friends'), False, URL('default', 'friends')),
    (T('Essen'), False, URL('essen', 'index')),
    (T('Heimbeirat'), False, URL('beirat', 'index')),
    (T('Vertrauensperson'), False, URL('councellor', 'index')),
    (T('Hausordnung'), False, URL('pages', 'haussordnung')),
]
