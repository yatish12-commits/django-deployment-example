from basic_app import views
from django.conf.urls import url


## tagging learning_template

app_name = 'basic_app'

urlpatterns = [
    ##url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
