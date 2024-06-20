from django.db import models
from django.contrib.auth.models import User, Group
from masters import models as master_models
from common.utility import FilePathManager

import datetime


class SystemAssignmentDetails(models.Model):

    employee= models.OneToOneField(master_models.Employee, null=True, on_delete=models.SET_NULL, related_name='system_assigend_to')
    section = models.ForeignKey(master_models.Section, null=True, on_delete=models.SET_NULL, related_name='emp_section')
    ip_address = models.CharField(max_length=15, null=True, unique=True)
    remarks = models.CharField(max_length=1024, null=True, default='')

class AllotedDevices(models.Model):
    system_assignment_details= models.ForeignKey(SystemAssignmentDetails, null=True, on_delete=models.SET_NULL, related_name='system_assigend_to')
    system_details = models.CharField(max_length=1024, null=False, default='')
    remarks = models.CharField(max_length=1024, null=True, default='')