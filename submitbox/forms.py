from django import forms

from .models import CharacterSheet,AppUser

class PostForm(forms.ModelForm):

    class Meta:
        model = CharacterSheet
        fields = ('character_name', 'system_name','user_comment','page_url',)

class UserForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ('user_id','user_pass')
