from django.contrib import admin
from django.urls import include, path                
from rest_framework import routers                    
from todo import views                            

router = routers.DefaultRouter()                      
router.register(r'todos', views.TodoView, 'todo')     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),             
    ]