from django.shortcuts import get_object_or_404, redirect,  render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown

class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')

class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'

class BirthdayCreateView(BirthdayMixin ,CreateView):
    pass

class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass

# def birthday(request, pk=None):
#     if pk is not None:
#         instance = get_object_or_404(Birthday, pk=pk)
#     else:
#         instance = None
#     form = BirthdayForm(request.POST or None, instance=instance)
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context)

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass