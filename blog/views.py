from django.shortcuts import render
from django.views.generic import TemplateView


def post_list(request):
    return render(request, 'post_list.html', {})


class IndexView(TemplateView):
    template_name = 'index.html'


