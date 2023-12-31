# Generated by Django 4.2.5 on 2023-09-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_agentvanzari_managerdepozit_manipulatordepozit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar_factura', models.CharField(max_length=25)),
                ('beneficiar_factura', models.CharField(max_length=250)),
                ('status_incasare', models.CharField(choices=[('INCASATA', 'Incasata'), ('NEINCASATA', 'Neincasata')], max_length=20)),
                ('complexitate_factura', models.CharField(choices=[('USOARA', 'Usoara\n        (1 produs sau max 10 produse iluminat tehnic)'), ('MEDIE', 'Medie'), ('MARE', 'Mare(probabil necesita 2 persoane)')], max_length=250)),
                ('tip_livrare', models.CharField(choices=[('Curier', 'AWB Curier'), ('CLIENT DEPOZIT', 'Ridicare client de la depozit'), ('CLIENT SHOWROOM', 'Ridicare client de la showroom'), ('LIVRARE ARN', 'Livrare ARN(Romeo)'), ('TRANSPORT SPECIAL', 'Transport special de la depozit'), ('DEOZITARE PE TERMEN SCURT', 'Depozitare pe termen scurt < 7 zile'), ('DEPOZITARE TERMEN LUNG', 'Depozitare pe termen lung > 7 zile'), ('RIDICARE URGENTA IN MAX 2H', 'Ridicare urgenta in max 2h'), ('RIDICARE URGENTA IN 30 MIN', 'Ridicare urgenta in max 30 min')], max_length=250)),
                ('curier', models.CharField(choices=[('DRAGON STAR', 'Dragon Star'), ('PPT', 'PPT'), ('DPD', 'DPD'), ('DIMENSIUNI NECESARE', 'Dimensiuni necesare')], max_length=250)),
                ('informatii_factura', models.CharField(choices=[('LUCRU', 'Factura pregatita de a fi data in lucru'), ('INFORMATII SUPLIMENTARE VANZARI', 'Factura pregatita de a fi data in lucru'), ('INFORMATII SUPLIMENTARE FLORIN', 'Informatii suplimentare solicitate catre Florin Barascu'), ('INFORMATII SUPLIMENTARE RAZVAN', 'Informatii suplimentare solicitate catre Razvan')], max_length=250)),
                ('timp_factura', models.CharField(choices=[('5 MIN', '5 min'), ('15 MIN', '15 min'), ('30 MIN', '30 min'), ('60 MIN', '60 min'), ('90 MIN', '90 min'), ('120 MIN', '120 min'), ('>120 MIN', '>120 min')], max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.agentvanzari')),
            ],
        ),
    ]
