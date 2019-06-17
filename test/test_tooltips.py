from markyp_bootstrap4.tooltips import *

def test_enable_tooltips():
    assert enable_tooltips.markup == "\n".join((
        "<script >",
        "$(function () { $('[data-toggle=\"tooltip\"]').tooltip() })",
        "</script>"
    ))

def test_Placement():
    assert Placement.TOP == "top"
    assert Placement.BOTTOM == "bottom"
    assert Placement.LEFT == "left"
    assert Placement.RIGHT == "right"

def test_tooltip():
    assert tooltip("Title") == {
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "top"
    }

    assert tooltip("<h1>Title</h1>") == {
        "title": "<h1>Title</h1>",
        "data-toggle": "tooltip",
        "data-placement": "top"
    }

    assert tooltip("Title", placement=Placement.TOP) == {
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "top"
    }

    assert tooltip("Title", placement=Placement.BOTTOM) == {
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "bottom"
    }

    assert tooltip("Title", placement=Placement.LEFT) == {
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "left"
    }

    assert tooltip("Title", placement=Placement.RIGHT) == {
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "right"
    }

    assert tooltip("Title", attr1=11, attr2=22) == {
        "attr1": 11,
        "attr2": 22,
        "title": "Title",
        "data-toggle": "tooltip",
        "data-placement": "top"
    }
