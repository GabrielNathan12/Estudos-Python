from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.validate_cpf import validate_cpf

class Profile(models.Model):

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2,
                            default='SP',
                            choices=(
                                ('AC', 'Acre'),
                                ('AL', 'Alagoas'),
                                ('AP', 'Amapá'),
                                ('AM', 'Amazonas'),
                                ('BA', 'Bahia'),
                                ('CE', 'Ceará'),
                                ('DF', 'Distrito Federal'),
                                ('ES', 'Espírito Santo'),
                                ('GO', 'Goiás'),
                                ('MA', 'Maranhão'),
                                ('MT', 'Mato Grosso'),
                                ('MS', 'Mato Grosso do Sul'),
                                ('MG', 'Minas Gerais'),
                                ('PA', 'Pará'),
                                ('PB', 'Paraíba'),
                                ('PR', 'Paraná'),
                                ('PE', 'Pernambuco'),
                                ('PI', 'Piauí'),
                                ('RJ', 'Rio de Janeiro'),
                                ('RN', 'Rio Grande do Norte'),
                                ('RS', 'Rio Grande do Sul'),
                                ('RO', 'Rondônia'),
                                ('RR', 'Roraima'),
                                ('SC', 'Santa Catarina'),
                                ('SP', 'São Paulo'),
                                ('SE', 'Sergipe'),
                                ('TO', 'Tocantins'),
                                )
    )

    def __str__(self) -> str:
        return f'{self.user}'
    
    def clean(self):
        error_messages = {}

        cpf_send = self.cpf or None
        cpf_save = None
        profile = Profile.objects.filter(cpf=cpf_send).first()

        if profile:
            cpf_save = profile.cpf

            if cpf_save is not None and self.pk != profile.pk:
                error_messages['cpf'] = 'CPF já cadastrado'

            if not validate_cpf(self.cpf):
                error_messages['cpf'] = 'CPF inválido'

            if re.search(r'[^0-9]', self.cep) or len(self.cep) < 7:
                error_messages['cep'] = 'CEP inválido'

        if error_messages:
            raise ValidationError(error_messages)
        

