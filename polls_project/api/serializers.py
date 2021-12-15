from rest_framework import serializers

from .models import Poll


class PollCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id','name', 'date_start', 'questions', 'description']

