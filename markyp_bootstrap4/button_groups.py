"""
Bootstrap button groups.

See https://getbootstrap.com/docs/4.3/components/button-group/.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp_html import join
from markyp_html.block import div


__all__ = ("BGSize", "button_group", "toggle_button_group")


class BGSize(object):
    """
    Button group size constants.
    """

    DEFAULT: None = None

    SMALL: str = "sm"

    LARGE: str = "lg"


def button_group(*args: ElementType,
                 class_: Optional[str] = None,
                 size: Optional[str] = BGSize.DEFAULT,
                 **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element that is styled as a button group.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        size: Optional size specification. The value of this argument must
              come from the `BGSize` enumeration class.
    """
    return div(*args, class_=join(f"btn-group-{size}" if size else "btn-group", class_), **kwargs)


def toggle_button_group(*args: ElementType,
                        class_: Optional[str] = None,
                        size: Optional[str] = BGSize.DEFAULT,
                        **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element that is styled as a toggle button group.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        size: Optional size specification. The value of this argument must
              come from the `BGSize` enumeration class.
    """
    kwargs["data-toggle"] = "buttons"
    return button_group(*args, class_=join("btn-group-toggle", class_), size=size, **kwargs)
