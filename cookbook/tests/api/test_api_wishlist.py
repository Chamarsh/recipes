import json

import pytest
from django.contrib import auth
from django.urls import reverse
from django_scopes import scopes_disabled

from cookbook.models import Wishlist

LIST_URL = 'api:wishlist-list'
DETAIL_URL = 'api:wishlist-detail'


@pytest.fixture()
def obj_1(space_1, u1_s1, recipe_1_s1):
    return Wishlist.objects.create(recipe=recipe_1_s1, created_by=auth.get_user(u1_s1), space=space_1)


@pytest.fixture
def obj_2(space_1, u1_s1, recipe_1_s1):
    return Wishlist.objects.create(recipe=recipe_1_s1, created_by=auth.get_user(u1_s1), space=space_1)


@pytest.mark.parametrize("arg", [
    ['a_u', 403],
    ['g1_s1', 201],
    ['u1_s1', 201],
    ['a1_s1', 201],
])
def test_add(arg, request, u1_s2, u2_s1, recipe_1_s1):
    c = request.getfixturevalue(arg[0])
    r = c.post(
        reverse(LIST_URL),
        {'recipe': recipe_1_s1.id},
        content_type='application/json'
    )
    response = json.loads(r.content)
    assert r.status_code == arg[1]
    if r.status_code == 201:
        assert response['recipe'] == recipe_1_s1.id
        r = c.get(reverse(DETAIL_URL, args={response['id']}))
        assert r.status_code == 200
        r = u2_s1.get(reverse(DETAIL_URL, args={response['id']}))
        assert r.status_code == 404
        r = u1_s2.get(reverse(DETAIL_URL, args={response['id']}))
        assert r.status_code == 404


def test_delete(u1_s1, u1_s2, obj_1):
    r = u1_s2.delete(
        reverse(
            DETAIL_URL,
            args={obj_1.id}
        )
    )
    assert r.status_code == 404

    r = u1_s1.delete(
        reverse(
            DETAIL_URL,
            args={obj_1.id}
        )
    )

    assert r.status_code == 204
    with scopes_disabled():
        assert Wishlist.objects.count() == 0
