from django.contrib import admin

from diaries.models import Diary, Note

admin.site.register(Diary)
admin.site.register(Note)
