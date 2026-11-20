from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string

def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)

def csrf_failure(request, reason=''):
    context = {'error_message': 'Доступ запрещен'}
    return HttpResponseForbidden(
        render_to_string('core/403csrf.html', context, request)
    )