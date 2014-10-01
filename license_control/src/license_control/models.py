# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DatedModel(models.Model):
    creation_time = models.DateTimeField(
        _(u'data de criação'),
        auto_now_add=True
    )
    modification_time = models.DateTimeField(
        _(u'data de atualização'),
        auto_now=True
    )

    class Meta:
        abstract = True


class ControlLicense(DatedModel):
    descricao = models.CharField(
        max_length=200,
        verbose_name=_(u'Descrição da licença'),
        help_text=_(u'Coloque uma identificação da licença')
    )
    orgaos_renovaveis = models.CharField(
        max_length=200,
        verbose_name=_(u'Orgaos disponiveis para renovacao'),
        choices=settings.ORGAOS_CHOICES
    )
    date_emissao = models.DateTimeField(
        _(u'data de emissão')
    )
    date_vencimento = models.DateTimeField(
        _(u'data de vencimento')
    )

    def __unicode__(self):
        return self.descricao
