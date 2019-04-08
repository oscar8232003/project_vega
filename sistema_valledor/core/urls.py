from django.urls import path
from .views import index,contactanos

core_patterns = ([
path("",index, name = "index"),
path("contactanos/",contactanos, name = "contactanos"),
],'core')