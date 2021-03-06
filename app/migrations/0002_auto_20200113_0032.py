# Generated by Django 2.1.2 on 2020-01-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sample_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_7',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_9',
        ),
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='日付'),
        ),
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='場所'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, '完了'), (2, '進行中'), (3, '実行前')], null=True, verbose_name='状態'),
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='イベント名'),
        ),
        migrations.AddField(
            model_name='item',
            name='whatisthis',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
    ]
