"""
Bootstrap carousel elements.

See https://getbootstrap.com/docs/4.0/components/carousel/.
"""

from typing import Optional, Tuple

from markyp import ElementType, PropertyValue
from markyp_html import join
from markyp_html.block import div
from markyp_html.inline import a, span
from markyp_html.lists import ol, li


__all__ = ("carousel", "controls", "indicators", "inner", "item", "item_caption", "slide")


def carousel(*args: ElementType,
             identifier: str,
             add_controls: bool = True,
             add_indicators: bool = True,
             interval: Optional[int] = None,
             keyboard: Optional[bool] = None,
             wrap: Optional[bool] = None,
             class_: Optional[str] = None,
             **kwargs: PropertyValue) -> div:
    """
    Creates a carousel.

    Keyword arguments not listed in the arguments section are turned into element attributes
    on the created `slide` element. If you need to put multiple HTML elements into the same
    carousel item and you would like to save a wrapper `div`, you should have a look at the
    `markyp.elements.ElementSequence` element.

    Positional arguments are wrapped in `item` elements one-by-one and they will form
    the main content of the carousel.

    Arguments:
        identifier: The identifier of the carousel. It must be unique in the entire webpage.
        add_controls: Whether to add control elements to the carousel.
        add_indicators: Whether to add indicator elements to the carousel.
        interval: The amount of time (in milliseconds) to wait between cycling carousel items.
        keyboard: Whether the carousel should react to keyboard events.
        wrap: Whether the carousel should cycle continuously or have hard stops.
        class_: CSS classes to add to the created `slide` element.
    """
    if "data-interval" not in kwargs and interval is not None:
        kwargs["data-interval"] = interval
    if "data-keyboard" not in kwargs and keyboard is not None:
        kwargs["data-keyboard"] = keyboard
    if "data-wrap" not in kwargs and wrap is not None:
        kwargs["data-wrap"] = wrap
    return slide(
        indicators(identifier, len(args)) if add_indicators else "",
        inner(*[item(arg, active=i==0) for i, arg in enumerate(args)]),
        *controls(identifier) if add_controls else ("", ""),
        identifier=identifier,
        class_=class_,
        **kwargs
    )


def controls(carousel_id: str, *, class_: Optional[str] = None, **kwargs: PropertyValue) -> Tuple[a, a]:
    """
    Creates a pair of anchor elements that serve as the previous and next item controls
    for the carousel with the given identifier.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created anchor elements.

    Arguments:
        carousel_id: The identifier of the carousel to control.
        class_: CSS classes to add to the created anchor elements besides `carousel-control-{prev|next}`.
    """
    return (
        a(
            span(class_="carousel-control-prev-icon", **{"aria-hdden": True}),
            span("Previous", class_="sr-only"),
            class_=join("carousel-control-prev", class_),
            href=f"#{carousel_id}",
            role="button",
            **{**kwargs, "data-slide": "prev"}
        ),
        a(
            span(class_="carousel-control-next-icon", **{"aria-hdden": True}),
            span("Next", class_="sr-only"),
            class_=join("carousel-control-next", class_),
            href=f"#{carousel_id}",
            role="button",
            **{**kwargs, "data-slide": "next"}
        )
    )


def indicators(carousel_id: str, n: int, *, active_index: int = 0, class_: Optional[str] = None, **kwargs: PropertyValue) -> ol:
    """
    Creates an indicator list for the carousel with the given identifier.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created indicator elements.

    Arguments:
        carousel_id: The identifier of the carousel to control.
        n: The number of items in the carousel (and the number of required indicators).
        active_index: The index of the indicator that should be active by default.
        class_: CSS classes to add to the created indicator elements.
    """
    return ol(
        *(li(class_=join("active" if active_index == i else None, class_) or None, **{**kwargs, "data-target": f"#{carousel_id}", "data-slide-to": i}) for i in range(n)),
        class_="carousel-indicators"
    )


def inner(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `carousel-inner` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("carousel-inner", class_), **kwargs)


def item(*args: ElementType, active: bool = False, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `div` element with `carousel-item` style.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        active: Whether this item should be the active one in the carousel.
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("carousel-item", "active" if active else None, class_), **kwargs)


def item_caption(*args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a caption element for a carousel item.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments are turned into element attributes on the created `div`.

    Arguments:
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("carousel-caption d-none d-md-block", class_), **kwargs)


def slide(*args: ElementType, identifier: str, class_: Optional[str] = None, **kwargs: PropertyValue) -> div:
    """
    Creates a `carousel slide` `div`, the outer, main element of carousels.

    Positional arguments will become the children elements of the created `div`.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created `div`.

    Arguments:
        identifier: The identifier of the carousel. It must be unique in the entire webpage.
        class_: Additional CSS class names to set on the created `div`.
    """
    return div(*args, class_=join("carousel slide", class_), **{**kwargs, "data-ride": "carousel", "id": identifier})
