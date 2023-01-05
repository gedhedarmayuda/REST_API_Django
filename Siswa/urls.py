from django.conf.urls import url
from Siswa import views

urlpatterns = [
    url(r'^api/tutorial$', views.siswa_list),
    url(r'')
]
