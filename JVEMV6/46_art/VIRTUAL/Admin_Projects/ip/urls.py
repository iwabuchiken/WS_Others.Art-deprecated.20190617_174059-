from django.conf.urls import url

from ip import views

urlpatterns = [
    
    url(r'^$', views.index, name='im_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='im_index'),
    
    #test
    url(r'^test/$', views.test, name='ip_test'),
    
    
]
