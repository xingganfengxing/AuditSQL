# Generated by Django 2.1.7 on 2019-04-09 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('query', '0001_initial'),
        ('orders', '0002_auto_20190409_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='querybusinessgroup',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='mysqlusergroupmap',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MysqlConfig', verbose_name='主机描述'),
        ),
        migrations.AddField(
            model_name='mysqlusergroupmap',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='mysqlprivblacklist',
            unique_together={('schema', 'table')},
        ),
        migrations.AlterUniqueTogether(
            name='mysqlusergroupmap',
            unique_together={('comment', 'group')},
        ),
    ]