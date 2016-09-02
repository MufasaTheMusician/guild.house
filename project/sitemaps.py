# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from project.blog.sitemaps import sitemaps as blog
from project.library.sitemaps import sitemaps as library
from project.site.sitemaps import sitemaps as site


sitemaps = {}
sitemaps.update(blog)
sitemaps.update(site)
