# Previews module

This module provides a mixin for easily augmenting a form view with a preview at the same URL.

## PreviewMixin
PreviewMixin augments a single-form view by providing the capability to process a "preview" command. The form is processed through the `process_form` function before being provided to the special preview form in the same page's template. The `ispreview` boolean variable will be set to `True` to help the template decide whether to render the preview or the base form.

PreviewMixin overloads:
1. `get_context_data()`
2. `form_valid()`

### New members:
* `edit_button_name`: The `name` attr for the button that triggers a return to the form view. Default is 'edit'.
* `preview_button_name`: The `name` attr for the button that triggers a preview. Default is 'preview'.

### New methods:

`def preprocess_preview(self, form, context)`
**
Allows the user to process the preview for viewing. Previewed data needs to be manually added to the context.

**form**: The form that is being processed, after it is validated
**context**: The context for the template renderer, like `get_context_data()`'s kwargs

`def form_valid_nopreview(self, form)`

This method is called if the form is valid and not an edit or preview action, and is equivalent to a typical form's `form_valid()`.

**form**: The form that is being processed and is validated

### New template variables:
* `ispreview`: `True` if preview has been triggered, otherwise `None`.

### Example usage
Model
```python
class MyModel(models.Model):
    myvar = models.IntegerField()
```
View
```python
class EditModelView(PreviewMixin, UpdateView):
    model = MyModel
    fields = ['myvar']

    def preprocess_form(self, form, context):
    	context['myvar'] = form.cleaned_data['myvar']
```
Template
```html
{% if preview %}
My var: {{ myvar }}
<form action='POST'>
  {% csrf_token %}
  {% for field in form %}
  {{ field.as_hidden }}
  {% endfor %}
  <input type='submit' name='edit' value='Keep editing'>
  <input type='submit' name='submit' value='Submit'>
</form>
{% else %}
<form action='POST'>
  {% csrf_token %}
  {{ form.as_p }}
  <input type='submit' name='preview' value='Preview'>
  <input type='submit' name='submit' value='Submit'>
</form>
```
