
from operation import models as op_models
from masters import models as master_models
from django.conf import settings

FILE_UPLOAD_PATHS = settings.FILE_UPLOAD_PATHS
class FilePathManager():
    def get_file_path_to_upload_health_test_report(instance, filename):

            # Generate the dynamic path based on the instance and filename
    # For example, you can use the instance's ID and the original filename

        path=''
        # emp_health_profile_test = []
        # if instance:

        #     emp_health_profile_test = op_models.EmpHealthProfileTest.objects.filter(id = instance.emp_health_profile_test.id).last()
           
        # medical_test_session = []
        # path=FILE_UPLOAD_PATHS['report']
        # if emp_health_profile_test:
        #     medical_test_session= conf_models.MedicalTestSession.objects.filter(id=emp_health_profile_test.medical_test_session.id).last()
        #     if medical_test_session:
        #         path= path + f'{medical_test_session.year}/{medical_test_session.session.replace(" ","_")}'

        # path= path + f'{filename}'
       
        return  path
