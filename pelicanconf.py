#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/Users/martin/Projects/pelican-responsive/src/responsive'

AUTHOR = u'Martin Brochhaus'
SITENAME = u'martinbrochhaus.com'
SITEURL = 'http://martinbrochhaus.com'
MINI_BIO = u"I build software with Python & Django. Every day. All day long."

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/mbrochh'),
    ('Google Plus', 'https://plus.google.com/101162916953876296847/about'),
    ('Twitter', 'https://twitter.com/mbrochh'),
    ('Facebook', 'https://facebook.com/mbrochh'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', ]

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
    ('extra/avatar.jpg', 'theme/img/avatar.jpg'),
)

GOOGLE_ANALYTICS = 'UA-XXXXXXX-XX'