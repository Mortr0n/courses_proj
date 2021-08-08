from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('destroy-yn/<int:course_id>', views.destroy_yn),
    path('destroy/<int:course_id>', views.destroy),
    path('comments/<int:course_id>', views.comments),
    path('comment/<int:course_id>/create', views.comment_create),
    path('comment/<int:course_id>/<int:comment_id>/destroy', views.comment_destroy),
]
