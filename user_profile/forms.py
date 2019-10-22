from django import forms
from django.core.validators import RegexValidator
from .models import User, UserProfile
from django.contrib.auth.hashers import make_password
from .mixins import EmailDuplicationMixin


class SignUpForm(EmailDuplicationMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    cinc_number = forms.CharField(max_length=20,  label="CNIC Number", validators=[RegexValidator(
        regex=r'[0-9]{5}-[0-9]{7}-[0-9]{1}',
        message="CNIC Number is not valid. CNIC number format should be 00000-0000000-0."
    )])
    occupation = forms.CharField(max_length=500,  label="Your Occupation")
    bio = forms.CharField(max_length=500,  label="About (Bio)", widget=forms.Textarea)
    address = forms.CharField(max_length=255,  label="Permanent Address")
    contact_number = forms.CharField(max_length=30,  label="Contact Number", validators=[RegexValidator(
        regex=r'[0-9]{4}-[0-9]{7}',
        message="Contact number is not valid. Contact number format should be 0000-0000000."
    )])
    city = forms.CharField(max_length=30,  label="Your Location (City)")
    country = forms.CharField(max_length=30, label="Your Nationality (Country)")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data.get('password'))
        user.user_profile = {i:self.cleaned_data[i] for i in self.cleaned_data if i not in SignUpForm.Meta.fields}
        user.save()
        return user

