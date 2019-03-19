from django.urls import path
from .views import index

core_patterns = ([
path("",index, name = "index"),
],'core')