from django.db.models import QuerySet
from django.shortcuts import render
from .forms import CookNameSearchForm
from .models import CookName, Ingredients



def detail(request, pk):
    qs: QuerySet = CookName.objects \
        .prefetch_related('recipes_set__unit') \
        .prefetch_related('recipes_set__ingredient')

    qs = qs.filter(id=pk)

    return render(request, 'recipes.html', {"data": qs})

def home(request):
    qs: QuerySet = CookName.objects\
        .prefetch_related('recipes_set__unit')\
        .prefetch_related('recipes_set__ingredient')

    form = CookNameSearchForm(request.GET)
    cook_name = ''
    ingr_id = -1
    if form.is_valid():
        print(form.cleaned_data)
        if form.cleaned_data['cook_name'] != '':
            cook_name = form.cleaned_data['cook_name']
        if form.cleaned_data['ingr_id'] != '':
            try:
                ingr_id = int(form.cleaned_data['ingr_id'])
            except Exception as e:
                ingr_id = -1
    else:
        print(form.errors)

    if len(cook_name) > 0:
        qs = qs.filter(name__icontains=cook_name)

    if ingr_id > 0:
        qs = qs.filter(recipes__ingredient=ingr_id)

    ingredients = Ingredients.objects.all()

    return render(request, 'cook.html', {
        "data": qs,
        "ingredients": ingredients,
        "form": form,
    })


