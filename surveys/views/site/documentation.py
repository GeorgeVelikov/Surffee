from django.shortcuts import render


def documentation(request):
    template = 'documentation.html'
    context = {}
    return render(request, template, context)
