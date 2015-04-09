from django.shortcuts import render, redirect, get_object_or_404

from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from gear.models import Gear
from member.models import Member, Organization, OrganizationQueue

from django.contrib.auth.decorators import login_required

def login_manager(request):
    username = request.POST['username']
    password = request.POST['password']
    next = request.POST['next']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request,'You logged in with success!')
            try: 
                return redirect(next)
            except:
                return redirect(reverse('home'))
        else:
            messages.error(request,'Your account is disabled.')
            try: 
                return redirect(next)
            except:
               return redirect(reverse('home'))
    else:
        messages.error(request,'Your username or password is incorrect.')
        try: 
            return redirect(next)
        except:
            return redirect(reverse('home'))


def logout_manager(request):
    logout(request)
    messages.success(request,'You logged out with success!')
    return redirect(reverse('home'))

        
def register(request):
    pass

def home(request):
    pass

def show_member(request,user_pk):
    member = get_object_or_404(Member, pk=user_pk)
    gears = Gear.objects.all()
    context = {'member': member, 'gears':gears}
    return render(request, 'member/show_member.html', context)

@login_required
def add_gear(request):
    gear_pk = request.POST['gear_pk']
    member = get_object_or_404(Member, pk=request.user.pk)
    member.gears.add(get_object_or_404(Gear, pk=gear_pk))
    messages.success(request,'Gear added')
    return redirect(reverse('show_member', args=[request.user.pk]))

@login_required
def add_organization(request):
    organization_pk = request.POST['organization_pk']
    is_answer = request.POST['is_answer']
    member_pk = request.user.pk

    organization = get_object_or_404(Organization, pk=organization_pk)
    member = get_object_or_404(Member, pk=member_pk)

    is_in_queue = (len(OrganizationQueue.objects.filter(member_id=member_pk,organization_id=organization_pk)) > 0)


    if organization.auto_accept or (is_answer & is_in_queue):
        if is_in_queue:
            OrganizationQueue.objects.filter(member_id=member_pk,organization_id=organization_pk).delete()
        member.organizations.add(organization)
        messages.success(request,'Organization added')
        return redirect(reverse('show_member', args=[member_pk]))

    else:
        ask_join_organization(organization,pk)
        messages.success(request,'You application has been sent.')
        return redirect(reverse('show_member', args=[member_pk]))

@login_required
def ask_join_organization(organization,member):
    organizationQueueEntry = OrganizationQueue(organization=organization,member=member)
    organizationQueueEntry.save()