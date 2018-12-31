from django import forms

class PreviewMixin:
    edit_button_name = 'edit'
    preview_button_name = 'preview'

    # if form valid, check if it's a preview request or a submit
    def form_valid(self, form):
        if self.request.POST.get(self.preview_button_name) or \
                self.request.POST.get(self.edit_button_name):
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

    # This is where you can inject extra processing
    # into the context, if it is a preview
    def preprocess_form(self, form, context):
        pass

    # inject necessary data for preview
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        if self.request.POST.get(self.preview_button_name):
            kwargs['preview'] = True
            kwargs['form']._meta.widgets = {field_name: forms.HiddenInput() for field_name in self.model._meta.get_all_field_names()}
            self.preprocess_form(kwargs['form'], kwargs)
        return kwargs
