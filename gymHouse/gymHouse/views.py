from multiprocessing import get_context
from webbrowser import get
from django.shortcuts import render
from django.views import generic

class IndexView(generic.View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
