from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
from .forms import BookmarkForm, PersonalBookmarkForm

# Create your views here.

def index(request):
  # import pdb; pdb.set_trace()

  if request.method == 'POST':
    # if request.user.
    form = BookmarkForm(request.POST) # if request.user.is_anonymous else PersonalBookmarkForm(request.POST)
    # print("here is the form: {}".format(form))
    # print("here is the request.user: {}".format(request.user))
    if form.is_valid():
      if not request.user.is_anonymous:
        form_user = PersonalBookmarkForm(request.POST)
        print("beginning {} end>>>>>>>>.".format(form_user))
        form.user = form_user.cleaned_data.get('user')
        print(form.user)
      form.save()
    else:
      # TODO error
      print('error with the post, wtf knows why')
      print(form)
      pass
  
  context = {}

  pbid = PersonalBookmark.objects.values_list('id')

  context['bookmarks'] = Bookmark.objects.exclude(id__in=pbid)

  if request.user.is_anonymous:
    context['personal_bookmarks'] = PersonalBookmark.objects.none()
  else:
    context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)

  context['form'] = BookmarkForm

  return render(request, 'bookmarks/index.html', context)
