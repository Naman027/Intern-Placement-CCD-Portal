from django.shortcuts import render
from .models import company,remarks
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def session_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('main_page'))

def getPlacement(request):
    print("Entered in getPlacement")
    list = company.objects.filter(placement=True)
    if request.POST:
        print("CHECK1")
        print('post', request.POST)
        if request.user.is_authenticated:
            return getmainpage(request)
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print('{} {}'.format(username, password))
        user = authenticate(username=username, password=password)
        if user and user.first_name=="PLACEMENT":
            print("CHECK2")
            if user.is_active:
                print("CHECK3")
                login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
            else:
                print("CHECK4")
                messages.error(request, 'Invalid Details')
                form = forms.authentication()
                return render(request, 'diary/Auth.html', {'form': form})
        else:
            print("CHECK5")
            messages.error(request, 'Invalid Details')
            form = forms.authentication()
            return render(request, 'diary/Auth.html', {'form': form})
    else:
        print("CHECK6")
        form = forms.authentication()
        return render(request, 'diary/Auth.html', {'form': form})


def getIntern(request):
    list = company.objects.filter(placement=False)
    if request.POST:
        print("CHECK1")
        print('post', request.POST)
        if request.user.is_authenticated:
            return getmainpage(request)
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print('{} {}'.format(username, password))
        user = authenticate(username=username, password=password)
        if user and user.first_name=="INTERN":
            print("CHECK2")
            if user.is_active:
                print("CHECK3")
                login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
            else:
                print("CHECK4")
                messages.error(request, 'Invalid Details')
                form = forms.authentication()
                return render(request, 'diary/Auth.html', {'form': form})
        else:
            print("CHECK5")
            messages.error(request, 'Invalid Details')
            form = forms.authentication()
            return render(request, 'diary/Auth.html', {'form': form})
    else:
        print("CHECK6")
        form = forms.authentication()
        return render(request, 'diary/Auth.html', {'form': form})

def placement_edit(request,cpk):
    c = company.objects.get(pk=cpk)
    final1 = []
    final1.append(c)
    return render(request, 'diary/edit_company.html', {'company': final1})

def getmainpage(request):
    if request.user.is_authenticated:
        print("Authenticated")
        print('{} {}',request.user.username)
        if request.user.first_name=="INTERN":
            return render(request, 'diary/intern_base.html')
        if request.user.first_name=="PLACEMENT":
            return render(request, 'diary/placement_base.html')
    else:
        print("Not Authenticated")
        return render(request,'diary/placement_or_intern.html')


def getremarks(request,pk):
    c = company.objects.get(pk=pk)
    remark = remarks.objects.filter(company=c).order_by('datetime').reverse()
    return render(request,'diary/company_remarks.html',{'remark':remark})


def save_changes_view(request,pk):
    c = company.objects.get(pk=pk)
    if request.method=='POST':
        form = forms.save_changes(request.POST)
        if form.is_valid():
            poc = form.cleaned_data['POC']
            cpoc = form.cleaned_data['CPOC']
            remark = form.cleaned_data['Remark']
            c.CPOC = cpoc
            c.POC  = poc
            c.TopRemark = remark
            c.save()
            print(poc+" "+cpoc+" "+remark)
            remarks(company=c,remark=remark,CPOC=cpoc).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.save_changes()
        return render(request,'diary/edit_company.html',{'form':form,'c':c})


def add_placement_company(request):
    if request.method=='POST':
        form = forms.add_company(request.POST)
        if form.is_valid():
            c = company()
            c.CompanyName = form.cleaned_data['CompanyName']
            c.POC = form.cleaned_data['POC']
            c.CPOC = form.cleaned_data['CPOC']
            c.placement = True
            c.TopRemark = form.cleaned_data['Remark']
            c.save()
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC,POC=c.POC).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.add_company()
        return render(request,'diary/add_company.html',{'form':form})

def add_intern_company(request):
    if request.method=='POST':
        form = forms.add_company(request.POST)
        if form.is_valid():
            c = company()
            c.CompanyName = form.cleaned_data['CompanyName']
            c.POC = form.cleaned_data['POC']
            c.CPOC = form.cleaned_data['CPOC']
            c.placement = False
            c.TopRemark = form.cleaned_data['Remark']
            c.save()
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC,POC=c.POC).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.add_company()
        return render(request,'diary/add_company.html',{'form':form})

def searchPlacement(request):
    print('I m Here')
    if request.method == 'POST':
        print("success")
        search_text = request.POST['search_text1']
        all_company =(company.objects.filter(CompanyName__contains=search_text)|company.objects.filter(POC__contains=search_text))
        temp = all_company
        for c in all_company:
            if c.placement == False:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results1.html', {'all_company': temp})
    else:
        print("fail")
        search_text = ''
        all_company = company.objects.all()
        temp = all_company
        for c in all_company:
            if c.placement == False:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results1.html', {'all_company': temp})


def searchIntern(request):
    print('I m Here')
    if request.method == 'POST':
        print("success")
        search_text = request.POST['search_text2']
        all_company = (company.objects.filter(CompanyName__contains=search_text) | company.objects.filter(POC__contains=search_text))
        temp = all_company
        for c in all_company:
            if c.placement == True:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results2.html', {'all_company': temp})
    else:
        print("fail")
        search_text = ''
        all_company = company.objects.all()
        temp = all_company
        for c in all_company:
            if c.placement == True:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results2.html', {'all_company': temp})



def change_password(request):
	if request.user.is_authenticated:
	    if request.method == 'POST':
	        form = PasswordChangeForm(request.user, request.POST)
	        if form.is_valid():
	            user = form.save()
	            messages.success(request, 'Your password was successfully updated!')
	            return HttpResponseRedirect(reverse('main_page'))
	        else:
	            messages.error(request, 'Please correct the error below.')
	    else:
	        form = PasswordChangeForm(request.user)
	        return render(request, 'diary/edit_ID.html', {
	        'form': form
	    })
	return HttpResponseRedirect(reverse('main_page'))