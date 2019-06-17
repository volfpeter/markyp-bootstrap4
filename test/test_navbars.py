from markyp_bootstrap4.navbars import *
from markyp_html import block

def test_navbar_text():
    assert navbar_text.p("Text").markup == "<p class=\"navbar-text\">Text</p>"
    assert navbar_text.h1("Text").markup == "<h1 class=\"navbar-text\">Text</h1>"
    assert navbar_text.h2("Text").markup == "<h2 class=\"navbar-text\">Text</h2>"
    assert navbar_text.h3("Text").markup == "<h3 class=\"navbar-text\">Text</h3>"
    assert navbar_text.h4("Text").markup == "<h4 class=\"navbar-text\">Text</h4>"
    assert navbar_text.h5("Text").markup == "<h5 class=\"navbar-text\">Text</h5>"
    assert navbar_text.h6("Text").markup == "<h6 class=\"navbar-text\">Text</h6>"

def test_ExpandPoint():
    assert ExpandPoint.XS == "navbar-expand-xs"
    assert ExpandPoint.SM == "navbar-expand-sm"
    assert ExpandPoint.MD == "navbar-expand-md"
    assert ExpandPoint.LG == "navbar-expand-lg"
    assert ExpandPoint.XL == "navbar-expand-xl"

def test_Theme():
    assert Theme.DARK == "navbar-dark"
    assert Theme.LIGHT == "navbar-light"

def test_brand():
    assert brand("Foo").markup == '<a href="#" class="navbar-brand">Foo</a>'
    assert brand("Foo", href="#foo").markup == '<a href="#foo" class="navbar-brand">Foo</a>'
    assert brand("Foo", class_="my-nb", attr=42).markup == '<a href="#" attr="42" class="navbar-brand my-nb">Foo</a>'

def test_collapse():
    assert collapse(id="c1").markup == '<div id="c1" class="collapse navbar-collapse"></div>'
    assert collapse("First", "Second", id="c1").markup == "\n".join((
        '<div id="c1" class="collapse navbar-collapse">',
            'First',
            'Second',
        '</div>'
    ))
    assert collapse("First", "Second", id="c1", class_="my-nc", attr=42).markup == "\n".join((
        '<div id="c1" attr="42" class="collapse navbar-collapse my-nc">',
            'First',
            'Second',
        '</div>'
    ))
    assert collapse("First", "Second", id="c1", nav_factory=block.div).markup == "\n".join((
        '<div id="c1" class="collapse navbar-collapse">',
            '<div class="navbar-nav">',
                'First',
                'Second',
            '</div>',
        '</div>'
    ))

def test_navbar():
    assert navbar().markup == '<nav class="navbar"></nav>'
    assert navbar("First", "Second").markup == "\n".join((
        '<nav class="navbar">',
            'First',
            'Second',
        '</nav>'
    ))
    assert navbar("First", "Second", class_="my-nb", attr=42).markup == "\n".join((
        '<nav attr="42" class="navbar my-nb">',
            'First',
            'Second',
        '</nav>'
    ))
    assert navbar("First", "Second", class_="my-nb", expand_point=ExpandPoint.LG, theme=Theme.DARK).markup == "\n".join((
        '<nav class="navbar navbar-expand-lg navbar-dark my-nb">',
            'First',
            'Second',
        '</nav>'
    ))

def test_navbar_nav():
    assert navbar_nav().markup == '<div class="navbar-nav"></div>'
    assert navbar_nav("First", "Second", class_="my-nbn", attr=42).markup == "\n".join((
        '<div attr="42" class="navbar-nav my-nbn">',
            'First',
            'Second',
        '</div>'
    ))
    assert navbar_nav("First", "Second", class_="my-nbn", attr=42, factory=block.nav).markup == "\n".join((
        '<nav attr="42" class="navbar-nav my-nbn">',
            'First',
            'Second',
        '</nav>'
    ))

def test_navbar_toggler():
    assert navbar_toggler(collapse_id="nc").markup == (
        '<button type="button" '
            'data-toggle="collapse" data-target="#nc" '
            'aria-controls="nc" aria-expanded="false" aria-label="Toggle navigation" '
            'class="navbar-toggler">'
            '<span class="navbar-toggler-icon"></span>'
        '</button>'
    )
    assert navbar_toggler(collapse_id="nc", class_="my-nt", attr=42).markup == (
        '<button type="button" attr="42" '
            'data-toggle="collapse" data-target="#nc" '
            'aria-controls="nc" aria-expanded="false" aria-label="Toggle navigation" '
            'class="navbar-toggler my-nt">'
            '<span class="navbar-toggler-icon"></span>'
        '</button>'
    )
