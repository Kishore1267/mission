from django import forms
from .models import Receipes  # Replace 'Employee' with your actual model name
'''

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee   # Ensure this line is present
        fields = '__all__'  # Specify fields or use '__all__' to include all fields
'''
class ReceipesForm(forms.ModelForm):
    class Meta:
        model = Receipes
        fields = '__all__'
