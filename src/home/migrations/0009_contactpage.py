# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('home', '0008_auto_20170712_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_sv', models.CharField(max_length=255)),
                ('contact_point_en', wagtail.core.fields.StreamField((('person', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False))))),))),
                ('contact_point_sv', wagtail.core.fields.StreamField((('person', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False))))),))),
                ('other_contacts_en', wagtail.core.fields.StreamField((('contact', wagtail.core.blocks.StructBlock((('person', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False))))), ('group', wagtail.core.blocks.CharBlock(required=False))), icon='user')),))),
                ('other_contacts_sv', wagtail.core.fields.StreamField((('contact', wagtail.core.blocks.StructBlock((('person', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False))))), ('group', wagtail.core.blocks.CharBlock(required=False))), icon='user')),))),
                ('map_location', models.CharField(blank=True, help_text='Enter comma separated coordinates', max_length=255, verbose_name='Map Location')),
                ('location_description', wagtail.core.fields.RichTextField(blank=True, help_text='Enter the text to show on the map', verbose_name='Location Description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
