from re import template
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse
import textwrap
import urllib.parse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        qs = urllib.parse.urlparse(url).query
        id = qs[-4:]

        subject = "【あしあと】貴社サイトにアクセスがありました"
        message = id
        from_email = "decube.ashiato@gmail.com"
        recipient_list = ["web.decube@gmail.com"]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse('無効なヘッダが検出されました。')
        return render(request, 'decube/redirect.html')
    template_name = 'index.html'

class RedirectView(View):
    template_name = 'redirect.html'
    