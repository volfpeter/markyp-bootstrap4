"""
Bootstrap button elements.

See https://getbootstrap.com/docs/4.3/components/buttons/.
"""

from typing import Optional, Type

from markyp import ElementType, PropertyDict, PropertyValue
from markyp.elements import Element, StandaloneElement
from markyp_html import join
from markyp_html.forms import button, input_, label
from markyp_html.inline import a


__all__ = (
    "ButtonContext", "ButtonStyle", "BaseButtonFactory", "BaseToggleButtonFactory",
    "ElementButtonFactory", "ElementToggleButtonFactory",
    "StandaloneElementButtonFactory", "StandaloneElementToggleButtonFactory",
    "a_button", "a_toggle",
    "b_button", "b_toggle",
    "i_button", "i_toggle",
    "l_button", "l_toggle"
)


class ButtonContext(object):
    """
    The set of existing button contexts.
    """

    PRIMARY: str = "primary"

    SECONDARY: str = "secondary"

    SUCCESS: str = "success"

    DANGER: str = "danger"

    WARNING: str = "warning"

    INFO: str = "info"

    LIGHT: str = "light"

    DARK: str = "dark"

    LINK: str = "link"


class ButtonStyle(object):
    """
    A set of CSS class names that can be applied on buttons.
    """

    __slots__ = ()

    ACTIVE: str = "active"

    BLOCK: str = "btn-block"

    DISABLED: str = "disabled"

    LARGE: str = "btn-lg"

    SMALL: str = "btn-sm"


class BaseButtonFactory(object):
    """
    Base class for button factories.

    See https://getbootstrap.com/docs/4.3/components/buttons/.
    """

    __slots__ = ()

    def create_element(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new element.

        Positional arguments will become the children of the created element if the element
        can have children, otherwise these arguments might be ignored or converted into an
        attribute (it is up to the factory).

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
        """
        raise NotImplementedError("create_element() is abstract.")

    def get_css_class(self,
                      context: str,
                      *,
                      class_: Optional[str] = None,
                      outline: bool = False,
                      active: bool = False) -> str:
        """
        Returns the CSS class string to set on the created element.

        Arguments:
            context: One of the constants from `ButtonContext`.
            class_: Additional CSS class names to include.
            outline: Whether an outline button is being created a basic one.
            active: Whether the button is active (i.e. selected).
        """
        base = f"btn btn-outline-{context}" if outline else f"btn btn-{context}"
        if active:
            base += " active"
        return f"{base} {class_}" if class_ else base

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        """
        Updates the given dictionary of element attribute name-value pairs with the
        attributes that are required by the button that is being created.

        _Never_ set the `class_` or `class` attributes in this method. Those attributes
        are dealt with in `get_css_class()`.

        Arguments:
            attributes: The element attribute dictionary to update.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        attributes["type"] = "button"
        if disabled:
            attributes["disabled"] = None
        if active:
            attributes["aria-pressed"] = True
        return attributes

    def primary(self,
                *args: ElementType,
                class_: Optional[str] = None,
                disabled: bool = False,
                active: bool = False,
                **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with primary context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.PRIMARY, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def primary_outline(self,
                        *args: ElementType,
                        class_: Optional[str] = None,
                        disabled: bool = False,
                        active: bool = False,
                        **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with primary context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.PRIMARY, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def secondary(self,
                  *args: ElementType,
                  class_: Optional[str] = None,
                  disabled: bool = False,
                  active: bool = False,
                  **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with secondary context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.SECONDARY, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def secondary_outline(self,
                          *args: ElementType,
                          class_: Optional[str] = None,
                          disabled: bool = False,
                          active: bool = False,
                          **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with secondary context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.SECONDARY, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def success(self,
                *args: ElementType,
                class_: Optional[str] = None,
                disabled: bool = False,
                active: bool = False,
                **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with success context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.SUCCESS, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def success_outline(self,
                        *args: ElementType,
                        class_: Optional[str] = None,
                        disabled: bool = False,
                        active: bool = False,
                        **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with success context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.SUCCESS, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def danger(self,
               *args: ElementType,
               class_: Optional[str] = None,
               disabled: bool = False,
               active: bool = False,
               **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with danger context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.DANGER, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def danger_outline(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       disabled: bool = False,
                       active: bool = False,
                       **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with danger context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.DANGER, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def warning(self,
                *args: ElementType,
                class_: Optional[str] = None,
                disabled: bool = False,
                active: bool = False,
                **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with warning context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.WARNING, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def warning_outline(self,
                        *args: ElementType,
                        class_: Optional[str] = None,
                        disabled: bool = False,
                        active: bool = False,
                        **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with warning context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.WARNING, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def info(self,
             *args: ElementType,
             class_: Optional[str] = None,
             disabled: bool = False,
             active: bool = False,
             **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with info context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.INFO, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def info_outline(self,
                     *args: ElementType,
                    class_: Optional[str] = None,
                    disabled: bool = False,
                    active: bool = False,
                    **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with info context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.INFO, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def light(self,
              *args: ElementType,
              class_: Optional[str] = None,
              disabled: bool = False,
              active: bool = False,
              **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with light context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.LIGHT, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def light_outline(self,
                      *args: ElementType,
                      class_: Optional[str] = None,
                      disabled: bool = False,
                      active: bool = False,
                      **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with light context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.LIGHT, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def dark(self,
             *args: ElementType,
             class_: Optional[str] = None,
             disabled: bool = False,
             active: bool = False,
             **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with dark context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.DARK, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def dark_outline(self,
                     *args: ElementType,
                     class_: Optional[str] = None,
                     disabled: bool = False,
                     active: bool = False,
                     **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with dark context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.DARK, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def link(self,
             *args: ElementType,
             class_: Optional[str] = None,
             disabled: bool = False,
             active: bool = False,
             **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new button with link context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.LINK, class_=class_, outline=False, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )

    def link_outline(self,
                     *args: ElementType,
                     class_: Optional[str] = None,
                     disabled: bool = False,
                     active: bool = False,
                     **kwargs: PropertyValue) -> ElementType:
        """
        Creates a new outline button with link context.

        Positional arguments will become the children of the created element if the element
        can have children. Otherwise these arguments might be converted into an attribute
        of the created element or be completely ignored - it is up to the factory.

        Keyword arguments are converted into element attributes.

        Arguments:
            class_: CSS class names to set on the created element.
            disabled: Whether the element should be disabled.
            active: Whether the button is active (i.e. selected).
        """
        return self.create_element(
            *args,
            class_=self.get_css_class(ButtonContext.LINK, class_=class_, outline=True, active=active),
            **self.update_attributes(kwargs, disabled=disabled, active=active)
        )


class BaseToggleButtonFactory(BaseButtonFactory):
    """
    Base class for toggle button factories.

    See https://getbootstrap.com/docs/4.3/components/buttons/#button-plugin.
    """

    __slots__ = ()

    def update_attributes(self,
                          attributes: PropertyDict,
                          *,
                          disabled: bool = False,
                          active: bool = False) -> PropertyDict:
        attributes = super().update_attributes(attributes, disabled=disabled, active=active)
        attributes["aria-pressed"] = active
        attributes["autocomplete"] = "off"
        attributes["data-toggle"] = "button"
        return attributes


class ElementButtonFactory(BaseButtonFactory):
    """
    Button element factory for `Element` instances.
    """

    __slots__ = ("_generator",)

    def __init__(self, generator: Type[Element]) -> None:
        """
        Initialization.

        Arguments:
            generator: The type of the elements the factory will produce.
        """
        super().__init__()
        self._generator: Type[Element] = generator
        """
        The type of the elements the object will produce.
        """

    def create_element(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       **kwargs: PropertyValue) -> ElementType:
        return self._generator(*args, class_=class_, **kwargs)


class ElementToggleButtonFactory(BaseToggleButtonFactory):
    """
    Toggle button element factory for `Element` instances.
    """

    __slots__ = ("_generator",)

    def __init__(self, generator: Type[Element]) -> None:
        """
        Initialization.

        Arguments:
            generator: The type of the elements the factory will produce.
        """
        super().__init__()
        self._generator: Type[Element] = generator
        """
        The type of the elements the object will produce.
        """

    def create_element(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       **kwargs: PropertyValue) -> ElementType:
        return self._generator(*args, class_=class_, **kwargs)


class StandaloneElementButtonFactory(BaseButtonFactory):
    """
    Button element factory for `StandaloneElement` instances.
    """

    __slots__ = ("_generator", "_pos_arg_attr")

    def __init__(self,
                 generator: Type[StandaloneElement],
                 *,
                 pos_arg_attr: str = "value") -> None:
        """
        Initialization.

        Arguments:
            generator: The type of the elements the factory will produce.
            pos_arg_attr: The name of the element attribute factory methods should store
                          the stringified version of positional arguments in.
        """
        super().__init__()
        self._generator: Type[StandaloneElement] = generator
        """
        The type of the elements the object will produce.
        """
        self._pos_arg_attr: str = pos_arg_attr
        """
        The name of the element attribute factory methods should store
        the stringified version of positional arguments in.
        """

    def create_element(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       **kwargs: PropertyValue) -> ElementType:
        kwargs[self._pos_arg_attr] = " ".join(str(a) for a in args)
        return self._generator(class_=class_, **kwargs)


class StandaloneElementToggleButtonFactory(BaseToggleButtonFactory):
    """
    Toggle button element factory for `StandaloneElement` instances.
    """

    __slots__ = ("_generator", "_pos_arg_attr")

    def __init__(self,
                 generator: Type[StandaloneElement],
                 *,
                 pos_arg_attr: str = "value") -> None:
        """
        Initialization.

        Arguments:
            generator: The type of the elements the factory will produce.
            pos_arg_attr: The name of the element attribute factory methods should store
                          the stringified version of positional arguments in.
        """
        super().__init__()
        self._generator: Type[StandaloneElement] = generator
        """
        The type of the elements the object will produce.
        """
        self._pos_arg_attr: str = pos_arg_attr
        """
        The name of the element attribute factory methods should store
        the stringified version of positional arguments in.
        """

    def create_element(self,
                       *args: ElementType,
                       class_: Optional[str] = None,
                       **kwargs: PropertyValue) -> ElementType:
        kwargs[self._pos_arg_attr] = " ".join(str(a) for a in args)
        return self._generator(class_=class_, **kwargs)


a_button: ElementButtonFactory = ElementButtonFactory(a)
"""
Button factory that produces anchor (`a`) elements.

Anchor elements don't support the `disabled` flag. To achieve the same effect,
you should apply the `ButtonStyle.disabled` CSS class on the element instead.
"""


a_toggle: ElementToggleButtonFactory = ElementToggleButtonFactory(a)
"""
Toggle button factory that produces anchor (`a`) elements.

Anchor elements don't support the `disabled` flag. To achieve the same effect,
you should apply the `ButtonStyle.disabled` CSS class on the element instead.
"""


b_button: ElementButtonFactory = ElementButtonFactory(button)
"""
Button factory that produces `button` elements.
"""


b_toggle: ElementToggleButtonFactory = ElementToggleButtonFactory(button)
"""
Toggle button factory that produces `button` elements.
"""


i_button: StandaloneElementButtonFactory = StandaloneElementButtonFactory(input_, pos_arg_attr="value")
"""
Button factory that produces `input_` elements.
"""


i_toggle: StandaloneElementToggleButtonFactory = StandaloneElementToggleButtonFactory(input_, pos_arg_attr="value")
"""
Toggle button factory that produces `input_` elements.
"""


l_button: ElementButtonFactory = ElementButtonFactory(label)
"""
Button factory that produces `label` elements.
"""


l_toggle: ElementToggleButtonFactory = ElementToggleButtonFactory(label)
"""
Toggle button factory that produces `label` elements.
"""
