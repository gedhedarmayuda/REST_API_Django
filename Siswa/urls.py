from django.conf.urls import url
from Siswa import views

urlpatterns = [
    url(r'^api/siswa$', views.siswa_list),
    url(r'^api/siswa/(?P<pk>[0-9]+)$', views.siswa_detail),
    url(r'^api/siswa/published$', views.siswa_list_published),
]
