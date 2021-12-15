from rest_framework import serializers

from .models import Poll, Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class PollCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id','name', 'date_start', 'date_end', 'questions', 'description']
        read_only_fields = ['id', 'date_start']

    def update(self, instance, validated_data):
        instance.questions.set(validated_data['questions'])
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['id', 'participant']


# class AnswerListSerializer(serializers.ModelSerializer):
#serializers.RelatedField(source='category', read_only=True)