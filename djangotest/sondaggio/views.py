from django.shortcuts import render
from .models import Domanda, Scelta
from django.template import loader
from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

#def dettagli(request, voto_id):
#	return HttpResponse("Stai guardando la domanda %s." % voto_id)

#def risultati(request, voto_id):
#	return HttpResponse("Stai guardando i risultati della domanda %s." % voto_id)

def risultati(request, domanda_id):
    domanda = get_object_or_404(Domanda, pk = domanda_id)
    return render(request, 'sondaggio/risultati.html', {'domanda': domanda})

#def voto(request, sas_id):
#	return HttpResponse("Stai guardanto il voto %s." % sas_id)

def dettagli(request, domanda_id):
    dom = Domanda.objects.get(pk = domanda_id)
    elenco_scelte = Scelta.objects.filter(domanda = dom)
    contesto = {
        'domanda' : dom,
        'elenco_scelte' : elenco_scelte,
    }

    return render(request, 'sondaggio/dettagli.html', contesto)

def vote(request,  domanda_id):
    domanda = get_object_or_404(Domanda, pk = domanda_id)
    try:
        selezionata = domanda.scelta_set.get(pk = request.POST['scelta'])
    except (KeyError, Scelta.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'domanda': domanda,
            'errore': "Non hai fatto la scelta.",
        })
    else:
        selezionata.voto += 1
        selezionata.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return redirect('/sondaggio/' + str(domanda.id) + "/risultati")