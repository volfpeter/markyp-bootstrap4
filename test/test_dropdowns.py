from markyp_html.inline import a
from markyp_bootstrap4.buttons import ButtonContext
from markyp_bootstrap4.dropdowns import *

def test_DropdownButtonFactory():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = DropdownButtonFactory()

    assert factory.create_element().markup == '<button ></button>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-{context} dropdown-toggle"></button>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-{context} dropdown-toggle">Value</button>'

def test_dropdown_button():
    assert dropdown_button.primary("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-primary dropdown-toggle">Value</button>'
    assert dropdown_button.primary("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-primary dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.primary_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-primary dropdown-toggle">Value</button>'
    assert dropdown_button.primary_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-primary dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.secondary("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-secondary dropdown-toggle">Value</button>'
    assert dropdown_button.secondary("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-secondary dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.secondary_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-secondary dropdown-toggle">Value</button>'
    assert dropdown_button.secondary_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-secondary dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.success("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-success dropdown-toggle">Value</button>'
    assert dropdown_button.success("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-success dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.success_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-success dropdown-toggle">Value</button>'
    assert dropdown_button.success_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-success dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.danger("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-danger dropdown-toggle">Value</button>'
    assert dropdown_button.danger("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-danger dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.danger_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-danger dropdown-toggle">Value</button>'
    assert dropdown_button.danger_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-danger dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.warning("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-warning dropdown-toggle">Value</button>'
    assert dropdown_button.warning("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-warning dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.warning_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-warning dropdown-toggle">Value</button>'
    assert dropdown_button.warning_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-warning dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.info("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-info dropdown-toggle">Value</button>'
    assert dropdown_button.info("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-info dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.info_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-info dropdown-toggle">Value</button>'
    assert dropdown_button.info_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-info dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.light("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-light dropdown-toggle">Value</button>'
    assert dropdown_button.light("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-light dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.light_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-light dropdown-toggle">Value</button>'
    assert dropdown_button.light_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-light dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.dark("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-dark dropdown-toggle">Value</button>'
    assert dropdown_button.dark("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-dark dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.dark_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-dark dropdown-toggle">Value</button>'
    assert dropdown_button.dark_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-dark dropdown-toggle my-btn">Value</button>'

    assert dropdown_button.link("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-link dropdown-toggle">Value</button>'
    assert dropdown_button.link("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-link dropdown-toggle my-btn">Value</button>'
    assert dropdown_button.link_outline("Value").markup ==\
        '<button type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-link dropdown-toggle">Value</button>'
    assert dropdown_button.link_outline("Value", class_="my-btn", attr=42).markup ==\
        '<button attr="42" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="btn btn-outline-link dropdown-toggle my-btn">Value</button>'

def test_menu_header():
    assert menu_header.h1("Value").markup == '<h1 class="dropdown-header">Value</h1>'
    assert menu_header.h1("Value", class_="my-header", attr=42).markup == '<h1 attr="42" class="dropdown-header my-header">Value</h1>'

    assert menu_header.h2("Value").markup == '<h2 class="dropdown-header">Value</h2>'
    assert menu_header.h2("Value", class_="my-header", attr=42).markup == '<h2 attr="42" class="dropdown-header my-header">Value</h2>'

    assert menu_header.h3("Value").markup == '<h3 class="dropdown-header">Value</h3>'
    assert menu_header.h3("Value", class_="my-header", attr=42).markup == '<h3 attr="42" class="dropdown-header my-header">Value</h3>'

    assert menu_header.h4("Value").markup == '<h4 class="dropdown-header">Value</h4>'
    assert menu_header.h4("Value", class_="my-header", attr=42).markup == '<h4 attr="42" class="dropdown-header my-header">Value</h4>'

    assert menu_header.h5("Value").markup == '<h5 class="dropdown-header">Value</h5>'
    assert menu_header.h5("Value", class_="my-header", attr=42).markup == '<h5 attr="42" class="dropdown-header my-header">Value</h5>'

    assert menu_header.h6("Value").markup == '<h6 class="dropdown-header">Value</h6>'
    assert menu_header.h6("Value", class_="my-header", attr=42).markup == '<h6 attr="42" class="dropdown-header my-header">Value</h6>'

    assert menu_header.p("Value").markup == '<p class="dropdown-header">Value</p>'
    assert menu_header.p("Value", class_="my-header", attr=42).markup == '<p attr="42" class="dropdown-header my-header">Value</p>'

def test_dropdown():
    assert dropdown().markup ==\
        '<div class="dropdown"></div>'
    assert dropdown("First", "Second", class_="my-dd", attr=42).markup ==\
        '<div attr="42" class="dropdown my-dd">\nFirst\nSecond\n</div>'

def test_menu():
    assert menu(button_id="button1").markup ==\
        '<div aria-labelledby="button1" class="dropdown-menu"></div>'
    assert menu("First", "Second", button_id="button1", class_="my-menu", attr=42).markup ==\
        '<div attr="42" aria-labelledby="button1" class="dropdown-menu my-menu">\nFirst\nSecond\n</div>'

def test_menu_divider():
    assert menu_divider().markup ==\
        '<div class="dropdown-divider"></div>'
    assert menu_divider(class_="my-divider", attr=42).markup ==\
        '<div attr="42" class="dropdown-divider my-divider"></div>'

def test_menu_item():
    assert menu_item().markup ==\
        '<button type="button" class="dropdown-item"></button>'
    assert menu_item("Label").markup ==\
        '<button type="button" class="dropdown-item">Label</button>'
    assert menu_item("Label", class_="my-item").markup ==\
        '<button type="button" class="dropdown-item my-item">Label</button>'
    assert menu_item("Label", active=True, class_="my-item").markup ==\
        '<button type="button" class="dropdown-item active my-item">Label</button>'
    assert menu_item("Label", class_="my-item", disabled=True).markup ==\
        '<button type="button" class="dropdown-item disabled my-item">Label</button>'
    assert menu_item("Label", active=True, class_="my-item", disabled=True).markup ==\
        '<button type="button" class="dropdown-item active disabled my-item">Label</button>'
    assert menu_item("Label", active=True, class_="my-item", attr=42).markup ==\
        '<button type="button" attr="42" class="dropdown-item active my-item">Label</button>'
    assert menu_item("Label", active=True, class_="my-item", attr=42, factory=a).markup ==\
        '<a type="button" attr="42" class="dropdown-item active my-item">Label</a>'
