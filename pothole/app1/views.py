from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http.response import StreamingHttpResponse
from pothole.pothole_detection.camera_video import *
# Create your views here.

def firstpage(request):
    return render (request,'first.html')

def streampage(request):
    return render (request,'stream.html')

def start(request):
    return redirect('stream')

def stop(request):
    global b
    del b
    return redirect('first')

def gen(camera1):
	while True:
		frame = camera1.camera_gen()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    global b
    b=camera()
    return StreamingHttpResponse(gen(b),content_type='multipart/x-mixed-replace; boundary=frame')