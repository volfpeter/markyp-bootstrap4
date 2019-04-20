"""
Bootstrap badge elements.
"""

from typing import Optional, Type, Union

from markyp import ElementType, PropertyValue
from markyp.elements import Element
from markyp_html.inline import a, span


__all__ = ("BadgeFactory", "a_badge", "span_badge")


class BadgeFactory(object):
    """
    Badge element factory.
    """

    __slots__ = ("_generator",)

    def __init__(self, generator: Type[Element]) -> None:
        """
        Initialization.

        Arguments:
            generator: The type of the elements the factory will produce.
        """
        self._generator: Type[Element] = generator
        """
        The type of the elements the object will produce.
        """

    def primary(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-primary"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def primary_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-primary"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def secondary(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-secondary"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def secondary_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-secondary"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def success(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-success"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def success_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-success"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def danger(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-danger"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def danger_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-danger"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def warning(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-warning"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def warning_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-warning"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def info(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-info"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def info_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-info"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def light(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-light"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def light_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-light"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def dark(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-dark"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)

    def dark_pill(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> Element:
        base_class = "badge badge-pill badge-dark"
        return self._generator(*args, class_=f"{base_class} {class_}" if class_ else base_class, **kwargs)


a_badge: BadgeFactory = BadgeFactory(a)
"""
Badge factory that creates anchor (`a`) elements.
"""


span_badge: BadgeFactory = BadgeFactory(span)
"""
Badge factory that creates `span` elements.
"""
