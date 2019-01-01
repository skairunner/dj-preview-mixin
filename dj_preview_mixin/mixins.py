from django import forms

class PreviewMixin:
    edit_button_name = 'edit'
    preview_button_name = 'preview'

    # If form is valid and it's not a preview or edit request
    def form_valid_nopreview(self, form):
        return super().form_valid(form)

    # if form valid, check if it's a preview request or a submit
    def form_valid(self, form):
        if self.request.POST.get(self.preview_button_name) or \
                self.request.POST.get(self.edit_button_name):
            return self.render_to_response(self.get_context_data(form=form))
        return self.form_valid_nopreview(form)

    # This is where you can inject extra processing
    # into the context, if it is a preview
    def preprocess_preview(self, form, context):
        pass

    # inject necessary data for preview
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        if self.request.POST.get(self.preview_button_name):
            kwargs['ispreview'] = True
            self.preprocess_preview(kwargs['form'], kwargs)
        return kwargs
