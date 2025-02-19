from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image']

        # You can customize form widgets if needed, for example:
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book name'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


from .models import LibraryDetails

class LibraryDetailsForm(forms.ModelForm):
    class Meta:
        model = LibraryDetails
        fields = ['total_books', 'operating_hours', 'membership_info', 'policies']
        widgets = {
            'total_books': forms.NumberInput(attrs={'class': 'form-control'}),
            'operating_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'membership_info': forms.Textarea(attrs={'class': 'form-control'}),
            'policies': forms.Textarea(attrs={'class': 'form-control'}),
        }


from.models import userdetails
class UserForm(forms.ModelForm):
    class Meta:
        model=userdetails
        fields='__all__'
# blog/forms.py
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'message', 'image']  # Fields to include in the form

   

