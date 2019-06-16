"""
Bootstrap popover elements.

See https://getbootstrap.com/docs/4.0/components/popovers/.
"""

from typing import Optional

from markyp import PropertyDict, PropertyValue
from markyp_html import script


__all__ = ("enable_auto_dismiss", "enable_popovers", "Placement", "popover")


enable_auto_dismiss = script("$('.popover-dismiss').popover({ trigger: 'focus' })")
"""
Script element that enables the focus trigger for automatically dismissing popovers.

See https://getbootstrap.com/docs/4.0/components/popovers/#dismiss-on-next-click.
"""


enable_popovers = script("$(function () { $('[data-toggle=\"popover\"]').popover() })")
"""
Script element that enables popovers on the page.

See https://getbootstrap.com/docs/4.0/components/popovers/#example-enable-popovers-everywhere.
"""


class Placement(object):
    """
    Enumeration class that lists popover placement options.
    """

    TOP = "top"

    BOTTOM = "bottom"

    LEFT = "left"

    RIGHT = "right"


def popover(content: str,
            *,
            auto_dismissed: bool = False,
            container: Optional[str] = None,
            placement: str = Placement.TOP,
            title: Optional[str] = None,
            **kwargs: PropertyValue) -> PropertyDict:
    """
    Returns a `PropertyDict` whose items must be added to the button that triggers this popover.

    The button must be either a `button` or `a` element (see `buttons.a_button` and `buttons.b_button`).

    Examples:

    ```Python
    b_button.primary("Button label", **popover("Popover content"))

    b_button.info("Button label", **popover("Popover content", title="Popover title", placement=Placement.TOP))

    a_button.danger("Button label", **popover("Content", auto_dismissed=True))
    ```

    Please see `enable_popovers` and `enable_auto_dismiss` for information on how to enable popovers.

    Keyword arguments not listed in the arguments section will be included in the returned `PropertyDict`.

    Arguments:
        content: The content of popover.
        auto_dismissed: Whether the popover should be dismissed automatically when it loses focus.
            Requires `enable_auto_dismiss` to be added to the page.
        container: An optional element the popover should be appended to.
        placement: The desired placement of the popover, one of the constants from `Placement`.
        title: An optional title for the popover.
    """
    kwargs["data-content"] = content
    kwargs["data-placement"] = placement
    kwargs["data-toggle"] = "popover"

    if auto_dismissed:
        kwargs["tabindex"] = 0
        kwargs["data-trigger"] = "focus"

    if container is not None:
        kwargs["data-container"] = container

    if title is not None:
        kwargs["title"] = title

    return kwargs
