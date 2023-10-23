from django.urls import path
from crudapp.views import *



urlpatterns = [
    path('',index,name='index'),
    #path('emp', emp,name='emp'),  
    path('show/',show,name='show'),  
    path('edit/<int:id>',edit,name='edit'),  
    path('update/<int:id>',update,name='update'),  
    path('delete/<int:id>',delete,name='delete'),
    #path('deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('project/',project,name='project'),
    path('department/',department,name='department'),
    path('departmentlab/',departmentlab,name='departmentlab'),
    path('order/',order,name='order'),
    path('customer/',customer,name='customer'),
    path('showcustomerorder/',showcustomerorder,name='showcustomerorder'),
    
    #path('customerorder<str:name>/',customerorder, name='customerorder' ),
    

]