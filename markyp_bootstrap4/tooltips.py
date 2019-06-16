"""
Bootstrap tooltip elements.

See https://getbootstrap.com/docs/4.0/components/tooltips/.
"""

from typing import Optional

from markyp import PropertyDict, PropertyValue
from markyp_html import script


__all__ = ("enable_tooltips", "Placement", "tooltip")


enable_tooltips = script("$(function () { $('[data-toggle=\"tooltip\"]').tooltip() })")
"""
Script element that enables tooltip elements on the page.

See https://getbootstrap.com/docs/4.0/components/tooltips/#example-enable-tooltips-everywhere.
"""


class Placement(object):
    """
    Enumeration class that lists tooltip placement options.
    """

    TOP = "top"

    BOTTOM = "bottom"

    LEFT = "left"

    RIGHT = "right"


def tooltip(title: str,
            *,
            placement: str = Placement.TOP,
            **kwargs: PropertyValue) -> PropertyDict:
    """
    Returns a `PropertyDict` whose items must be added to the element that has the tooltip.

    Examples:

    ```Python
    p("Adding", em("tooltips", **tooltip("Hello")), "is pretty easy.")

    p("Adding", em("tooltips", **tooltip("Hello", placement=Placement.BOTTOM)), "is pretty easy.")
    ```

    Please see `enable_tooltips` for information on how to enable tooltips.

    Keyword arguments not listed in the arguments section will be included in the returned `PropertyDict`.

    Arguments:
        title: The content of the tooltip.
        placement: The desired placement of the tooltip, one of the constants from `Placement`.
    """
    kwargs["title"] = title
    kwargs["data-toggle"] = "tooltip"
    kwargs["data-placement"] = placement
    return kwargs
