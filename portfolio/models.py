from django.db import models

# Create your models here.

class Brian(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

class Projects(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    language = models.CharField(max_length=60)
    owner = models.ForeignKey(Brian)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='post/', default='card')
    link = models.CharField(max_length=200,null=True)
