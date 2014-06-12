# -*- coding: utf-8 -*-
from django.contrib import admin

from app.models import Item, RelatedItem, Category


class RelatedItemInline(admin.TabularInline):
    model = RelatedItem


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [RelatedItemInline]

admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
