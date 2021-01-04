from django import forms
from survey.models import Survey
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.admin.widgets import AdminDateWidget

class SurveyForm(forms.Form):
	surveyname=forms.CharField(max_length=50)
	surveymessage=forms.CharField(max_length=2000,widget=forms.Textarea())
	#datetillopen=forms.CharField(max_length=10)
	dateuntilopen=forms.DateField(widget = forms.SelectDateWidget())
	#numberofquestions=forms.IntegerField()
	#super=forms.CharField(max_length=100,widget=forms.HiddenInput())

	def clean(self):
		cleaned_data=super(SurveyForm,self).clean()
		surveyname=cleaned_data.get('surveyname')
		surveymessage=cleaned_data.get('surveymessage')
		dateuntilopen=cleaned_data.get('dateuntilopen')
		if not surveyname and not surveymessage and not dateuntilopen:
			raise forms.ValidationError('You have to write something')
class questionForm(forms.Form):
	#questionid=forms.IntegerField()
	question=forms.CharField(max_length=200)
	option1=forms.CharField(max_length=100)
	option2=forms.CharField(max_length=100)
	option3=forms.CharField(max_length=100,required=False)
	option4=forms.CharField(max_length=100,required=False)
	#choice=['option1','option2','option3','option4']
	#like=forms.ChoiceField(choices=choice,widget=forms.RadioSelect())
	def clean(self):
		cleaned_data=super(questionForm,self).clean()
		question=cleaned_data.get('question')
		option1=cleaned_data.get('option1')
		option2=cleaned_data.get('option2')
		option3=cleaned_data.get('option3')
		option4=cleaned_data.get('option4')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=200)

    def clean(self):
        cleaned_data =super(ProfileForm,self).clean()
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        email=cleaned_data.get('email')		

class approverForm(forms.Form):
	Username=forms.CharField(max_length=200)
	password=forms.CharField(max_length=200,widget=forms.PasswordInput)

	def clean(self):
		cleaned_data=super(approverForm,self).clean()
		Username=cleaned_data.get('Username')
		password=cleaned_data.get('password')
class ForgotpasswordForm(forms.Form):
	username=forms.CharField(max_length=100)
	email=forms.EmailField(max_length=100)

	def clean(self):
		cleaned_data=super(ForgotpasswordForm,self).clean()
		Username=cleaned_data.get('Username')
		email=cleaned_data.get('email')