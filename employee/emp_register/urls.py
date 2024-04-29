from django.urls import path, include, re_path
from . import views
# from django.views.decorators.cache import cache_page
import debug_toolbar


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)), 
    path('list/', views.employee_list, name='employee_list'), 
    # path('object/cache/<int:object_id>/', cache_page(60 * 15)(views.employee_list)),
    path('', views.employee_form, name='employee_insert'), 
    # path('object/cache/<int:object_id>/', cache_page(60 * 15)(views.employee_form)),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), 
    # path('object/cache/<int:object_id>/', cache_page(60 * 15)(views.employee_delete)),
    path('update/<int:id>/', views.employee_update, name='employee_update'), 
    # path('add/<int:a>/<int:b>', views.add, name='add'), 
    re_path(r"^add/(?P<a>[0-9]{1,5})/(?P<b>[0-9]{1,5})/$", views.add), 
    # path('cached/', views.cached, name='cached'), 
    # path('cacheless/', views.cacheless, name='cacheless'), 
]