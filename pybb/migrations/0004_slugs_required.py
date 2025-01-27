# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pybb", "0003_slugs_fill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True, max_length=255, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="forum",
            name="slug",
            field=models.SlugField(max_length=255, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug",
            field=models.SlugField(max_length=255, verbose_name="Slug"),
        ),
        migrations.AlterUniqueTogether(
            name="forum",
            unique_together={("category", "slug")},
        ),
        migrations.AlterUniqueTogether(
            name="topic",
            unique_together={("forum", "slug")},
        ),
    ]
