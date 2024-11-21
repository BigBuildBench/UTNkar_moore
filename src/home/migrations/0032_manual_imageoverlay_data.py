# Generated by Django 2.2.10 on 2020-04-03 00:36

from django.db import migrations
from itertools import chain
from utils.data_migrations import stream_field_filter_map

def button_to_group(block):
    return {
        'type': 'image_overlay',
        'value': {
            'image': block['value']['image'],
            'title': block['value']['title'],
            'description': block['value']['description'],
            'text_color': block['value']['text_color'],
            'buttons': {
                'buttons': [
                    {
                        'text': block['value']['button'],
                        'link': block['value']['link']
                    }
                ]    
            }
        }
    }


def group_to_button(block):
    return {
        'type': 'image_overlay',
        'value': {
            'image': block['value']['image'],
            'title': block['value']['title'],
            'description': block['value']['description'],
            'text_color': block['value']['text_color'],
            'link': block['value']['buttons']['buttons'][0]['link'],
            'button': block['value']['buttons']['buttons'][0]['text'],
            'include_bottom_margin': False,
            'include_top_margin': False,
        }
    }

        
def apply_to_all_pages(apps, mapper):
    HomePage = apps.get_model('home', 'HomePage')
    WebPage = apps.get_model('home', 'WebPage')
    hps = HomePage.objects.all()
    wps = WebPage.objects.all();
    for obj in chain(hps, wps):
        obj.body_en = stream_field_filter_map(obj.body_en, "image_overlay", mapper)
        obj.body_sv = stream_field_filter_map(obj.body_sv, "image_overlay", mapper)
        obj.save();

def forwards(apps, schema_editor):
    apply_to_all_pages(apps, button_to_group)

def backwards(apps, schema_editor):
    apply_to_all_pages(apps, group_to_button)
    


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20200403_0236'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
