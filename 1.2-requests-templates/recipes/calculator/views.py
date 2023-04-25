from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet(request):
    persons = int(request.GET.get('servings', 1))
    context = {'recipe': {k: v * persons for k, v in DATA['omlet'].items()}}
    return render(request, 'calculator/index.html', context)


def pasta(request):
    persons = int(request.GET.get('servings', 1))
    context = {'recipe': {k: v * persons for k, v in DATA['pasta'].items()}}
    return render(request, 'calculator/index.html', context)


def buter(request):
    persons = int(request.GET.get('servings', 1))
    context = {'recipe': {k: v * persons for k, v in DATA['buter'].items()}}
    return render(request, 'calculator/index.html', context)
