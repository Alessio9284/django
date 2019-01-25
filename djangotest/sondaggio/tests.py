from django.test import TestCase
from django.utils import timezone
from .models import Domanda
import datetime

# Create your tests here.

class TestDomanda(TestCase):
	def test_pubblicata_di_recente(self):
		t = timezone.now()
		domanda = Domanda(data_pub = t)
		self.assertIs(domanda.pubblicata_di_recente(), True)
		t = timezone.now() - datetime.timedelta(days = 60)
		domanda_nel_passato = Domanda(data_pub = t)
		self.assertIs(domanda_nel_passato.pubblicata_di_recente(), False)

	def test_pubblicata_in_futuro(self):
		t = timezone.now() + datetime.timedelta(days = 60)
		domanda_nel_futuro = Domanda(data_pub = t)
		self.assertIs(domanda_nel_futuro.pubblicata_di_recente(), False)