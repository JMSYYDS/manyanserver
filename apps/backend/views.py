from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django import http

# Create your views here.


class TestView(View):

    def get(self, request):
        return http.JsonResponse({'data': ['ada', 'asda'], 'state': 'ok'})