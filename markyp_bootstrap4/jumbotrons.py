"""
Bootstrap jumbotron elements.

See https://getbootstrap.com/docs/4.0/components/jumbotron/.
"""

from typing import Optional

from markyp import ElementType, PropertyDict, PropertyValue
from markyp_html import join
from markyp_html.block import div


__all__ = ("jumbotron", "rectangular_jumbotron")


def jumbotron(*args: ElementType,
              class_: Optional[str] = None,
              fluid: bool = False,
              **kwargs: PropertyValue) -> div:
    """
    Creates a `jumbotron` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        fluid: Whether to add the `jumbotron-fluid` CSS class to the jumbotron
               and make it take up the full width of its parent.
    """
    return div(*args, class_=join("jumbotron", "jumbotron-fluid" if fluid else None, class_), **kwargs)


def rectangular_jumbotron(*args: ElementType,
                          class_: Optional[str] = None,
                          fluid: bool = False,
                          **kwargs: PropertyValue) -> div:
    """
    Creates a rectangular `jumbotron` `div` by wrapping all the positional arguments
    in a `container` `div`.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
        fluid: Whether to add the `jumbotron-fluid` CSS class to the jumbotron
               and make it take up the full width of its parent.
    """
    return div(div(*args, class_="container"), class_=join("jumbotron", "jumbotron-fluid" if fluid else None, class_), **kwargs)
