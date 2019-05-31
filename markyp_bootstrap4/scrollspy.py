"""
Bootstrap scrollspy-related components.

See https://getbootstrap.com/docs/4.0/components/scrollspy/.
"""

__all__ = ("spied_by",)


from markyp import PropertyDict


def spied_by(spy: str, *, offset: int = 0) -> PropertyDict:
    """
    Returns a `PropertyDict` whose items must be added to the spied element as attributes
    (it is usually done by `element(..., **spied_by())`).

    Arguments:
        spy: The ID of the element (typically a `nav` or `list_group` with anchor elements in it)
             or the CSS class of the elements (in which case the attribute must start with a `.`
             character) that are spying on the scroll position.
        offset: Pixels to offset from top when calculating position of scroll.
    """
    return {
        "data-spy": "scroll",
        "data-target": spy if spy[0] in (".", "#") else f"#{spy}",
        "data-offset": offset
    }
