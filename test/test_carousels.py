from markyp_bootstrap4.carousels import *

identifier = "identifier"

def test_carousel():
    assert carousel(identifier=identifier).markup == "\n".join([
        '<div data-ride="carousel" id="identifier" class="carousel slide">',
        '<ol class="carousel-indicators"></ol>',
        '<div class="carousel-inner"></div>',
        '<a href="#identifier" role="button" data-slide="prev" class="carousel-control-prev"><span aria-hdden="true" class="carousel-control-prev-icon"></span> <span class="sr-only">Previous</span></a>',
        '<a href="#identifier" role="button" data-slide="next" class="carousel-control-next"><span aria-hdden="true" class="carousel-control-next-icon"></span> <span class="sr-only">Next</span></a>',
        '</div>'
    ])

    assert carousel(identifier=identifier, add_controls=False).markup == "\n".join([
        '<div data-ride="carousel" id="identifier" class="carousel slide">',
        '<ol class="carousel-indicators"></ol>',
        '<div class="carousel-inner"></div>',
        '',
        '',
        '</div>'
    ])

    assert carousel(identifier=identifier, add_indicators=False).markup == "\n".join([
        '<div data-ride="carousel" id="identifier" class="carousel slide">',
        '',
        '<div class="carousel-inner"></div>',
        '<a href="#identifier" role="button" data-slide="prev" class="carousel-control-prev"><span aria-hdden="true" class="carousel-control-prev-icon"></span> <span class="sr-only">Previous</span></a>',
        '<a href="#identifier" role="button" data-slide="next" class="carousel-control-next"><span aria-hdden="true" class="carousel-control-next-icon"></span> <span class="sr-only">Next</span></a>',
        '</div>'
    ])

    assert carousel(identifier=identifier, add_controls=False, add_indicators=False,
                    interval=1000, keyboard=True, wrap=False, class_="my-slide", attr=42).markup == "\n".join([
        '<div attr="42" data-interval="1000" data-keyboard="true" data-wrap="false" data-ride="carousel" id="identifier" class="carousel slide my-slide">',
        '',
        '<div class="carousel-inner"></div>',
        '',
        '',
        '</div>'
    ])

    assert carousel("First", "Second", identifier=identifier).markup == "\n".join([
        '<div data-ride="carousel" id="identifier" class="carousel slide">',
        '<ol class="carousel-indicators">',
        '<li data-target="#identifier" data-slide-to="0" class="active"></li>',
        '<li data-target="#identifier" data-slide-to="1"></li>',
        '</ol>',
        '<div class="carousel-inner">',
        '<div class="carousel-item active">\nFirst\n</div>',
        '<div class="carousel-item">\nSecond\n</div>',
        '</div>',
        '<a href="#identifier" role="button" data-slide="prev" class="carousel-control-prev"><span aria-hdden="true" class="carousel-control-prev-icon"></span> <span class="sr-only">Previous</span></a>',
        '<a href="#identifier" role="button" data-slide="next" class="carousel-control-next"><span aria-hdden="true" class="carousel-control-next-icon"></span> <span class="sr-only">Next</span></a>',
        '</div>'
    ])

def test_controls():
    previous, following = controls(identifier)
    assert previous.markup == "".join([
        '<a href="#identifier" role="button" data-slide="prev" class="carousel-control-prev">',
        '<span aria-hdden="true" class="carousel-control-prev-icon"></span> '
        '<span class="sr-only">Previous</span>',
        '</a>'
    ])
    assert following.markup == "".join([
        '<a href="#identifier" role="button" data-slide="next" class="carousel-control-next">',
        '<span aria-hdden="true" class="carousel-control-next-icon"></span> '
        '<span class="sr-only">Next</span>',
        '</a>'
    ])

    previous, following = controls(identifier, class_="my-a", attr="42")
    assert previous.markup == "".join([
        '<a href="#identifier" role="button" attr="42" data-slide="prev" class="carousel-control-prev my-a">',
        '<span aria-hdden="true" class="carousel-control-prev-icon"></span> '
        '<span class="sr-only">Previous</span>',
        '</a>'
    ])
    assert following.markup == "".join([
        '<a href="#identifier" role="button" attr="42" data-slide="next" class="carousel-control-next my-a">',
        '<span aria-hdden="true" class="carousel-control-next-icon"></span> '
        '<span class="sr-only">Next</span>',
        '</a>'
    ])

def test_indicators():
    assert indicators(identifier, 3).markup == "\n".join([
        '<ol class="carousel-indicators">',
        '<li data-target="#identifier" data-slide-to="0" class="active"></li>',
        '<li data-target="#identifier" data-slide-to="1"></li>',
        '<li data-target="#identifier" data-slide-to="2"></li>',
        '</ol>'
    ])
    assert indicators(identifier, 3, active_index=2).markup == "\n".join([
        '<ol class="carousel-indicators">',
        '<li data-target="#identifier" data-slide-to="0"></li>',
        '<li data-target="#identifier" data-slide-to="1"></li>',
        '<li data-target="#identifier" data-slide-to="2" class="active"></li>',
        '</ol>'
    ])
    assert indicators(identifier, 3, class_="my-indicator", attr=42).markup == "\n".join([
        '<ol class="carousel-indicators">',
        '<li attr="42" data-target="#identifier" data-slide-to="0" class="active my-indicator"></li>',
        '<li attr="42" data-target="#identifier" data-slide-to="1" class="my-indicator"></li>',
        '<li attr="42" data-target="#identifier" data-slide-to="2" class="my-indicator"></li>',
        '</ol>'
    ])

def test_inner():
    assert inner().markup ==\
        '<div class="carousel-inner"></div>'
    assert inner("First", "Second", class_="my-inner", attr=42).markup ==\
        '<div attr="42" class="carousel-inner my-inner">\nFirst\nSecond\n</div>'

def test_item():
    assert item().markup ==\
        '<div class="carousel-item"></div>'
    assert item("First", "Second", class_="my-item", attr=42).markup ==\
        '<div attr="42" class="carousel-item my-item">\nFirst\nSecond\n</div>'
    assert item("First", "Second", class_="my-item", attr=42, active=False).markup ==\
        '<div attr="42" class="carousel-item my-item">\nFirst\nSecond\n</div>'
    assert item("First", "Second", class_="my-item", attr=42, active=True).markup ==\
        '<div attr="42" class="carousel-item active my-item">\nFirst\nSecond\n</div>'

def test_item_caption():
    assert item_caption().markup ==\
        '<div class="carousel-caption d-none d-md-block"></div>'
    assert item_caption("First", "Second", class_="my-caption", attr=42).markup ==\
        '<div attr="42" class="carousel-caption d-none d-md-block my-caption">\nFirst\nSecond\n</div>'

def test_slide():
    assert slide(identifier=identifier).markup ==\
        f'<div data-ride="carousel" id="{identifier}" class="carousel slide"></div>'
    assert slide("First", "Second", identifier=identifier, class_="my-slide", attr=42).markup ==\
        f'<div attr="42" data-ride="carousel" id="{identifier}" '\
        'class="carousel slide my-slide">\nFirst\nSecond\n</div>'
