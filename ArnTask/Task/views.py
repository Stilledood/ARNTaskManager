from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

from .models import Task

class OrdersByAgent(View):
    '''Class to create a view to display all sales agent bills'''

    template_name = "Task/orders.html"
    model_name = Task

    def get(self,request):
        user = get_user_model()
        if user.is_superuser:
            orders = Task.objects.all()
        elif user.role == "SALES":
            orders = Task.objects.filter(created_by=user.username)

        context = {
            'orders':orders
        }

        return render(request,template_name=self.template_name, context=context)

