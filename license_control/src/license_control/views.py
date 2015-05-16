# -*- coding: utf-8 -*-
import logging
import datetime

from django.conf import settings
from django.http import HttpResponse

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    View
)

from .models import ControlLicense

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

PAGE_NAME = 'licenças'


class ViewPage(object):
    PAGE_NAME = ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ViewPage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ViewPage, self).get_context_data(*args, **kwargs)
        if not 'page' in context:
            context['page_name'] = self.PAGE_NAME
        return context


class ApiView(View):
    logging.basicConfig()
    logger = logging.getLogger("controle_financeiro")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        api_key = request.GET.get('key')
        if not int(api_key) == int(settings.API_KEY):
            self.logger.error(u'API_KEY inválida')
            return HttpResponse(status=401)
        return super(ApiView, self).dispatch(request, *args, **kwargs)


class LicensingCreateView(ViewPage, CreateView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Licença cadastrada com sucesso')
        )
        return super(LicensingCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Licença: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class LicensingUpdateView(ViewPage, UpdateView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Licença cadastrada com sucesso')
        )
        return super(LicensingUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Licença: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class LicensingHomeView(ViewPage, View):
    template_name = 'license_control/home.html'

    def get(self, request, *args, **kwargs):
        date_now = datetime.datetime.today()
        date_expire = datetime.date.fromordinal(date_now.toordinal() + 31)
        object_list = ControlLicense.objects.all()
        objects_a_vencer = object_list.filter(
            date_vencimento__lte=date_expire
        )
        list_objects = []

        for item_venc in objects_a_vencer:
            setattr(item_venc, 'vencido', True)
            list_objects.append(item_venc.pk)

        for item in object_list:
            if item.id in list_objects:
                setattr(item, 'vencido', True)
        context = {
            'object_list': object_list,
            'objects_a_vencer': objects_a_vencer
        }
        return render(request, self.template_name, context)


class LicensingDeleteView(ViewPage, DeleteView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    http_method_names = ['post', ]
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, _(u'Licença removido com sucesso'))
        return super(LicensingDeleteView, self).get_success_url()

"""
Cadastro de filiais

"""


class BranchCreateView(ViewPage, CreateView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Licença cadastrada com sucesso')
        )
        return super(BranchCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Licença: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class BranchUpdateView(ViewPage, UpdateView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _(u'Licença cadastrada com sucesso')
        )
        return super(BranchUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(u'Erro ao cadastrar Licença: {}'.format(form.errors))
        )
        return HttpResponseRedirect(self.success_url)


class BranchDeleteView(ViewPage, DeleteView):
    PAGE_NAME = PAGE_NAME
    model = ControlLicense
    http_method_names = ['post', ]
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, _(u'Licença removido com sucesso'))
        return super(BranchDeleteView, self).get_success_url()
