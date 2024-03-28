from django.shortcuts import render, redirect
from .models import Objetconnecte, Capteur, Actionneur
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'ardjson/intro.html')

def objconnView(request):
    return render(request, 'ardjson/objconn.html')

def soundView(request):
    return render(request, 'ardjson/sound.html')

def photoresistanceView(request):
    return render(request, 'ardjson/photoresistance.html')

def dht11View(request):
    return render(request, 'ardjson/dht11.html')

def masterView(request):
    return render(request, 'ardjson/master.html')

def room101View(request):
    return render(request, 'ardjson/room101.html')

def room102View(request):
    return render(request, 'ardjson/room102.html')

def room103View(request):
    return render(request, 'ardjson/room103.html')

def add_objView(request):
    return render(request, 'ardjson/add_obj.html')

def objconnView(request):
    objets = Objetconnecte.objects.all().order_by('-objet_id')
    return render(request, 'ardjson/objconn.html', {'objets': objets})

def savedataView(request):
    if request.method == 'POST':
        try:
            form_data = json.loads(request.body.decode('utf-8'))
            print('Données du formulaire reçues :', form_data)
            
            objet = Objetconnecte.objects.create(
                nom=form_data.get('nom'),
                device_id=form_data.get('Device ID'),
                type=form_data.get('type'),
                typemesure=form_data.get('typemesure')
            )

            capteur = Capteur.objects.create(
                objet=objet,
                status=form_data.get('Status'),
                temperature=form_data.get('Temperature'),
                humidite=form_data.get('Humidite'),
                son=form_data.get('Son'),
                distance=form_data.get('Distance'),
                lumiere=form_data.get('Lumiere'),
                formatted_date=form_data.get('Date'),
                formatted_time=form_data.get('Time')
            )

            actionneur = Actionneur.objects.create(
                objet=objet,
                status=form_data.get('Status'),
                formatted_date=form_data.get('Date'),
                formatted_time=form_data.get('Time')
            )

            print('Données enregistrées avec succès')
            return JsonResponse({'message': 'Données enregistrées avec succès'})
        except Exception as e:
            print('Échec de l\'enregistrement des données :', e)
            return JsonResponse({'erreur': 'Échec de l\'enregistrement des données'}, status=500)
    else:
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

def delete_obj_view(request, obj_id):
    if request.method == 'DELETE':
        try:
            obj = get_object_or_404(Objetconnecte, pk=obj_id)
            obj.delete()  
            print('Objet supprimé avec succès')
            return JsonResponse({'message': 'Objet supprimé avec succès'})
        except Exception as e:
            print('Échec de la suppression de l\'objet :', e)  
            return JsonResponse({'error': 'Échec de la suppression de l\'objet'}, status=500)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def upd_obj_view(request, obj_id):
    try:
        obj = Objetconnecte.objects.get(objet_id=obj_id)
        print('Objet trouvé :', obj.nom, obj.type, obj.typemesure)
        if request.method == 'POST':
            obj.nom = request.POST.get('nom')
            obj.type = request.POST.get('type')
            obj.save()  
            print('Objet mis à jour :', obj.nom, obj.type, obj.typemesure)  
            return JsonResponse({'message': 'Objet mis à jour avec succès'})
        else:
            return render(request, 'ardjson/upd_obj.html', {'objet': obj})
    except Objetconnecte.DoesNotExist:
        return redirect('objconn')
    except Exception as e:
        print('Erreur lors de la mise à jour de l\'objet :', e) 
        return JsonResponse({'error': 'Erreur lors de la mise à jour de l\'objet'}, status=500)
