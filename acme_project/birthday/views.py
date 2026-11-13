from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from .utils import calculate_birthday_countdown
from .forms import BirthdayForm
from .models import Birthday


class BirthdayMixin:
    model = Birthday

    def get_success_url(self):
        return reverse_lazy('birthday:detail', args=(self.object.pk,))

class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context

class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'

class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass

class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
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
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BirthdayForm(instance=self.object)
        return context