# Generated by Django 3.2.8 on 2023-05-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='application',
            name='adress',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='application',
            name='contact_phone_number',
            field=models.IntegerField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]