import pytest
from unittest.mock import Mock
from payment import charge_customer, PaymentFailedError


@pytest.fixture
def mock_api():
    return Mock()


def test_charge_succeeds_first_try(mock_api):
    mock_api.charge.return_value = {"status": 200}

    result = charge_customer(mock_api, 100)

    assert result == {"status": 200}
    assert mock_api.charge.call_count == 1


def test_charge_succeeds_after_one_retry(mock_api):
    mock_api.charge.side_effect = [
        {"status": 500},
        {"status": 200},
    ]

    result = charge_customer(mock_api, 100)

    assert result == {"status": 200}
    assert mock_api.charge.call_count == 2


def test_charge_fails_after_max_retries(mock_api):
    mock_api.charge.side_effect = [
        {"status": 500},
        {"status": 500},
        {"status": 500},
    ]

    with pytest.raises(PaymentFailedError, match="failed after 3 attempts"):
        charge_customer(mock_api, 100, max_retries=3)

    assert mock_api.charge.call_count == 3


@pytest.mark.parametrize("bad_amount", [0, -1, -100])
def test_invalid_amount_raises_without_calling_api(mock_api, bad_amount):
    with pytest.raises(ValueError, match="must be positive"):
        charge_customer(mock_api, bad_amount)

    mock_api.charge.assert_not_called()
