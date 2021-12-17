# Generated by Django 3.2.3 on 2021-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_auto_20210524_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег')),
                ('post', models.ManyToManyField(related_name='tags', to='posts.Post')),
            ],
        ),
    ]