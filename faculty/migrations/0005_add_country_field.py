from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_exchange_add_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeprogram',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
