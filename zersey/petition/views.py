from django.shortcuts import render,redirect,render_to_response
from .models import Petition_info,User
import os
# Create your views here.
def create(request):
	return render(request,'creator.html',{'UserEmail':'Anonymous'})
def handle_uploaded_file(f,n):
    destination = open(os.path.dirname(os.path.dirname(__file__))+'/static/images/uploads/P'+str(n)+'.jpg','wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    return

def first_page(request):
	arry1 = [100,500,20]	
	x=[]
	ximg=[]
	petition = Petition_info.objects.all()
	print petition
	for i in petition:
		x.append(str(i.title))

	return render_to_response('first_page.html',{'array1': x,'UserEmail':'Anonymous'})

def save_create(request):
	print "hEAA"
	if request.method == 'POST':
		s1=Petition_info()
		s1.title=request.POST['title']
		s1.to_whom=request.POST['to_whom']
		s1.what_is=request.POST['what_is']
		s1.desc=request.POST['desc']
		s1.signers=0
		f = open('Petition_num.txt','r')
        n = f.readline().strip('\n')
        f.close()
        f = open('Petition_num.txt','w')
        lol = int(n) + 1
        f.write(str(lol))
        f.close()
        s1.num=n
        s1.users=""
        print request.FILES
        if('img' in request.FILES):
        	print(request.FILES['img'].size)
        	img_size=request.FILES['img'].size/1024
        	if(img_size<=1024): # for 50 kb
        		s1.img= request.FILES['img']
        		handle_uploaded_file(s1.img,n)

		#S1.imgd
		s1.save()
		print s1
		print s1
		return redirect('/petition/'+str())
	return redirect('/')

def open_petition(request,num1):
	print "the num is " + num1
	petition = Petition_info.objects.get(num=num1)
	return render(request,'open_petition.html',{'num':num1,'signers':petition.signers,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg','UserEmail':'Anonymous'})

def sign_petition(request,num1):
	print 'hi'
	if request.method=='POST':
		petition = Petition_info.objects.get(num=num1)

		petition.signers=petition.signers+1
		print request.POST['userEmail']
		user=User.objects.get(email=request.POST['userEmail'])
		x=petition.users
		print x
		y=[int(i) for i in x[1:].split(',')]
		if(user.usernum in y):
			return render(request,'open_petition.html',{'UserEmail':request.POST['userEmail'],'printer':"signeduser();",'signers':petition.signers-1,'num':num1,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg'})
		petition.users=petition.users+','+str(user.usernum)

		petition.save()
		print 'hello'
	return redirect('/')

def create_user(request):
	print "hi"
	if request.method=='GET':
		return redirect('/')	
	if request.method=='POST':
		print "hello"
		num1=request.POST['num2']
		petition = Petition_info.objects.get(num=num1)
		sign_num=petition.signers
		email1=request.POST['user_email']
		password1=request.POST['user_pass']
		f = open('User_num.txt','r')
        n = f.readline().strip('\n')
        f.close()
        f = open('User_num.txt','w')
        lol = int(n) + 1
        f.write(str(lol))
        f.close()
        num_results = (User.objects.filter(email = email1)).count()
        print num_results
        if(num_results>0):
        	return render(request,'open_petition.html',{'UserEmail':'Anonymous','printer':"alertgive();",'signers':sign_num,'num':num1,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg'})
        s1=User(usernum=n,email=email1,password=password1)
        s1.save()
        return render(request,'open_petition.html',{'UserEmail':email1,'num':num1,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg','signers':sign_num})
	return redirect('/')

def check(request):
	if request.method=='POST':
		num1=request.POST['num1']
		petition = Petition_info.objects.get(num=num1)
		email1=request.POST['email']
		password1=request.POST['pass']
		sign_num=petition.signers
		user = User.objects.filter(email = email1)
		print user
		if(user.count()>0 and user[0].password==password1):
			return render(request,'open_petition.html',{'UserEmail':email1,'signers':sign_num,'num':num1,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg'})
		else:
			return render(request,'open_petition.html',{'UserEmail':'Anonymous','printer':"invalidpass();",'signers':sign_num,'num':num1,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg'})

	return render(request,'open_petition.html',{'UserEmail':'Anonymous','num':num1,'signers':sign_num,'title':petition.title,'to_whom':petition.to_whom,'what_is':petition.what_is,'desc':petition.desc,'img_src':'/static/images/uploads/P'+num1+'.jpg'})
		
