# Generated by Django 4.2.11 on 2024-03-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_goal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='category',
            field=models.CharField(choices=[('F', 'Family'), ('H', 'Health'), ('M', 'Financial'), ('S', 'Social'), ('E', 'Education'), ('C', 'Career'), ('G', 'Character Growth')], default='F', max_length=1),
        ),
    ]
