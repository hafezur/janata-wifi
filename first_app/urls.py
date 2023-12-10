
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('data/',views.find_data,name='find_data'),
    path('edit_data/<int:id>',views.edit_data,name='edit_data'),
    path('store_data/',views.store_data,name='store_data'),
    path('delete_data/<int:id>',views.delete_data,name='delete_data'),
]
