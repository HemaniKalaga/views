from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class Templateview(TemplateView):
    template_name='cbt.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='SeethaRam'
        ECDO['age']=1000000
        return ECDO
    

class Insert_data_by_tv(TemplateView):
    template_name='insert_data_by_tv.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['BFO']=BookForm()
        return ECDO
    
    def post(self,request):
        BFDO=BookForm(request.POST)
        if BFDO.is_valid():
            BFDO.save()
            return HttpResponse('Data is inserted')

    

class Insert_data_by_fv(FormView):
    template_name='insert_data_by_fv.html'
    form_class=BookForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Data is inserted')
    



