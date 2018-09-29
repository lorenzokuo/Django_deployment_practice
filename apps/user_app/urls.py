from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.home, name = "home"),
    url(r'^new$', views.add, name = "add"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = "destroy"),
    url(r'^granted/(?P<job_id>\d+)$', views.add_to_granteds, name = "granted"),
    url(r'^remove_granted/(?P<job_id>\d+)$', views.remove_granteds, name = "remove_granted"),
    url(r'^(?P<job_id>\d+)$', views.show, name = "show"),
    url(r'^edit/(?P<job_id>\d+)$', views.edit, name = "edit"),
    url(r'^update$', views.update, name = "update")

]