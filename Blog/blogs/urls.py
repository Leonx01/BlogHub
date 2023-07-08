from django.urls import path

from blogs import views
urlpatterns=[
  path(r'',views.index,name='index'),
  
  path(r'posts/',views.posts,name='posts'),
  path(r'posts/<int:post_id>/',views.post,name='post'),
  path(r'edit_post/<int:post_id>/',views.edit_post,name='edit_post'),
  path(r'new_post/',views.new_post,name='new_post')
]