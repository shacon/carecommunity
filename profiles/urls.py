from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profiles_list', views.profiles_list, name='profiles_list'),
	url(r'^profile/(?P<id>[0-9]+)', views.individual_profile, name='individual_profile'),


]
