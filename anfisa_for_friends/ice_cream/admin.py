# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано in app'


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0
    filter_horizontal = ('toppings',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)





# ...и регистрируем её в админке:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)

