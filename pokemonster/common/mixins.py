class FormWidgetsMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'
            field.widget.attrs['class'] += ' mb-4 mt-1'
            if field.label:
                field.widget.attrs['placeholder'] = f'Enter {field.label.lower()}'
            else:
                field.widget.attrs['placeholder'] = f'Enter value'



class DisableFieldsMixin:
    fields = {}

    def _disable_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
