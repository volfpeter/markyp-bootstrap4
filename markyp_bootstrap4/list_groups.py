"""
Bootstrap list group elements.

See https://getbootstrap.com/docs/4.0/components/list-group/.
"""

from typing import Optional, Type

from markyp import ElementType, PropertyValue
from markyp.elements import Element
from markyp_html import join
from markyp_html.lists import li, ul


__all__ = ("ItemContext", "list_group", "list_group_item")


class ItemContext(object):
    """
    Class that list possible list group item contexts.
    """

    PRIMARY: str = "primary"

    SECONDARY: str = "secondary"

    SUCCESS: str = "success"

    DANGER: str = "danger"

    WARNING: str = "warning"

    INFO: str = "info"

    LIGHT: str = "light"

    DARK: str = "dark"

    @staticmethod
    def get_class(context: Optional[str] = None) -> Optional[str]:
        """
        Returns the list group item CSS class name for the given context or
        `None` if no context was specified.

        Arguments:
            context: One of the context constants from this class or `None`.
        """
        return f"list-group-item-{context}" if context else None


def list_group(*args: ElementType,
               class_: Optional[str] = None,
               factory: Type[Element] = ul,
               flush: bool = False,
               **kwargs: PropertyValue) -> Element:
    """
    Creates a list group.

    Positional arguments will become the children elements of the created list group.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created list group.

    Arguments:
        class_: Additional CSS class names to set on the created list item.
        factory: Element factory to use to create the list group.
        flush: Whether the created list group should have the `list-group-flush`
               CSS class that removes some borders and rounded corners to render
               items edge-to-edge in the parent container.
    """
    return factory(
        *args,
        class_=join(
            "list-group",
            "list-group-flush" if flush else None,
            class_
        ),
        **kwargs
    )


def list_group_item(*args: ElementType,
                    action: bool = False,
                    active: bool = False,
                    class_: Optional[str] = None,
                    context: Optional[str] = None,
                    disabled: bool = False,
                    factory: Type[Element] = li,
                    **kwargs: PropertyValue) -> Element:
    """
    Creates a list group item.

    Positional arguments will become the children elements of the created list group item.

    Keyword arguments not listed in the arguments section are turned into element
    attributes on the created list group item.

    Arguments:
        action: Whether the item represents an action and should have the
                `list-group-item-action` CSS class. When `True`, the factory
                should be an actionable element such as `a` or `button`.
        active: Whether the created item should have the `active` CSS class.
        class_: Additional CSS class names to set on the created list item.
        context: An `ItemContext` constant to create the list group item with.
        disabled: Whether the created item should have the `disabled` CSS class.
        factory: Element factory to use to create the list group item.
    """
    return factory(
        *args,
        class_=join(
            "list-group-item",
            "list-group-item-action" if action else None,
            ItemContext.get_class(context),
            "active" if active else None,
            "disabled" if disabled else None,
            class_),
        **kwargs
    )
