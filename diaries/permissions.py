from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser
from .models import Diary, Note


class IsPrivateNote(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not isinstance(request.user, AnonymousUser):
            query_filter = Note.objects.filter(diary__user=request.user).exists()
            return query_filter

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.diary.kind == 'public'


class IsPrivateDiary(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not isinstance(request.user, AnonymousUser):
            query_filter = Diary.objects.filter(kind='private', user=request.user).exists()

            return query_filter

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.kind == 'public'
