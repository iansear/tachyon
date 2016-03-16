from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import CharField
from django.forms import BooleanField
from django.forms import DurationField
from django.forms import IntegerField
from django.forms import DecimalField
from django.forms import EmailField
from django.forms import PasswordInput
from delivery.models import Client
from delivery.models import Job

class RegisterClientForm(ModelForm):

    alias = CharField(label = ("Alias"))
    phone = CharField(label = ("Your Phone"))
    
    class Meta:
        model = Client
        fields = ['alias', 'phone']

class RegisterUserForm(UserCreationForm):

    error_messages = { 'password_mismatch': ("The two passwords do not match."),}
    
    password1 = CharField(label = ("Password"),
                widget = PasswordInput)
    
    password2 = CharField(label = ("Password Confirmations"),
                widget = PasswordInput,
                help_text = ("Enter the same password as above."))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PlaceJobForm(ModelForm):

    round_trip = BooleanField(label = ("Round Trip"), required = False)
    time_frame = IntegerField(label = ("Choose Service"))
    pick_company = CharField(label = ("Pickup Company"))
    pick_name = CharField(label = ("Contact"))
    pick_address = CharField(label = ("Pickup Address"))
    pick_phone = CharField(label = ("Pickup Phone"))
    pick_email = EmailField(label = ("Pickup Email"), required = False)
    drop_company = CharField(label = ("Dropoff Company"))
    drop_name = CharField(label = ("Contact"))
    drop_address = CharField(label = ("Dropoff Address"))
    drop_phone = CharField(label = ("Dropoff Phone"))
    drop_email = EmailField(label = ("Dropoff Email"), required = False)
    instructions = CharField(label = ("Special Instructions"), required = False)
    package_type = CharField(label = ("Description"))
    size = DecimalField(label = ("How Big"))
    quantity = IntegerField(label = ("How Many"))
    weight = DecimalField(label = ("How Heavy"))

    class Meta:
        model = Job
        fields = ['round_trip', 'time_frame', 'pick_company', 'pick_name',
                  'pick_address', 'pick_phone', 'pick_email', 'drop_company',
                  'drop_name', 'drop_address', 'drop_phone', 'drop_email',
                  'instructions', 'package_type', 'size', 'quantity', 'weight']
