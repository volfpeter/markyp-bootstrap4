from markyp_bootstrap4.popovers import *

def test_enable_auto_dismiss():
    assert enable_auto_dismiss.markup == "\n".join((
        "<script >",
        "$('.popover-dismiss').popover({ trigger: 'focus' })",
        "</script>"
    ))

def test_enable_popovers():
    assert enable_popovers.markup == "\n".join((
        "<script >",
        "$(function () { $('[data-toggle=\"popover\"]').popover() })",
        "</script>"
    ))

def test_Placement():
    assert Placement.TOP == "top"
    assert Placement.BOTTOM == "bottom"
    assert Placement.LEFT == "left"
    assert Placement.RIGHT == "right"

def test_popover():
    assert popover("Content") == {
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover"
    }

    assert popover("Content", title="Title") == {
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover",
        "title": "Title"
    }

    assert popover("Content", placement=Placement.TOP) == {
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover"
    }

    assert popover("Content", placement=Placement.BOTTOM) == {
        "data-content": "Content",
        "data-placement": "bottom",
        "data-toggle": "popover"
    }

    assert popover("Content", placement=Placement.LEFT) == {
        "data-content": "Content",
        "data-placement": "left",
        "data-toggle": "popover"
    }

    assert popover("Content", placement=Placement.RIGHT) == {
        "data-content": "Content",
        "data-placement": "right",
        "data-toggle": "popover"
    }

    assert popover("Content", auto_dismissed=True) == {
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover",
        "tabindex": 0,
        "data-trigger": "focus"
    }

    assert popover("Content", container="body") == {
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover",
        "data-container": "body"
    }

    assert popover(
        "Content",
        auto_dismissed=True,
        container="body",
        placement=Placement.TOP,
        title="Title",
        attr1=11, attr2=22) == \
    {
        "attr1": 11,
        "attr2": 22,
        "data-content": "Content",
        "data-placement": "top",
        "data-toggle": "popover",
        "tabindex": 0,
        "data-trigger": "focus",
        "data-container": "body",
        "title": "Title"
    }
