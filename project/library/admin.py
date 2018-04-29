# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .forms import CategoryAdminForm, GameAdminForm
from .models import Category, Game
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Content', {'fields': ['title', 'heading', 'featured_content',
                                'content', 'meta_description']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured', 'site', 'slug',
                                   ('created_at', 'updated_at')],
                        'classes': ['collapse']}),
    ]

    form = CategoryAdminForm

    list_display = ['name', 'is_active', 'is_featured']

    list_filter = ['is_enabled', 'is_featured']

    prepopulated_fields = {'slug': ['name']}

    readonly_fields = ['created_at', 'updated_at']

    search_fields = ['name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name', 'categories', 'expansion_for',
                           'publisher', 'boardgamegeek_id', 'boardgamegeek_rank',
                           'year_published',
                           ('minimum_players', 'maximum_players'),
                           ('minimum_playtime', 'maximum_playtime'),
                           ]}),
        ('Content', {'fields': ['title', 'heading', 'featured_content',
                                'content', 'meta_description']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured', 'site', 'slug',
                                   'tags', ('created_at', 'updated_at')],
                        'classes': ['collapse']}),
    ]

    form = GameAdminForm

    list_display = ['name', 'is_active', 'is_featured', 'is_expansion']

    list_filter = ['is_enabled', 'is_featured']

    prepopulated_fields = {'slug': ['name']}

    readonly_fields = ['created_at', 'updated_at']

    search_fields = ['name']
