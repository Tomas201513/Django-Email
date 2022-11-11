from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


# from rest_framework import serializers
# from .models import *

# # from dataclasses import field
# class GrandparentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Grandparent
#         fields='__all__'