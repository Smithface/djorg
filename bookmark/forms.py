from django import forms
from .models import Bookmark, PersonalBookmark

class BookmarkForm(forms.ModelForm):

  class Meta:
    model = Bookmark
    fields = ('name', 'url', 'notes')

class PersonalBookmarkForm(forms.ModelForm):

  class Meta:
    model = PersonalBookmark
    fields = ('user',)