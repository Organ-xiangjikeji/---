# Generated by Django 2.0.5 on 2018-08-31 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('size', models.CharField(max_length=128, verbose_name='规格')),
                ('date', models.DateTimeField(verbose_name='数据年份')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传日期')),
                ('data_addr', models.CharField(max_length=128, verbose_name='存储地址')),
                ('status', models.SmallIntegerField(choices=[(1, '原始数据'), (2, '标注数据')], verbose_name='数据状态')),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.DataSource', verbose_name='数据来源'),
        ),
        migrations.AddField(
            model_name='data',
            name='data_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.DataType', verbose_name='数据形式'),
        ),
        migrations.AddField(
            model_name='data',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Industry', verbose_name='行业类型'),
        ),
    ]
