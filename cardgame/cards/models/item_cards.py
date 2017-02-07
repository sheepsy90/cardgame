# -*- coding:utf-8 -*-
from django.core.validators import MinValueValidator
from django.db import models
from cards.models.general_cards import Card
from cards.models.static_effects import EquipmentCardModifier, ConsumableCardModifier


class ItemCard(Card):
    """ All item cards """
    mean_lifespan = models.IntegerField(validators=[MinValueValidator(-1)])
    var_lifespan = models.IntegerField(validators=[MinValueValidator(0)])
    weight = models.IntegerField(validators=[MinValueValidator(1)])
    bulkiness = models.IntegerField(validators=[MinValueValidator(1)])


class GeneralItemCard(ItemCard):
    """ Cards to model tools that are necessary to carry to perform certain crafting actions"""


class ConsumableCard(ItemCard):
    """ Cards to model tools that are necessary to carry to perform certain crafting actions"""
    modifiers = models.ManyToManyField(ConsumableCardModifier, through='ConsumableCardModifierRelation')


class EquipmentCard(ItemCard):
    """ Cards to model tools that are necessary to carry to perform certain crafting actions"""
    modifiers = models.ManyToManyField(EquipmentCardModifier, through='EquipmentCardModifierRelation')


class ShoeEquipmentCard(EquipmentCard):
    """ Cards to model the shoes equipment """


class HandEquipmentCard(EquipmentCard):
    """ Cards to model the equipment one can take in the hand """
    is_two_hand = models.BooleanField()


class HeadEquipmentCard(EquipmentCard):
    """ Cards to model the head equipment """


class BodyEquipmentCard(EquipmentCard):
    """ Cards to model the body equipment """


class CompanionEquipmentCard(EquipmentCard):
    """ Cards to model the companion a player can has """


class PersonalEquipmentCard(EquipmentCard):
    """ Cards to model a specific item that the player values and wears """


############## Relations ######################

class EquipmentCardModifierRelation(models.Model):
    """ The relation from EquipmentCards to EquipmentCardModifiers """
    item_card = models.ForeignKey(EquipmentCard)
    modifier = models.ForeignKey(EquipmentCardModifier)
    value = models.IntegerField()


class ConsumableCardModifierRelation(models.Model):
    """ The relation from ConsumableCards to ConsumableCardModifiers """
    item_card = models.ForeignKey(ConsumableCard)
    modifier = models.ForeignKey(ConsumableCardModifier)
    value = models.IntegerField()

############# Grouping ###############


class ItemGrouping(models.Model):
    """ Group items together to reference them in other cards """
    group_name = models.CharField(max_length=50)
    group_items = models.ManyToManyField(ItemCard)

    def __str__(self):
        return "Item Group: {}".format(self.group_name)