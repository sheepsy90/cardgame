from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Card(models.Model):
    """ This is a general model of a card """
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_link = models.CharField(null=True, max_length=2000)

    def __str__(self):
        return "Card: {}".format(self.name, self.id)


class CharacterCard(Card):
    """ Models a starting character """
    strength = models.IntegerField(validators=[MinValueValidator(1)])
    intelligence = models.IntegerField(validators=[MinValueValidator(1)])
    swiftness = models.IntegerField(validators=[MinValueValidator(1)])
    diplomacy = models.IntegerField(validators=[MinValueValidator(1)])
    militant = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return "CharacterCard: {} ".format(self.name)


class TerrainCard(Card):
    """ This cards models terrain as a representation to the player """
    terrain_difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    terrain_wilderness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return "Terrain: {}".format(self.name)


############## Relations ######################


class StarterCard(Card):
    """ Models all the starting cards """
    character = models.ForeignKey(CharacterCard, related_name="starting_character")
    starting_card = models.ForeignKey(Card, related_name="starting_card")
    amount = models.IntegerField()

    def __str__(self):
        return "StarterCard for {} is {} with amount {}".format(self.character.name, self.starting_card.name, self.amount)


