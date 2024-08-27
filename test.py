import pytest
import responses
from main import get_random_cat_image

@responses.activate
def test_successful_cat_image_request():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        json=[{"url": "https://example.com/cat.jpg"}],
        status=200
    )

    url = get_random_cat_image()
    assert url == "https://example.com/cat.jpg"

@responses.activate
def test_unsuccessful_cat_image_request():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        status=404
    )

    url = get_random_cat_image()
    assert url is None