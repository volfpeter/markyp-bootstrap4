"""
Bootstrap breadcrumb elements.
"""

from typing import Optional, Tuple

from markyp import ElementType, PropertyValue
from markyp_html.block import nav
from markyp_html.inline import a
from markyp_html.lists import ol, li


__all__ = ("custorm_breadcrumb", "breadcrumb", "breadcrumb_item")


def custom_breadcrumb(*args: li, class_: Optional[str] = None, **kwargs) -> nav:
    """
    Customizable Bootstrap breadcrumb element.

    Positional arguments must be list items (`li` instance) and they are added to
    the breadcrumb without modifications.

    Keyword arguments are added to the `breadcrumb` `ol` element as attributes.

    Arguments:
        class_: Additional CSS class names to apply on the `breadcrumb` `ol` element
                besides `breadcrumb`.
    """
    return nav(
        ol(
            *args,
            class_=f"breadcrumb {class_}" if class_ else "breadcrumb",
            **kwargs
        ),
        **{"aria-label": "breadcrumb"}
    )


def breadcrumb(*args: ElementType) -> nav:
    """
    Bootstrap breadcrumb element.

    ```HTML
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item">{pos-argument-1}</li>
            <li class="breadcrumb-item">{pos-argument-2}</li>
            ...
            <li class="breadcrumb-item active">{pos-argument-n}</li>
        </ol>
    </nav>
    ```

    Positional arguments are wrapped in breadcrumb list items and are added to
    the breadcrumb ordered list one-by-one. The last item will be the active one.
    """
    n = len(args) - 1
    return custom_breadcrumb(
        *(breadcrumb_item(item, active=i==n) for i, item in enumerate(args))
    )


def breadcrumb_item(*args: ElementType,
                    active: bool = False,
                    class_: Optional[str] = None,
                    **kwargs: PropertyValue) -> li:
    """
    Bootstrap breadcrumb item element.

    ```HTML
    <li class="breadcrumb-item {active}" aria-current="page">{positional arguments}</li>
    ```

    Positional arguments will become the children elements of the breadcrumb item.

    Keyword arguments that are not listed in the arguments section will be added to
    the created breadcrumb item (i.e. the wrapper `li` element).

    Arguments:
        active: Whether this is the active breadcrumb item.
        class_: CSS class names to set on the created `li` element.
    """
    base_class = "breadcrumb-item active" if active else "breadcrumb-item"
    return li(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)
