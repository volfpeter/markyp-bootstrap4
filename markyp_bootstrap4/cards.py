"""
Bootstrap card elements.

See https://getbootstrap.com/docs/4.0/components/card/.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp.elements import Element
from markyp_html import join
from markyp_html.block import div
from markyp_html.inline import img
from markyp_html.text import StyledTextFactory


title: StyledTextFactory = StyledTextFactory("card-title")
"""
Text element factory that produces elements with `card-title` CSS class.
"""


subtitle: StyledTextFactory = StyledTextFactory("card-subtitle text-muted mb-2")
"""
Text element factory that produces elements with `card-subtitle text-muted mb-2` CSS class.
"""


text: StyledTextFactory = StyledTextFactory("card-text")
"""
Text element factory that produces elements with `card-text` CSS class.
"""


def card(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `card` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card", class_), **kwargs)


def card_body(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` that should wrap the body of a card.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card-body", class_), **kwargs)


def image_top(src: str, *, class_: Optional[str] = None, **kwargs: PropertyValue) -> img:
    """
    Creates an `img` element that is meant to be positioned at the top of the card.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        src: The URL of the image the card should show.
        class_: Additional CSS class names to set on the created `img`.
    """
    return img(src=src, class_=join("card-img-top", class_), **kwargs)
