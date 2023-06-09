# Generated by Django 4.2 on 2023-04-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_alter_book_author_alter_book_id_alter_book_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=64, verbose_name="author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.IntegerField(
                primary_key=True, serialize=False, verbose_name="id"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="name",
            field=models.CharField(max_length=64, verbose_name="name"),
        ),
    ]
