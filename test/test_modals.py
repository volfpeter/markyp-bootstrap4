from markyp_bootstrap4.buttons import ButtonContext
from markyp_bootstrap4.modals import *

def test_title():
    assert title.h1("Value").markup == '<h1 class="modal-title">Value</h1>'
    assert title.h1("Value", class_="my-title", attr=42).markup == '<h1 attr="42" class="modal-title my-title">Value</h1>'

    assert title.h2("Value").markup == '<h2 class="modal-title">Value</h2>'
    assert title.h2("Value", class_="my-title", attr=42).markup == '<h2 attr="42" class="modal-title my-title">Value</h2>'

    assert title.h3("Value").markup == '<h3 class="modal-title">Value</h3>'
    assert title.h3("Value", class_="my-title", attr=42).markup == '<h3 attr="42" class="modal-title my-title">Value</h3>'

    assert title.h4("Value").markup == '<h4 class="modal-title">Value</h4>'
    assert title.h4("Value", class_="my-title", attr=42).markup == '<h4 attr="42" class="modal-title my-title">Value</h4>'

    assert title.h5("Value").markup == '<h5 class="modal-title">Value</h5>'
    assert title.h5("Value", class_="my-title", attr=42).markup == '<h5 attr="42" class="modal-title my-title">Value</h5>'

    assert title.h6("Value").markup == '<h6 class="modal-title">Value</h6>'
    assert title.h6("Value", class_="my-title", attr=42).markup == '<h6 attr="42" class="modal-title my-title">Value</h6>'

    assert title.p("Value").markup == '<p class="modal-title">Value</p>'
    assert title.p("Value", class_="my-title", attr=42).markup == '<p attr="42" class="modal-title my-title">Value</p>'

def test_CloseButtonFactory():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = CloseButtonFactory()

    assert factory.create_element().markup == '<button ></button>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-dismiss="modal" class="btn btn-{context}"></button>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-dismiss="modal" class="btn btn-{context}">Value</button>'

def test_ModalToggleButtonFactory():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = ModalToggleButtonFactory()

    assert factory.create_element().markup == '<button ></button>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({"modal_id": "modal-id"})).markup ==\
            f'<button type="button" data-toggle="modal" data-target="#modal-id" class="btn btn-{context}"></button>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({"modal_id": "modal-id"})).markup ==\
            f'<button type="button" data-toggle="modal" data-target="#modal-id" class="btn btn-{context}">Value</button>'

def test_close_button():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = close_button

    assert factory.create_element().markup == '<button ></button>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-dismiss="modal" class="btn btn-{context}"></button>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<button type="button" data-dismiss="modal" class="btn btn-{context}">Value</button>'

def test_toggle_button():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = toggle_button

    assert factory.create_element().markup == '<button ></button>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({"modal_id": "modal-id"})).markup ==\
            f'<button type="button" data-toggle="modal" data-target="#modal-id" class="btn btn-{context}"></button>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({"modal_id": "modal-id"})).markup ==\
            f'<button type="button" data-toggle="modal" data-target="#modal-id" class="btn btn-{context}">Value</button>'

def test_modal():
    assert modal(id="modal-1").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", title="Example").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        'Example',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", add_close_button=False).markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", centered=True).markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog modal-dialog-centered">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", fade=False).markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", class_="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade my-class">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", dialog_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog my-class">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", content_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content my-class">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", header_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header my-class">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", body_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body my-class"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", footer_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                '</div>',
            '</div>',
        '</div>'
    ))

    assert modal(id="modal-1", footer="Footer", footer_class="my-class").markup == "\n".join((
        '<div role="dialog" tabindex="-1" id="modal-1" class="modal fade">',
            '<div role="document" class="modal-dialog">',
                '<div class="modal-content">',
                    '<div class="modal-header">',
                        '<button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">&times;</span></button>',
                    '</div>',
                    '<div class="modal-body"></div>',
                    '<div class="modal-footer my-class">\nFooter\n</div>',
                '</div>',
            '</div>',
        '</div>'
    ))

def test_modal_element():
    assert modal_element().markup ==\
        '<div role="dialog" tabindex="-1" class="modal fade"></div>'
    assert modal_element("First", "Second", class_="my-modal", attr=42).markup ==\
        '<div role="dialog" tabindex="-1" attr="42" class="modal fade my-modal">\nFirst\nSecond\n</div>'
    assert modal_element("First", "Second", class_="my-modal", fade=False, attr=42).markup ==\
        '<div role="dialog" tabindex="-1" attr="42" class="modal my-modal">\nFirst\nSecond\n</div>'

def test_modal_dialog_base():
    assert modal_dialog_base().markup ==\
        '<div role="document" class="modal-dialog"></div>'
    assert modal_dialog_base("First", "Second", class_="my-dialog", attr=42).markup ==\
        '<div role="document" attr="42" class="modal-dialog my-dialog">\nFirst\nSecond\n</div>'
    assert modal_dialog_base("First", "Second", class_="my-dialog", centered=True, attr=42).markup ==\
        '<div role="document" attr="42" class="modal-dialog modal-dialog-centered my-dialog">\nFirst\nSecond\n</div>'

def test_modal_content():
    assert modal_content().markup ==\
        '<div class="modal-content"></div>'
    assert modal_content("First", "Second", class_="my-content", attr=42).markup ==\
        '<div attr="42" class="modal-content my-content">\nFirst\nSecond\n</div>'

def test_modal_header():
    assert modal_header().markup ==\
        '<div class="modal-header"></div>'
    assert modal_header("First", "Second", class_="my-header", attr=42).markup ==\
        '<div attr="42" class="modal-header my-header">\nFirst\nSecond\n</div>'

def test_modal_body():
    assert modal_body().markup ==\
        '<div class="modal-body"></div>'
    assert modal_body("First", "Second", class_="my-body", attr=42).markup ==\
        '<div attr="42" class="modal-body my-body">\nFirst\nSecond\n</div>'

def test_modal_footer():
    assert modal_footer().markup ==\
        '<div class="modal-footer"></div>'
    assert modal_footer("First", "Second", class_="my-footer", attr=42).markup ==\
        '<div attr="42" class="modal-footer my-footer">\nFirst\nSecond\n</div>'
