# Generated by Django 4.1.9 on 2023-06-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0190_auto_20230525_1506'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE cookbook_food_properties RENAME TO cookbook_foodproperty",
                    reverse_sql="ALTER TABLE cookbook_foodproperty RENAME TO cookbook_food_properties",
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name='FoodProperty',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.food')),
                        ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.property')),
                    ],
                ),
                migrations.AlterField(
                    model_name='food',
                    name='properties',
                    field=models.ManyToManyField(blank=True, through='cookbook.FoodProperty', to='cookbook.property'),
                ),
            ]
        ),
        migrations.AddConstraint(
            model_name='foodproperty',
            constraint=models.UniqueConstraint(fields=('food', 'property'), name='property_unique_food'),
        ),
        migrations.AddField(
            model_name='property',
            name='import_food_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name='property',
            constraint=models.UniqueConstraint(fields=('space', 'property_type', 'import_food_id'), name='property_unique_import_food_per_space'),
        ),
    ]