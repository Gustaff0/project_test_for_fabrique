from rest_framework import serializers
from api_v1.models import Poll, AnswChecker, Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['id']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['id']


class AnswCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswChecker
        fields = '__all__'
        read_only_fields = ['id']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ['id']