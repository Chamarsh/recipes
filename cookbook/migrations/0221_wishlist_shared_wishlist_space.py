# Generated by Django 4.2.16 on 2024-12-08 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0220_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='shared',
            field=models.ManyToManyField(blank=True, related_name='wishlist_shared_with', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='space',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cookbook.space'),
            preserve_default=False,
        ),
    ]
