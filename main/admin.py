from django.contrib import admin
from main.models import GroupeSymbio, Stage, Discipline
from main.forms import StageForm


# Register your models here.
class GroupeSymbioAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Horaire", {
            'fields': ('day', 'start', 'end')
        }),
        ('Complet ou non', {
            'fields': ('isFull', )
        }),
    )
    ordering = ['day','start']

class StageAdmin(admin.ModelAdmin):
    form = StageForm
    fieldsets = (
        ("Stage", {
            'fields': ('title', 'disciplines', 'photo', 'short')
        }),
        ('Date, prix et réservation', {
            'fields': ('dates', 'showDates', 'prices', 'showPrices')
        }),
        ('Description du stage', {
            'fields': ('description',)
        }),
        ('Autres informations', {
            'fields': ('state', 'isFull', 'deleteTimer')
        }),
    )
    ordering = ['deleteTimer']

class DisciplineAdmin(admin.ModelAdmin):
    exclude = ('logo_height', 'logo_width')
    ordering = ('name', )

admin.site.register(GroupeSymbio,GroupeSymbioAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Discipline,DisciplineAdmin)