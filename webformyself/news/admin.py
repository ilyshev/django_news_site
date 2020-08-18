from django.contrib import admin
from .models import News, Category

# меняем отображение в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title') # какие поля будут ссылками в админке
    search_fields = ('title', 'content')
    list_editable = ('is_published',) # возможность редактировать прямо в списке новостей
    list_filter = ('is_published', 'category') # возможность фильтрации по выбранным полям


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin) # порядок перечисления важен! сначала основную модель, затем класс ее настройки
admin.site.register(Category, CategoryAdmin)
