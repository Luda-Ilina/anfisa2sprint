# from django.db.models import Q
from django.shortcuts import render
from ice_cream.models import IceCream  # Category


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description', 'price'
    ).filter(
        is_published=True,
        is_on_main=True,
        category__is_published=True
    )

    # Запрос c примером Ку-объектов:
    # ice_cream_list = IceCream.objects.values(
    #    'id', 'title', 'description'
    # ).filter(
    #     (Q(is_published=True) & Q(is_on_main=True))
    #     | (Q(title__contains='эскимо') & Q(is_published=True))
    # ).order_by('title')[1:4]

    # categories = Category.objects.values(
    #     'id', 'output_order', 'title'
    # ).order_by(
    #     # Сортируем записи по значению поля output_order,
    #     # а если значения output_order у каких-то записей равны -
    #     # сортируем эти записи по названию в алфавитном порядке.
    #     'output_order', 'title'
    # )

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
        # 'categories': categories
    }

    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
