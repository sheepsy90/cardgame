from django.contrib import admin

# Register your models here.
from cards.models.action_cards import MovementCard, CraftingCard, ForagingCard, ActionCardModifierRelation
from cards.models.animal_cards import AnimalCard, AnimalOccurrence
from cards.models.general_cards import Card, CharacterCard, TerrainCard, StarterCard
from cards.models.item_cards import ConsumableCard, ItemGrouping, EquipmentCardModifierRelation, \
    ShoeEquipmentCard, HeadEquipmentCard, BodyEquipmentCard, CompanionEquipmentCard, PersonalEquipmentCard, \
    HandEquipmentCard, ConsumableCardModifierRelation, GeneralItemCard

# -- General related block --

admin.site.register(Card)
admin.site.register(CharacterCard)
admin.site.register(TerrainCard)
admin.site.register(StarterCard)

# -- Animal related block --
admin.site.register(AnimalCard)
admin.site.register(AnimalOccurrence)

# -- Action related block --
class ActionInline(admin.TabularInline):
    model = ActionCardModifierRelation
    extra = 4

class ActionCardAdmin(admin.ModelAdmin):
    inlines = (ActionInline,)

class CraftingCardAdmin(admin.ModelAdmin):
    inlines = (ActionInline,)
    filter_horizontal = ("consumes", "produces", "needs")

admin.site.register(MovementCard, ActionCardAdmin)
admin.site.register(ForagingCard, ActionCardAdmin)
admin.site.register(CraftingCard, CraftingCardAdmin)
# admin.site.register(ActionCardModifierRelation)



# -- Equipment related block --
class EquipmentInline(admin.TabularInline):
    model = EquipmentCardModifierRelation
    extra = 4

class EquipmentCardAdmin(admin.ModelAdmin):
    inlines = (EquipmentInline,)

admin.site.register(ShoeEquipmentCard, EquipmentCardAdmin)
admin.site.register(HeadEquipmentCard, EquipmentCardAdmin)
admin.site.register(BodyEquipmentCard, EquipmentCardAdmin)
admin.site.register(CompanionEquipmentCard, EquipmentCardAdmin)
admin.site.register(PersonalEquipmentCard, EquipmentCardAdmin)
admin.site.register(HandEquipmentCard, EquipmentCardAdmin)

# -- Consumables related block --
class ConsumableInline(admin.TabularInline):
    model = ConsumableCardModifierRelation
    extra = 4

class ConsumableCardAdmin(admin.ModelAdmin):
    inlines = (ConsumableInline,)

admin.site.register(ConsumableCard, ConsumableCardAdmin)

admin.site.register(GeneralItemCard)
admin.site.register(ItemGrouping)
