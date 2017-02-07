# -*- coding:utf-8 -*-
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from cards.models.animal_cards import AnimalCard
from cards.models.general_cards import Card
from cards.models.item_cards import ItemGrouping, ItemCard
from cards.models.static_effects import ActionCardModifier


class ActionCard(Card):
    """ A general model for action cards """
    base_success = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    mean_time = models.IntegerField(validators=[MinValueValidator(0)])
    var_time = models.IntegerField(validators=[MinValueValidator(0)])
    modifiers = models.ManyToManyField(ActionCardModifier, through='ActionCardModifierRelation')


class HuntingCard(ActionCard):
    """ A hunting card that targets specific animals """
    target_game = models.ManyToManyField(AnimalCard)


class MovementCard(ActionCard):
    """ Cards that allow movement actions """
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
    NORTH_WEST = 'NW'
    NORTH_EAST = 'NE'
    SOUTH_WEST = 'SW'
    SOUTH_EAST = 'SE'

    OCCURRENCE_CHOICE = (
        (NORTH, 'North'),
        (SOUTH, 'South'),
        (EAST, 'East'),
        (WEST, 'West'),
        (NORTH_WEST, 'North West'),
        (NORTH_EAST, 'North East'),
        (SOUTH_WEST, 'South West'),
        (SOUTH_EAST, 'South East'),
    )
    direction = models.CharField(max_length=2, choices=OCCURRENCE_CHOICE, default=NORTH)


class ForagingCard(ActionCard):
    """ Cards to model foraging """
    target_item_group = models.ForeignKey(ItemGrouping)


class CraftingCard(ActionCard):
    """ Cards to model crafting """
    consumes = models.ManyToManyField(ItemCard, related_name="consumes")
    produces = models.ManyToManyField(ItemCard, related_name="produces")
    needs = models.ManyToManyField(ItemCard, related_name="needs")


############## Relations ################

class ActionCardModifierRelation(models.Model):
    """ The relation from ActionCards to ActionCardModifiers """
    action_card = models.ForeignKey(ActionCard)
    modifier = models.ForeignKey(ActionCardModifier)
    value = models.IntegerField()