from django.urls import path
from.import views
from .views import TaskCreate, TaskDelete,TaskList,TaskDetail,RegisterTodoApp,TaskListLoginView,TaskUpdate
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path("", TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TaskListLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterTodoApp.as_view(), name="register"),
    path("my_page1/", views.my_page_view, name='my_page'),
    path("suionn/", views.suionn_view, name='suionn'),
    path("nissyaryou/", views.nissyaryou_view, name='nissyaryou'),
    path("DO/", views.DO_view, name='DO'),
    path("ennbunn/", views.ennbunn_view, name='ennbunn'),
    path("tyouryuu/", views.tyouryuu_view, name='tyouryuu'),
    path("yosoku/", views.yosoku_view, name='yosoku'),
    path("yosoku2/", views.yosoku_view2, name='yosoku2'),

]
