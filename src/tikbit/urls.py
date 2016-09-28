from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    # urls
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^projects/$', 'newsletter.views.projects', name='projects'),
    url(r'^games/$', 'newsletter.views.games', name='games'),
    url(r'^squiggles/$', 'newsletter.views.squiggles', name='squiggles'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'newsletter.views.about', name='about'),
    url(r'^herbs/$', 'newsletter.views.herbs', name='herbs'),
    url(r'^friends/$', 'newsletter.views.friends', name='friends'),
    url(r'^fitness/$', 'newsletter.views.fitness', name='fitness'),
    url(r'^goodnews/$', 'newsletter.views.goodnews', name='goodnews'),
    url(r'^business/$', 'newsletter.views.business', name='business'),
    url(r'^ranger/$', 'newsletter.views.ranger', name='ranger'),
    url(r'^business_contact/$', 'newsletter.views.business_contact', name='business_contact'),
    url(r'^signup/$', 'newsletter.views.signup', name='signup'),
    url(r'^lab/$', 'newsletter.views.lab', name='lab'),


    # custom mothership admin pages
    url(r'^terminal/$', 'newsletter.views.terminal', name='terminal'),
    url(r'^test/$', 'newsletter.views.test', name='test'),
    url(r'^sitemap.xml/$', 'newsletter.views.sitemap', name='sitemap.xml'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)