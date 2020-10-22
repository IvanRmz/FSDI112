from django.shortcuts import render
from django.views.generic import TemplateView

class CalculationViewTemplate(TemplateView):
    template_name = "calc/calculation.html"
