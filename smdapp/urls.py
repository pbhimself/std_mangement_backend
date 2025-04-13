from django.urls import path
from . import views

urlpatterns = [
    path('', views.testapp, name='testapp'),
    path('insertdata', views.InserData.as_view(), name='insertdata'),
    path('readcsvfile', views.ReadCSVFile.as_view(), name='readcsvfile'),
    path('getuploadeddata', views.GetUploadedData.as_view(), name='getuploadeddata'),
]