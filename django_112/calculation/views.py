from django.shortcuts import render
from django.views.generic import TemplateView

class CalculationViewTemplate(TemplateView):
    template_name = "calc/calculation.html"
    num = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print("********Ivan : " + str(self.num))
        num = self.num
        print("********Ivan : " + str(num))
        return  num
