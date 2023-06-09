from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.views import generic
from .models import Post,Tools,full_post
from django.shortcuts import get_object_or_404
import numpy as np
from django.http import HttpResponse
from .forms import PostForm,PostForm_tinymce
from .models import User,jobs , Projects
from .models import Profile as model_profile



def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    a = jobs.objects.all()
    print(a)
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # form.save()


            obj =form.save()
            
            form.save()

            b =model_profile.objects.all().last()
            b.job_position_id =int(request.POST['job_position'])
            b.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def tools(request):
    queryset = Tools.objects.filter(status=1).order_by('-title').reverse()
    print('queryset',queryset)
    print('show tools page')
    
    return render(request, 'users/tools_new.html',{'tools':queryset})


@login_required
def full_create_post_tiny(request):
    if request.method == 'POST':
        form = PostForm_tinymce(request.POST)
        if form.is_valid():
            obj =form.save(commit=False)
            obj.author = User.objects.get(pk=request.user.id)
            form.save()
            messages.success(request,'New Forum Successfully Added')
            return redirect(to='/profile')
        
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'users/create_post.html',{'form':form})
        
    else:
        form = PostForm_tinymce()
        context = {
            'form':form
        }
        return render(request, 'users/create_post.html',context)


@login_required
def my_posts(request):
    post_list = full_post.objects.filter(author = request.user.id)
    return render(request, 'users/user_post_list_quil.html', {'posts': post_list})


@login_required
def post_edit_quil(request,id):
    post = get_object_or_404(full_post,id=id)

    if request.method == 'GET':

        context = {'form': PostForm_tinymce(instance=post), 'id': id}
        return render(request,'users/create_post.html',context)

   
    elif request.method == 'POST':
        form = PostForm_tinymce(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('/profile/my_posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'posts/post_form.html',{'form':form})
        

def post_list_quil(request):
    post_list = full_post.objects.all()
    return render(request, 'users/post_list_quil.html', {'posts': post_list})

def post_view_quil(request,slug):
    post_view = full_post.objects.filter(slug=slug)
    return render(request, 'users/post_view.html', {'post': post_view})


def projects_list(request):
    queryset = Projects.objects.all()
    return render(request, 'users/projects_list.html',{'projects':queryset})


def project_view(request,id):
    # print('asd'*50,id)
    post_view = Projects.objects.filter(id = id)[0]
    return render(request, 'users/project_view.html',{'project':post_view})




###############################################################
#####################   SPHINIX   #############################
###############################################################


from django.conf import settings
DOCS_BASE_PATH = getattr(settings, 'DOCS_BASE_PATH', None)
DOCS_ROOT = getattr(settings, 'DOCS_ROOT', None)

from django.views.generic import RedirectView
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.views.static import serve
import os
from django.template import loader


def sphinix_view(request):
    template = loader.get_template('users/sphinix_list.html')
    modules = os.listdir(DOCS_BASE_PATH)
    context = {
        'modules': modules,
    }
    return HttpResponse(template.render(context, request))


def serve_docs(request, type, path, **kwargs):
    doc_path = DOCS_ROOT.format(type)
    if 'document_root' not in kwargs:
        kwargs['document_root'] = doc_path
    
    return serve(request, path, **kwargs)


class DocsRootView(RedirectView):
    def get_redirect_url(self, **kwargs):
        view_name = ':'.join(filter(None, [self.request.resolver_match.namespace, 'docs_files']))
        print('view_name'*50,view_name)
        ret = reverse(view_name, kwargs={'type': kwargs['type'], 'path': 'index.html'})
        print(ret)
        return ret
    

###############################################################
###############################################################
###############################################################
