import pytest

from app.restore_names import restore_names


@pytest.fixture
def test_users() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Alex Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Johny Adams",
        }
    ]


def test_restore_names(test_users: list) -> None:
    restore_names(test_users)
    assert test_users[0]["first_name"] == "Alex"
    assert test_users[1]["first_name"] == "Johny"
