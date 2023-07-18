from django.db import models

# Create your models here.
class PLayers(models.Model):

    name = models.CharField("Nome", max_length=100, null=False, blank=True)
    highest_ranking = models.IntegerField('Ranking mais alto', null=True, blank=True)
    current_ranking = models.IntegerField("Ranking atual", null=True, blank=True)
    years = models.IntegerField('Idade', null=False, blank=True)
    favorite_surface = models.CharField('Superfície favorita', max_length=20, null=True, blank=False) 