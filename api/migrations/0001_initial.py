# Generated by Django 3.2.6 on 2021-08-27 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('goal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.goal')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.goal')),
            ],
            bases=('api.goal',),
        ),
    ]
