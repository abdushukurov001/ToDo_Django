from django import forms
from .models import UserModel



class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=16)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=6,  max_length=16)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data.pop('confirm_password'):
            raise forms.ValidationError('Password do not match')
        


class ProfileEditForm(forms.ModelForm):

     class Meta:
         model = UserModel
         fields = [ 'username', 'first_name', 'last_name', 'email', 'birth_date', 'profile_pic']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ('username',  'first_name', 'last_name', 'email', 'password', 'confirm_password')
     
    def clean_confirm_password(self):
        print(self.cleaned_data, "work")
        if self.cleaned_data['password'] != self.cleaned_data.pop('confirm_password'):
            raise forms.ValidationError('Passwords do not match')

    def clean_email(self):
        print(self.cleaned_data)
        print(self.cleaned_data['email'])
        if not self.cleaned_data['email'].split("@")[1] in ["gmail.com", "mail.ru"]:
           raise forms.ValidationError("Email must contain 'gmail.com' or 'mail.ru'. ")
