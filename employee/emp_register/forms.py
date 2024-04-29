from django import forms
from .models import Employee
    
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname', 'emp_code', 'mobile', 'email', 'position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'Emp Code',
            'email':'Email',
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        
        
class EmployeeUpdate(forms.ModelForm):
    emp_code = forms.CharField(disabled=True)
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname', 'emp_code','mobile', 'email', 'position')
        
        labels = {
            'fullname':'Full Name',
            'emp_code':'Emp Code',
            'email':'Email',
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeUpdate, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"