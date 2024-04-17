from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page
import debug_toolbar


urlpatterns = [
    # path('object/<int:object_id>/', cache_page(60 * 15)(views.employee_form)),
    # path('object/<int:object_id>/', cache_page(60 * 15)(views.employee_list)),
    # path('object/<int:object_id>/', cache_page(60 * 15)(views.employee_delete)),
    path('__debug__/', include(debug_toolbar.urls)), 
    path('list/', views.employee_list, name='employee_list'), 
    path('', views.employee_form, name='employee_insert'), 
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), 
    path('<int:id>/', views.employee_form, name='employee_update'), 
    # path('cached/', views.cached, name='cached'), 
    # path('cacheless/', views.cacheless, name='cacheless'), 
]