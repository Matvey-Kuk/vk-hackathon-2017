from django.conf.urls import url

from .views import AmazingSPA

urlpatterns = [
    url(r'^$', AmazingSPA.as_view(), name='amazing-spa'),
]
