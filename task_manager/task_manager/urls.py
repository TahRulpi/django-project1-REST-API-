
from django.contrib import admin
from django.urls import path,include
#from tasks.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
 #   path('',index, name = "index"),
    path('tasks/',include('tasks.urls')),
]