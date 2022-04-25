import django_filters

from .models import Diary, Note


class DiaryFilter(django_filters.FilterSet):
    class Meta:
        model = Diary
        fields = '__all__'


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = '__all__'
