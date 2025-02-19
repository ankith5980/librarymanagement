from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/')  # Requires Pillow library

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LibraryDetails(models.Model):
    total_books = models.IntegerField()
    operating_hours = models.CharField(max_length=100)
    membership_info = models.TextField()
    policies = models.TextField()

    def __str__(self):
        return f"Library Details (Books: {self.total_books})"

class userdetails(models.Model):
    username=models.CharField(max_length=20,null=False,default="username")
    password=models.CharField(max_length=20,null=False,default="password")
    phone=models.CharField(max_length=20,null=False)      
    address=models.CharField(max_length=20,null=False,default="address")
    location=models.CharField(max_length=20,null=False,default="location")  



class Blog(models.Model):
    title = models.CharField(max_length=200)  # The title of the blog
    message = models.TextField()  # The content/message of the blog
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image field
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the blog is created

    def __str__(self):
        return self.title


