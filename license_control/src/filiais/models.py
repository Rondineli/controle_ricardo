# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from license_control.models import DatedModel


class BranchLicense(DatedModel):
    CITIES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goias'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraiba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuca'),
        ('PI', 'Piaui'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )
    nome_fantasia = models.CharField(
        max_length=200,
        verbose_name=_(u'Nome Fantasia'),
        help_text=_(u'Coloque o Nome Fantasia')
    )
    razao_social = models.CharField(
        max_length=255,
        verbose_name=_(u'Razão Social'),
        help_text=_(u'Digite sua razão social')
    )
    cnpj = models.CharField(
        max_length=14,
        verbose_name=_(u'Digite o cnpj'),
        help_text=_(u'00.000.000/0000-00')
    )
    inscricao_estadual = models.CharField(
        max_length=20,
        verbose_name=_(u'Digite a inscrição estadual'),
        help_text=_(u'Veja a inscrição estadual')
    )
    endereco = models.CharField(
        max_length=255,
        verbose_name=_(u'Endereço'),
        help_text=_(u'Ex: Rua joao de abreu, 123')
    )
    cep = models.CharField(
        max_length=8,
        verbose_name=_(u'Cep'),
        help_text=_(u'Ex: 00000-000')
    )
    estado = models.CharField(
        max_length=2,
        choices=CITIES,
        verbose_name=_(u'Estado'),
        help_text=_(u'Escolha seu estado')
    )
    cidade = models.CharField(
        max_length=255,
        verbose_name=_(u'Cidade'),
        help_text=_(u'Informe sua cidade')
    )
    nire = models.CharField(
        max_length=255,
        verbose_name=_(u'Nire'),
        help_text=_(u'Informe o Nire')
    )
    objeto_social = models.CharField(
        max_length=255,
        verbose_name=_(u'Objeto Social'),
        help_text=_(u'Informe o objeto social')
    )

    def __unicode__(self):
        return self.nome_fantasia
