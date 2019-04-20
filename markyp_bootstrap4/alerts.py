"""
Boostrap alert elements and utilities.

See https://getbootstrap.com/docs/4.0/components/alerts/.
"""

from typing import Optional

from markyp import ElementType
from markyp_bootstrap4.elements import close_icon
from markyp_html.block import div


__all__ = ("alert", "dismissable")


class alert(div):
    """
    Bootstrap alert element.

    See https://getbootstrap.com/docs/4.0/components/alerts/.
    """

    __slots__ = ()

    @classmethod
    def primary(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `primary` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="primary", class_=class_)

    @classmethod
    def secondary(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `secondary` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="secondary", class_=class_)

    @classmethod
    def success(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `success` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="success", class_=class_)

    @classmethod
    def danger(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `danger` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="danger", class_=class_)

    @classmethod
    def warning(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `warning` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="warning", class_=class_)

    @classmethod
    def info(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `info` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="info", class_=class_)

    @classmethod
    def light(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `light` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="light", class_=class_)

    @classmethod
    def dark(cls, *args: ElementType, class_: Optional[str] = None) -> "alert":
        """
        Returns an alert element with `dark` context.

        Positional arguments will become the children elements of the alert.

        Arguments:
            class_: Any additional CSS class names to add to the element.
        """
        return cls(*args, context="dark", class_=class_)

    def __init__(self,
                 *args: ElementType,
                 context: str,
                 class_: Optional[str] = None) -> None:
        """
        Initialization.

        Positional arguments will become the children elements of the alert.

        Arguments:
            context: One of Bootstrap's context string (primary, info, success, danger, etc.).
            class_: Any additional CSS class names to add to the element.
        """
        base_class = f"alert alert-{context}"
        super().__init__(
            *args,
            class_=f"{base_class} {class_}" if class_ else base_class,
            role="alert"
        )

    @property
    def element_name(self) -> str:
        return "div"


class dismissable(alert):
    """
    Dismissable Bootstrap alert element.

    See https://getbootstrap.com/docs/4.0/components/alerts/.
    """

    __slots__ = ()

    def __init__(self,
                 *args: ElementType,
                 context: str,
                 class_: Optional[str] = None) -> None:
        """
        Initialization.

        Positional arguments will become the children elements of the alert.

        Additionally, a dismiss button will be automatically added to the alert.

        Arguments:
            context: One of Bootstrap's context string (primary, info, success, danger, etc.).
            class_: Any additional CSS class names to add to the element.
        """
        base_class = "alert-dismissible fade show"
        super().__init__(
            *args, close_icon(**{"data-dismiss": "alert"}),
            class_=f"{base_class} {class_}" if class_ else base_class,
            context=context
        )
