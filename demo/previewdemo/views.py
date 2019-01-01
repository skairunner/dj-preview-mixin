from django.views.generic import DetailView, CreateView, UpdateView
from dj_preview_mixin.mixins import PreviewMixin
from .models import GenericModel

class Create(CreateView):
    model = GenericModel
    fields = ['data']
    template_name = 'genericmodel_create.html'

class Edit(PreviewMixin, UpdateView):
    model = GenericModel
    fields = ['data']
    template_name = 'genericmodel_form.html'

    def preprocess_preview(self, form, context):
        context['data'] = form.cleaned_data['data']

class Detail(DetailView):
    model = GenericModel
    template_name = 'genericmodel_detail.html'
