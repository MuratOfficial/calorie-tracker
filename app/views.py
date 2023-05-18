from django.shortcuts import render, HttpResponseRedirect
from .models import Food, Stats

def index(request):
    foods = Food.objects.all()
    stats = Stats.objects.all()
    calorie_sum = sum(stat.calories_full for stat in stats)
    indicator = 0
    if calorie_sum < 500:
        indicator = 0
    elif calorie_sum > 500 and calorie_sum < 1000:
        indicator = 25
    elif calorie_sum > 1000 and calorie_sum < 1500:
        indicator = 50
    elif calorie_sum > 1500 and calorie_sum < 2000:
        indicator = 75
    else:
        indicator = 100
    context = {
        "foods": foods,
        "stats": stats,
        "sum": calorie_sum,
        "indicator": indicator,
    }
    return render(request, 'app/index.html', context)

def add_food(request, food_id):
    current_page = request.META.get('HTTP_REFERER')
    food = Food.objects.get(id=food_id)
    stats = Stats.objects.filter(food_name=food)
    if not stats.exists():
        Stats.objects.create(
            food_name=food,
            carbs_full=food.carbs,
            protein_full=food.protein,
            fats_full=food.fats,
            calories_full=food.calories
        )
        return HttpResponseRedirect(current_page)
    else:
        stat = stats.first()
        stat.carbs_full += food.carbs
        stat.protein_full += food.protein
        stat.fats_full += food.fats
        stat.calories_full += food.calories
        stat.save()
        return HttpResponseRedirect(current_page)
    # stats.carbs_full += food.carbs
    # stats.protein_full += food.protein
    # stats.fats_full += food.fats
    # stats.calories_full += food.calories
    # stats.save()
    # return HttpResponseRedirect(current_page)

def delete_food(request, id):
    stat = Stats.objects.get(id=id)
    stat.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Create your views here.
