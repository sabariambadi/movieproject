from django.urls import path
from . import views
app_name='inmakesapp'
urlpatterns = [

    path('',views.demo,name="demo"),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.movie_add,name='movie_add'),
    path('update/<int:id>/',views.update,name='update'),
]




