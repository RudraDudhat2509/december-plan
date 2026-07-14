import pytest
from inventory import apply_discount_batch


@pytest.mark.parametrize("bad_amount", [-1, 101])
def test_bad_inputs(bad_amount):
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        apply_discount_batch([], bad_amount)


def test_empty():
    result = apply_discount_batch([], 1)
    assert result == []


def test_item_discount():
    items = [{"name": "Widget", "price": 100}]
    result = apply_discount_batch(items, 10)
    assert result[0]["price"] == 90

def test_filter():
    items = [{"name": "Widget", "price": 100},{"name": "Widget2", "price": 10},{"name": "Widget", "price": 10} ]
    result=apply_discount_batch(items,5,20)
    assert len(result)==1
def test_immumatabilty():
    items = [{"name": "Widget", "price": 100},{"name": "Widget2", "price": 10},{"name": "Widget", "price": 10}]
    copy=items
    apply_discount_batch(items,5)
    assert copy == items 