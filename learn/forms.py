from django import forms
from .models import CourseLearn

class AddLearn(forms.ModelForm):
    class Meta:
        model=CourseLearn
        fields='__all__'
        labels={'title':'Title','CourseImage':'Course Image','description':'Description','web_link_learn':'Web tutorial','video_learn':'Video (Link)','scription_learn':'Scription (link)'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'CourseImage':forms.FileInput(attrs={'class':'form-control'}),'description':forms.Textarea(attrs={'class':'form-control'}),'web_link_learn':forms.URLInput(attrs={'class':'form-control'}),'doc_link_learn':forms.URLInput(attrs={'class':'form-control'}),'video_learn':forms.URLInput(attrs={'class':'form-control'}),'scription_learn':forms.URLInput(attrs={'class':'form-control'})}