from django.db import models


class CookName(models.Model):
    """Наименование блюда"""

    name = models.CharField("Наименование блюда", max_length=50, null=False)
    comments = models.TextField("Описание блюда")

    def __str__(self):
        return f"{self.name}, {self.comments[0:200]}..".strip()

    class Meta:
        verbose_name = u'Блюда'
        verbose_name_plural = u'Блюда'


class Units(models.Model):
    name = models.CharField(
        "Наименование единицы измерения", max_length=50, null=False
    )

    class Meta:
        verbose_name = u'Единицы измерения'
        verbose_name_plural = u'Единицы измерения'

    def __str__(self):
        return f"{self.name}".strip()


class Ingredients(models.Model):
    """Наименование ингредиента"""
    name = models.CharField(
        "Ингредиент", max_length=50, null=False
    )

    class Meta:
        verbose_name = u'Ингредиенты'
        verbose_name_plural = u'Ингредиенты'

    def __str__(self):
        return f"{self.name}"

class Recipes(models.Model):
    """Рецепты блюд """

    cook_name = models.ForeignKey(
        CookName,
        models.CASCADE,
        verbose_name='Блюдо'
    )

    ingredient = models.ForeignKey(
        Ingredients,
        models.CASCADE,
        verbose_name='Ингредиент'
    )

    count = models.SmallIntegerField(
        "Количество ингредиентов",
        null=False,
        blank=False,
    )

    unit = models.ForeignKey(
        Units,
        models.CASCADE,
        verbose_name='Единица измерения'
    )


    class Meta:
        verbose_name = u'Рецепты'
        verbose_name_plural = u'Рецепты'


    def __str__(self):
        return f"{self.ingredient}, {self.count}, {self.unit}"

