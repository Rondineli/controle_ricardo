# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

from license_control.views import ViewPage
from filiais.models import BranchLicense

PAGE_NAME = 'filiais'


class BranchListView(ViewPage, ListView):
    PAGE_NAME = PAGE_NAME
    model = BranchLicense


class BranchCreateView(ViewPage, CreateView):
    PAGE_NAME = PAGE_NAME
    model = BranchLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Filial cadastrada com sucesso')
        )
        return super(BranchCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Filial: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class BranchUpdateView(ViewPage, UpdateView):
    PAGE_NAME = PAGE_NAME
    model = BranchLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Filial cadastrada com sucesso')
        )
        return super(BranchUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Filial: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class BranchDeleteView(ViewPage, DeleteView):
    PAGE_NAME = PAGE_NAME
    model = BranchLicense
    http_method_names = ['post', ]
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, _(u'Fialial removido com sucesso'))
        return super(BranchDeleteView, self).get_success_url()
