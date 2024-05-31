from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Profile,Post_quill,jobs,SnappFoodList,cities
from django import forms
from .models import QuillPost , full_post , raw_material , mother_material
from django import forms
from django_quill.forms import QuillFormField


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    jobs_list = jobs.objects.values_list('id','name')
    # print(a)
    job_position = forms.ChoiceField(choices=jobs_list,required=True,
                                     widget=forms.Select(attrs={'class':'form-control'}))


    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','job_position']






class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    job_position = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    class Meta:
        model = Profile
        fields = ['avatar', 'bio','job_position']




class QuillFieldForm(forms.Form):
    content = QuillFormField()



class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'content',
        )




class PostForm(forms.ModelForm):
   class Meta:
      model = Post_quill
      fields = ['slug','title', 'body','author']




class full_PostForm(forms.ModelForm):
   class Meta:
      model = Post_quill
      fields = ['slug','title', 'body','author']


from django import forms
# from django.contrib.flatpages.models import FlatPage
# from tinymce.widgets import TinyMCE

from django.forms import ModelForm, TextInput, EmailInput , CharField ,SlugField

class PostForm_tinymce(forms.ModelForm):
    class Meta:
        model = full_post
        fields = ['slug','title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'title'
                }),
            'slug': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Url'
                }),
            # 'author':forms.HiddenInput(),
        }


        
class PostForm_add_material(forms.ModelForm):
    choice = mother_material.objects.values_list('id', 'name')
    job_position = forms.ChoiceField(choices=choice, required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = raw_material
        fields = ['name', 'describe', 'unit', 'job_position']  # Include 'name' field here

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Material name'
            }),
            'describe': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'describe'
            }),
            'unit': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'unit'
            }),
        }



class PostFormAddMotherMaterial(forms.ModelForm):

    class Meta:
        model = mother_material
        fields = ['name','describe']



        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Material name'
                }),
            'describe': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'describe'
                }),

        }


class PostFormAddRestaurant(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=cities.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='name'
    )

    class Meta:
        model = SnappFoodList
        fields = ['name', 'link', 'city']  # Include 'name', 'link', and 'city' fields here

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Restaurant name'
            }),
            'link': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Link'
            }),
            'city': forms.Select(attrs={
                'class': "form-control",
            }),
        }

    def save(self, commit=True):
        instance = super(PostFormAddRestaurant, self).save(commit=False)
        if commit:
            instance.save()
        return instance