from django.db import models

class Application(models.Model):
	student_name = models.CharField('ФИО ученика', max_length=150)
	student_date = models.DateField('Дата рождения')
	family_name = models.CharField('ФИО родителя/законного представителя', max_length=150)
	contact_phone_number = models.IntegerField('Номер телефона')
	email = models.CharField('Email',max_length=150)
	adress = models.CharField('Адрес', max_length=150)


	def __str__(self):
		return self.student_name


	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'