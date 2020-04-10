from django.views import generic

from .models import User, Interval


class IndexView(generic.ListView):
    template_name = 'collector/index.html'

    def get_queryset(self):
        return User.objects.get(pk=1).interval_set.all().order_by('-start_time')[:5]
