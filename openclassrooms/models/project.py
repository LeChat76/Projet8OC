from django.db import models
from .technology import Technology
from .skill import Skill


class Project(models.Model):
    """
    This class describe projects done when my training
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    url_github = models.URLField(max_length=200)
    image_path = models.CharField(max_length=200)
    project_duration = models.CharField(max_length=20)
    skill = models.ManyToManyField(Skill)
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title

    class Meta:
        """
        just for the pluralisation and FR translation, perfection is perfection you know!  ;-)
        """
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
