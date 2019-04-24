"""
Bootstrap card elements.

See https://getbootstrap.com/docs/4.0/components/card/.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp.elements import Element
from markyp_html import join
from markyp_html.block import div
from markyp_html.inline import a, img
from markyp_html.text import StyledTextFactory


__all__ = (
    "title", "subtitle", "text", "header", "footer", "TextAlign",
    "Image", "card", "body", "footer_div", "header_div", "link"
)


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


header: StyledTextFactory = StyledTextFactory("card-header")
"""
Text element factory that produces elements with `card-header` CSS class.
"""


footer: StyledTextFactory = StyledTextFactory("card-footer")
"""
Text element factory that produces elements with `card-footer` CSS class.
"""


class TextAlign(object):
    """
    Class that lists text alignment options for cards.
    """

    LEFT: str = "text-left"

    CENTER: str = "text-center"

    RIGHT: str = "text-right"


class Image(object):
    """
    Factory for images that are part of a card.
    """

    @staticmethod
    def bottom(src: str, *, class_: Optional[str] = None, **kwargs: PropertyValue) -> img:
        """
        Creates an `img` element that is meant to be positioned at the bottom of the card.

        Keyword arguments are turned into element attributes on the created `div`.

        Arguments:
            src: The URL of the image the card should show.
            class_: Additional CSS class names to set on the created `img`.
        """
        return img(src=src, class_=join("card-img-bottom", class_), **kwargs)

    @staticmethod
    def top(src: str, *, class_: Optional[str] = None, **kwargs: PropertyValue) -> img:
        """
        Creates an `img` element that is meant to be positioned at the top of the card.

        Keyword arguments are turned into element attributes on the created `div`.

        Arguments:
            src: The URL of the image the card should show.
            class_: Additional CSS class names to set on the created `img`.
        """
        return img(src=src, class_=join("card-img-top", class_), **kwargs)


def card(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `card` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card", class_), **kwargs)


def body(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` that should wrap the body of a card.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card-body", class_), **kwargs)


def footer_div(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `card-footer` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card-footer", class_), **kwargs)


def header_div(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `card-header` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("card-header", class_), **kwargs)


def link(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> a:
    """
    Creates an anchor (`a`) element with `card-link` style.

    Positional arguments will become the children elements of the created anchor.

    Keyword arguments are turned into element attributes on the created anchor.

    Arguments:
        class_: Additional CSS class names to set on the created anchor.
    """
    return a(*args, class_=join("card-link", class_), **kwargs)
