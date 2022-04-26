from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from diaries.models import Diary, Note
from diaries.serializers import DiarySerializer, NoteSerializer

from .filters import DiaryFilter, NoteFilter
from .permissions import IsPrivateDiary, IsPrivateNote


class ApiViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 500


class DiaryViewSet(viewsets.ModelViewSet):
    filter_class = DiaryFilter
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    pagination_class = ApiViewPagination
    permission_classes = (IsPrivateDiary, )


class NoteViewSet(viewsets.ModelViewSet):
    filter_class = NoteFilter
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = ApiViewPagination
    permission_classes = (IsPrivateNote, )
