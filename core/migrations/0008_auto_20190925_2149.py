# Generated by Django 2.2.5 on 2019-09-25 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0007_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='content_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='vote',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
        ),
    ]