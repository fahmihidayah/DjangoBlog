from django_tables2 import Table, TemplateColumn
from .models import Post


class PostTable(Table):

    detail = TemplateColumn(template_name='table/detail.html')

    edit = TemplateColumn(template_name='table/edit.html')

    delete = TemplateColumn(template_name='table/delete.html')

    class Meta:
        model = Post
        fields = ["slug", "title", "is_published", "created", "updated"]
        template_name = 'django_tables2/bootstrap4.html'


