#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marine Lasbleis'
SITENAME = 'Marine Lasbleis'
SITEURL = 'http://marinelasbleis.github.io'

SITESUBTITLE = u'Planetary Interior Researcher'


PATH = 'content'
STATIC_PATHS = ['images', 'files']

DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = 'sortorder'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
# DEFAULT_DATE = 'fs' #to be used if 2 languages
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
LOCALE = 'en_US.UTF-8' # On Unix/Linux


# Specify name of a theme installed via the pelican-themes tool
THEME = "./theme/nest"
NEST_HEADER_LOGO = '/images/logo.png'
NEST_INDEX_HEADER_TITLE  = 'Recent activities'
NEST_INDEX_HEADER_SUBTITLE  = 'I am currently a Post Doctoral researcher at the Laboratoire de Planétologie et Géodynamique, Université de Nantes'
NEST_INDEX_CONTENT_TITLE  = 'Recent posts'
NEST_COPYRIGHT = "CC Marine Lasbleis"
NEST_HEADER_IMAGES = "DSC_0004.JPG"
#THEME = "pelican-bootstrap3"

SUMMARY_MAX_LENGTH = 200

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = ()
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['/Users/marine/ownCloud/Dev/python/pelican-plugins']
PLUGINS = [] #['render_math']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
