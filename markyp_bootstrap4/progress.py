"""
Bootstrap progress elements.

See https://getbootstrap.com/docs/4.0/components/progress/.
"""

from typing import Optional

from markyp import ElementType, PropertyDict, PropertyValue
from markyp_html import block, join


__all__ = ("progress", "progress_base", "progressbar")


def progress(*args: ElementType,
             value: int,
             animated: bool = False,
             bar_attributes: Optional[PropertyDict] = None,
             bar_class: Optional[str] = None,
             class_: Optional[str] = None,
             striped: bool = False,
             **kwargs: PropertyValue) -> block.div:
    """
    Higher order component that wraps a `progressbar` element in a `progress_base` element.

    Positional arguments will become the children of the inner `progressbar` element.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the outer `progress_base` element.

    Arguments:
        value: The percent value the bar should show, an integer in the [0, 100] interval.
        bar_attributes: Dictionary whose items will be set on the inner `progressbar` element
            as element attributes.
        bar_class: Additional CSS class names to set on the inner `progressbar` element.
        animated: Whether to animate the progressbar (requires `striped` to be `True`)
        class_: Additional CSS class names to set on the outer `progress_base` element.
        striped: Whether the progressbar should be striped.
    """
    return progress_base(
        progressbar(
            *args,
            value=value,
            animated=animated,
            class_=bar_class,
            striped=striped,
            **bar_attributes if bar_attributes else {}
        ),
        class_=class_,
        **kwargs
    )


def progress_base(*args: ElementType,
                  class_: Optional[str] = None,
                  **kwargs: PropertyValue) -> block.div:
    """
    Creates a `div` element with `progress` style.

    The created `div` serves as the background container for progress element and it
    usually contains one or more `progressbar` elements. If this default structure
    suits you, then have a look at `progress()`.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
    """
    return block.div(*args, class_=join("progress", class_), **kwargs)


def progressbar(*args: ElementType,
                value: int,
                animated: bool = False,
                class_: Optional[str] = None,
                striped: bool = False,
                **kwargs: PropertyValue) -> block.div:
    """
    Creates a `div` element with `progressbar` style.

    Progressbars are normally wrapped by `progress_base` elements. If this default
    structure suits you, then have a look at `progress()`.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        value: The percent value the bar should show, an integer in the [0, 100] interval.
        animated: Whether to animate the progressbar (requires `striped` to be `True`)
        class_: Additional CSS class names to set on the created element.
        striped: Whether the progressbar should be striped.
    """
    kwargs["style"] = join(f"width: {value}%;", kwargs.get("style", None))
    kwargs["role"] = "progressbar"
    kwargs["aria-valuenow"] = value
    kwargs["aria-valuemin"] = 0
    kwargs["aria-valuemax"] = 100
    return block.div(
        *args,
        class_=join(
            "progress-bar",
            "progress-bar-striped" if striped else None,
            "progress-bar-animated" if animated else None,
            class_
        ),
        **kwargs
    )
