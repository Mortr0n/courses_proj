from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('destroy-yn/<int:course_id>', views.destroy_yn),
    path('destroy/<int:course_id>', views.destroy),
]
