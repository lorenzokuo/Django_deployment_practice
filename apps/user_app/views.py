from django.shortcuts import render, redirect, HttpResponse
from .models import Job, Granted
from ..login_app.models import User
from django.db.models import Count
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count

def home(request):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:

        all_jobs = Job.objects.all().order_by('-created_at')
        all_granteds = Granted.objects.filter(user_id = request.session['user_id']).order_by('-created_at')

        my_granted_jobs =[]
        granteds_list =[]
        for granted in all_granteds:
            granteds_list.append(granted.job.id)
            my_granted_jobs.append(granted.job)

        context = {
            'all_jobs': all_jobs,
            'granteds_list': granteds_list,
            'my_granted_jobs': my_granted_jobs,
            # 'all_granteds': all_granteds
        }
        return render(request, 'user_app/home.html', context)

def add(request):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        location = request.POST.get('location')
        this_user = User.objects.get(id=request.session['user_id'])

        cate1 = request.POST.get("cate1")
        cate2 = request.POST.get("cate2")
        cate3 = request.POST.get("cate3")
        cate4 = request.POST.get("cate4")

        if len(title)<1 or len(desc)<1 or len(location)<1:
            messages.warning(request, 'no blanks!')
            return redirect('userspace:add')
        elif len(title)<3:
            messages.warning(request, 'title must be at least 3 characters')
            return redirect('userspace:add')
        elif len(desc)<5:
            messages.warning(request, 'description must be at least 5 characters')
            return redirect('userspace:add')
        elif len(location)<3:
            messages.warning(request, 'location must be at least 3 characters')
            return redirect('userspace:add')
        else:

            Job.objects.create(title = title, desc = desc, location = location, posted_by=this_user, cate1 = cate1, cate2 = cate2, cate3 = cate3, cate4 = cate4)

            return redirect(reverse('userspace:home'))
    return render(request, 'user_app/add.html')

def destroy(request, id):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:
        Job.objects.get(id=id).delete()
        return redirect(reverse('userspace:home'))

def add_to_granteds(request, job_id):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:
        this_user = User.objects.get(id=request.session['user_id'])
        this_job = Job.objects.get(id=job_id)

        Granted.objects.create(user=this_user, job=this_job)
        messages.success(request, 'Job has been assigned!')
        return redirect(reverse('userspace:home'))

def remove_granteds(request,job_id):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:
        user_id = request.session['user_id']
        this_job = Job.objects.get(id=job_id)
        this_user = User.objects.get(id=request.session['user_id'])

        this_granted = Granted.objects.filter(user=user_id,job=job_id)
        this_granted.delete()

        messages.success(request, 'Job removed from your jobs')

        return redirect(reverse('userspace:home'))

def show(request, job_id):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:
        jobs = Job.objects.filter(id = job_id)

        context = {
            'jobs': jobs,
            }

        return render(request, 'user_app/show.html', context)

def edit(request, job_id):
    if not 'first_name' in request.session:
        return redirect('loginspace:index')
    else:
        context={
            'jobs': Job.objects.get(id=job_id)
        }

        return render(request, 'user_app/edit.html', context)

def update(request):
    job = Job.objects.get(id=request.POST['id'])
    job.title = request.POST['title']
    job.desc = request.POST['desc']
    if len(job.title)<1 or len(job.desc)<1 or len(job.location)<1:
        messages.warning(request, 'No blanks!')
        return redirect(reverse('userspace:edit', kwargs = {"job_id" : request.POST['id']}))
    elif len(job.title)<3:
        messages.warning(request, 'title must be at least 3 characters')
        return redirect(reverse('userspace:edit', kwargs = {"job_id" : request.POST['id']}))
    elif len(job.desc)<5:
        messages.warning(request, 'description must be at least 5 characters')
        return redirect(reverse('userspace:edit', kwargs = {"job_id" : request.POST['id']}))
    elif len(job.location)<3:
        messages.warning(request, 'location must be at least 3 characters')
        return redirect(reverse('userspace:edit', kwargs = {"job_id" : request.POST['id']}))
    job.save()
    return redirect(reverse('userspace:home'))