from django.contrib import admin
from django.urls import path, include
from .models import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_published')  # Поля, отображаемые в списке
    list_filter = ('is_published',)  # Фильтры по полям
    search_fields = ('name',)  # Поля для поиска

    @admin.action(description='Опубликовать выбранные товары')
    def publish_products(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Снять публикацию с выбранных товаров')
    def unpublish_products(self, request, queryset):
        queryset.update(is_published=False)

    @admin.action(description='Изменить цену выбранных товаров')
    def change_price(self, request, queryset):
        # Здесь вы можете добавить логику для изменения цены,
        # например, через форму или просто установить фиксированное значение.
        for product in queryset:
            product.price += 10.00  # Увеличиваем цену на 10.00
            product.save()

    actions = [publish_products, unpublish_products, change_price]  # Добавляем действия в админку