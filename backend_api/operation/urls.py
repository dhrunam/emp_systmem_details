from django.urls import include, path
from operation import views as op_views

urlpatterns = [
    path('operation/system_assignment_details', op_views.SystemAssignmentDetailsList.as_view()),
    path('operation/system_assignment_details/<int:pk>', op_views.SystemAssignmentDetailsDetails.as_view()),
    
    
    
]
