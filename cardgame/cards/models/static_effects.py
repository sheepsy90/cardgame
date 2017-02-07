# -*- coding:utf-8 -*-

from django.db import models


class ActionCardModifier(models.Model):
    affected_field = models.CharField(max_length=100)
    influencing_stat = models.CharField(max_length=100)
    percentage = models.BooleanField(default=False)

    def __str__(self):
        description = "{} delta affected per {}".format(self.affected_field, self.influencing_stat)
        if self.percentage:
            description += " in %"
        return description


class EquipmentCardModifier(models.Model):
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class ConsumableCardModifier(models.Model):
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.description