# -*- coding:utf-8 -*-
from cards.models.general_cards import Card


class ReactionCard(Card):
    """ Models a general reaction card """


class DiplomaticCard(Card):
    """ Models a reaction card applied ina  diplomatic situation """


class FightCard(Card):
    """ Models a reaction card used in fighting """


class AttackCard(FightCard):
    """ Models a reaction cards that are used for attacks """


class DefenseCard(FightCard):
    """ Models a reaction cards that are used for defence """