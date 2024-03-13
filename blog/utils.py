menu = [
    {'title': 'about', 'url_name': 'about'},
    # {'title': 'add page', 'url_name': 'add_page'},
    {'title': 'contacts', 'url_name': 'contacts'},
    # {'title': 'login', 'url_name': 'users:login'},
]


class DataMixin:
    title_page = None
    selected_cat = None
    paginate_by = 3
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        if self.selected_cat is not None:
            self.extra_context['selected_cat'] = self.selected_cat

    def get_mixin_context(self, context, **kwargs):
        context['selected_cat'] = None
        context.update(kwargs)
        return context

