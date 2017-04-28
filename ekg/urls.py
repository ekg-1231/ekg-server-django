from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^RegisterPatient$', views.register_patient, name='register_patient'),
    url(r'^RegisterDoctor$', views.register_doctor, name='register_doctor'),
    url(r'^UploadHistory$', views.upload_history, name='upload_history'),
    url(r'^LookHistory$', views.look_history, name='look_history'),
    url(r'^GetDoctorData$', views.get_doctor_data, name='get_doctor_data'),
    url(r'^GetHospitalData$', views.get_hospital_data, name='get_hospital_data'),
    url(r'^GetUnverifiedHistory$', views.get_unverified_history, name='get_doctor_data'),
    url(r'^VerifyHistory$', views.verify_history, name='verify_history'),
    url(r'^RegisterHospital$', views.register_hospital, name='register_hospital'),
    url(r'^RegisterAffiliation$', views.register_affiliation, name='register_affiliation'),
    url(r'^GetDoctorAffiliation$', views.get_doctor_affiliation, name='get_doctor_affiliation'),
]