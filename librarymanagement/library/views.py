from django.shortcuts import render, get_object_or_404
from . import forms,models
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News
from .forms import NewsForm
from django.urls import reverse
from .models import Book


# Create your views here.
# views.py
from django.shortcuts import render
from .models import Blog, Book, News, LibraryDetails

def home_view(request):
    # Fetching blogs, books, news, and library details
    blogs = Blog.objects.all()
    print(blogs)  # Fetch all blogs
    books = Book.objects.all()  # If you're displaying books, fetch them as well
    news_items = News.objects.all().order_by('-created_at')[:4]  # Latest 4 news items
    details = LibraryDetails.objects.latest('id')  # Latest library details

    return render(request, 'index.html', {
        'blogs': blogs,
        'books': books,
        'news_items': news_items,
        'details': details
    })




    
def afterlogin_view(request):
        return render(request,'adminafterlogin.html')



def book_view(request):
    return render(request,'book.html')

def addbook_view(request):
    form = forms.BookForm()
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)  # Include request.FILES to handle image upload
        if form.is_valid():
            book = form.save()  # Save the book and capture the instance
            messages.success(request, 'Book added successfully!')  # Add success message
            return redirect('/viewbook')  # Redirect to the viewbook page
    return render(request, 'addbook.html', {'form': form})

def viewbook_view(request):
    books=models.Book.objects.all()
    print(books)
    return render(request,'viewbook.html',{'books':books})


def update_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = forms.BookForm(instance=book)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect(reverse('viewbook'))
    return render(request, 'updatebook.html', {'form': form, 'book': book})

def delete_book_view(request,pk):
    services = models.Book.objects.get(id=pk)
    services.delete()
    return redirect('viewbook')

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_news')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

def view_news(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'view_news.html', {'news_items': news_items})

def news_view(request):
    return render(request,'news.html')


def update_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('view_news')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'add_news.html', {'form': form})

# Delete a news item
def delete_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_item.delete()
        return redirect('view_news')
    return render(request, 'delete_news.html', {'news_item': news_item})


from .models import LibraryDetails
from .forms import LibraryDetailsForm

def library_details(request):
    return render(request,'librarydetails.html')


def add_library_details(request):
    if request.method == 'POST':
        form = LibraryDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_library_details')
    else:
        form = LibraryDetailsForm()
    return render(request, 'add_library_details.html', {'form': form})

def view_library_details(request):
    details = LibraryDetails.objects.latest('id')  # Fetch the latest entry
    return render(request, 'view_library_details.html', {'details': details})




from .forms import UserForm

def user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
        else:
            print(form.errors)  # This will print the errors in the terminal/console
    else:
        form = UserForm()

    return render(request, 'user.html', {'form': form})

from . models import userdetails
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = userdetails.objects.get(username=username)

            if user.password == password:  # In a real-world scenario, use password hashing!
                request.session['user_id'] = user.id  # Store user ID in the session
                messages.success(request, f"Welcome, {username}!")
                return redirect('userdashboard')  
            else:
                messages.error(request, "Incorrect password.")
        except userdetails.DoesNotExist:
            messages.error(request, "Username does not exist.")

    return render(request, 'userlogin.html') 


def userdashboard(request):
    return render(request, 'userdashboard.html')


from .forms import BlogForm

def blog_create(request):
    if request.method == 'POST':  # If the form has been submitted
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            form.save()  # Save the new blog post to the database
            return redirect('userdashboard')  # Redirect to the blog list after saving the blog
    else:
        form = BlogForm()  # Display the empty form when the page is first loaded

    return render(request, 'blog_form.html', {'form': form})

def viewblog_view(request):
    blogs=models.Blog.objects.all()
    print(blogs)
    return render(request,'index.html',{'blogs':blogs})
