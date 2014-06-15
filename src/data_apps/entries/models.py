from django.db import models
from django.contrib.auth.models import User

class Sprint(models.Model):
    titel = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.titel
    
class Comment(models.Model):
    text = models.TextField()
    sprint = models.ForeignKey(Sprint, related_name='comment_sprint')
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.datetime

class Project(models.Model):
    titel = models.CharField(max_length=50)
    beschrijving = models.TextField()
    deadline = models.DateField()
    sprint = models.ForeignKey(Sprint, related_name='project_sprint')

    def __unicode__(self):
        return '%s' % self.titel
    
class DeelTaak(models.Model):
    titel = models.CharField(max_length=50)
    beschrijving = models.TextField()
    project = models.ForeignKey(Project, related_name='deeltaak_project')
    verwachte_tijd = models.FloatField()

    def __unicode__(self):
        return '%s' % self.titel

class TijdEntry(models.Model):
    titel = models.CharField(max_length=50)
    beschrijving = models.TextField()
    tijdbesteding = models.FloatField()
    deeltaak = models.ForeignKey(DeelTaak, related_name='tijdentry_deeltaak')

    def __unicode__(self):
        return '%s' % self.titel
