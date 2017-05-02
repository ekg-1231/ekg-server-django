# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Patient

# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome to E-Cardio Server</h1>')

def register_patient(request):
	id_patient = request.GET.get('id')
	p_password = request.GET.get('password')
	p_name = request.GET.get('name')
	p_phone = request.GET.get('phone')
	p_email = request.GET.get('email')
	p_address = request.GET.get('address')
	print id_patient,p_name,p_password,p_phone,p_email,p_address
	patient = Patient(password=p_password, name=p_name, phone=p_phone, email=p_email, address=p_address)
	patient.save()
	return HttpResponse('berhasil')

def register_doctor(request):
	id_doctor = request.GET.get('id_doctor')
	password = request.GET.get('password')
	name = request.GET.get('name')
	phone = request.GET.get('phone')
	email = request.GET.get('email')
	address = request.GET.get('address')
	doctor = Doctor(id_doctor, password, name, phone, email, address)
	doctor.save()
	return HttpResponse('berhasil')

def upload_history(request):
	id = request.POST.get('id')
	id_patient = request.POST.get('id_patient')
	pass_patient = request.POST.get('pass_patient')
	ndata = request.POST.get('data')
	history = History(id = id_patient, data = ndata)
	return HttpResponse('berhasil')

def look_history(request):
	print '/look_history: '
	look_id = request.GET.get('id')
	print id
	try:
		history = History.objects.get(id=look_id)
	except model.DoesNotExist:
		history = None
	if(history != None):
		print 'History ditemukan'
		return HttpResponse(history.data)
	else:
		print 'Data history tidak ada dalam database'
		return HttpResponse('Data history tidak ada dalam database')

def get_doctor_data(request):
	print '/get_doctor_data: '
	doctor_id = request.GET.get('id_doctor')
	id_patient = request.GET.get('id_patient')
	pass_patient = request.GET.get('pass_patient')
	patient = None
	try:
		patient = Patient.objects.get(id=id_patient)
	except Exception as e:
		pass
	if(pass_patient == None or patient == None or (patient.password != pass_patient)):
		return HttpResponse('Akun tidak valid\nSilakan gunakan akun yang valid')
	doctor = None
	try:
		doctor = Doctor.objects.get(id=doctor_id)
	except Exception as e:
		print 'Data dokter tidak ada dalam database'
		return HttpResponse('Data dokter tidak ada dalam database')
	else:
		print 'berhasil'
		return HttpResponse('' + doctor.id + '\n' + doctor.name + '\n' + doctor.email +'\n' + doctor.address)

def get_hospital_data(request):
	print '/get_hospital_data: '
	id_hospital = request.GET.get('id_hospital')
	id_patient = request.GET.get('id_patient')
	pass_patient = request.GET.get('pass_patient')
	patient = None
	try:
		patient = Patient.objects.get(id=id_patient)
	except Exception as e:
		pass
	if(pass_patient == None or patient == None):
		return HttpResponse('Akun tidak valid\nSilakan gunakan akun yang valid')
	if(patient.password != pass_patient):
		return HttpResponse('Password salah')
	hospital = None
	try:
		hospital = Hospital.objects.get(id=hospital_id)
	except Exception as e:
		print 'Data rumah sakit tidak ada dalam database'
		return HttpResponse('Data rumah sakit tidak ada dalam database')
	else:
		print 'berhasil'
		return HttpResponse('' + '\n' + hospital.id + '\n' + hospital.name + '\n' + hospital.email + '\n' + hospital.address)

def get_unverified_history(request):
	doctor_id = request.GET.get('id_doctor')
	doctor_pass = request.GET.get('pass_doctor')
	number = request.GET.get('number')
	history = None
	try:
		history = History.objects.get(id=number)
	except Exception as e:
		print 'Data history tidak ada'
		return HttpResponse('Data history tidak ada')
	else:
		print 'Data history ditemukan'
		return HttpResponse(history)

def verify_history(request):
	doctor_id = request.GET.get('id_doctor')
	doctor_pass = request.GET.get('pass_doctor')
	id_history = request.GET.get('id')
	message = request.GET.get('message')
	hos_suggested = request.GET.get('hos_suggested')
	is_dataset = request.GET.get('is_dataset')
	tclass = request.GET.get('class')

	history = None
	try:
		history = History.objects.get(id=id_history)
	except Exception as e:
		print 'History tidak ditemukan'
		return HttpResponse('History tidak ditemukan')
	else:
		history.message = message
		history.suggestion = hos_suggested
		history.verifier = doctor_id
		history.dataset_is_dataset = is_dataset
		history.dataset_class = tclass
		history.save()
		return HttpResponse('berhasil')

def register_hospital(request):
	name = request.GET.get('name')
	phone = request.GET.get('phone')
	address = request.GET.get('address')
	id_doctor = request.GET.get('id_doctor')
	pass_doctor = request.GET.get('pass_doctor')
	doctor = None
	try:
		doctor = Doctor.objects.get(id=id_doctor)
	except Exception as e:
		return HttpResponse('Dokter tidak ditemukan')
	else:
		if(pass_doctor != doctor.password):
			return HttpResponse('Otentikasi gagal, password salah')
		hospital = Hospital()
		hospital.name = name
		hospital.phone = phone
		hospital.address = address
		hospital.save()
		return HttpResponse('berhasil')

def register_affiliation(request):
	id_doctor = request.GET.get('id_doctor')
	pass_doctor = request.GET.get('pass_doctor')
	id_hospital = request.GET.get('id_hospital')
	doctor = None
	patient = None

	try:
		doctor = Doctor.objects.get(id=id_doctor)
		hospital = Hospital.objects.get(id=id_hospital)
	except Exception as e:
		return HttpResponse('Dokter atau rumah sakit tidak ditemukan')
	else:
		if(pass_doctor != doctor.password):
			return HttpResponse('Password salah')
		affiliation = Affiliation()
		affiliation.id_doctor = id_doctor
		affiliation.id_hospital = id_hospital
		affiliation.save()
		return HttpResponse('berhasil')

def get_doctor_affiliation(request):
	id_patient = request.GET.get('id_patient')
	pass_patient = request.GET.get('pass_patient')
	id_doctor = request.GET.get('id_doctor')
	patient = None
	affiliation = None

	try:
		patient = Patient.objects.get(id=id_patient)
		affiliation = Affiliation.objects.get(id_doctor=id_doctor)
	except Exception as e:
		return HttpResponse('Dokter atau pasien tidak ditemukan')
	else:
		if(pass_patient != patient.password):
			return HttpResponse('Password salah')
		return HttpResponse('' + affiliation.id_doctor + '\n' + affiliation.id_hospital)

def get_all_patients(request):
	patients = Patient.objects.all()
	response = HttpResponse()
	for i in patients:
		print i.name,i.address
		response.write(i.name + ' ' + i.address + '\n')
	return response