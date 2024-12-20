from django.utils import timezone 
from django import forms
from .models import TodoModel


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'description', 'cron']
        widgets = {
            'cron': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_cron(self):
        cron_date = self.cleaned_data.get('cron') 
        current_date = timezone.now() 
        if cron_date and cron_date < current_date:
            raise forms.ValidationError('Cron is not valid: must be in the future')
        return cron_date
