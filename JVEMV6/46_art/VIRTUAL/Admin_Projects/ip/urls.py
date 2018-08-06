from django.conf.urls import url

from ip import views

urlpatterns = [
    
    url(r'^$', views.index, name='ip_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='ip_index'),
    
    url(r'^basics/$', views.basics, name='ip_basics'),
    
    #test
    url(r'^test/$', views.test, name='ip_test'),
    
    url(r'^get_4_corners/$', views.get_4_corners, name='get_4_corners'),
    
    url(r'^open_image_dir/$', views.open_image_dir, name='open_image_dir'),
    
    url(r'^exec_get_4_corners/$', views.exec_get_4_corners, name='exec_get_4_corners'),
    
    url(r'^gen_Cake_CSV/$', views.gen_Cake_CSV, name='gen_Cake_CSV'),
    
    url(r'^dos_attack/$', views.dos_attack, name='dos_attack'),
    
    url(r'^ip_ops/$', views.ip_ops, name='ip_ops'),
    
    
]
