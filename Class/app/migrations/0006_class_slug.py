from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Class = apps.get_model("app", "Class")
    used_slugs = set()

    for class_obj in Class.objects.all().order_by("id"):
        base_slug = slugify(class_obj.name) or "class"
        slug = base_slug
        counter = 1

        while slug in used_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1

        class_obj.slug = slug
        class_obj.save(update_fields=["slug"])
        used_slugs.add(slug)


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_class_ends_at_alter_class_starts_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="slug",
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="class",
            name="slug",
            field=models.SlugField(blank=True, max_length=120, unique=True),
        ),
    ]
