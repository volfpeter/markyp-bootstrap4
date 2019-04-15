import pytest

from markyp.elements import Element, StandaloneElement
from markyp_bootstrap4.buttons import ButtonContext,\
                                      ButtonStyle,\
                                      BaseButtonFactory,\
                                      BaseToggleButtonFactory,\
                                      ElementButtonFactory,\
                                      ElementToggleButtonFactory,\
                                      StandaloneElementButtonFactory,\
                                      StandaloneElementToggleButtonFactory,\
                                      a_button, a_toggle,\
                                      b_button, b_toggle,\
                                      i_button, i_toggle,\
                                      l_button, l_toggle

def test_ButtonContext():
    assert ButtonContext.PRIMARY == "primary"
    assert ButtonContext.SECONDARY == "secondary"
    assert ButtonContext.SUCCESS == "success"
    assert ButtonContext.DANGER == "danger"
    assert ButtonContext.WARNING == "warning"
    assert ButtonContext.INFO == "info"
    assert ButtonContext.LIGHT == "light"
    assert ButtonContext.DARK == "dark"
    assert ButtonContext.LINK == "link"

def test_ButtonStyle():
    assert ButtonStyle.ACTIVE == "active"
    assert ButtonStyle.BLOCK == "btn-block"
    assert ButtonStyle.DISABLED == "disabled"
    assert ButtonStyle.LARGE == "btn-lg"
    assert ButtonStyle.SMALL == "btn-sm"

def test_BaseButtonFactory():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = BaseButtonFactory()

    for context in contexts:
        assert factory.get_css_class(context) == f"btn btn-{context}"
        assert factory.get_css_class(context, class_="my") == f"btn btn-{context} my"
        assert factory.get_css_class(context, active=True) == f"btn btn-{context} active"
        assert factory.get_css_class(context, class_="my", outline=True) == f"btn btn-outline-{context} my"
        assert factory.get_css_class(context, class_="my", outline=True, active=True) == f"btn btn-outline-{context} active my"

    assert factory.update_attributes({}) == {"type": "button"}
    assert factory.update_attributes({"type": "whatever"}) == {"type": "button"}
    assert factory.update_attributes({"key": "value"}) == {"key": "value", "type": "button"}
    assert factory.update_attributes({"key": "value"}, disabled=True) == {"key": "value", "type": "button", "disabled": None}
    assert factory.update_attributes({"key": "value"}, active=True) == {"key": "value", "type": "button", "aria-pressed": True}
    assert factory.update_attributes({"key": "value"}, disabled=True, active=True) == {"key": "value", "type": "button", "disabled": None, "aria-pressed": True}

    with pytest.raises(NotImplementedError):
        factory.create_element()


def test_BaseToggleButtonFactory():
    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = BaseToggleButtonFactory()

    for context in contexts:
        assert factory.get_css_class(context) == f"btn btn-{context}"
        assert factory.get_css_class(context, class_="my") == f"btn btn-{context} my"
        assert factory.get_css_class(context, active=True) == f"btn btn-{context} active"
        assert factory.get_css_class(context, class_="my", outline=True) == f"btn btn-outline-{context} my"
        assert factory.get_css_class(context, class_="my", outline=True, active=True) == f"btn btn-outline-{context} active my"

    assert factory.update_attributes({}) ==\
        {"type": "button", "aria-pressed": False, "autocomplete": "off", "data-toggle": "button"}
    assert factory.update_attributes({"type": "whatever"}) ==\
        {"type": "button", "aria-pressed": False, "autocomplete": "off", "data-toggle": "button"}
    assert factory.update_attributes({"key": "value"}) ==\
        {"key": "value", "type": "button", "aria-pressed": False, "autocomplete": "off", "data-toggle": "button"}
    assert factory.update_attributes({"key": "value"}, disabled=True) ==\
        {"key": "value", "type": "button", "disabled": None, "aria-pressed": False, "autocomplete": "off", "data-toggle": "button"}
    assert factory.update_attributes({"key": "value"}, active=True) ==\
        {"key": "value", "type": "button", "aria-pressed": True, "autocomplete": "off", "data-toggle": "button"}
    assert factory.update_attributes({"key": "value"}, disabled=True, active=True) ==\
        {"key": "value", "type": "button", "disabled": None, "aria-pressed": True, "autocomplete": "off", "data-toggle": "button"}

    with pytest.raises(NotImplementedError):
        factory.create_element()

def test_ElementButtonFactory():
    class e(Element):
        __slots__ = ()

    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = ElementButtonFactory(e)

    assert factory.create_element().markup == '<e ></e>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" class="btn btn-{context}"></e>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" class="btn btn-{context}">\nValue\n</e>'

def test_ElementToggleButtonFactory():
    class e(Element):
        __slots__ = ()

    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = ElementToggleButtonFactory(e)

    assert factory.create_element().markup == '<e ></e>'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-{context}"></e>'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-{context}">\nValue\n</e>'

def test_StandaloneElementButtonFactory():
    class e(StandaloneElement):
        __slots__ = ()

    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = StandaloneElementButtonFactory(e)

    assert factory.create_element().markup == '<e value="">'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" value="" class="btn btn-{context}">'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" value="Value" class="btn btn-{context}">'

    factory = StandaloneElementButtonFactory(e, pos_arg_attr="attr")

    assert factory.create_element().markup == '<e attr="">'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" attr="" class="btn btn-{context}">'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" attr="Value" class="btn btn-{context}">'

def test_StandaloneElementToggleButtonFactory():
    class e(StandaloneElement):
        __slots__ = ()

    contexts = (
        ButtonContext.PRIMARY, ButtonContext.SECONDARY, ButtonContext.SUCCESS,
        ButtonContext.DANGER, ButtonContext.WARNING, ButtonContext.INFO,
        ButtonContext.LIGHT, ButtonContext.DARK, ButtonContext.LINK
    )
    factory = StandaloneElementToggleButtonFactory(e)

    assert factory.create_element().markup == '<e value="">'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="" class="btn btn-{context}">'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-{context}">'

    factory = StandaloneElementToggleButtonFactory(e, pos_arg_attr="attr")

    assert factory.create_element().markup == '<e attr="">'
    for context in contexts:
        assert factory.create_element(class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" attr="" class="btn btn-{context}">'
        assert factory.create_element("Value", class_=factory.get_css_class(context), **factory.update_attributes({})).markup ==\
            f'<e type="button" aria-pressed="false" autocomplete="off" data-toggle="button" attr="Value" class="btn btn-{context}">'

def test_a_button():
    assert a_button.primary("Value").markup ==\
        '<a type="button" class="btn btn-primary">Value</a>'
    assert a_button.primary_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-primary">Value</a>'

    assert a_button.secondary("Value").markup ==\
        '<a type="button" class="btn btn-secondary">Value</a>'
    assert a_button.secondary_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-secondary">Value</a>'

    assert a_button.success("Value").markup ==\
        '<a type="button" class="btn btn-success">Value</a>'
    assert a_button.success_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-success">Value</a>'

    assert a_button.danger("Value").markup ==\
        '<a type="button" class="btn btn-danger">Value</a>'
    assert a_button.danger_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-danger">Value</a>'

    assert a_button.warning("Value").markup ==\
        '<a type="button" class="btn btn-warning">Value</a>'
    assert a_button.warning_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-warning">Value</a>'

    assert a_button.info("Value").markup ==\
        '<a type="button" class="btn btn-info">Value</a>'
    assert a_button.info_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-info">Value</a>'

    assert a_button.light("Value").markup ==\
        '<a type="button" class="btn btn-light">Value</a>'
    assert a_button.light_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-light">Value</a>'

    assert a_button.dark("Value").markup ==\
        '<a type="button" class="btn btn-dark">Value</a>'
    assert a_button.dark_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-dark">Value</a>'

    assert a_button.link("Value").markup ==\
        '<a type="button" class="btn btn-link">Value</a>'
    assert a_button.link_outline("Value").markup ==\
        '<a type="button" class="btn btn-outline-link">Value</a>'

def test_a_toggle():
    assert a_toggle.primary("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-primary">Value</a>'
    assert a_toggle.primary_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-primary">Value</a>'

    assert a_toggle.secondary("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-secondary">Value</a>'
    assert a_toggle.secondary_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-secondary">Value</a>'

    assert a_toggle.success("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-success">Value</a>'
    assert a_toggle.success_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-success">Value</a>'

    assert a_toggle.danger("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-danger">Value</a>'
    assert a_toggle.danger_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-danger">Value</a>'

    assert a_toggle.warning("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-warning">Value</a>'
    assert a_toggle.warning_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-warning">Value</a>'

    assert a_toggle.info("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-info">Value</a>'
    assert a_toggle.info_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-info">Value</a>'

    assert a_toggle.light("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-light">Value</a>'
    assert a_toggle.light_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-light">Value</a>'

    assert a_toggle.dark("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-dark">Value</a>'
    assert a_toggle.dark_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-dark">Value</a>'

    assert a_toggle.link("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-link">Value</a>'
    assert a_toggle.link_outline("Value").markup ==\
        '<a type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-link">Value</a>'

def test_b_button():
    assert b_button.primary("Value").markup ==\
        '<button type="button" class="btn btn-primary">Value</button>'
    assert b_button.primary_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-primary">Value</button>'

    assert b_button.secondary("Value").markup ==\
        '<button type="button" class="btn btn-secondary">Value</button>'
    assert b_button.secondary_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-secondary">Value</button>'

    assert b_button.success("Value").markup ==\
        '<button type="button" class="btn btn-success">Value</button>'
    assert b_button.success_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-success">Value</button>'

    assert b_button.danger("Value").markup ==\
        '<button type="button" class="btn btn-danger">Value</button>'
    assert b_button.danger_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-danger">Value</button>'

    assert b_button.warning("Value").markup ==\
        '<button type="button" class="btn btn-warning">Value</button>'
    assert b_button.warning_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-warning">Value</button>'

    assert b_button.info("Value").markup ==\
        '<button type="button" class="btn btn-info">Value</button>'
    assert b_button.info_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-info">Value</button>'

    assert b_button.light("Value").markup ==\
        '<button type="button" class="btn btn-light">Value</button>'
    assert b_button.light_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-light">Value</button>'

    assert b_button.dark("Value").markup ==\
        '<button type="button" class="btn btn-dark">Value</button>'
    assert b_button.dark_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-dark">Value</button>'

    assert b_button.link("Value").markup ==\
        '<button type="button" class="btn btn-link">Value</button>'
    assert b_button.link_outline("Value").markup ==\
        '<button type="button" class="btn btn-outline-link">Value</button>'

def test_b_toggle():
    assert b_toggle.primary("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-primary">Value</button>'
    assert b_toggle.primary_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-primary">Value</button>'

    assert b_toggle.secondary("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-secondary">Value</button>'
    assert b_toggle.secondary_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-secondary">Value</button>'

    assert b_toggle.success("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-success">Value</button>'
    assert b_toggle.success_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-success">Value</button>'

    assert b_toggle.danger("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-danger">Value</button>'
    assert b_toggle.danger_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-danger">Value</button>'

    assert b_toggle.warning("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-warning">Value</button>'
    assert b_toggle.warning_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-warning">Value</button>'

    assert b_toggle.info("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-info">Value</button>'
    assert b_toggle.info_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-info">Value</button>'

    assert b_toggle.light("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-light">Value</button>'
    assert b_toggle.light_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-light">Value</button>'

    assert b_toggle.dark("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-dark">Value</button>'
    assert b_toggle.dark_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-dark">Value</button>'

    assert b_toggle.link("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-link">Value</button>'
    assert b_toggle.link_outline("Value").markup ==\
        '<button type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-link">Value</button>'

def test_i_button():
    assert i_button.primary("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-primary">'
    assert i_button.primary_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-primary">'

    assert i_button.secondary("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-secondary">'
    assert i_button.secondary_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-secondary">'

    assert i_button.success("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-success">'
    assert i_button.success_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-success">'

    assert i_button.danger("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-danger">'
    assert i_button.danger_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-danger">'

    assert i_button.warning("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-warning">'
    assert i_button.warning_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-warning">'

    assert i_button.info("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-info">'
    assert i_button.info_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-info">'

    assert i_button.light("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-light">'
    assert i_button.light_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-light">'

    assert i_button.dark("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-dark">'
    assert i_button.dark_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-dark">'

    assert i_button.link("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-link">'
    assert i_button.link_outline("Value").markup ==\
        '<input type="button" value="Value" class="btn btn-outline-link">'

def test_i_toggle():
    assert i_toggle.primary("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-primary">'
    assert i_toggle.primary_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-primary">'

    assert i_toggle.secondary("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-secondary">'
    assert i_toggle.secondary_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-secondary">'

    assert i_toggle.success("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-success">'
    assert i_toggle.success_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-success">'

    assert i_toggle.danger("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-danger">'
    assert i_toggle.danger_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-danger">'

    assert i_toggle.warning("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-warning">'
    assert i_toggle.warning_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-warning">'

    assert i_toggle.info("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-info">'
    assert i_toggle.info_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-info">'

    assert i_toggle.light("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-light">'
    assert i_toggle.light_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-light">'

    assert i_toggle.dark("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-dark">'
    assert i_toggle.dark_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-dark">'

    assert i_toggle.link("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-link">'
    assert i_toggle.link_outline("Value").markup ==\
        '<input type="button" aria-pressed="false" autocomplete="off" data-toggle="button" value="Value" class="btn btn-outline-link">'

def test_l_button():
    assert l_button.primary("Value").markup ==\
        '<label type="button" class="btn btn-primary">Value</label>'
    assert l_button.primary_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-primary">Value</label>'

    assert l_button.secondary("Value").markup ==\
        '<label type="button" class="btn btn-secondary">Value</label>'
    assert l_button.secondary_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-secondary">Value</label>'

    assert l_button.success("Value").markup ==\
        '<label type="button" class="btn btn-success">Value</label>'
    assert l_button.success_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-success">Value</label>'

    assert l_button.danger("Value").markup ==\
        '<label type="button" class="btn btn-danger">Value</label>'
    assert l_button.danger_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-danger">Value</label>'

    assert l_button.warning("Value").markup ==\
        '<label type="button" class="btn btn-warning">Value</label>'
    assert l_button.warning_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-warning">Value</label>'

    assert l_button.info("Value").markup ==\
        '<label type="button" class="btn btn-info">Value</label>'
    assert l_button.info_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-info">Value</label>'

    assert l_button.light("Value").markup ==\
        '<label type="button" class="btn btn-light">Value</label>'
    assert l_button.light_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-light">Value</label>'

    assert l_button.dark("Value").markup ==\
        '<label type="button" class="btn btn-dark">Value</label>'
    assert l_button.dark_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-dark">Value</label>'

    assert l_button.link("Value").markup ==\
        '<label type="button" class="btn btn-link">Value</label>'
    assert l_button.link_outline("Value").markup ==\
        '<label type="button" class="btn btn-outline-link">Value</label>'

def test_l_toggle():
    assert l_toggle.primary("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-primary">Value</label>'
    assert l_toggle.primary_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-primary">Value</label>'

    assert l_toggle.secondary("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-secondary">Value</label>'
    assert l_toggle.secondary_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-secondary">Value</label>'

    assert l_toggle.success("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-success">Value</label>'
    assert l_toggle.success_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-success">Value</label>'

    assert l_toggle.danger("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-danger">Value</label>'
    assert l_toggle.danger_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-danger">Value</label>'

    assert l_toggle.warning("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-warning">Value</label>'
    assert l_toggle.warning_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-warning">Value</label>'

    assert l_toggle.info("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-info">Value</label>'
    assert l_toggle.info_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-info">Value</label>'

    assert l_toggle.light("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-light">Value</label>'
    assert l_toggle.light_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-light">Value</label>'

    assert l_toggle.dark("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-dark">Value</label>'
    assert l_toggle.dark_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-dark">Value</label>'

    assert l_toggle.link("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-link">Value</label>'
    assert l_toggle.link_outline("Value").markup ==\
        '<label type="button" aria-pressed="false" autocomplete="off" data-toggle="button" class="btn btn-outline-link">Value</label>'
