from rest_framework import generics, status, response
from operation import models as op_models, serializers as op_serializers
from django.db import transaction, IntegrityError
from rest_framework.exceptions import ValidationError
import json

class SystemAssignmentDetailsList(generics.ListCreateAPIView):

    queryset = op_models.SystemAssignmentDetails.objects.all().order_by('-id')
    serializer_class = op_serializers.SystemAssignmentDetailsSerializer

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        data = self.request.data
        try:
            with transaction.atomic():
               
                # Save data in ModelA
                system_assignment_details_instance = serializer.save()

                alloted_devices = json.loads(data.get('devices'))

                if alloted_devices:
                    for item in alloted_devices:
                        # Save data in ModelB
                        alloted_device = {
                            'system_assignment_details': system_assignment_details_instance.id,
                            'system_details': item['system_details'],
                            'remarks': item['remarks']
                            # Add other fields as needed
                        }
                        model_b_serializer = op_serializers.AllotedDevicesSerializer(data=alloted_device)
                        model_b_serializer.is_valid(raise_exception=True)
                        model_b_serializer.save()
        except IntegrityError:
            raise ValidationError("An error occurred while trying to save the data.")


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class SystemAssignmentDetailsDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = op_models.SystemAssignmentDetails
    serializer_class = op_serializers.SystemAssignmentDetailsSerializer
    