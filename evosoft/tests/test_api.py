from django.urls import reverse
from rest_framework.test import APITestCase
from diaries.models import Diary, Note
from django.contrib.auth.models import User

from diaries.serializers import DiarySerializer


class DiariesApiTestCase(APITestCase):
    def test_get(self):
        User.objects.create_user(username='TestUser')

        diary_test_1 = Diary.objects.create(
            title='Test Title',
            kind='public',
            user_id=1)

        url = reverse('diary-list')
        response = self.client.get(url)

        serializer_data = DiarySerializer([diary_test_1], many=True).data
        self.assertEqual(serializer_data, response.data.get('results'))

    def test_get_with_filters(self):
        User.objects.create_user(username='TestUser')
        diary_test_1 = Diary.objects.create(
            title='Test Title 1',
            kind='public',
            user_id=1
        )
        Diary.objects.create(
            title='Test Title 2',
            kind='public',
            user_id=1
        )

        url = reverse('diary-list')
        response = self.client.get(url + '?title=Test Title 1')

        serializer_data = DiarySerializer([diary_test_1], many=True).data
        self.assertEqual(serializer_data, response.data.get('results'))

    def test_put(self):
        pass

    def test_delete(self):
        pass


class NotesApiTestCase(APITestCase):
    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass

    def test_delete(self):
        pass
