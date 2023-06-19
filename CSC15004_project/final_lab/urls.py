from django.urls import path
from . import views

app_name = "final_lab"

urlpatterns = [
    path("clone_index", views.Clone_indexView.as_view(), name="clone_index"),
    path("index", views.IndexView.as_view(), name="index"),
    path("base", views.BaseView.as_view(), name="base"),
    path('index/<str:category>/', views.index_view, name='category'),

    # path("cat", views.cat_view, name="cat"),
]
