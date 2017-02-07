from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cards.models.general_cards import CharacterCard, Card


class LivingCharacter(models.Model):
    user = models.ForeignKey(User)
    chosen_character = models.ForeignKey(CharacterCard, related_name="character")
    cards = models.ManyToManyField(Card)


