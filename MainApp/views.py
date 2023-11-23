from django.shortcuts import render

def main_view(request):
    print("Main view")
    context = {}
    return render(request, 'base.html', context)
