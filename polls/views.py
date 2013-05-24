# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll,Choice
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You din't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))