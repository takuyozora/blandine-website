from django.shortcuts import render, get_object_or_404
from main.models import GroupeSymbio, Stage

from datetime import date

from django.http import HttpResponse


def home(request):
    stages = Stage.objects.order_by('-pk').filter(deleteTimer__gte=date.today())[:1]
    context = {"stages":stages}
    return render(request, 'main/index.html', context)


def contact(request):
    return render(request, 'main/contact.html')


def symbio(request):
    groupes = GroupeSymbio.objects.all().order_by("start")
    week = [[],[],[],[],[],[],[]]
    finalweek=list()
    try:
        for groupe in groupes:
            week[int(groupe.day)-1].append(groupe)
    except Exception:
        pass
    # for day in week:
    #     if len(day) is not 0:
    #         finalweek.append(day)
    context = {"groupes":week}
    return render(request, 'main/symbio.html', context)


def psycho(request):
    # TODO to implement !
    return render(request, 'main/psycho.html')


def stages(request):
    stages = Stage.objects.filter(deleteTimer__gte=date.today()) #Filtre pour n'afficher que ceux dont la date n'est pas dépassée
    context = {"stages": stages}
    return render(request, 'main/stages.html', context)


def view_stage(request, id):
    stage = get_object_or_404(Stage, id=id)
    context = {"stage": stage}
    return render(request, 'main/vue-stage.html', context)