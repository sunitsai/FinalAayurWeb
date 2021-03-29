from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewsitemap(Sitemap):

    def items(self):
        return ['index', 'aboutus', 'about-owner', 'blogpage', 'becomesellerpage', 'ayurveda', 'privacy', 'Tnc']

    def location(self, item):
        return reverse(item)
