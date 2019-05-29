"""
Bootstrap navitation elements.

See https://getbootstrap.com/docs/4.0/components/navs/.
"""


from typing import Optional, Tuple, Type

from markyp import ElementType, PropertyDict, PropertyValue, elements
from markyp_html import inline, join, lists


__all__ = (
    "NavPosition", "NavStyle",
    "nav", "nav_item", "nav_link",
    "tab_link", "navigated_tabs"
)


class NavPosition(object):
    """
    Enumeration class that lists possible `nav` positions.
    """

    CENTER = "justify-content-center"

    DEFAULT = None

    END = "justify-content-end"


class NavStyle(object):
    """
    Enumeration class tat lists possible `nav` styles.
    """

    DEFAULT = None

    PILLS = "nav-pills"

    TABS = "nav-tabs"


def nav(*args: ElementType,
        class_: Optional[str] = None,
        factory: Type[elements.Element] = lists.ul,
        fill: bool = False,
        justified: bool = False,
        nav_position: Optional[str] = NavPosition.DEFAULT,
        nav_style: Optional[str] = NavStyle.DEFAULT,
        **kwargs: PropertyValue) -> elements.Element:
    """
    Creates a `nav` element using the provided factory type.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        class_: Additional CSS class names to set on the created element.
        factory: The type or factory to use to create the `nav`.
        fill: Whether the nav should fill the available space horizontally.
        justified: Whether all `nav` items should have the same width.
        nav_position: The desired position of the `nav` items, one of the
                      constants from the `NavPosition` class.
        nav_style: The desired style of the nav, one of the constants from
                   the `NavStyle` class.
    """
    return factory(
        *args,
        class_=join(
            "nav",
            "nav-fill" if fill else None,
            "nav-justified" if justified else None,
            nav_position,
            nav_style,
            class_
        ),
        **kwargs
    )


def nav_item(*args: ElementType,
             active: bool = False,
             class_: Optional[str] = None,
             disabled: bool = False,
             is_dropdown: bool = False,
             **kwargs: PropertyValue) -> lists.li:
    """
    Creates a `li` element with `nav-item` style.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        active: Whether the nav item should have the active state.
        class_: Additional CSS class names to set on the created element.
        disabled: Whether the nav item should be disabled.
        is_dropdown: Whether the nav item contains a dropdown and should
                     be styled accordingly.
    """
    return lists.li(
        *args,
        class_=join(
            "nav-item",
            "active" if active else None,
            "disabled" if disabled else None,
            "dropdown" if is_dropdown else None,
            class_
        ),
        **kwargs
    )


def nav_link(*args: ElementType,
             active: bool = False,
             class_: Optional[str] = None,
             disabled: bool = False,
             is_nav_item: bool = False,
             **kwargs: PropertyValue) -> inline.a:
    """
    Creates an anchor (`a`) element with `nav-link` style.

    Positional arguments will become the children of the created element.

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element.

    Arguments:
        active: Whether the nav item should have the active state.
        class_: Additional CSS class names to set on the created element.
        disabled: Whether the nav item should be disabled.
        is_nav_item: Whether the created element is a nav item as well and
                     should have the `nav-item` style as a result.
    """
    return inline.a(
        *args,
        class_=join(
            "nav-link",
            "nav-item" if is_nav_item else None,
            "active" if active else None,
            "disabled" if disabled else None,
            class_
        ),
        **kwargs
    )


def tab_link(*args: ElementType,
             pane_id: str,
             active: bool = False,
             class_: Optional[str] = None,
             disabled: bool = False,
             **kwargs: PropertyValue) -> inline.a:
    """
    Higher order component that creates a `nav_item` that wraps a `nav_link`
    that navigates a `tab_pane`.

    Positional arguments will become the children of the created element
    (the internal `nav_link`).

    Keyword arguments not listed in the arguments section are turned into
    element attributes on the created element (the internal `nav_link`).

    See `markyp_botstrap4.tabs` for more information on tab elements.

    Arguments:
        pane_id: The identifier of the `tab_pane` the created nav item should navigate.
        active: Whether the nav item should have the active state.
        class_: Additional CSS class names to set on the created element.
        disabled: Whether the nav item should be disabled.
    """
    return nav_item(
        nav_link(
            *args,
            active=active,
            class_=class_,
            disabled=disabled,
            href=f"#{pane_id}",
            role="tab",
            **kwargs,
            **{
                "data-toggle": "tab",
                "aria-controls": pane_id,
                "aria-selected": active
            }
        )
    )


def navigated_tabs(*args: Tuple[ElementType, ElementType],
                   id: str,
                   active_index: int = 0,
                   content_attributes: Optional[PropertyDict] = None,
                   content_class: Optional[str] = None,
                   item_attributes: Optional[PropertyDict] = None,
                   item_class: Optional[str] = None,
                   nav_attributes: Optional[PropertyDict] = None,
                   nav_class: Optional[str] = None,
                   nav_fill: bool = False,
                   nav_justified: bool = False,
                   nav_position: Optional[str] = NavPosition.DEFAULT,
                   pane_attributes: Optional[PropertyDict] = None,
                   pane_class: Optional[str] = None) -> Tuple[elements.Element, elements.Element]:
    """
    Higher order component that turns a list of element pairs (name and content) into
    a single navigated `nav` and `tab_content` pair.

    Positional arguments must be _name_ (typically a string) - _content_ (any HTML) pairs.
    The method will create a nav item from each name that will navigate the tab pane that
    is created from the corresponding content. The created nav items and tab panes will
    finally be wrapped in a `nav` and a `tab_content` element respectively thus creating
    the return value.

    See `markyp_botstrap4.tabs` for more information on tab elements.

    Arguments:
        id: A required base identifier to create element identifier from.
        active_index: The index of the nav item and tab pane that should be active
                      and visible by default.
        content_attributes: Dictionary whose items will be set on the created tab
                            container as element attributes.
        content_class: CSS class names to set on the created tab container.
        item_attributes: Dictionary whose items will be set on the created nav items
                         as element attributes.
        item_class: CSS class names to set on the created nav items.
        nav_attributes: Dictionary whose items will be set on the created nav
                        as element attributes.
        nav_class: CSS class names to set on the created nav.
        nav_fill: Whether the created nav should fill the available space horizontally.
        nav_justified: Whether all `nav` items should have the same width.
        nav_position: The desired position of the `nav` items, one of the
                      constants from the `NavPosition` class.
        pane_attributes: Dictionary whose items will be set on the created tab panes
                         as element attributes.
        pane_class: CSS class names to set on the created tab panes.

    Returns:
        A `nav` and `tab_content` pair whose content is created from the given list of element pairs.
    """
    from markyp_bootstrap4.tabs import tab_content, tab_pane

    empty: PropertyDict = {}
    if len(args) > 0:
        nav_items, tab_items = zip(*(
            (
                tab_link(
                    item,
                    active=index==active_index,
                    id=f"{id}-nav-{index}",
                    pane_id=f"{id}-pane-{index}",
                    class_=item_class,
                    **item_attributes if item_attributes else empty
                ),
                tab_pane(
                    data,
                    active=index==active_index,
                    id=f"{id}-pane-{index}",
                    class_=pane_class,
                    **pane_attributes if pane_attributes else empty,
                    **{"aria-labelled-by": f"{id}-nav-{index}"}
                )
            )
            for index, (item, data) in enumerate(args)
        ))
    else:
        nav_items, tab_items = [], []

    return (
        nav(
            *nav_items,
            id=f"{id}-nav",
            fill=nav_fill,
            justified=nav_justified,
            nav_position=nav_position,
            nav_style=NavStyle.TABS,
            class_=nav_class,
            **nav_attributes if nav_attributes else empty
        ),
        tab_content(
            *tab_items,
            id=f"{id}-tab-content",
            class_=content_class,
            **content_attributes if content_attributes else empty
        )
    )
