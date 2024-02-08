from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def main_view(request):
    context = {}
    return render(request, 'calendar_templates/calendar.html', context)