from django.test import TestCase
from .functionsPy.vereficadores import *


class CpfTestCase(TestCase):
  def test_cpf_digitosRepetidos_tamanho_poluido(self):
    self.assertEqual(verificaCPF("681.477.449-600"), False)
    self.assertEqual(verificaCPF("681.477.449-0"), False)
    self.assertEqual(verificaCPF("681.477.449060"), False)
    self.assertEqual(verificaCPF("11111111111"), False)
    self.assertEqual(verificaCPF("681.477.449-60"), True)
    self.assertEqual(verificaCPF("681.477.44960"), True)
    self.assertEqual(verificaCPF("681.477.449--60"), True)

  
  def test_cpf_formatados(self):
    self.assertEqual(verificaCPF("681.477.449-60"), True)
    self.assertEqual(verificaCPF("060.673.772-33"), True)
    self.assertEqual(verificaCPF("712.734.212-13"), True)
    self.assertEqual(verificaCPF("615.037.222-94"), False)
    self.assertEqual(verificaCPF("615.037.323-92"), False)
    self.assertEqual(verificaCPF("615.037.333-24"), False)

class CnpjTestCase(TestCase):
  def test_cnpj_digitosRepetidos_tamanho_poluido(self):
    self.assertEqual(verificaCNPJ("46.691.648/0001-5223"), False)
    self.assertEqual(verificaCNPJ("46.691.648/0001252"), False)
    self.assertEqual(verificaCNPJ("02.6892036/0001-50."), False)
    self.assertEqual(verificaCNPJ("02.689.036/0001-5/0."), True)
    self.assertEqual(verificaCNPJ("02.6892030001-5//0."), False)


  def test_cpf_formatados(self):
    self.assertEqual(verificaCNPJ("46.691.648/0001-52"), True)
    self.assertEqual(verificaCNPJ("02.689.036/0001-50"), True)
    self.assertEqual(verificaCNPJ("83.331.155/0001-38"), True)
    self.assertEqual(verificaCNPJ("11.111.111/1111-11"), False)
    self.assertEqual(verificaCNPJ("32.657.234/0001-18"), False)
    self.assertEqual(verificaCNPJ("83.648.335/0201-48"), False)

class CepTestCase(TestCase):
  def test_cep(self):
    self.assertEqual(verificaReorganizeCep("89245-000"), (True, "89245-000"))
    self.assertEqual(verificaReorganizeCep("8924--000"), (False, "8924--000"))
    self.assertEqual(verificaReorganizeCep("8924-5-000"), (False, "8924-5-000"))
    self.assertEqual(verificaReorganizeCep("8924-5000"), (True, "89245-000"))
    self.assertEqual(verificaReorganizeCep("8924-50002"), (False, "8924-50002"))
