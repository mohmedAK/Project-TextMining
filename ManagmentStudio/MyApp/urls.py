from django.urls import path

from .views import register_page,add_person_data,confirm

urlpatterns = [
     path('', register_page, name='Register'),
     path('addperson/', add_person_data, name='add_person_data'),
     path('confirm/<str:person_name>', confirm, name='confirm'),
]
