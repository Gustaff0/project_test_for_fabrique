from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404, render, redirect
from .models import Choice, AnswChecker, Question, Poll
import json
from django.http import HttpResponse, JsonResponse
from .serializer import ChoiceSerializer, AnswCheckerSerializer, QuestionSerializer, PollSerializer
from django.utils import timezone


class PollListView(generics.ListAPIView):
    today = timezone.now().date()
    queryset = Poll.objects.filter(start_date__gte=today)
    serializer_class = PollSerializer



class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # lookup_field = 'slug'


class AnswerChecker(APIView):
    def post(self, request, *args, **kwargs):
        parsed_answers = []
        for question in request.data['answers']:
            answer = {}
            answer['user'] = request.data['user']
            answer['question'] = question['question']
            answer['text'] = question.get('text', '')
            if question.get('choices'):
                for choice in question['choices']:
                    answer['choice'] = choice
                    parsed_answers.append(answer.copy())
            else:
                parsed_answers.append(answer.copy())
        serializer_answer = AnswCheckerSerializer(data=parsed_answers, many=True)
        if serializer_answer.is_valid():
            serializer_answer.save()
            return Response(serializer_answer.data)
        return Response(serializer_answer.errors)


class Result(APIView):
    def get(self, request, *args, **kwargs):
        user = kwargs.get('pk')
        parsed_result = []
        results = AnswChecker.objects.filter(user=user)
        for result in results:
            result_dict = {}
            result_dict['question'] = result.question.text
            result_dict['poll'] = result.question.poll.title
            if result.choice:
                result_dict['answer'] = result.choice.text
            else:
                result_dict['answer'] = result.answer
            parsed_result.append(result_dict.copy())
        return JsonResponse(parsed_result, safe=False)
