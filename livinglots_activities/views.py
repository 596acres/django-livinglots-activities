from django.views.generic import ListView

from actstream.models import Action


class BaseActivityListView(ListView):
    model = Action
    paginate_by = 4
    template_name = 'livinglots/activities/activity_list.html'
