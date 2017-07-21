from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

insChoices = (
    ('CHOP', "Childrens Hospital of Philadelphia"),
    ('CCHMC', "Cincinnati Children's Hospital Medical Center"),
    ('Other', "Other"),
)

class SignUpForm(UserCreationForm):
    institution = forms.ChoiceField(choices=insChoices)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'institution')
        help_texts = {
            'username': _('Letters, digits and @/./+/-/_ only.')
        }
