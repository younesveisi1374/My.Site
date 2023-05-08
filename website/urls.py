from django.urls import path, include
from website.views import index_view
urlpatterns = [
    path("",index_view),
]
 