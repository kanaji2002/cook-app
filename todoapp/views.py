from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render
from .models import Image

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'todoapp/showall.html', context)




# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="tasks"

    def get_context_data(self, **kwargs: Any):

            context=super().get_context_data(**kwargs)
            user=self.request.user

            if user.username=="top":
                context["tasks"]=context["tasks"]
            else:
                context["tasks"]=context["tasks"].filter(user=user)  
            
            searchInputText=self.request.GET.get("search") or ""
            if searchInputText:
                context["tasks"]=context["tasks"].filter(title__icontains=searchInputText)
           
            context["search"]=searchInputText
            return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name="task"

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=["title","description","completed","image"]
    success_url=reverse_lazy("tasks")

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields="__all__"
    success_url=reverse_lazy("tasks")

    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    fields="__all__"
    success_url=reverse_lazy("tasks")
    context_object_name="task"

class TaskListLoginView(LoginView):
    fields="__all__"
    template_name="todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
    
class RegisterTodoApp(FormView):
    template_name="todoapp/register.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("tasks")

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            print("ddddd")
            login(self.request,user)
        return super().form_valid(form)