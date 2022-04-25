from django.urls import path, include
from rest_framework import routers

from .views import DiaryViewSet, NoteViewSet

router = routers.SimpleRouter()
router.register(r'diaries', DiaryViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
