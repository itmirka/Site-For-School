from .models import Application
from django.forms import ModelForm, TextInput, DateInput, NumberInput


class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['student_name', 'student_date', 'family_name', 'contact_phone_number', 'email', 'adress']


		widgets = {
			'student_name': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'ФИО ученика'
			}),
			'student_date': DateInput(attrs={
				'class': 'form-control',
				'placeholder': 'Дата рождения'
			}),
			'family_name': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'ФИО родителя/законного представителя'
			}),
			'contact_phone_number': NumberInput(attrs={
				'class': 'form-control',
				'placeholder': 'Контактный номер телефона'
			}),
			'email': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Email'
			}),
			'adress': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Адрес проживания'
			}),
		}