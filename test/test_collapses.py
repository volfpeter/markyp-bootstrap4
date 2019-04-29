from markyp_bootstrap4.collapses import *

def test_a_args_for():
    assert a_args_for("foo") == {
        "href": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": False
    }
    assert a_args_for("foo", expanded=True) == {
        "href": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": True
    }
    assert a_args_for("foo", foo="foo", bar=42) == {
        "foo": "foo",
        "bar": 42,
        "href": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": False
    }

def test_button_args_for():
    assert button_args_for("foo") == {
        "data-target": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": False
    }
    assert button_args_for("foo", expanded=True) == {
        "data-target": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": True
    }
    assert button_args_for("foo", foo="foo", bar=42) == {
        "foo": "foo",
        "bar": 42,
        "data-target": "#foo",
        "data-toggle": "collapse",
        "aria-controls": "foo",
        "aria-expanded": False
    }

def test_collapse():
    assert collapse(identifier="collapse-id").markup ==\
        '<div id="collapse-id" class="collapse"></div>'
    assert collapse("First", "Second", identifier="collapse-id").markup ==\
        '<div id="collapse-id" class="collapse">\nFirst\nSecond\n</div>'
    assert collapse("First", "Second", identifier="collapse-id", class_="my-collapse").markup ==\
        '<div id="collapse-id" class="collapse my-collapse">\nFirst\nSecond\n</div>'
    assert collapse("First", "Second", identifier="collapse-id", class_="my-collapse", show=True).markup ==\
        '<div id="collapse-id" class="collapse show my-collapse">\nFirst\nSecond\n</div>'
    assert collapse("First", "Second", identifier="collapse-id", class_="my-collapse", show=True, foo="foo", bar="bar").markup ==\
        '<div id="collapse-id" foo="foo" bar="bar" class="collapse show my-collapse">\nFirst\nSecond\n</div>'
    assert collapse("First", "Second", identifier="collapse-id", accordion_id="acc-1", class_="my-collapse", show=True, foo="foo", bar="bar").markup ==\
        '<div id="collapse-id" foo="foo" bar="bar" data-parent="#acc-1" class="collapse show my-collapse">\nFirst\nSecond\n</div>'
