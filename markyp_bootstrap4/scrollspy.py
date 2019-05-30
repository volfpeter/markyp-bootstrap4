"""
Bootstrap scrollspy-related components.

See https://getbootstrap.com/docs/4.0/components/scrollspy/.
"""

__all__ = ("spied_by",)


from markyp import PropertyDict


def spied_by(spy_id: str, offset: int = 0) -> PropertyDict:
    """
    Returns a `PropertyDict` whose items must be added to the spied element as attributes
    (it is usually done by `element(..., **spied_by())`).

    Arguments:
        spy_id: The ID of the element that is spying the scroll position
                (typically a `nav` or `list_group` with anchor elements in it).
        offset: Pixels to offset from top when calculating position of scroll.
    """
    return {
        "data-spy": "scroll",
        "data-target": f"#{spy_id}",
        "data-offset": offset
    }
