from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    """docstring for IndexView"""
    # def __init__(self, arg):
    #     super(IndexView, self).__init__()
    #     self.arg = arg


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    """docstring for DetailView"""
    # def __init__(self, arg):
    #     super(DetailView, self).__init__()
    #     self.arg = arg


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    """docstring for ResultView"""
    # def __init__(self, arg):
    #     super(ResultView, self).__init__()
    #     self.arg = arg


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     # return render(request, "You're looking at question %s." % question_id )
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always retturn an HttpResponseRedirect after successfylly dealing wiith POST data.
        # This prevent data form being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    finally:
        pass
    return HttpResponse("You're voting on question %s." % question_id)
