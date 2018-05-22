from django.conf.urls import url

from ip import views

urlpatterns = [
    
    url(r'^$', views.index, name='ip_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='ip_index'),
    
    url(r'^basics/$', views.basics, name='ip_basics'),
    
    #test
    url(r'^test/$', views.test, name='ip_test'),
    
    
]
