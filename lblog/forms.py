
from django import forms
from .models import Post,Category,Comment


# choices=[('coding','coding'),('sports','sports'),('entertainment','entertainment'),]
choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)
# Creation of custom add post form
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','header_image','snippet')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag'}),
            'author': forms.TextInput(attrs={'class':'form-control','id':'elder','value':'','type':'hidden'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':'choices'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter post text'}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Home snippet text'}),
        }

# Creation of Update form

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','category','body','header_image','snippet')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title tag'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':'choices'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter post text'}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Home snippet text'}),
        }

# Add Comment Form
class AddCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Comment '}),
        }
