# -*- coding: utf-8 -*-
from django import forms

from localflavor.au.forms import AUPhoneNumberField
from project.rolodex.models import Email, Phone

from . import settings
from .models import TemporaryMember


class TemporaryMemberForm(forms.Form):

    member_type = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=settings.MEMBERS_TYPES,
        initial=settings.MEMBERS_TYPES[0])
    sort_name = forms.CharField(label="Surname")
    ref_name = forms.CharField(label="First name")
    email = forms.EmailField()
    phone = AUPhoneNumberField()
    address = forms.CharField(widget=forms.Textarea)
    suburb = forms.CharField()
    postcode = forms.CharField()
    state = forms.CharField(initial="ACT")
    country = forms.CharField(initial="Australia")
    dob = forms.DateField(
        input_formats=('%d/%m/%Y', '%d-%m-%Y'),
        label="Birthday",
        help_text="Optional and confidential, so we can wish you happy birthday.",  # noqa
        required=False)
    year = forms.IntegerField(
        widget=forms.Select(choices=settings.YEAR_CHOICES),
        label="My generation:",  # noqa
        help_text="Did you know that there are more Generation Yers than Baby Boomers? Please answer this for our curiosity, so we can try to look after you the best.",  # noqa
        min_value=1890, max_value=2017)
    payment_method = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[('', '---')] + settings.PAYMENT_METHODS)
    survey_games = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="What's your favourite game?",
        help_text="List as many as you like.")
    survey_food = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="What food, drink or pizza would you like see on our menu?",  # noqa
        help_text="Say as much as you want.")
    survey_hear = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="How did you hear about us?",
        help_text="Tell us a story.")
    survey_suggestions = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="Any suggestions you would have for us?",
        help_text="We're still pretty new and learning as we go!")
    special = forms.CharField(
        label="other/special membership add reason",
        help_text="Add the reason for your special membership. Special memberships are arranged for you by Guild staff or management. Ignore otherwise.",  # noqa
        required=False)

    def __init__(self, *args, **kwargs):
        super(TemporaryMemberForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)

        self.fields['dob'].widget.attrs['placeholder'] = 'dd/mm/yyyy'
        self.fields['special'].widget.attrs['placeholder'] = '"other" membership explanation'  # noqa


class BlankForm(forms.Form):

    input_class = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[('member', 'Member'), ('membership', 'Membership')])

    input_data = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 15, 'cols': 100}))
