from django import forms
from django.forms import ModelForm
from ask.models import Question, Tag, Answer, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as dj_authenticate

class ProfileForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your login", 'class':"form-control"}), label = 'Login', required=True)
    email    = forms.EmailField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your e-mail", 'class':"form-control"}),label = 'E-mail', required=True)
    nickname     = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your nickname", 'class':"form-control"}),label = 'Nickname', required=True) 
    Avatar = forms.ImageField(widget=forms.FileInput(attrs={'name':"avatar"}),label = u'avatar', required = False)
    password1 = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Password", 'class':"form-control"})
    )
    password2 = forms.CharField(
        label=u'Password Validation',
        widget=forms.PasswordInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Repeat password", 'class':"form-control"})
    )
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1)<8:
            raise forms.ValidationError(u'Too short password')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(u'Wrong couple of passwords')
        return password2

    def clean_login(self):
        username = self.cleaned_data.get('login')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError(u'This login is already used')
        return username

    def clean_nickname(self):
        nick = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname = nick).exists():
            raise forms.ValidationError(u'This nickname is already used')
        return nick

    def get_user(self):
        return self.user or None

class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your login", 'class':"form-control"}), label = 'Login', required=True)
    password1 = forms.CharField( label=u'Password', widget=forms.PasswordInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Password", 'class':"form-control"}) )

    def clean_password1(self):
        username = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password1')
        user = dj_authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

class ProfileEditForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your login", 'class':"form-control"}), label = 'Login', required=False)
    email    = forms.EmailField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your e-mail", 'class':"form-control"}),label = 'E-mail', required=False)
    nickname     = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Your nickname", 'class':"form-control"}),label = 'Nickname', required=False) 
  #  avatar_url = forms.CharField(widget=forms.TextInput(attrs={'aria-describedby':"basic-addon1" , 'placeholder':"Avarar_url", 'class':"form-control"}), label = 'Avatar_url', required=False)
    Avatar = forms.ImageField(widget=forms.FileInput(attrs={'name':"avatar"}),label = u'avatar', required = False)

    def clean_nickname(self):
        nick = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname = nick).exists():
            raise forms.ValidationError(u'This nickname is already used')
        return nick  

    def clean_login(self):
        username = self.cleaned_data.get('login')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError(u'This login is already used')
        return username

class InputQuestionForm(forms.Form):
     Title = forms.CharField(widget=forms.Textarea(attrs={'name':"comment",'cols':"60", 'rows':"1"}), label = 'Title', required = True)
     Text = forms.CharField(widget=forms.Textarea(attrs={'name':"comment",'cols':"60", 'rows':"6"}), label = 'Text', required = True)
     Tags = forms.CharField(widget = forms.Textarea(attrs={'name':"comment",'cols':"60", 'rows':"1"}), label = 'Tags', required = False)

class InputAnswerForm(forms.Form):
     Text = forms.CharField(widget=forms.Textarea(attrs={'name':"comment",'cols':"60", 'rows':"3"}), label = 'Text', required = True)

