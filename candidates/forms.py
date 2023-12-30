from django import forms
from .models import Profile,Skill




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Full name', 'country', 'location', 
                  'resume', 'grad_year', 'looking_for']
        

class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skills']

