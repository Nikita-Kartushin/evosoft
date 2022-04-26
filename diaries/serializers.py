from rest_framework import serializers

from diaries.models import Diary, Note


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

    def create(self, validated_data):
        diary = Diary.objects.create(
            kind=validated_data.get('kind'),
            title=validated_data.get('title'),
            expiration=validated_data.get('expiration') if validated_data.get('kind') == 'private' else None,
            user=validated_data.get('user')
        )

        diary.save()
        return diary


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
