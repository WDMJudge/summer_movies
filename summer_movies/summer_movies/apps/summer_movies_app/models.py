from __future__ import unicode_literals
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    imdbID = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
            return "<Users object: {} {} {} {}>".format(self.title, self.year, self.type, self.imdbID)
    def __str__(self):
            return "<Users object: {} {} {} {}>".format(self.title, self.year, self.type, self.imdbID)