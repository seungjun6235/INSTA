from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = Usercreationsform.meta.fields
        fields = ('username','profile_image',)


class CustomAuthenticationForm(AuthenticationForm):
    pass