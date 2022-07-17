import sys
sys.dont_write_bytecode = True

from django.db.models import Count, Q

from .models import OutputTagModel


def common(request):
    context = {
        'tags': OutputTagModel.objects.all()
    }
    return context