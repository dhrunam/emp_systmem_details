from rest_framework import serializers
from operation import models as op_models

# import magic

class AllotedDevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = op_models.AllotedDevices
        fields = (
            'id',
            'system_assignment_details',
            'system_details',
            'remarks',

        )

   

class SystemAssignmentDetailsSerializer(serializers.ModelSerializer):

    related_devices = AllotedDevicesSerializer(source='system_assigend_to', many= True, read_only=True)

    class Meta:
        model = op_models.SystemAssignmentDetails
        fields = (
            'id',
            'employee',
            'section',
            'ip_address',
            'remarks',
            'related_devices',
        )

