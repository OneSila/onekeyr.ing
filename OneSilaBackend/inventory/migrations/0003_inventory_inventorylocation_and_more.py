# Generated by Django 4.2.5 on 2023-09-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('django_shared_multi_tenant', '0007_alter_multitenantcompany_language'),
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.PROTECT, to='django_shared_multi_tenant.multitenantcompany')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='products.productvariation')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.PROTECT, to='django_shared_multi_tenant.multitenantcompany')),
                ('parent_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventorylocation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='productstock',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='location',
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='multi_tenant_company',
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='stocklocation',
            name='multi_tenant_company',
        ),
        migrations.RemoveField(
            model_name='stocklocation',
            name='warehouse',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='multi_tenant_company',
        ),
        migrations.DeleteModel(
            name='MinimumStock',
        ),
        migrations.DeleteModel(
            name='ProductStock',
        ),
        migrations.DeleteModel(
            name='StockLocation',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.AddField(
            model_name='inventory',
            name='stocklocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.inventorylocation'),
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'stocklocation')},
        ),
    ]
