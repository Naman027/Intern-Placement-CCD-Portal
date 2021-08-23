from django.conf.urls import url,include
from . import views
urlpatterns = [

    url(r'^$',views.getmainpage,name='main_page'),
    url(r'^placement/remarks/(?P<pk>\d+)/$', views.getremarks, name='premarks'),
    url(r'^intern/remarks/(?P<pk>\d+)/$', views.getremarks, name='iremarks'),
    url(r'placement/$', views.getPlacement,name='placement'),
    url(r'intern/$', views.getIntern, name='intern'),
    url(r'^intern/(?P<pk>\d+)/$', views.save_changes_view, name='intern_company_edit'),
    url(r'^placement/(?P<pk>\d+)/$', views.save_changes_view, name='placement_company_edit'),
    url(r'placement_add_company/$', views.add_placement_company, name='placement_add_company'),
    url(r'intern_add_company/$', views.add_intern_company, name='intern_add_company'),
 	url(r'placement/search/$', views.searchPlacement, name='search'),
    url(r'intern/search/$', views.searchIntern, name='search'),
    url(r'logout/$', views.session_logout, name='logout'),
    url(r'edit_ID/$', views.change_password, name='edit_ID')

]