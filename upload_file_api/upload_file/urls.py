from django.urls import path
from .views import FileListAPIView, FileCreateAPIView


app_name = 'upload_file'

urlpatterns = [
    path('upload/', FileCreateAPIView.as_view(), name='upload-file'),
    path('list/', FileListAPIView.as_view(), name='list-file')
]

