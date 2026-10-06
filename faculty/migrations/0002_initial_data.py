from django.db import migrations


def load_fen_data(apps, schema_editor):
      FacultyInfo = apps.get_model('faculty', 'FacultyInfo')
      Department = apps.get_model('faculty', 'Department')
      Program = apps.get_model('faculty', 'Program')
      Teacher = apps.get_model('faculty', 'Teacher')
      Discipline = apps.get_model('faculty', 'Discipline')

      FacultyInfo.objects.create(
          title='Факультет економічних наук НаУКМА',
          description=(
              'Факультет економічних наук (ФЕН) заснований у 2000 році. Наш слоган'
              ' — «ЗРОСТАЙМО!». Ми поєднуємо принципи Liberal Arts Education'
              ' (вільне творче навчання), широку базову економічну освіту на'
              ' молодших курсах та профільну спеціалізацію на старших курсах із'
              ' глибокою інтеграцією в бізнес-середовище.'
          ),
          dean_name='Глущенко Світлана Василівна (к.е.н., доцент)',
          address='м. Київ, вул. Волоська, 8/5, 6 корпус, кімн. 406',
          phone='+38 (044) 425-60-42',
          email='gluschenkosv@ukma.edu.ua',
      )

      dept_finance = Department.objects.create(
          name='Кафедра фінансів',
          head='Лукʼяненко Ірина Григорівна',
      )
      dept_econ = Department.objects.create(
          name='Кафедра економічної теорії',
          head='Біла Ірина Сергіївна',
      )
      dept_marketing = Department.objects.create(
          name='Кафедра маркетингу та управління бізнесом',
          head='Пічик Катерина Валеріївна',
      )

      Teacher.objects.create(
          name='Лукʼяненко Ірина Григорівна',
          position='Завідувач кафедри',
          degree=(
              'Доктор економічних наук, професор, Заслужений діяч науки і техніки'
              ' України'
          ),
          department=dept_finance,
      )
      Teacher.objects.create(
          name='Девід Віт (David Wheat)',
          position='Запрошений професор (Professor Emeritus, University of Bergen)',
          degree='PhD, випускник Гарвардського університету',
          department=dept_finance,
      )
      Teacher.objects.create(
          name='Біла Ірина Сергіївна',
          position='Завідувач кафедри',
          degree='Кандидат економічних наук, доцент',
          department=dept_econ,
      )
      Teacher.objects.create(
          name='Глущенко Світлана Василівна',
          position='Декан факультету, доцент',
          degree='Кандидат економічних наук, доцент',
          department=dept_econ,
      )
      Teacher.objects.create(
          name='Пічик Катерина Валеріївна',
          position='Завідувач кафедри',
          degree='Кандидат економічних наук, доцент',
          department=dept_marketing,
      )

      prog_fin = Program.objects.create(
          name='Фінанси, банківська справа, страхування та фондовий ринок',
          code='072',
          description=(
              'Акцентом спеціальності є бізнес-аналітика та фінанси. З 2014 року'
              ' діє сертифікація CFA Institute. Програма готує фахівців для'
              ' банківського сектора, інвестиційного консалтингу, фондових бірж та'
              ' державного управління фінансами.'
          ),
          coordinator_name='Лукʼяненко Ірина Григорівна',
          coordinator_contact='iryna.lukianenko@ukma.edu.ua, (044) 425 60 42',
          department=dept_finance,
      )

      prog_econ = Program.objects.create(
          name='Економіка',
          code='051',
          description=(
              'Аналог найпоширеніших у світі бакалаврських програм Economics.'
              ' Включає вибіркові блоки дисциплін (minor): Економіка і політика,'
              ' Економіка інноваційного розвитку, Економіка і міжнародний розвиток.'
          ),
          coordinator_name='Біла Ірина Сергіївна',
          coordinator_contact='i.bila@ukma.edu.ua, (044) 425 60 42',
          department=dept_econ,
      )

      prog_mkt = Program.objects.create(
          name='Маркетинг',
          code='075',
          description=(
              'Практичне інтегрування у бізнес-середовище (МАМІ, ВРК, Genesis,'
              " L'Oreal). Програма включає сертифікатні курси з Customer Experience"
              ' та бізнес-кейси від провідних брендів.'
          ),
          coordinator_name='Пічик Катерина Валеріївна',
          coordinator_contact='pichykkv@ukma.edu.ua, (044) 425 77 87',
          department=dept_marketing,
      )

      prog_mgmt = Program.objects.create(
          name='Менеджмент',
          code='073',
          description=(
              'Підготовка управлінців нового покоління. Навчання спрямоване на'
              ' розвиток бізнесу, аналітику, проєктний менеджмент та консалтинг.'
          ),
          coordinator_name='Пічик Катерина Валеріївна',
          coordinator_contact='pichykkv@ukma.edu.ua, (044) 425 77 87',
          department=dept_marketing,
      )

      Discipline.objects.create(
          name='Поглиблений курс системної динаміки у фінансах', program=prog_fin
      )
      Discipline.objects.create(
          name='Corporate Finance (спільно зі SciencesPo)', program=prog_fin
      )
      Discipline.objects.create(
          name='Фінансовий та інвестиційний аналіз', program=prog_fin
      )
      Discipline.objects.create(
          name='Банківська справа та фондовий ринок', program=prog_fin
      )

      Discipline.objects.create(name='Мікроекономіка', program=prog_econ)
      Discipline.objects.create(name='Макроекономіка', program=prog_econ)
      Discipline.objects.create(name='Економіка і політика', program=prog_econ)
      Discipline.objects.create(
          name='Економіка інноваційного розвитку', program=prog_econ
      )
      Discipline.objects.create(
          name='Економіка і міжнародний розвиток', program=prog_econ
      )

      Discipline.objects.create(
          name='Customer Experience (сертифікатна програма МАМІ)',
          program=prog_mkt,
      )
      Discipline.objects.create(
          name='Цифровий маркетинг та таргетинг', program=prog_mkt
      )
      Discipline.objects.create(name='Маркетингова аналітика', program=prog_mkt)
      Discipline.objects.create(
          name='Управління бізнес-проєктами (Project Management)',
          program=prog_mgmt,
      )
      Discipline.objects.create(
          name='Антикризовий менеджмент та консалтинг', program=prog_mgmt
      )


def reverse_fen_data(apps, schema_editor):
    Discipline = apps.get_model('faculty', 'Discipline')
    Teacher = apps.get_model('faculty', 'Teacher')
    Program = apps.get_model('faculty', 'Program')
    Department = apps.get_model('faculty', 'Department')
    FacultyInfo = apps.get_model('faculty', 'FacultyInfo')

    Discipline.objects.all().delete()
    Teacher.objects.all().delete()
    Program.objects.all().delete()
    Department.objects.all().delete()
    FacultyInfo.objects.all().delete()


class Migration(migrations.Migration):

  dependencies = [
      ('faculty', '0001_initial'),
  ]

  operations = [
      migrations.RunPython(load_fen_data, reverse_fen_data),
  ]
