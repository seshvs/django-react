from django.conf.urls import url

from .views import CategoryViewset


urlpatterns = [
    url(r'category/(?P<category>.*)/average_cubic_weight/$', CategoryViewset.as_view(),
        name='category-average_cubic_weight')
]
