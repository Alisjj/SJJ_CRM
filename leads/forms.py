from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Agent, Lead, Category

User = get_user_model()


class LeadModelForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'description',
            'phone_number',
            'email',

        )
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(LeadModelForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class CustomerUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        fields_classes = {"username": UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
