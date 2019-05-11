"""
Bootstrap dropdown and dropdown button elements.

See https://getbootstrap.com/docs/4.0/components/dropdowns/.
"""

from typing import Optional, Type

from markyp import ElementType, IElement, PropertyDict, PropertyValue
from markyp_html import join
from markyp_html.block import div
from markyp_html.forms import button
from markyp_html.text import StyledTextFactory

from markyp_bootstrap4.buttons import ElementButtonFactory


__all__ = (
    "DropdownButtonFactory",
    "dropdown", "dropdown_button",
    "menu", "menu_item", "menu_header", "menu_divider"
)


class DropdownButtonFactory(ElementButtonFactory):
    """
    Button element factory that is specialized for dropdown buttons.
    """

    __slots__ = ()

    def __init__(self) -> None:
        """
        Initialization.
        """
        super().__init__(button)

    def get_css_class(self,
                      context: str,
                      *,
                      class_: Optional[str] = None,
                      outline: bool = False,
                      active: bool = False) -> str:
        return super().get_css_class(
            context,
            class_=join("dropdown-toggle", class_),
            outline=outline,
            active=active
        )

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        attributes = super().update_attributes(attributes, disabled=disabled, active=active)
        attributes["data-toggle"] = "dropdown"
        attributes["aria-haspopup"] = True
        attributes["aria-expanded"] = False
        return attributes


dropdown_button: DropdownButtonFactory = DropdownButtonFactory()
"""
Button factory that creates dropdown buttons.

Dropdown buttons should have a unique identifier (`id` attribute)
that can be referenced by the dropdown menu.
"""


menu_header: StyledTextFactory = StyledTextFactory("dropdown-header")
"""
Header item factory for dropdown menus.
"""


def dropdown(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `dropdown` `div` wrapper for a dropdown button and menu.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Positional arguments are typically a `dropdown_button` followed by a `menu`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("dropdown", class_), **kwargs)


def menu(*args: ElementType, button_id: str, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a dropdown menu element (`div` with `dropdown-menu` style).

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Positional argument are typically `menu_header`s, `menu_item`s and `menu_divider`s.

    Arguments:
        button_id: The identifier of the `dropdown` button that controls this menu.
        class_: Additional CSS class names to set on the created `div`.
    """
    kwargs["aria-labelledby"] = button_id
    return div(*args, class_=join("dropdown-menu", class_), **kwargs)


def menu_divider(*, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a divider menu item (`div` with `dropdown-divider` class).

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(class_=join("dropdown-divider", class_), **kwargs)


def menu_item(*args: ElementType,
              active: bool = False,
              class_: Optional[str] = None,
              disabled: bool = False,
              factory: Type[IElement] = button,
              **kwargs: PropertyValue) -> IElement:
    """
    Creates a dropdown menu item (from a `button` element).

    Positional arguments will become the children elements of the created `button`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `button`.

    Arguments:
        active: Whether to apply the `active` style on the menu item.
        class_: Additional CSS class names to set on the created menu item.
        disabled: Whether the menu item should be disabled.
        factory: An `IElement` type to create the menu item from, `button` by default.
                 The factory must support keyword arguments, and positional arguments
                 if they were passed in to this method.
    """
    class_ = join(
        "dropdown-item",
        "active" if active else None,
        "disabled" if disabled else None,
        class_
    )
    return factory(*args, class_=class_, type="button", **kwargs)
