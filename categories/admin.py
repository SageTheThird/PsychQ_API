from django.contrib import admin

# Register your models here.

# Register your models here.
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'total_posts_count', 'sub_categories']
    search_fields = ['id', 'title']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Category, CategoryAdmin)
