# Generated by Django 4.2.5 on 2023-09-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0005_remove_task_manipulator_task_manipulator'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='in_work',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_created_by_sales',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='problems_detected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='processed_by_warehouse_manager',
            field=models.BooleanField(default=False),
        ),
    ]
