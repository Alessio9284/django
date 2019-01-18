from django.shortcuts import render
from .models import Domanda
from django.template import loader
from django.http import HttpResponse
#from django.shortcuts import render_to_response

# Create your views here.

def index(request):
   elenco_domande = Domanda.objects.order_by('-data_pub')[:5]
   contesto = {
       'elenco_domande': elenco_domande,
   }
   return render(request, 'sondaggio/index.html', contesto)

#def index(request):
#	return HttpResponse("<marquee>Benarrivato. Sei all’indice del sondaggio.</marquee>")

#def index (request):
#    return render_to_response('sito/index.html')

#def index(request):    
#	return render(request, 'sito/index.html')

def dettagli(request, voto_id):
	return HttpResponse("Stai guardando la domanda %s." % voto_id)

def risultati(request, voto_id):
	return HttpResponse("Stai guardando i risultati della domanda %s." % voto_id)

def voto(request, sas_id):
	return HttpResponse("Stai guardanto il voto %s." % sas_id)