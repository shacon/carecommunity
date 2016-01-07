from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profiles_list', views.profiles_list, name='profiles_list'),
	url(r'^inividual_profile/(?P<client_id>\D+)', views.individual_profile, name='individual_profile'),


]
