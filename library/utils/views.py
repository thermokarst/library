from django.views.generic import DetailView, UpdateView
from django.http import HttpResponseRedirect


class SlugPKMixin:
    query_pk_and_slug = True

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.kwargs.get(self.pk_url_kwarg) is None:
            return HttpResponseRedirect(self.object.get_absolute_url())
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class SlugPKDetailView(SlugPKMixin, DetailView):
    pass


class SlugPKUpdateView(SlugPKMixin, UpdateView):
    pass
