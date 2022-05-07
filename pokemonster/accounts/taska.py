from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError

from pokemonster.celery import app
from pokemonster.settings import DEFAULT_FROM_EMAIL

logger = get_task_logger(__name__)


@shared_task
def send_email_task(self, to, subject, message):
    logger.info(f"from={DEFAULT_FROM_EMAIL}, {to=}, {subject=}, {message=}")
    try:
        logger.info("About to send_mail")
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
    except BadHeaderError:
        logger.info("BadHeaderError")
    except Exception as e:
        logger.error(e)


@shared_task
def five_seconds():
    time.sleep(10)
    return 'finished'
