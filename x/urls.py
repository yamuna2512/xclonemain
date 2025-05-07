from django.urls import path
from .import views
from x.views import xListView, xAdd, xDelete, xEditView, xLikeAdd, xLikeSubtract

urlpatterns = [
   path('first/', xListView, name='post1'),
    path('xAdd/', xAdd, name='x_add'),
    path('xDelete/<int:x_id>/', xDelete, name='x_delete'),
    path('xEditView/<int:x_id>/', xEditView, name='x_edit'),
    path('xLikeAdd/<int:x_id>/', xLikeAdd, name='x_like_add'),
    # path('api/xLikeAdd/<int:x_id>/', xLikeAdd, name='like-add')
    path('xLikeSubtract/<int:x_id>/', xLikeSubtract, name='x_like_subtract'),
] 


