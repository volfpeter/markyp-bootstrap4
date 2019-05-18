"""
Bootstrap tab elements.

This is not a separate component group in Bootstrap's documentation. You can find
examples in the List group and Navs sections of the documentation, see:

- https://getbootstrap.com/docs/4.0/components/list-group/
- https://getbootstrap.com/docs/4.0/components/navs/
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp_html import join
from markyp_html.block import div


__all__ = ("tab_content", "tab_pane")


def tab_content(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a wrapper `div` around a list of `tab_pane` elements.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created list item.
    """
    return div(*args, class_=join("tab-content", class_), **kwargs)


def tab_pane(*args: ElementType,
             active: bool = False,
             class_: Optional[str] = None,
             fade: bool = True,
             **kwargs: PropertyValue) -> div:
    """
    Create a tab pane element.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        active: Whether this should be the active pane by default.
        class_: Additional CSS class names to set on the created list item.
        fade: Whether to apply the fade effect on pane changes.
    """
    return div(
        *args,
        class_=join(
            "tab-pane",
            "fade" if fade else None,
            "show active" if active else None,
            class_
        ),
        role="tabpanel",
        **kwargs
    )
