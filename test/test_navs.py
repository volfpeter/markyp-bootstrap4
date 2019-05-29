from markyp_html import block
from markyp_bootstrap4.navs import *

def test_NavPosition():
    assert NavPosition.CENTER == "justify-content-center"
    assert NavPosition.DEFAULT is None
    assert NavPosition.END == "justify-content-end"

def test_NavStyle():
    assert NavStyle.DEFAULT is None
    assert NavStyle.PILLS == "nav-pills"
    assert NavStyle.TABS == "nav-tabs"

def test_nav():
    assert nav().markup == '<ul class="nav"></ul>'
    assert nav("First", "Second").markup == "\n".join((
        '<ul class="nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav").markup == "\n".join((
        '<ul class="nav my-nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav", fill=True, justified=True).markup == "\n".join((
        '<ul class="nav nav-fill nav-justified my-nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav", nav_position=NavPosition.CENTER, nav_style=NavStyle.PILLS).markup == "\n".join((
        '<ul class="nav justify-content-center nav-pills my-nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav", nav_position=NavPosition.END, nav_style=NavStyle.TABS).markup == "\n".join((
        '<ul class="nav justify-content-end nav-tabs my-nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav", nav_position=NavPosition.DEFAULT, nav_style=NavStyle.DEFAULT).markup == "\n".join((
        '<ul class="nav my-nav">',
            'First', 'Second',
        '</ul>'
    ))
    assert nav("First", "Second", class_="my-nav", attr=42).markup == "\n".join((
        '<ul attr="42" class="nav my-nav">',
            'First', 'Second',
        '</ul>'
    ))

    assert nav("First", "Second", class_="my-nav", attr=42, factory=block.nav).markup == "\n".join((
        '<nav attr="42" class="nav my-nav">',
            'First', 'Second',
        '</nav>'
    ))

def test_nav_item():
    assert nav_item().markup ==\
        '<li class="nav-item"></li>'
    assert nav_item("Content", class_="my-item").markup ==\
        '<li class="nav-item my-item">Content</li>'
    assert nav_item("Content", class_="my-item", active=True).markup ==\
        '<li class="nav-item active my-item">Content</li>'
    assert nav_item("Content", class_="my-item", disabled=True).markup ==\
        '<li class="nav-item disabled my-item">Content</li>'
    assert nav_item("Content", class_="my-item", is_dropdown=True).markup ==\
        '<li class="nav-item dropdown my-item">Content</li>'
    assert nav_item("Content", class_="my-item", active=True, disabled=True, is_dropdown=True, attr=42).markup ==\
        '<li attr="42" class="nav-item active disabled dropdown my-item">Content</li>'

def test_nav_link():
    assert nav_link().markup ==\
        '<a class="nav-link"></a>'
    assert nav_link("Content", class_="my-link").markup ==\
        '<a class="nav-link my-link">Content</a>'
    assert nav_link("Content", class_="my-link", active=True, disabled=True).markup ==\
        '<a class="nav-link active disabled my-link">Content</a>'
    assert nav_link("Content", class_="my-link", active=True, disabled=True, is_nav_item=True, attr=42).markup ==\
        '<a attr="42" class="nav-link nav-item active disabled my-link">Content</a>'

def test_tab_link():
    assert tab_link(pane_id="tab-pane-1").markup == (
        '<li class="nav-item">'
            '<a href="#tab-pane-1" role="tab" data-toggle="tab" aria-controls="tab-pane-1" '
                'aria-selected="false" class="nav-link">'
            '</a>'
        '</li>'
    )

    assert tab_link(pane_id="tab-pane-1", class_="my-tl", active=True, disabled=True, attr=42).markup == (
        '<li class="nav-item">'
            '<a href="#tab-pane-1" role="tab" attr="42" data-toggle="tab" aria-controls="tab-pane-1" '
                'aria-selected="true" class="nav-link active disabled my-tl">'
            '</a>'
        '</li>'
    )


def test_navigated_tabs():
    nav_element, tab_element = navigated_tabs(id="example")
    assert nav_element.markup ==\
        '<ul id="example-nav" class="nav nav-tabs"></ul>'
    assert tab_element.markup ==\
        '<div id="example-tab-content" class="tab-content"></div>'

    nav_element, tab_element = navigated_tabs(
        ("Title 0", "Content 0"),
        ("Title 1", "Content 1"),
        id="example"
    )
    assert nav_element.markup == "\n".join((
        '<ul id="example-nav" class="nav nav-tabs">',
            ('<li class="nav-item">'
                '<a href="#example-pane-0" role="tab" id="example-nav-0" data-toggle="tab" '
                    'aria-controls="example-pane-0" aria-selected="true" class="nav-link active">Title 0</a>'
            '</li>'),
            ('<li class="nav-item">'
                '<a href="#example-pane-1" role="tab" id="example-nav-1" data-toggle="tab" '
                    'aria-controls="example-pane-1" aria-selected="false" class="nav-link">Title 1</a>'
            '</li>'),
        '</ul>'
    ))
    assert tab_element.markup == "\n".join((
        '<div id="example-tab-content" class="tab-content">',
            '<div role="tabpanel" id="example-pane-0" aria-labelled-by="example-nav-0" class="tab-pane fade show active">',
                'Content 0',
            '</div>',
            '<div role="tabpanel" id="example-pane-1" aria-labelled-by="example-nav-1" class="tab-pane fade">',
                'Content 1',
            '</div>',
        '</div>'
    ))

    nav_element, tab_element = navigated_tabs(
        ("Title 0", "Content 0"),
        ("Title 1", "Content 1"),
        id="example",
        active_index=1
    )
    assert nav_element.markup == "\n".join((
        '<ul id="example-nav" class="nav nav-tabs">',
            ('<li class="nav-item">'
                '<a href="#example-pane-0" role="tab" id="example-nav-0" data-toggle="tab" '
                    'aria-controls="example-pane-0" aria-selected="false" class="nav-link">Title 0</a>'
            '</li>'),
            ('<li class="nav-item">'
                '<a href="#example-pane-1" role="tab" id="example-nav-1" data-toggle="tab" '
                    'aria-controls="example-pane-1" aria-selected="true" class="nav-link active">Title 1</a>'
            '</li>'),
        '</ul>'
    ))
    assert tab_element.markup == "\n".join((
        '<div id="example-tab-content" class="tab-content">',
            '<div role="tabpanel" id="example-pane-0" aria-labelled-by="example-nav-0" class="tab-pane fade">',
                'Content 0',
            '</div>',
            '<div role="tabpanel" id="example-pane-1" aria-labelled-by="example-nav-1" class="tab-pane fade show active">',
                'Content 1',
            '</div>',
        '</div>'
    ))

    nav_element, tab_element = navigated_tabs(
        ("Title 0", "Content 0"),
        ("Title 1", "Content 1"),
        id="example",
        content_attributes={"c-attr": 42},
        content_class="my-content",
        item_attributes={"i-attr": 42},
        item_class="my-item",
        nav_attributes={"n-attr": 42},
        nav_class="my-nav",
        nav_fill=True,
        nav_justified=True,
        nav_position=NavPosition.CENTER,
        pane_attributes={"p-attr": 42},
        pane_class="my-pane"
    )
    assert nav_element.markup == "\n".join((
        '<ul id="example-nav" n-attr="42" class="nav nav-fill nav-justified justify-content-center nav-tabs my-nav">',
            ('<li class="nav-item">'
                '<a href="#example-pane-0" role="tab" id="example-nav-0" i-attr="42" data-toggle="tab" '
                    'aria-controls="example-pane-0" aria-selected="true" class="nav-link active my-item">Title 0</a>'
            '</li>'),
            ('<li class="nav-item">'
                '<a href="#example-pane-1" role="tab" id="example-nav-1" i-attr="42" data-toggle="tab" '
                    'aria-controls="example-pane-1" aria-selected="false" class="nav-link my-item">Title 1</a>'
            '</li>'),
        '</ul>'
    ))
    assert tab_element.markup == "\n".join((
        '<div id="example-tab-content" c-attr="42" class="tab-content my-content">',
            '<div role="tabpanel" id="example-pane-0" p-attr="42" aria-labelled-by="example-nav-0" class="tab-pane fade show active my-pane">',
                'Content 0',
            '</div>',
            '<div role="tabpanel" id="example-pane-1" p-attr="42" aria-labelled-by="example-nav-1" class="tab-pane fade my-pane">',
                'Content 1',
            '</div>',
        '</div>'
    ))
