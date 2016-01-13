from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profiles_list', views.profiles_list, name='profiles_list'),
	url(r'^inividual_profile/(?P<client_id>\d+)', views.individual_profile, name='individual_profile'),
    url(r'^search/$', views.search, name='search'),
    url(r'^addclient', views.addclient, name='addclient'),

]
