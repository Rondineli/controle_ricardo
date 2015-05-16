# -*- coding: utf-8 -*-
import logging
import datetime
import time
from django.conf import settings
from django.core.mail import send_mail

from license_control.models import ControlLicense

logger = logging.getLogger("license.control")


class SendMailTasks(object):

    def run(self):
        recipient_list = []
        date_now = datetime.datetime.today()
        date_expire = datetime.date.fromordinal(date_now.toordinal() + 31)
        while True:
            list_objects_due = []
            try:
                objects = ControlLicense.objects.filter(
                    date_vencimento__lte=date_expire
                )
            except Exception as e:
                logger.error(u'Problema ao se conectar ao banco: {}'.format(
                    unicode(e)
                ))
            if objects:
                for item in objects:
                    list_objects_due.append({
                        "Licença": unicode(item.descricao),
                        "Vencimento": item.date_vencimento.strftime("%d/%m/%Y"),
                        "Emitido em:": item.date_emissao.strftime("%d/%m/%Y"),
                    })
                for recipient in settings.ADMINS:
                    recipient_list.append(recipient[1])
                subject = "Relatório de licenças a vencer"
                body = "Lista de licenças: {}".format(
                    list_objects_due
                )
                from_email = "licenças@localhost"
                logger.info(
                    "send email from: {},{},{},{}".format(
                        subject,
                        body,
                        from_email,
                        recipient_list
                    )
                )
                send_mail(
                    subject,
                    body,
                    from_email,
                    recipient_list
                )
            time.sleep(57600)
