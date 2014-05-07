#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User


def inicio(request):
	return render_to_response('inicio.html')

def nissan(request):
	return render_to_response('nissan.html')

def aston(request):
	return render_to_response('aston.html')

def ferrari(request):
	return render_to_response('ferrari.html')

def acercade(request):
	return render_to_response('acercade.html')

def contacto(request):
	return render_to_response('contacto.html')

