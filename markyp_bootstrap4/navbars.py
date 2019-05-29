"""
Bootstrap navbar elements.

See https://getbootstrap.com/docs/4.0/components/navbar/.
"""

from typing import Optional, Tuple

from markyp import ElementType, PropertyValue, elements
from markyp_html import block, forms, inline, join, text


__all__ = (
    "navbar_text", "ExpandPoint", "Theme", "brand",
    "collapse", "navbar", "navbar_nav", "navbar_toggler"
)


navbar_text: text.StyledTextFactory = text.StyledTextFactory("navbar-text")
"""
Text factory for text elements to be placed inside navbars.
"""


class ExpandPoint(object):
    """
    Enumeration class that lists the possible expand points for a navbar.
    """

    XS = "navbar-expand-xs"

    SM = "navbar-expand-sm"

    MD = "navbar-expand-md"

    LG = "navbar-expand-lg"

    XL = "navbar-expand-xl"


class Theme(object):
    """
    Enumeration class that lists the possible navbar themes.
    """

    DARK = "navbar-dark"

    LIGHT = "navbar-light"



def brand(*args: ElementType,
          class_: Optional[str] = None,
          href: str = "#",
          **kwargs: PropertyValue) -> inline.a:
    """
    Creates an anchor element with `navbar-brand` style.

    Positional argument will become the children of the created element.

    Keyword arguments not listed in the arguments section are tudned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
        href: Link to the page the brand element should navigate to when clicked.
    """
    return inline.a(*args, href=href, class_=join("navbar-brand", class_), **kwargs)


def collapse(*args: ElementType,
             id: str,
             class_: Optional[str] = None,
             nav_factory: Optional[elements.Element] = None,
             **kwargs: PropertyValue) -> block.div:
    """
    Creates a `navbar-collapse` element using the provided factory type.

    The collapse is normally placed inside a `navbar` element and holds the
    content of the navbar, typically wrapped in a `navbar_nav` element.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        id: The unique identifier of the collapse.
        class_: Additional CSS class names to set on the created element.
        nav_factory: An optional factory type to create a `navbar_nav` wrapper around
                     the positional arguments given to the method. If `None`, then the
                     positional arguments will not be wrapped in any way.
    """
    return block.div(
        *[navbar_nav(*args, factory=nav_factory)] if nav_factory is not None else args,
        class_=join("collapse navbar-collapse", class_),
        id=id,
        **kwargs
    )


def navbar(*args: ElementType,
           class_: Optional[str] = None,
           expand_point: Optional[str] = None,
           theme: Optional[str] = None,
           **kwargs: PropertyValue) -> block.nav:
    """
    Creates a `navbar` element.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
        expand_point: The point/screen size from which the navbar should be expanded.
                      It must be one of the constants from `ExpandPoint` or `None`.
        theme: The theme of the navbar. It must be one of the constants from the
               `Theme` class or `None`.
    """
    return block.nav(
        *args,
        class_=join(
            "navbar",
            expand_point,
            theme,
            class_
        ),
        **kwargs
    )


def navbar_nav(*args: ElementType,
               class_: Optional[str] = None,
               factory: elements.Element = block.div,
               **kwargs: PropertyValue) -> block.nav:
    """
    Creates a `navbar-nav` element using the given factory.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
        factory: The type or factory to use to create the element.
    """
    return factory(*args, class_=join("navbar-nav", class_), **kwargs)


def navbar_toggler(*,
                   collapse_id: str,
                   class_: Optional[str] = None,
                   **kwargs: PropertyValue) -> forms.button:
    """
    Creates a `navbar-toggler` button.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        collapse_id: The ID of the `collapse` the button toggles.
        class_: Additional CSS class names to set on the created button.
    """
    return forms.button(
        inline.span(class_="navbar-toggler-icon"),
        class_=join("navbar-toggler", class_),
        type="button",
        **kwargs,
        **{
            "data-toggle": "collapse",
            "data-target": f"#{collapse_id}",
            "aria-controls": collapse_id,
            "aria-expanded": False,
            "aria-label": "Toggle navigation"
        }
    )
