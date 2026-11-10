from django_filters import views as filters_views

__all__ = ["FilterMixin"]


class FilterMixin(filters_views.FilterMixin):
    """Drop the ``page`` query parameter before it reaches the filterset.

    This lets pagination and filtering be combined in one view without
    ``page`` being treated as filter data.
    """

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super().get_filterset_kwargs(filterset_class)
        if kwargs["data"] is not None and "page" in kwargs["data"]:
            data = kwargs["data"].copy()
            del data["page"]
            kwargs["data"] = data
        return kwargs
