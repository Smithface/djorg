from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

  def create(self, validated_data):
    # import pdb; pdb.set_trace()
    user = self.context['request'].user

    note = Note.objects.create(user=user, **validated_data)
    return note
  
  class Meta:
    model = Note
    fields = ('title', 'content', 'id')
  
class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()

  def get_queryset(self):
    # try:
    #   return Note.objects.filter(user=self.request.user)
    # except:
    #   return Note.objects.none()
    user = self.request.user

    if user.is_anonymous:
      return Note.objects.none()
    else:
      return Note.objects.filter(user=user)
