from django_tables2 import Table, TemplateColumn
from .models import Category


class CategoryTable(Table):

    detail = TemplateColumn(template_name='table/detail.html')

    edit = TemplateColumn(template_name='table/edit.html')

    delete = TemplateColumn(template_name='table/delete.html')

    class Meta:
        model = Category
        fields = ["slug", "name", "description", "created", "updated"]
        template_name = 'django_tables2/bootstrap4.html'


