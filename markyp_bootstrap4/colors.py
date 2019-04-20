"""
CSS class names for coloring.

See https://getbootstrap.com/docs/4.0/utilities/colors/ for more information.
"""


__all__ = ("bg", "text")


class __Background(object):
    """
    CSS class names for background coloring.
    """

    __slots__ = ()

    @property
    def primary(self) -> str:
        return "bg-primary"

    @property
    def secondary(self) -> str:
        return "bg-secondary"

    @property
    def success(self) -> str:
        return "bg-success"

    @property
    def danger(self) -> str:
        return "bg-danger"

    @property
    def warning(self) -> str:
        return "bg-warning"

    @property
    def info(self) -> str:
        return "bg-info"

    @property
    def light(self) -> str:
        return "bg-light"

    @property
    def dark(self) -> str:
        return "bg-dark"

    @property
    def white(self) -> str:
        return "bg-white"


class __Text(object):
    """
    CSS class names for text coloring.
    """

    __slots__ = ()

    @property
    def primary(self) -> str:
        return "text-primary"

    @property
    def secondary(self) -> str:
        return "text-secondary"

    @property
    def success(self) -> str:
        return "text-success"

    @property
    def danger(self) -> str:
        return "text-danger"

    @property
    def warning(self) -> str:
        return "text-warning"

    @property
    def info(self) -> str:
        return "text-info"

    @property
    def light(self) -> str:
        return "text-light"

    @property
    def dark(self) -> str:
        return "text-dark"

    @property
    def muted(self) -> str:
        return "text-muted"

    @property
    def white(self) -> str:
        return "text-white"


bg: __Background = __Background()
"""
CSS class names for background coloring.

See https://getbootstrap.com/docs/4.0/utilities/colors/.
"""


text: __Text = __Text()
"""
CSS class names for text coloring.

See https://getbootstrap.com/docs/4.0/utilities/colors/.
"""
