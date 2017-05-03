# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=64)
	date_of_birth = models.DateTimeField(auto_now_add=True)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	phone = models.CharField(max_length=16)
	email = models.CharField(max_length=128)
	address = models.TextField()

class Doctor(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=16)
	email = models.CharField(max_length=128)
	address = models.TextField()

class Hospital(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	name = models.CharField(max_length=80)
	phone = models.CharField(max_length=16)
	address = models.TextField()
	doctors = models.ManyToManyField(Doctor, through='Affiliation')

class Affiliation(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class History(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	dataset_is_dataset = models.BooleanField(default=False)
	dataset_class = models.CharField(null=True, max_length=40)
	message = models.TextField(default='', null=True)
	# data = models.BinaryField(null=False)
	data = models.TextField(null=False)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	suggestion = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)
	verifier = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
