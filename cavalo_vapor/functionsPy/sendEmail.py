from django.core.mail import send_mail

class EnviarEmail():
  def enviarEmail(self, dados):
    send_mail(
      dados["titulo"],
      dados["mensagem"],
      'Triunviratoifc@gmail.com',
      dados["emailsList"],
    )
