"""
Elements that did not fit into another category.
"""

from markyp import PropertyValue

from markyp_html.forms import button
from markyp_html.entities import times
from markyp_html.inline import span
from markyp_html.block import div

from markyp_bootstrap4.layout import PercentSize


__all__ = ("close_icon", "row_break")


def close_icon(**kwargs: PropertyValue) -> button:
    """
    Bootstrap's generic close icon.

    ```HTML
    <button type="button" class="close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
    </button>
    ```
    """
    return button(
        span(times, **{"aria-hidden": True}),
        class_="close", **{**kwargs, "type": "button", "aria-label": "Close"}
    )


def row_break() -> div:
    """
    Returns a `div` that always spans a full row and as a result adds a
    line-break between row items.
    """
    return div(class_=PercentSize.width_100)
