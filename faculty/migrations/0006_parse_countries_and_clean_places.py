from django.db import migrations


def split_uni_and_country(data):
  data = str(data).strip()
  if '(' in data and ')' in data:
    university, country = data.split('(', 1)
    return university.strip(), country.replace(')', '').strip()
  elif ' - ' in data:
    university, country = data.split(' - ', 1)
    return university.strip(), country.strip()
  elif ',' in data:
    university, country = data.rsplit(',', 1)
    return university.strip(), country.strip()
  return data, ''


def clean_amount_of_places(data):
  words = str(data).split()
  for item in words:
    clean_item = item.strip()
    if clean_item.isnumeric():
      return clean_item
  return '0'


def clean_and_parse(apps, schema_editor):
  ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
  for program in ExchangeProgram.objects.all():
    program.university, program.country = split_uni_and_country(
        program.university
    )
    program.places = clean_amount_of_places(program.places)
    program.save()


def reverse_clean_and_parse_data(apps, schema_editor):
  ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
  for prog in ExchangeProgram.objects.all():
    if prog.country:
      prog.university = f'{prog.university}, {prog.country}'
      prog.country = ''
      prog.save()


class Migration(migrations.Migration):

  dependencies = [
      ('faculty', '0005_add_country_field'),
  ]

  operations = [
      migrations.RunPython(clean_and_parse, reverse_clean_and_parse_data),
  ]
