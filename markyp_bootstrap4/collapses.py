"""
Bootstrap collapse elements and utility methods.

See https://getbootstrap.com/docs/4.0/components/collapse/.
"""

from typing import Optional

from markyp import ElementType, PropertyDict, PropertyValue
from markyp_html import join
from markyp_html.block import div


__all__ = ("a_args_for", "button_args_for", "collapse")


def a_args_for(collapse_id: str, *, expanded: bool = False, **kwargs: PropertyValue) -> PropertyDict:
    """
    Updates the given keyword arguments with the arguments that are required for the
    anchor (`a`) element to be able to toggle the collapse with the given identifier.

    You will need to unpack the result of this method (i.e. use `**a_args_for()`)
    to pass on the updated values to the anchor (`a`) element.

    Note that this method only works for anchor (`a`) elements.

    Arguments:
        collapse_id: The identifier of the collapse the button arguments are required for.
        expanded: Whether the collapse is expanded by default.

    Returns:
        The updated keyword arguments dictionary.
    """
    kwargs["href"] = f"#{collapse_id}"
    kwargs["data-toggle"] = "collapse"
    kwargs["aria-controls"] = collapse_id
    kwargs["aria-expanded"] = expanded
    return kwargs


def button_args_for(collapse_id: str, *, expanded: bool = False, **kwargs: PropertyValue) -> PropertyDict:
    """
    Updates the given keyword arguments with the arguments that are required for the
    `button` element to be able to toggle the collapse with the given identifier.

    You will need to unpack the result of this method (i.e. use `**button_args_for()`)
    to pass on the updated values to the `button` element.

    Note that this method only works for `button` elements.

    Arguments:
        collapse_id: The identifier of the collapse the button arguments are required for.
        expanded: Whether the collapse is expanded by default.

    Returns:
        The updated keyword arguments dictionary.
    """
    kwargs["data-target"] = f"#{collapse_id}"
    kwargs["data-toggle"] = "collapse"
    kwargs["aria-controls"] = collapse_id
    kwargs["aria-expanded"] = expanded
    return kwargs


def collapse(*args: ElementType,
             identifier: str,
             class_: Optional[str] = None,
             accordion_id: Optional[str] = None,
             show: bool = False, **kwargs: PropertyValue) -> div:
    """
    Creates a `collapse [show]` `div` that wraps the collapsed content.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        identifier: The identifier of the collapse, must be unique in the webpage.
        class_: Additional CSS class names to set on the created `div`.
        accordion_id: The identifier of the accordion `div` if the collapse is
                      part of an accordion.
        show: Whether the collapse content should be visible by default.
    """
    if accordion_id is not None:
        kwargs["data-parent"] = f"#{accordion_id}"
    return div(*args, id=identifier, class_=join("collapse", "show" if show else None, class_), **kwargs)
