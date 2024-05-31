from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

from django.db import models
from django_quill.fields import QuillField

from tinymce.models import HTMLField


class jobs(models.Model):
    name = models.CharField(max_length=200)
    persian_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3,unique=True)
    describe = models.CharField(max_length=800)
    level = models.IntegerField()

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-short_name']





# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    # job_position = models.CharField(max_length=400)
    job_position = models.ForeignKey(jobs, on_delete= models.CASCADE,related_name='job_position',default=1,blank=True,null=True)


    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print(reverse("blog/", kwargs={"slug": self.slug}))
        # asd
        return "blog/"+{"slug": self.slug}



class Tools(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
    


class FoodFilter(models.Model):


    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title




class QuillPost(models.Model):
    content = QuillField()


class Post_quill(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts_quil',default=1,blank=True,null=True)
    body = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    
    

    class Meta:
        ordering = ['-created_at']





class full_post(models.Model): 
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts_tinymce',default=1,blank=True,null=True)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created_at']

class cities(models.Model):

    name = models.CharField(max_length=200)
    persian_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3,unique=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-short_name']

class Projects(models.Model):
    name = models.CharField(max_length=200)
    persian_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10,unique=True)
    start_date = models.DateTimeField(null=False)
    project_maanger = models.ForeignKey(User, on_delete= models.CASCADE,related_name='project_manager',default=1,blank=True,null=True)
    city = models.ForeignKey(cities, on_delete= models.CASCADE,related_name='project_city',default=1,blank=True,null=False)
    describe = models.CharField(max_length=800)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-short_name']

from phonenumber_field.modelfields import PhoneNumberField

class PhoneBook(models.Model):
    
    first_name = models.CharField(max_length=200,null=False)
    last_name = models.CharField(max_length=200,null=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    description = models.CharField(max_length=3000,null=True,blank=True)
    project = models.ForeignKey(Projects, on_delete= models.CASCADE,related_name='project',default=1,blank=True,null=True)
    position = models.CharField(max_length=3000)

    def __str__(self):
        return str(self.first_name)
    
    class Meta:
        ordering = ['-first_name']




class mother_material(models.Model):


    name = models.CharField(max_length=200)
    describe = models.CharField(max_length=800)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-name']



class raw_material(models.Model):

    name = models.CharField(max_length=200)
    describe = models.CharField(max_length=800)
    unit = models.CharField(max_length=200)

    mother = models.ForeignKey(mother_material, on_delete= models.CASCADE,related_name='mother_material',blank=True,null=True)


    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-name']









class create_order(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_create_order',blank=True,null=True)
    content = HTMLField()


    

class SnappFoodList(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(cities, on_delete= models.CASCADE,related_name='city_name',blank=True,null=True)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=20000)


    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-name']
