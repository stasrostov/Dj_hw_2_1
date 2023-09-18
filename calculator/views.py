from django.shortcuts import render

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
}

def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))

    recipe = {}

    if dish in DATA:
        original_recipe = DATA[dish]
        recipe = {ingredient: amount * servings for ingredient, amount in original_recipe.items()}

    context = {'recipe': recipe}

    return render(request, 'calculator/index.html', context)
