from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^about/$', views.About),
    url(r'^grant/$', views.Grant),
    url(r'^test/$', views.Test),
	url(r'^2018/$', views.per2018),
	url(r'^performance1/$', views.Performance1),
	url(r'^indexedjournal/$', views.Indexedjournal),
	url(r'^nonindexedjournal/$', views.Nonindexedjournal),
	url(r'^otherpublication/$', views.Otherpublication),
	url(r'^nationalgrant/$', views.Nationalgrant),
	url(r'^nationalgrantRM/$', views.NationalgrantRM),
]
