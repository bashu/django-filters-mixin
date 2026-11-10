from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import RequestFactory

import django_filters
import pytest
from django_filters.views import FilterView

from filters.views import FilterMixin

PAGE_SIZE = 2


class UserFilterSet(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ["is_staff"]


class UserListView(FilterMixin, FilterView):
    filterset_class = UserFilterSet
    template_name = "filters/user_list.html"
    paginate_by = PAGE_SIZE
    queryset = User.objects.order_by("username")


@pytest.mark.django_db
def test_pagination_with_filtering():
    for name in ("alice", "bob", "carol"):
        User.objects.create(username=name, is_staff=True)
    User.objects.create(username="dave", is_staff=False)

    request = RequestFactory().get("/", {"page": "2", "is_staff": "true"})
    response = UserListView.as_view()(request)

    response.render()

    assert response.status_code == HTTPStatus.OK
    assert response.context_data["filter"].is_bound
    assert response.context_data["page_obj"].number == 2  # noqa: PLR2004
    assert [u.username for u in response.context_data["object_list"]] == ["carol"]
    assert response.content.decode().split() == ["carol", "page", "2", "of", "2"]


@pytest.mark.django_db
def test_filtering_without_pagination_parameter():
    User.objects.create(username="alice", is_staff=True)
    User.objects.create(username="bob", is_staff=False)

    request = RequestFactory().get("/", {"is_staff": "false"})
    response = UserListView.as_view()(request)
    response.render()

    assert response.status_code == HTTPStatus.OK
    assert response.content.decode().split() == ["bob", "page", "1", "of", "1"]
