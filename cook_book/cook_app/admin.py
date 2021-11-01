from django.contrib import admin
from .models import CookName, Recipes, Units, Ingredients


class RecipesInlineAdmin(admin.TabularInline):
    model = Recipes
    extra = 0

@admin.register(CookName)
class CookNameAdmin(admin.ModelAdmin):
    inlines = [RecipesInlineAdmin]

    list_display = [
        'name'
    ]


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    pass
