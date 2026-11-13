from __future__ import annotations

from typing import TYPE_CHECKING

from django_filters import views as filters_views

if TYPE_CHECKING:
    from typing import Any

    from django_filters import FilterSet

__all__ = ["FilterMixin"]


class FilterMixin(filters_views.FilterMixin):
    """Drop the ``page`` query parameter before it reaches the filterset.

    This lets pagination and filtering be combined in one view without
    ``page`` being treated as filter data.
    """

    def get_filterset_kwargs(self, filterset_class: type[FilterSet]) -> dict[str, Any]:
        kwargs = super().get_filterset_kwargs(filterset_class)

        if kwargs["data"] is not None and "page" in kwargs["data"]:
            data = kwargs["data"].copy()
            del data["page"]
            kwargs["data"] = data

        return kwargs
