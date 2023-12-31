from django import forms
from .models import Profile,Skill


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'country', 'location', 
                  'resume', 'grad_year', 'lookingfor']
        

class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']




