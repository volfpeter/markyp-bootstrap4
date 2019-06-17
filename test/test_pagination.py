from markyp_bootstrap4.pagination import *

def test_PaginationPosition():
    assert PaginationPosition.START is None
    assert PaginationPosition.CENTER == "justify-content-center"
    assert PaginationPosition.END == "justify-content-end"

def test_PaginationSize():
    assert PaginationSize.DEFAULT is None
    assert PaginationSize.LARGE == "pagination-lg"
    assert PaginationSize.SMALL == "pagination-sm"

def test_base_page_item():
    assert base_page_item().markup == '<li class="page-item"></li>'
    assert base_page_item("First", "Second", class_="my-pi").markup == (
        '<li class="page-item my-pi">First Second</li>'
    )
    assert base_page_item("Content", active=True, class_="my-pi").markup == (
        '<li class="page-item active my-pi">Content</li>'
    )
    assert base_page_item("Content", disabled=True, class_="my-pi").markup == (
        '<li class="page-item disabled my-pi">Content</li>'
    )
    assert base_page_item("Content", attr=42).markup == (
        '<li attr="42" class="page-item">Content</li>'
    )

def test_page_item():
    assert page_item("Foo").markup == (
        '<li class="page-item">'
            '<a class="page-link">Foo</a>'
        '</li>'
    )
    assert page_item("Foo", active=True, class_="my-pi").markup == (
        '<li class="page-item active my-pi">'
            '<a class="page-link">Foo</a>'
        '</li>'
    )
    assert page_item("Foo", disabled=True, class_="my-pi").markup == (
        '<li class="page-item disabled my-pi">'
            '<a class="page-link">Foo</a>'
        '</li>'
    )
    assert page_item("Foo", attr=42).markup == (
        '<li class="page-item">'
            '<a attr="42" class="page-link">Foo</a>'
        '</li>'
    )
    assert page_item("Foo", class_="my-pi", link_class="my-pl").markup == (
        '<li class="page-item my-pi">'
            '<a class="page-link my-pl">Foo</a>'
        '</li>'
    )

def test_page_link():
    assert page_link().markup == '<a class="page-link"></a>'
    assert page_link("Foo").markup == '<a class="page-link">Foo</a>'
    assert page_link("Foo", class_="my-pl", attr=42).markup == '<a attr="42" class="page-link my-pl">Foo</a>'

def test_pagination():
    assert pagination("First", "Second", wrap_in_nav=False).markup == "\n".join((
        '<ul class="pagination">',
            'First',
            'Second',
        '</ul>'
    ))
    assert pagination("First", "Second").markup == "\n".join((
        '<nav aria-label="Pagination">',
            '<ul class="pagination">',
                'First',
                'Second',
            '</ul>',
        '</nav>'
    ))
    assert pagination("First", "Second", aria_label=None).markup == "\n".join((
        '<nav >',
            '<ul class="pagination">',
                'First',
                'Second',
            '</ul>',
        '</nav>'
    ))
    assert pagination("First", "Second", class_="my-p").markup == "\n".join((
        '<nav aria-label="Pagination">',
            '<ul class="pagination my-p">',
                'First',
                'Second',
            '</ul>',
        '</nav>'
    ))
    assert pagination("First", "Second", class_="my-p", position=PaginationPosition.CENTER, size=PaginationSize.LARGE).markup == "\n".join((
        '<nav aria-label="Pagination">',
            '<ul class="pagination pagination-lg justify-content-center my-p">',
                'First',
                'Second',
            '</ul>',
        '</nav>'
    ))
    assert pagination("First", "Second", class_="my-p", attr=42).markup == "\n".join((
        '<nav aria-label="Pagination">',
            '<ul attr="42" class="pagination my-p">',
                'First',
                'Second',
            '</ul>',
        '</nav>'
    ))
