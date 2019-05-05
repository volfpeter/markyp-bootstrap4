from markyp_html.forms import option
from markyp_bootstrap4.forms import *

def test_muted_text():
    assert muted_text.h1("Value").markup == '<h1 class="form-text text-muted">Value</h1>'
    assert muted_text.h1("Value", class_="my-header", attr=42).markup == '<h1 attr="42" class="form-text text-muted my-header">Value</h1>'

    assert muted_text.h2("Value").markup == '<h2 class="form-text text-muted">Value</h2>'
    assert muted_text.h2("Value", class_="my-header", attr=42).markup == '<h2 attr="42" class="form-text text-muted my-header">Value</h2>'

    assert muted_text.h3("Value").markup == '<h3 class="form-text text-muted">Value</h3>'
    assert muted_text.h3("Value", class_="my-header", attr=42).markup == '<h3 attr="42" class="form-text text-muted my-header">Value</h3>'

    assert muted_text.h4("Value").markup == '<h4 class="form-text text-muted">Value</h4>'
    assert muted_text.h4("Value", class_="my-header", attr=42).markup == '<h4 attr="42" class="form-text text-muted my-header">Value</h4>'

    assert muted_text.h5("Value").markup == '<h5 class="form-text text-muted">Value</h5>'
    assert muted_text.h5("Value", class_="my-header", attr=42).markup == '<h5 attr="42" class="form-text text-muted my-header">Value</h5>'

    assert muted_text.h6("Value").markup == '<h6 class="form-text text-muted">Value</h6>'
    assert muted_text.h6("Value", class_="my-header", attr=42).markup == '<h6 attr="42" class="form-text text-muted my-header">Value</h6>'

    assert muted_text.p("Value").markup == '<p class="form-text text-muted">Value</p>'
    assert muted_text.p("Value", class_="my-header", attr=42).markup == '<p attr="42" class="form-text text-muted my-header">Value</p>'

def test_text():
    assert text.h1("Value").markup == '<h1 class="form-text">Value</h1>'
    assert text.h1("Value", class_="my-header", attr=42).markup == '<h1 attr="42" class="form-text my-header">Value</h1>'

    assert text.h2("Value").markup == '<h2 class="form-text">Value</h2>'
    assert text.h2("Value", class_="my-header", attr=42).markup == '<h2 attr="42" class="form-text my-header">Value</h2>'

    assert text.h3("Value").markup == '<h3 class="form-text">Value</h3>'
    assert text.h3("Value", class_="my-header", attr=42).markup == '<h3 attr="42" class="form-text my-header">Value</h3>'

    assert text.h4("Value").markup == '<h4 class="form-text">Value</h4>'
    assert text.h4("Value", class_="my-header", attr=42).markup == '<h4 attr="42" class="form-text my-header">Value</h4>'

    assert text.h5("Value").markup == '<h5 class="form-text">Value</h5>'
    assert text.h5("Value", class_="my-header", attr=42).markup == '<h5 attr="42" class="form-text my-header">Value</h5>'

    assert text.h6("Value").markup == '<h6 class="form-text">Value</h6>'
    assert text.h6("Value", class_="my-header", attr=42).markup == '<h6 attr="42" class="form-text my-header">Value</h6>'

    assert text.p("Value").markup == '<p class="form-text">Value</p>'
    assert text.p("Value", class_="my-header", attr=42).markup == '<p attr="42" class="form-text my-header">Value</p>'

def test_FormStyle():
    assert FormStyle.SMALL == "form-control-sm"
    assert FormStyle.LARGE == "form-control-lg"
    assert FormStyle.LABEL_COLUMN == "col-form-label"

def test_input_():
    assert str(input_(type_="text", name="input_1")) ==\
        '<input name="input_1" type="text" class="form-control">'
    assert str(input_(type_="submit", value="Submit")) ==\
        '<input value="Submit" type="submit" class="form-control">'

    assert input_.button(name="input-1").markup ==\
        '<input name="input-1" type="button" class="form-control">'

    assert input_.checkbox(name="input-1").markup ==\
        '<input name="input-1" type="checkbox" class="form-check-input">'

    assert input_.email(name="input-1").markup ==\
        '<input name="input-1" type="email" class="form-control">'

    assert input_.file(name="input-1").markup ==\
        '<input name="input-1" type="file" class="form-control-file">'

    assert input_.hidden(name="input-1").markup ==\
        '<input name="input-1" type="hidden" class="form-control">'

    assert input_.number(name="input-1").markup ==\
        '<input name="input-1" type="number" class="form-control">'

    assert input_.password(name="input-1").markup ==\
        '<input name="input-1" type="password" class="form-control">'

    assert input_.radio(name="input-1").markup ==\
        '<input name="input-1" type="radio" class="form-check-input">'

    assert input_.search(name="input-1").markup ==\
        '<input name="input-1" type="search" class="form-control">'

    assert input_.submit(name="input-1").markup ==\
        '<input name="input-1" type="submit" class="form-control">'

    assert input_.text(name="input-1").markup ==\
        '<input name="input-1" type="text" class="form-control">'

    assert input_.time(name="input-1").markup ==\
        '<input name="input-1" type="time" class="form-control">'

def test_select():
    assert str(select(option("First", value="first"), option("Second", value="second"))) ==\
        '<select class="form-control">\n<option value="first">First</option>\n<option value="second">Second</option>\n</select>'

def test_textarea():
    assert str(textarea("Text", rows=4, cols=80)) ==\
        '<textarea rows="4" cols="80" class="form-control">\nText\n</textarea>'

def test_form_check():
    assert form_check("First", "Second").markup ==\
        '<div class="form-check">\nFirst\nSecond\n</div>'
    assert form_check("First", "Second", class_="my-fc", inline=False, attr=42).markup ==\
        '<div attr="42" class="form-check my-fc">\nFirst\nSecond\n</div>'

    assert form_check("First", "Second", inline=True).markup ==\
        '<div class="form-check-inline">\nFirst\nSecond\n</div>'
    assert form_check("First", "Second", class_="my-fc", inline=True, attr=42).markup ==\
        '<div attr="42" class="form-check-inline my-fc">\nFirst\nSecond\n</div>'

def test_check_label():
    assert form_check_label().markup ==\
        '<label class="form-check-label"></label>'
    assert form_check_label("Label").markup ==\
        '<label class="form-check-label">Label</label>'
    assert form_check_label("Label", class_="my-c-label", attr=42).markup ==\
        '<label attr="42" class="form-check-label my-c-label">Label</label>'

def test_form_label():
    assert form_label().markup ==\
        '<label class="col-form-label"></label>'
    assert form_label("Label").markup ==\
        '<label class="col-form-label">Label</label>'
    assert form_label("Label", class_="my-f-label", attr=42).markup ==\
        '<label attr="42" class="col-form-label my-f-label">Label</label>'

def test_form_group():
    assert form_group("First", "Second").markup ==\
        '<div class="form-group">\nFirst\nSecond\n</div>'

    assert form_group("First", "Second", row=False).markup ==\
        '<div class="form-group">\nFirst\nSecond\n</div>'
    assert form_group("First", "Second", row=False, class_="my-fg", attr=42).markup ==\
        '<div attr="42" class="form-group my-fg">\nFirst\nSecond\n</div>'

    assert form_group("First", "Second", row=True).markup ==\
        '<div class="form-group row">\nFirst\nSecond\n</div>'
    assert form_group("First", "Second", row=True, class_="my-fg", attr=42).markup ==\
        '<div attr="42" class="form-group row my-fg">\nFirst\nSecond\n</div>'

def test_form_row():
    assert form_row("First", "Second").markup ==\
        '<div class="form-row">\nFirst\nSecond\n</div>'
    assert form_row("First", "Second", class_="my-fr").markup ==\
        '<div class="form-row my-fr">\nFirst\nSecond\n</div>'

def test_inline_form():
    assert inline_form().markup ==\
        '<form class="form-inline"></form>'
    assert inline_form("First", "Second").markup ==\
        '<form class="form-inline">\nFirst\nSecond\n</form>'
    assert inline_form("First", "Second", class_="my-form").markup ==\
        '<form class="form-inline my-form">\nFirst\nSecond\n</form>'
    assert inline_form("First", "Second", class_="my-form", attr=42).markup ==\
        '<form attr="42" class="form-inline my-form">\nFirst\nSecond\n</form>'
