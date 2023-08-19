from django import forms
from .models import BlogPost,CommentModel

#blogs Model
class BlogSh(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields='__all__'
        labels={'title':'Title','image':'Image','discription':'Discription','web_link':'Reference Link'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}), 'image':forms.FileInput(attrs={'class':'form-control'}),'discription':forms.Textarea(attrs={'class':'form-control'}),'web_link':forms.URLInput(attrs={'class':'form-control'}),'author':forms.Select(attrs={'class':'form-select'})}

#comments model 
class CommentFm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields='__all__'
        labels={'Umessage':'Message','uname':'Name','uemail':'Email'}
        widgets={'Umessage':forms.Textarea(attrs={'class':'form-control'}),'uname':forms.TextInput(attrs={'class':'form-control'}),'uemail':forms.EmailInput(attrs={'class':'form-control'})}