from django.db import models

class Sport(models.Model):

    UNDEFINED = 0
    FUTEBOL = 1
    BASKETBALL = 2
    TENNIS = 3
    FORMULA_ONE = 4
    MMA = 5
    SURF = 6
    CYCLING = 7

    SPORT_CHOICES = (
        (UNDEFINED, "Indefinido")
        (FUTEBOL, "Futebol"),
        (BASKETBALL, "Basquete"),
        (TENNIS, "Tênis"),
        (FORMULA_ONE, "Formula 1"),
        (MMA, "MMA"),
        (SURF, "Surf"),
        (CYCLING, "Ciclismo"),
    )

    sport = models.IntegerField('Esport', null=False, blank=True, default=UNDEFINED)


class Games(models.Model):

    game_date = models.DateField('Data do jogo', null=False, blank=True)
    participants = models.CharField('Participantes', max_length=255, null=False, blank=True)


class League(models.Model):

    name = models.CharField("Nome", max_length=100, null=False, blank=True)
    participants = models.CharField('Participantes', max_length=255, null=False, blank=True)
    maximum_participants = models.IntegerField('maximo de participantes', null=True, blank=False)
