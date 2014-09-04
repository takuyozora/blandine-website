from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class GroupeSymbio(models.Model):
    class Meta:
        verbose_name = "Groupe de Symbiotonie"
        verbose_name_plural = "Groupes de Symbiotonie"

    DAYS = (
        ('1', 'Lundi'),
        ('2', 'Mardi'),
        ('3', 'Mercredi'),
        ('4', 'Jeudi'),
        ('5', 'Vendredi'),
        ('6', 'Samedi'),
        ('7', 'Dimanche')
    )
    day = models.CharField("Jour",max_length=1, choices=DAYS)
    start = models.TimeField("Heure de début",help_text="Format HH:mm (ex 17:30)")
    end = models.TimeField("Heure de fin",help_text="Format HH:mm (ex 17:30)")
    isFull = models.BooleanField("Groupe complet")

    def __unicode__(self):
        return "Groupe du " + self.DAYS[int(self.day) - 1][1] + " " + str(self.start)

    def __str__(self):
        return self.__unicode__()

class Discipline(models.Model):
    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"

    name = models.CharField("Nom",max_length=50)
    logo_height = models.PositiveSmallIntegerField("Hauteur",default=32)
    logo_width = models.PositiveSmallIntegerField("Largeur",default=32)
    logo = models.ImageField("Logo",upload_to="logos",width_field='logo_width',height_field='logo_height',help_text="Logo de la discipline, dimension 32x32",blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class Stage(models.Model):
    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

    STATES = (
        ("De","Normal"),
        ("Ok","Confirmé"),
        ("Ca","Annulé"),
    )
    title = models.CharField("Titre",max_length=140)
    disciplines = models.ManyToManyField(Discipline)
    photo_height = models.PositiveSmallIntegerField("Hauteur",default=125)
    photo_width = models.PositiveSmallIntegerField("Largeur",default=150)
    photo = models.ImageField("Photo",upload_to="stages",width_field="photo_width",height_field="photo_height",help_text="Miniature du stage, dimension 150x125",blank=True)
    short = models.CharField("Résumé",max_length=600,help_text="Petit résumé qui sera affiché dans l'encadré, max 600 charactères")
    dates = models.TextField("Dates",help_text="Les dates du stages seront affichées dans le petit encadré et dans la page détaillées, il faut qu'elles soient tout de même consises")
    showDates = models.BooleanField("Montrer les dates dans l'encadré",help_text="Décide si les dates seront affichées également dans le petit encadré",default=True)
    prices = models.TextField("Prix et réservation",help_text="Les prix et modalités de réservation seront affichées dans un cadre spécifique et seront visible ou non dans le petit encadré")
    showPrices = models.BooleanField("Montrer les prix et réservation dans l'encadré",help_text="Décide si les prix et réservations seront affichées également dans le petit encadré",default=False)
    description = models.TextField("Description",help_text="La description complète du stage")
    state = models.CharField("État",help_text="Donne l'état du stage entre `normal`, `confirmé`, ou `annulé`",max_length=2,choices=STATES,default=STATES[0])
    isFull = models.BooleanField("Complet",help_text="Le stage est montré comme complet si coché")
    deleteTimer = models.DateField("Date de suppression",help_text="Définie la date à partir de la quelle le stage ne doit plus apparaître",blank=True)

    def __unicode__(self):
        showName = self.title+" : «"+self.short
        showName = showName[:140]+" [...] »"
        return showName

    def __str__(self):
        return self.__unicode__()



