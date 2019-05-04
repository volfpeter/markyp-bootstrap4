"""
Bootstrap input group elements.

See https://getbootstrap.com/docs/4.0/components/input-group/.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp_html import join
from markyp_html.block import div
from markyp_html.text import StyledTextFactory


__all__ = ("text", "InputGroupStyle", "input_group", "pre_group", "post_group")


text: StyledTextFactory = StyledTextFactory("input-group-text")
"""
Input group text factory.

Elements created by this factory are normally placed in `pre_group()` or `post_group()` elements.
"""


class InputGroupStyle(object):
    """
    A set of CSS class names that can be applied on input groups.
    """

    __slots__ = ()

    SMALL: str = "input-group-sm"

    LARGE: str = "input-group-lg"


def input_group(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates an `input-group` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Positional arguments typically consist of zero or one `pre_group()` element,
    one or more `input_` elements, and finally zero or one `post_group()` element.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("input-group", class_), **kwargs)


def pre_group(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates an `input-group-prepend` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("input-group-prepend", class_), **kwargs)


def post_group(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates an `input-group-append` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("input-group-append", class_), **kwargs)
