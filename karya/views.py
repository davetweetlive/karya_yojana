from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

    def post(self, request, *kwargs):
        pass
