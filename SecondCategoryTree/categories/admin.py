from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from SecondCategoryTree.categories.models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'description', 'image', )
    list_filter = ('name', )
    search_fields = ('name', )
    list_display_links = ('indented_title', )
    list_per_page = 20

