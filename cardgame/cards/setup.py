# -*- coding:utf-8 -*-
import random
import django

django.setup()

from django.contrib.auth.models import User
from cards.models.general_cards import CharacterCard, StarterCard
from cards.models.item_cards import GeneralItemCard
from cards.models.static_effects import ActionCardModifier, EquipmentCardModifier, ConsumableCardModifier


def setup_constant_values():
    # 1. Create superusers so we can edit stuff
    if not User.objects.filter(username='sheepy').exists():
        User.objects.create_superuser("sheepy", "sheepy@localhost.de", "sheepy")

    # 2. Action Card modifiers

    for field in ['mean_time', 'var_time', 'base_success']:
        for stat in ['intelligence', 'strength', 'swiftness', 'diplomatic', 'militant']:
            for percent in [True, False]:
                ActionCardModifier(affected_field=field, influencing_stat=stat, percentage=percent).save()

    # 3. Equipment Card modifiers

    for stat in ['intelligence', 'strength', 'swiftness', 'diplomatic', 'militant']:
        EquipmentCardModifier(description="Delta on Status {} ".format(stat), tag="delta_{}".format(stat)).save()
        EquipmentCardModifier(description="Delta on Status {} in %".format(stat),
                              tag="delta_{}_percent".format(stat)).save()

    for field in ['mean_time', 'var_time', 'base_success']:
        for card_class in ['HuntingCard', 'MovementCard', 'CraftinCard', 'ForagingCard']:
            EquipmentCardModifier(description="Delta {} on {}".format(field, card_class),
                                  tag="delta_{}_on_{}".format(field, card_class.lower())).save()
            EquipmentCardModifier(description="Delta {} on {} in %".format(field, card_class),
                                  tag="delta_{}_on_{}_with_percent".format(field, card_class.lower())).save()

    EquipmentCardModifier(description="Delta on number of combat rounds", tag="delta_number_rounds").save()

    # 4. Consumable Card modifiers

    ConsumableCardModifier(description="Delta health", tag="delta_health").save()

    for stat in ['intelligence', 'strength', 'swiftness', 'diplomatic', 'militant']:
        ConsumableCardModifier(description="Delta on Status {} for amount of seconds".format(stat),
                               tag="delta_{}_expires".format(stat)).save()

    # 5. Some standard cards

    stone = GeneralItemCard(name="Riverbed Stone", description="A small stone from a river bed.", image_link="",
                            mean_lifespan=-1, var_lifespan=0, weight=1, bulkiness=1)
    stone.save()

    branch = GeneralItemCard(name="Small Branch", description="A small branch from a tree.", image_link="",
                             mean_lifespan=-1, var_lifespan=0, weight=1, bulkiness=1)
    branch.save()

    for character_name in ["Hunter", "Priest", "Thief", "Soldier", "Fisher", "Gatherer"]:
        hunter = CharacterCard(name=character_name, description="A {}.".format(character_name), image_link="",
                               strength=random.randint(0, 9), intelligence=random.randint(0, 9), swiftness=random.randint(0, 9), diplomacy=random.randint(0, 9), militant=random.randint(0, 9))
        hunter.save()

        StarterCard(character=hunter, starting_card=stone, amount=2).save()
        StarterCard(character=hunter, starting_card=branch, amount=1).save()