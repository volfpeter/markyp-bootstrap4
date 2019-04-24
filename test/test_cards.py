from markyp_bootstrap4.cards import *

def test_title():
    assert title.h1("Text").markup ==\
        '<h1 class="card-title">Text</h1>'
    assert title.h2("Text").markup ==\
        '<h2 class="card-title">Text</h2>'
    assert title.h3("Text").markup ==\
        '<h3 class="card-title">Text</h3>'
    assert title.h4("Text").markup ==\
        '<h4 class="card-title">Text</h4>'
    assert title.h5("Text").markup ==\
        '<h5 class="card-title">Text</h5>'
    assert title.h6("Text").markup ==\
        '<h6 class="card-title">Text</h6>'
    assert title.p("Text").markup ==\
        '<p class="card-title">Text</p>'

    assert title.h1("Text", class_="my-title", attr="attr-value").markup ==\
        '<h1 attr="attr-value" class="card-title my-title">Text</h1>'
    assert title.h2("Text", class_="my-title", attr="attr-value").markup ==\
        '<h2 attr="attr-value" class="card-title my-title">Text</h2>'
    assert title.h3("Text", class_="my-title", attr="attr-value").markup ==\
        '<h3 attr="attr-value" class="card-title my-title">Text</h3>'
    assert title.h4("Text", class_="my-title", attr="attr-value").markup ==\
        '<h4 attr="attr-value" class="card-title my-title">Text</h4>'
    assert title.h5("Text", class_="my-title", attr="attr-value").markup ==\
        '<h5 attr="attr-value" class="card-title my-title">Text</h5>'
    assert title.h6("Text", class_="my-title", attr="attr-value").markup ==\
        '<h6 attr="attr-value" class="card-title my-title">Text</h6>'
    assert title.p("Text", class_="my-title", attr="attr-value").markup ==\
        '<p attr="attr-value" class="card-title my-title">Text</p>'

def test_subtitle():
    assert subtitle.h1("Text").markup ==\
        '<h1 class="card-subtitle text-muted mb-2">Text</h1>'
    assert subtitle.h2("Text").markup ==\
        '<h2 class="card-subtitle text-muted mb-2">Text</h2>'
    assert subtitle.h3("Text").markup ==\
        '<h3 class="card-subtitle text-muted mb-2">Text</h3>'
    assert subtitle.h4("Text").markup ==\
        '<h4 class="card-subtitle text-muted mb-2">Text</h4>'
    assert subtitle.h5("Text").markup ==\
        '<h5 class="card-subtitle text-muted mb-2">Text</h5>'
    assert subtitle.h6("Text").markup ==\
        '<h6 class="card-subtitle text-muted mb-2">Text</h6>'
    assert subtitle.p("Text").markup ==\
        '<p class="card-subtitle text-muted mb-2">Text</p>'

    assert subtitle.h1("Text", class_="my-title", attr="attr-value").markup ==\
        '<h1 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h1>'
    assert subtitle.h2("Text", class_="my-title", attr="attr-value").markup ==\
        '<h2 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h2>'
    assert subtitle.h3("Text", class_="my-title", attr="attr-value").markup ==\
        '<h3 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h3>'
    assert subtitle.h4("Text", class_="my-title", attr="attr-value").markup ==\
        '<h4 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h4>'
    assert subtitle.h5("Text", class_="my-title", attr="attr-value").markup ==\
        '<h5 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h5>'
    assert subtitle.h6("Text", class_="my-title", attr="attr-value").markup ==\
        '<h6 attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</h6>'
    assert subtitle.p("Text", class_="my-title", attr="attr-value").markup ==\
        '<p attr="attr-value" class="card-subtitle text-muted mb-2 my-title">Text</p>'

def test_text():
    assert text.h1("Text").markup ==\
        '<h1 class="card-text">Text</h1>'
    assert text.h2("Text").markup ==\
        '<h2 class="card-text">Text</h2>'
    assert text.h3("Text").markup ==\
        '<h3 class="card-text">Text</h3>'
    assert text.h4("Text").markup ==\
        '<h4 class="card-text">Text</h4>'
    assert text.h5("Text").markup ==\
        '<h5 class="card-text">Text</h5>'
    assert text.h6("Text").markup ==\
        '<h6 class="card-text">Text</h6>'
    assert text.p("Text").markup ==\
        '<p class="card-text">Text</p>'

    assert text.h1("Text", class_="my-title", attr="attr-value").markup ==\
        '<h1 attr="attr-value" class="card-text my-title">Text</h1>'
    assert text.h2("Text", class_="my-title", attr="attr-value").markup ==\
        '<h2 attr="attr-value" class="card-text my-title">Text</h2>'
    assert text.h3("Text", class_="my-title", attr="attr-value").markup ==\
        '<h3 attr="attr-value" class="card-text my-title">Text</h3>'
    assert text.h4("Text", class_="my-title", attr="attr-value").markup ==\
        '<h4 attr="attr-value" class="card-text my-title">Text</h4>'
    assert text.h5("Text", class_="my-title", attr="attr-value").markup ==\
        '<h5 attr="attr-value" class="card-text my-title">Text</h5>'
    assert text.h6("Text", class_="my-title", attr="attr-value").markup ==\
        '<h6 attr="attr-value" class="card-text my-title">Text</h6>'
    assert text.p("Text", class_="my-title", attr="attr-value").markup ==\
        '<p attr="attr-value" class="card-text my-title">Text</p>'

def test_header():
    assert header.h1("Text").markup ==\
        '<h1 class="card-header">Text</h1>'
    assert header.h2("Text").markup ==\
        '<h2 class="card-header">Text</h2>'
    assert header.h3("Text").markup ==\
        '<h3 class="card-header">Text</h3>'
    assert header.h4("Text").markup ==\
        '<h4 class="card-header">Text</h4>'
    assert header.h5("Text").markup ==\
        '<h5 class="card-header">Text</h5>'
    assert header.h6("Text").markup ==\
        '<h6 class="card-header">Text</h6>'
    assert header.p("Text").markup ==\
        '<p class="card-header">Text</p>'

    assert header.h1("Text", class_="my-title", attr="attr-value").markup ==\
        '<h1 attr="attr-value" class="card-header my-title">Text</h1>'
    assert header.h2("Text", class_="my-title", attr="attr-value").markup ==\
        '<h2 attr="attr-value" class="card-header my-title">Text</h2>'
    assert header.h3("Text", class_="my-title", attr="attr-value").markup ==\
        '<h3 attr="attr-value" class="card-header my-title">Text</h3>'
    assert header.h4("Text", class_="my-title", attr="attr-value").markup ==\
        '<h4 attr="attr-value" class="card-header my-title">Text</h4>'
    assert header.h5("Text", class_="my-title", attr="attr-value").markup ==\
        '<h5 attr="attr-value" class="card-header my-title">Text</h5>'
    assert header.h6("Text", class_="my-title", attr="attr-value").markup ==\
        '<h6 attr="attr-value" class="card-header my-title">Text</h6>'
    assert header.p("Text", class_="my-title", attr="attr-value").markup ==\
        '<p attr="attr-value" class="card-header my-title">Text</p>'

def test_footer():
    assert footer.h1("Text").markup ==\
        '<h1 class="card-footer">Text</h1>'
    assert footer.h2("Text").markup ==\
        '<h2 class="card-footer">Text</h2>'
    assert footer.h3("Text").markup ==\
        '<h3 class="card-footer">Text</h3>'
    assert footer.h4("Text").markup ==\
        '<h4 class="card-footer">Text</h4>'
    assert footer.h5("Text").markup ==\
        '<h5 class="card-footer">Text</h5>'
    assert footer.h6("Text").markup ==\
        '<h6 class="card-footer">Text</h6>'
    assert footer.p("Text").markup ==\
        '<p class="card-footer">Text</p>'

    assert footer.h1("Text", class_="my-title", attr="attr-value").markup ==\
        '<h1 attr="attr-value" class="card-footer my-title">Text</h1>'
    assert footer.h2("Text", class_="my-title", attr="attr-value").markup ==\
        '<h2 attr="attr-value" class="card-footer my-title">Text</h2>'
    assert footer.h3("Text", class_="my-title", attr="attr-value").markup ==\
        '<h3 attr="attr-value" class="card-footer my-title">Text</h3>'
    assert footer.h4("Text", class_="my-title", attr="attr-value").markup ==\
        '<h4 attr="attr-value" class="card-footer my-title">Text</h4>'
    assert footer.h5("Text", class_="my-title", attr="attr-value").markup ==\
        '<h5 attr="attr-value" class="card-footer my-title">Text</h5>'
    assert footer.h6("Text", class_="my-title", attr="attr-value").markup ==\
        '<h6 attr="attr-value" class="card-footer my-title">Text</h6>'
    assert footer.p("Text", class_="my-title", attr="attr-value").markup ==\
        '<p attr="attr-value" class="card-footer my-title">Text</p>'

def test_TextAlign():
    assert TextAlign.LEFT == "text-left"
    assert TextAlign.CENTER == "text-center"
    assert TextAlign.RIGHT == "text-right"

def test_Image():
    assert Image.top(src="https://via.placeholder.com/150").markup ==\
        '<img src="https://via.placeholder.com/150" class="card-img-top">'
    assert Image.bottom(src="https://via.placeholder.com/150").markup ==\
        '<img src="https://via.placeholder.com/150" class="card-img-bottom">'

    assert Image.top(src="https://via.placeholder.com/150", class_="my-card-img", attr="attr-value").markup ==\
        '<img src="https://via.placeholder.com/150" attr="attr-value" class="card-img-top my-card-img">'
    assert Image.bottom(src="https://via.placeholder.com/150", class_="my-card-img", attr="attr-value").markup ==\
        '<img src="https://via.placeholder.com/150" attr="attr-value" class="card-img-bottom my-card-img">'

def test_card():
    assert card().markup == '<div class="card"></div>'
    assert card("Content").markup == '<div class="card">\nContent\n</div>'
    assert card("Content", class_="my-card", attr="attr-value").markup ==\
        '<div attr="attr-value" class="card my-card">\nContent\n</div>'

def test_body():
    assert body().markup == '<div class="card-body"></div>'
    assert body("Content").markup == '<div class="card-body">\nContent\n</div>'
    assert body("Content", class_="my-body", attr="value").markup ==\
        '<div attr="value" class="card-body my-body">\nContent\n</div>'

def test_footer_div():
    assert footer_div().markup == '<div class="card-footer"></div>'
    assert footer_div("Text").markup == '<div class="card-footer">\nText\n</div>'
    assert footer_div("Text", class_="my-footer", attr="value").markup ==\
        '<div attr="value" class="card-footer my-footer">\nText\n</div>'

def test_header_div():
    assert header_div().markup == '<div class="card-header"></div>'
    assert header_div("Text").markup == '<div class="card-header">\nText\n</div>'
    assert header_div("Text", class_="my-header", attr="value").markup ==\
        '<div attr="value" class="card-header my-header">\nText\n</div>'

def test_link():
    assert link().markup == '<a class="card-link"></a>'
    assert link("Content").markup == '<a class="card-link">Content</a>'
    assert link("Content", class_="my-link", attr="value").markup ==\
        '<a attr="value" class="card-link my-link">Content</a>'
