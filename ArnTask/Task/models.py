from django.db import models
from django.conf import settings
from Users.models import ManipulatorDepozit,AgentVanzari

class Task(models.Model):
    '''Class to define a model for task objects'''

    class StatusFactura(models.TextChoices):
        INCASATA = "INCASATA", "Incasata"
        NEINCASATA = "NEINCASATA", "Neincasata"

    class ComplexitateFactura(models.TextChoices):
        USOARA = "USOARA", '''Usoara
        (1 produs sau max 10 produse iluminat tehnic)'''
        MEDIE = "MEDIE", "Medie"
        MARE = "MARE", '''Mare(probabil necesita 2 persoane)'''

    class TipLivrare(models.TextChoices):
        CURIER = "Curier", "AWB Curier"
        CLIENT_DEPOZIT = "CLIENT DEPOZIT", "Ridicare client de la depozit"
        CLIENT_SHOWROOM = "CLIENT SHOWROOM", "Ridicare client de la showroom"
        LIVRARE_ARN = "LIVRARE ARN", "Livrare ARN(Romeo)"
        TRANSPORT_SPECIAL = "TRANSPORT SPECIAL", "Transport special de la depozit"
        DEPOZITARE_TERMEN_SCURT = "DEOZITARE PE TERMEN SCURT", "Depozitare pe termen scurt < 7 zile"
        DEPOZITARE_TERMEN_LUNG = "DEPOZITARE TERMEN LUNG", "Depozitare pe termen lung > 7 zile"
        RIDICARE_URGENTA_2H = "RIDICARE URGENTA IN MAX 2H", "Ridicare urgenta in max 2h"
        RIDICARE_URGENTA_30MIN = "RIDICARE URGENTA IN 30 MIN", "Ridicare urgenta in max 30 min"

    class Curier(models.TextChoices):
        DRAGON = "DRAGON STAR", "Dragon Star"
        PPT = "PPT", "PPT"
        DPD = "DPD", "DPD"
        DIMENSIUNI_NECESARE = "DIMENSIUNI NECESARE", "Dimensiuni necesare"

    class ObservatiiFactura(models.TextChoices):
        STORNARE = "STORNARE", "Contine produse stornate"
        FARA_OBSERVATII = "FARA OBSERVATII", "Nici o observatie"
        OTHER = "OTHER", "Alte Observatii"

    class InformatiiFactura(models.TextChoices):
        LUCRU = "LUCRU", "Factura pregatita de a fi data in lucru"
        INFO_SUPLIMENTARE_VANZARI = "INFORMATII SUPLIMENTARE VANZARI", "Factura pregatita de a fi data in lucru"
        INFO_SUPLIMENTARE_FLORIN = "INFORMATII SUPLIMENTARE FLORIN", "Informatii suplimentare solicitate catre Florin Barascu"
        INFO_SUPLIMENTARE_RAZVAN = "INFORMATII SUPLIMENTARE RAZVAN", "Informatii suplimentare solicitate catre Razvan"

    class PrepTime(models.TextChoices):
        TIME_A = "5 MIN", "5 min"
        TIME_B = "15 MIN", "15 min"
        TIME_C = "30 MIN", "30 min"
        TIME_D = "60 MIN", "60 min"
        TIME_E = "90 MIN", "90 min"
        TIME_F = "120 MIN", "120 min"
        TIME_G = ">120 MIN", ">120 min"

    class ConfirmareManipulare(models.TextChoices):
        VARIANTA_A = "ALONE", "Incep comanda si ma descurc singur"
        VARIANTA_B = "NOT ALONE", "Incep comanda si am nevoie de ajutor"

    class StatusComanda(models.TextChoices):
        STATUS_A = "PRODUSE VERIFICATE - FARA PROBLEME", "Toate produsele sunt verificate - nu prezinta probleme"
        STATUS_B = "PRODUSE VERIFICATE - PROBLEME MICI", "Toate produsele sunt verificate - dar exista probleme mici"
        STATUS_C = "PRODUSE VERIFICATE - PROBLEME MARI", "Toate produsele sunt verificate - dar exista probleme mari"
        STATUS_D = "PROBLEME IDENTIFICARE", "Am probleme la identificarea produselor"
        STATUS_E = "PROBLEME CALITATE", "Am probleme cu calitatea produselor"

    class VolumComanda(models.TextChoices):
        FOARTE_MIC = "FOARTE MIC", " Foarte mic"
        MIC = "MIC", "Mic"
        MEDIU = "MEDIU", "Mediu"
        MARE = "MARE", "Mare"
        PACHETE_MARI = "PACHETE MARI", "Contine pachete mari"

    class StatusPreluare(models.TextChoices):
        CURIER = "CURIER", "Preluata Curier"
        TRANSPORT_SPECIAL = "TRANSPORT SPECIAL", "Preluata transport special"
        TRANSPORT_ARN = "TRANSPORT ARN", "Preluata transport ARN"
        RECEPTIE_CLIENT = "RECEPTIE CLIENT", "Receptie client"




    created_by = models.ForeignKey(AgentVanzari, on_delete=models.DO_NOTHING, related_name="Agent")
    numar_factura = models.CharField(max_length=25, null=False)
    beneficiar_factura = models.CharField(max_length=250, null=False)
    status_incasare = models.CharField(max_length=20, choices=StatusFactura.choices)
    complexitate_factura = models.CharField(max_length=250, choices=ComplexitateFactura.choices)
    tip_livrare = models.CharField(max_length=250, choices=TipLivrare.choices)
    curier = models.CharField(max_length=250, choices=Curier.choices, blank=True)
    observatii_factura = models.CharField(max_length=100, choices=ObservatiiFactura.choices,default=ObservatiiFactura.FARA_OBSERVATII)
    extra_observatii = models.TextField(blank=True)
    informatii_factura = models.CharField(max_length=250, choices=InformatiiFactura.choices)
    timp_factura = models.CharField(max_length=50, choices=PrepTime.choices)
    manipulator = models.ForeignKey(ManipulatorDepozit,on_delete=models.DO_NOTHING,related_name='manipulator')
    confirmare_manipulare = models.CharField(max_length=100, choices=ConfirmareManipulare.choices, blank=True)
    status_pregatire_produse = models.CharField(max_length=250, choices=StatusComanda.choices,default=StatusComanda.STATUS_A)
    status_ambalare = models.CharField(max_length=250,default="Produsele sunt ambalate si depozitate")
    numar_colete = models.IntegerField(default=1)
    volum_comanda= models.CharField(max_length=100, choices=VolumComanda.choices, blank=True)
    status_preluare = models.CharField(max_length=150, choices=StatusPreluare.choices, blank=True)




    def __str__(self):
        return f" Factura nr: {self.numar_factura}"







