"""
Bootstrap modal elements.

See https://getbootstrap.com/docs/4.0/components/modal/.
"""

from typing import List, Optional, Type

from markyp import ElementType, PropertyDict, PropertyValue, elements
from markyp_html import join
from markyp_html.block import div
from markyp_html.forms import button
from markyp_html.text import StyledTextFactory

from markyp_bootstrap4.buttons import ElementButtonFactory


__all__ = (
    "title",
    "CloseButtonFactory", "close_button",
    "ModalToggleButtonFactory", "toggle_button",
    "modal",
    "modal_element", "modal_dialog_base", "modal_content",
    "modal_header", "modal_body", "modal_footer"
)


title: StyledTextFactory = StyledTextFactory("modal-title")
"""
Factory that creates text elements with `modal-title` style for modal titles.
"""


class CloseButtonFactory(ElementButtonFactory):
    """
    Button factory that creates "close" buttons for modals.
    """

    __slots__ = ()

    def __init__(self, generator: Optional[Type[elements.Element]] = None) -> None:
        super().__init__(generator or button)

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        attributes = super().update_attributes(attributes, disabled=disabled, active=active)
        attributes["data-dismiss"] = "modal"
        return attributes


class ModalToggleButtonFactory(ElementButtonFactory):
    """
    Button factory that creates buttons that can toggle the visibility of a modal.

    The `modal_id` attribute must be set on the button to the ID of the modal it should toggle,
    otherwise clicking the button will not have any effect.
    """

    __slots__ = ()

    def __init__(self, generator: Optional[Type[elements.Element]] = None) -> None:
        super().__init__(generator or button)

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        attributes = super().update_attributes(attributes, disabled=disabled, active=active)
        attributes["data-toggle"] = "modal"
        if "modal_id" in attributes:
            attributes["data-target"] = f"#{attributes['modal_id']}"
            del attributes["modal_id"]
        return attributes


close_button: CloseButtonFactory = CloseButtonFactory()
"""
Factory that creates buttons that dismiss the modal they are in.
"""


toggle_button: ModalToggleButtonFactory = ModalToggleButtonFactory()
"""
Factory that creates buttons that can toggle the visibility of a modal.

The `modal_id` attribute must be set on the button to the ID of the modal it should toggle,
otherwise clicking the button will not have any effect.
"""


def modal(*args: ElementType,
          id: str,
          title: Optional[ElementType] = None,
          footer: Optional[ElementType] = None,
          add_close_button: bool = True,
          centered: bool = False,
          fade: bool = True,
          class_: Optional[str] = None,
          dialog_class: Optional[str] = None,
          content_class: Optional[str] = None,
          header_class: Optional[str] = None,
          body_class: Optional[str] = None,
          footer_class: Optional[str] = None) -> div:
    """
    Higher order component that creates a complete Bootstrap modal.

    Positional arguments will form the modal's main content after being wrapped
    in a `modal_body` element.

    Arguments:
        id: The unique identifier of the modal.
        title: The title of the modal, normally an element produced by the `title` factory.
        footer: The element to put inside the footer of the modal
              (not a `modal_footer()`, only its content).
        add_close_button: Whether to add a close button to the top right corner.
        centered: Whether the content of the modal should be centered.
        fade: Whether to apply the fade effect when the modal is shown.
        class_: Additional CSS class names to set on the `modal`.
        dialog_class: Additional CSS class names to set on the `modal`'s `modal_dialog_base`.
        content_class: Additional CSS class names to set on the `modal`'s `modal_content`.
        header_class: Additional CSS class names to set on the `modal`, `modal_header`.
        body_class: Additional CSS class names to set on the `modal`, `modal_body`.
        footer_class: Additional CSS class names to set on the `modal`, `modal_footer`.
    """
    header: List[ElementType] = []
    if title:
        header.append(title)
    if add_close_button:
        from markyp_html.entities import times
        from markyp_html.inline import span
        header.append(button(
            span(times, **{"aria-hidden": True}),
            type="button", class_="close", **{"data-dismiss": "modal", "aria-label": "Close"}
        ))
    return modal_element(
        modal_dialog_base(
            modal_content(
                modal_header(*header, class_=header_class) if len(header) > 0 else None,
                modal_body(*args, class_=body_class),
                modal_footer(footer, class_=footer_class) if footer is not None else None,
                class_=content_class
            ),
            centered=centered,
            class_=dialog_class
        ),
        class_=class_,
        fade=fade,
        id=id
    )


def modal_element(*args: ElementType,
                  class_: Optional[str] = None,
                  fade: bool = True,
                  **kwargs: PropertyValue) -> div:
    """
    Creates a `modal` `div` that is the root element of modals.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        fade: Whether to apply the fade effect when the modal is shown.
    """
    return div(
        *args,
        class_=join("modal", "fade" if fade else None, class_),
        role="dialog",
        tabindex=-1,
        **kwargs
    )


def modal_dialog_base(*args: ElementType,
                      centered: bool = False,
                      class_: Optional[str] = None,
                      **kwargs: PropertyValue) -> div:
    """
    Creates a `modal-dialog` `div` that is the element right inside `modal_element`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        centered: Whether to center the content of the modal.
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(
        *args,
        class_=join("modal-dialog", "modal-dialog-centered" if centered else None, class_),
        role="document",
        **kwargs
    )


def modal_content(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `modal-content` `div` that is the element inside `modal_dialog_base`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("modal-content", class_), **kwargs)


def modal_header(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `modal-header` `div` that is the optional first element inside `modal_content`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("modal-header", class_), **kwargs)


def modal_body(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `modal-body` `div` that is the element following `modal_header` inside `modal_content`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("modal-body", class_), **kwargs)


def modal_footer(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `modal-footer` `div` that is an optional element following `modal_body` inside `modal_content`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("modal-footer", class_), **kwargs)
