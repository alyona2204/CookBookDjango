from django import forms


class CookNameSearchForm(forms.Form):
    prefix = 'CookNameSearchForm'

    cook_name = forms.CharField(
        required=False,
        label='Часть названия',
        initial='',
    )

    ingr_id = forms.IntegerField(
        required=False,
        label='ingre',
        initial=-1,
    )


'''del'''
class RecipesForm(forms.Form):
    prefix = 'RecipesForm'

    reciped_id = forms.IntegerField(
        required=False,
        label='i',
        initial=-1,
    )