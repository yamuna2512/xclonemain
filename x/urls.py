from django.urls import path
from .import views
from x.views import xListView, xAdd, xDelete, xEditView, xLikeAdd, xLikeSubtract

urlpatterns = [
   path('first/', xListView),
    path('xAdd/', xAdd),
    path('xDelete/<int:x_id>/', xDelete),
    path('xEditView/<int:x_id>/', xEditView),
    path('xLikeAdd/<int:x_id>/', xLikeAdd),
    path('xLikeSubtract/<int:x_id>/', xLikeSubtract),
]


