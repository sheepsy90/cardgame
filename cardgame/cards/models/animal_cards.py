# -*- coding:utf-8 -*-
from django.core.validators import MinValueValidator
from django.db import models
from cards.models.general_cards import Card, TerrainCard


class AnimalCard(Card):
    """ A general card model for an animal in the wilderness """
    swiftness = models.IntegerField(validators=[MinValueValidator(1)])
    strength = models.IntegerField(validators=[MinValueValidator(1)])
    intelligence = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return "Animal: {}".format(self.name)


############## Relations ######################

class AnimalOccurrence(models.Model):
    """ A model that describes which animals can be found where """
    VERY_RARE = 'VR'
    RARE = 'RR'
    MEDIUM = 'MM'
    FREQUENT = 'FF'
    VERY_FREQUENT = 'VF'

    OCCURRENCE_CHOICE = (
        (VERY_RARE, 'very rare'),
        (RARE, 'rare'),
        (MEDIUM, 'medium'),
        (FREQUENT, 'frequent'),
        (VERY_FREQUENT, 'very frequent'),
    )

    animal = models.ForeignKey(AnimalCard)
    terrain = models.ForeignKey(TerrainCard)
    occurrence = models.CharField(max_length=2, choices=OCCURRENCE_CHOICE, default=MEDIUM)

    def __str__(self):
        return "AnimalOccurrence for {} in terrain {} is {}".format(self.animal.name, self.terrain.name, self.occurrence)