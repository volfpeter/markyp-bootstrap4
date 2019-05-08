"""
Bootstrap form elements.

Forms vary a lot and can get very complex. As a consequence, chances are you will not find
the exact component you are looking for. The goal of this module is rather to provide all
the required building blocks that can be combined to create the desired form.


See https://getbootstrap.com/docs/4.0/components/forms/.
"""

from typing import Optional

from markyp import ElementType, PropertyDict, PropertyValue
from markyp_html import join
from markyp_html import forms
from markyp_html.block import div
from markyp_html.forms import button
from markyp_html.text import StyledTextFactory

from markyp_bootstrap4.buttons import ElementButtonFactory


__all__ = (
    "muted_text", "text",
    "SubmitButtonFactory", "submit_button",
    "FormStyle",
    "input_", "select", "textarea", "inline_form",
    "form_check", "form_check_label",
    "form_label", "form_group", "form_row"
)


muted_text: StyledTextFactory = StyledTextFactory("form-text text-muted")
"""
Factory that creates text element with `form-text text-muted` style.
"""


text: StyledTextFactory = StyledTextFactory("form-text")
"""
Factory that creates text element with `form-text` style.
"""


class SubmitButtonFactory(ElementButtonFactory):
    """
    Button element factory that creates `submit` buttons for forms.
    """

    __slots__ = ()

    def __init__(self) -> None:
        """
        Initialization.
        """
        super().__init__(button)

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        attributes = super().update_attributes(attributes, disabled=disabled, active=active)
        # Override type to submit.
        attributes["type"] = "submit"
        return attributes


submit_button: SubmitButtonFactory = SubmitButtonFactory()
"""
Button factory that creates `submit` buttons for forms.
"""


class FormStyle(object):
    """
    A set of CSS class names that can be applied on form elements.
    """

    __slots__ = ()

    SMALL: str = "form-control-sm"

    LARGE: str = "form-control-lg"

    LABEL_COLUMN: str = "col-form-label"


class input_(forms.input_):
    """
    `markyp_html.forms.input_` element that creates elements with the appropriate
    `form-control` CSS class depending on the input's type.

    See https://getbootstrap.com/docs/4.0/components/forms/#form-controls.
    """

    __slots__ = ()

    def __init__(self, class_: Optional[str] = None, type_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        if type_ == "file":
            class_ = join("form-control-file", class_)
        elif type_ in ("radio", "checkbox"):
            class_ = join("form-check-input")
        else:
            class_ = join("form-control", class_)
        super().__init__(class_=class_, type_=type_, **kwargs)


class select(forms.select):
    """
    `markyp_html.forms.select` element with `form-control` CSS class.
    """

    __slots__ = ()

    def __init__(self, *args: forms.option, class_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        super().__init__(*args, class_=join("form-control", class_), **kwargs)


class textarea(forms.textarea):
    """
    `markyp_html.forms.textarea` element with `form-control` CSS class.
    """

    __slots__ = ()

    def __init__(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        super().__init__(*args, class_=join("form-control", class_), **kwargs)


def form_check(*args: ElementType,
               inline: bool = False,
               class_: Optional[str] = None,
               **kwargs: PropertyValue) -> div:
    """
    Creates a `div` with `form-check` style.

    Positional arguments will become the children elements of the created `div`.
    This element usually wraps a checkbox or radio `input_` element and its label.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    See https://getbootstrap.com/docs/4.0/components/forms/#checkboxes-and-radios.

    Arguments:
        inline: Whether the `input_` element and its label is part of an inline (horizontal)
                group of elements, rather than a vertical group.
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("form-check-inline" if inline else "form-check", class_), **kwargs)


def form_check_label(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> forms.label:
    """
    Creates a `forms.label` element with `form-check-label` style (a label for a
    checkbox or radio `input_`).

    Positional arguments will become the children elements of the created `label`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `label`.

    Arguments:
        class_: Additional CSS class names to set on the created `label`.
    """
    return forms.label(*args, class_=join("form-check-label", class_), **kwargs)


def form_label(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> forms.label:
    """
    Creates a `forms.label` element with `col-form-label` style.

    Positional arguments will become the children elements of the created `label`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `label`.

    See https://getbootstrap.com/docs/4.0/components/forms/#horizontal-form.

    Arguments:
        class_: Additional CSS class names to set on the created `label`.
    """
    return forms.label(*args, class_=join(FormStyle.LABEL_COLUMN, class_), **kwargs)


def form_group(*args: ElementType, class_: Optional[str] = None, row: bool = False, **kwargs: PropertyValue) -> div:
    """
    Creates an `form-group` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    See https://getbootstrap.com/docs/4.0/components/forms/#form-groups.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        row: Whether to also add the `row` CSS class to the form group.
    """
    return div(*args, class_=join("form-group", "row" if row else None, class_), **kwargs)


def form_row(*args: ElementType, class_: Optional[str] = None) -> div:
    """
    Creates a `form-row` `div` element.

    Positional arguments will become the children elements of the created `div`.

    See https://getbootstrap.com/docs/4.0/components/forms/#form-grid.

    Arguments:
        class_: Additional classes to add to the `form-row` `div` that wraps the given elements.
    """
    return div(*args, class_=join("form-row", class_))


def inline_form(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> forms.form:
    """
    Creates a `form-inline` `form` element.

    Positional arguments will become the children elements of the created `form`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `form`.

    See https://getbootstrap.com/docs/4.0/components/forms/#inline-forms.

    Arguments:
        class_: Additional CSS class names to set on the created `form`.
    """
    return forms.form(*args, class_=join("form-inline", class_), **kwargs)
