# -*- coding: utf-8 -*-
from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Game


class TestGameCreateFromBGGIDSave(TestCase):

    def test_game_saves_passes(self):
        new_obj = Game.create_from_bgg_id(31260)
        test_obj = Game.objects.get(name='Agricola')
        self.assertEqual(new_obj, test_obj)

    def test_game_invalid_saves_fails(self):
        self.assertRaises(ValidationError, Game.create_from_bgg_id, 'asdfg')

    def test_game_empty_saves_fails(self):
        self.assertRaises(ValidationError, Game.create_from_bgg_id, '')

