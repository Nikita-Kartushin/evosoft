from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser
from .models import Diary, Note


class IsPrivateNote(permissions.BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser) and request.user.is_authenticated:
            query_filter = Note.objects.filter(diary__user=request.user).exists()
            return query_filter

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user == obj.diary.user:
            return True

        return False


class IsPrivateDiary(permissions.BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser) and request.user.is_authenticated:
            query_filter = Diary.objects.filter(user=request.user).exists()

            return query_filter

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.user == request.user:
            return True

        return False
