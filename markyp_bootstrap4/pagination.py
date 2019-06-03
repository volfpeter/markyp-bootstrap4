"""
Bootstrap pagination elements.

See https://getbootstrap.com/docs/4.0/components/pagination/.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp_html import block, inline, join, lists

__all__ = (
    "PaginationPosition", "PaginationSize",
    "base_page_item", "page_item", "page_link", "pagination"
)


class PaginationPosition(object):
    """
    Enumeration class that lists pagination position options.
    """

    LEFT = None

    CENTER = "justify-content-center"

    END = "justify-content-end"


class PaginationSize(object):
    """
    Enumeration class that lists pagination size options.
    """

    DEFAULT = None

    LARGE = "pagination-lg"

    SMALL = "pagination-sm"


def base_page_item(*args: ElementType,
                   active: bool = False,
                   class_: Optional[str] = None,
                   disabled: bool = False,
                   **kwargs: PropertyValue) -> lists.li:
    """
    Creates a `li` element with `page-item` style.

    Page items typically contain an anchor element (`page_link()`) that holds their content
    and performs the pagination. If this typical page item configuration suits you and you
    don't need special styling, then have a look at `page_item()` that automatically creates
    the inner anchor (`page_link()`) for you.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        active: Whether the page item should have the active state.
        class_: Additional CSS class names to set on the created element.
        disabled: Whether the page item should be disabled.
    """
    return lists.li(
        *args,
        class_=join(
            "page-item",
            "active" if active else None,
            "disabled" if disabled else None,
            class_
        ),
        **kwargs
    )


def page_item(*args: ElementType,
              active: bool = False,
              class_: Optional[str] = None,
              disabled: bool = False,
              link_class: Optional[str] = None,
              **kwargs: PropertyValue) -> lists.li:
    """
    Creates a `li` element with `page-item` style that automatically wraps its children
    elements in a `page_link()` element.

    The key difference between this element and `base_page_item()` is that `page_item()`
    automatically wraps its content in a `page_link()` element, that is the typicaly use-case.

    Positional arguments will become the children of the `page_link()` element that is
    inside the created page item.

    Keyword arguments not listed in the arguments section are turned into element attributes
    on the `page_link()` element that is inside the created page item.

    Arguments:
        active: Whether the page item should have the active state.
        class_: Additional CSS class names to set on the created element.
        disabled: Whether the page item should be disabled.
        link_class: Additional CSS class names to set on the inner `page_link()` element.
    """
    return base_page_item(
        page_link(*args, class_=link_class, **kwargs),
        active=active,
        class_=class_,
        disabled=disabled
    )


def page_link(*args: ElementType,
              class_: Optional[str] = None,
              **kwargs: PropertyValue) -> inline.a:
    """
    Creates an anchor (`a`) element with `page-link` style.

    `page_link()` elements are normally placed inside `base_page_item()` elements. This
    arrangment is automatically implemented by `page_item()`, use that method unless
    you have very specific requirements.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
    """
    return inline.a(*args, class_=join("page-link", class_), **kwargs)


def pagination(*args: ElementType,
               aria_label: Optional[str] = "Pagination",
               class_: Optional[str] = None,
               position: Optional[str] = PaginationPosition.LEFT,
               size: Optional[str] = PaginationSize.DEFAULT,
               wrap_in_nav: bool = True,
               **kwargs: PropertyValue) -> block.nav:
    """
    Creates a `pagination` `ul` element.

    Positional arguments will become the children of the created list element.
    They should normally be `page_item()` elements.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        aria_label: The desired ARIA label for the wrapping `nav` (if one is created).
        class_: Additional CSS class names to set on the created element.
        position: The desired position of the created element, must be one of the constants
                  from the `PaginationPosition` class.
        size: The desired size of the created element, must be one of the constants from
              the `PaginationSize` class.
        wrap_in_nav: Whether to wrap the `pagination` `ul` in a `nav` component.
    """
    result = lists.ul(
        *args,
        class_=join("pagination", size, position, class_),
        **kwargs
    )
    return block.nav(result, **{"aria-label": aria_label} if aria_label else {}) \
        if wrap_in_nav else result
