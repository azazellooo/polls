from rest_framework import serializers

from .models import Poll, Question


class PollCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id','name', 'date_start', 'date_end', 'questions', 'description']

    def update(self, instance, validated_data):
        instance.questions.set(validated_data['questions'])
        instance.save()
        return instance