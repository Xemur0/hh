# Generated by Django 4.0.4 on 2022-05-28 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cvs', '0001_initial'),
        ('approvals', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='employee_profile_id',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='users.employeeprofile'),
        ),
        migrations.AddField(
            model_name='cv',
            name='status',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='approvals.approvalstatus'),
        ),
    ]
