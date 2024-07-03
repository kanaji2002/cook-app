from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from datetime import datetime

import sys
import os

# 現在のスクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# your_module の絶対パスを生成し sys.path に追加
module_path = os.path.join(script_dir, 'AI_scripts')
sys.path.append(module_path)

# モジュールが追加されたか確認
print(sys.path)


# 自作関数の呼び出し
import akashio_random


def my_page_view(request):
    return render(request, 'todoapp/my_page.html')

def suionn_view(request):
    return render(request, 'todoapp/suionn.html')

def nissyaryou_view(request):
    return render(request, 'todoapp/nissyaryou.html')

def DO_view(request):
    return render(request, 'todoapp/DO.html')

def ennbunn_view(request):
    return render(request, 'todoapp/ennbunn.html')

def tyouryuu_view(request):
    return render(request, 'todoapp/tyouryuu.html')



def yosoku_view(request):
    now = datetime.now()
    yosoku=akashio_random.yosoku()
    # yosoku=test.test()
    context = {
        'text': 'テストです。',
        'time': now,
        'yosoku': yosoku,
    }
    return render(request, 'todoapp/yosoku.html', context)

def yosoku_view2(request):
    now = datetime.now()
    yosoku2=akashio_random.yosoku2()
    # yosoku=test.test()
    context = {
        'yosoku2': yosoku2,
        'text': '過去のデータをもとにした直近の予測値です．',
        'time': now,
        
    }
    return render(request, 'todoapp/yosoku2.html', context)



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs: Any):

        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.username == "top":
            pass
        else:
            context["tasks"] = context["tasks"].filter(user=user)

        searchInputText = self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(prod_name__icontains=searchInputText)

        context["search"] = searchInputText
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["prod_name", "device_num", "model_year", "work_date", "divA", "divB", "disassemble_fig", "order_fig"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"


class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            print("ddddd")
            login(self.request, user)
        return super().form_valid(form)
