from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('caretaker.urls')),
    url(r'^about', 'caretaker.views.about', name='about'),
    url(r'^behavior/', include('behavior.urls')),
	url(r'^profiles/', include('profiles.urls')),

    url(r'^', 'caretaker.views.index'),
]



