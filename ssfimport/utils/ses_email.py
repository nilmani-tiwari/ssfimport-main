from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template


def send_email(subject=None, message=None, html_message=None, from_email="Tickle.Life <social@tickle.life>", recipient_list=[], template=None, data=None, fail_silently=False):

    if template:
        html = get_template(template)
        data = data

        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently,
            html_message=html.render(data)
        )
    else:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently
        )

    return
