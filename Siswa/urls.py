from django.urls import re_path
from Siswa import views

urlpatterns = [
    re_path(r'^api/siswa$', views.siswa_list),
    re_path(r'^api/siswa/(?P<pk>[0-9])$', views.siswa_detail),
    re_path(r'^api/siswa/published$', views.siswa_list_published),
]
