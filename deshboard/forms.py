from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,SetPasswordForm,PasswordChangeForm
from django.core.exceptions import ValidationError  


# from .models import UserImg
class EditAdminProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), 'date_joined': forms.DateTimeInput(attrs={'class': 'form-control'}), 'last_login': forms.DateTimeInput(attrs={'class': 'form-control'})}
        # fields="__all__"

# profile form
class user_profile_change(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name',
                  'email', 'username']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), 'date_joined': forms.DateTimeInput(attrs={'class': 'form-control'}), 'last_login': forms.DateTimeInput(attrs={'class': 'form-control'})}


# user's create
class usersAdd(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', ]
        # labels = {'first_name': 'First Name', 'last_name': 'Last Name',
        #           'email': 'Email', 'username': 'User name'}
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), 'username': forms.TextInput(attrs={'class': 'form-control'})}
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
        if len(password1 and password2) < 8:
            raise ValidationError("please Enter more than 8 charactrics!")
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['first_name'],  
    #         self.cleaned_data['last_name'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user  


#user password change
class UserPassChangewithout(SetPasswordForm):
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password2=forms.CharField(label='Password Confirm', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    model=User
    fields='__all__'
    
#with the old password
class UserPassChangewithold(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password2=forms.CharField(label='Password Confirm', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    model=User
    fields='__all__'
    

#image update
# class Profile_img_Form(UserImg):
#     fields="__all__"    