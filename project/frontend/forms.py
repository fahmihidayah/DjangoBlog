from django.forms import Form, CharField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Fieldset, Submit, Button

class SearchForm(Form):

    keyword = CharField(max_length=255, label="Kata kunci", empty_value='', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'keyword'
            ),
        )
