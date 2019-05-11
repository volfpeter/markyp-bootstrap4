"""
Generic Bootstrap layout elements.

In Bootstrap's grid layout system, content is organized into _containers_. A
container can hold any number of _rows_. Each row can hold multiple items that
span one or more columns. The number of columns in each row is _12_.

This module implements one or more elements (higher order components) for each of
Bootstrap's aforementioned layout system components (see `container()`, `row()` and
`row_item()` for example) that allow you to easily create correct Bootstrap layouts.

See https://getbootstrap.com/docs/4.3/layout/grid/ for more information on
Bootstrap's grid layout system.

See https://getbootstrap.com/docs/4.0/utilities/spacing/ for more information
on Bootstrap's spacing and margin definition system.
"""

from typing import Optional, Tuple, Union

from markyp import ElementType
from markyp_html.block import div


__all__ = (
    "ColumnSize", "MarginSize", "PaddingSize",
    "container", "container_fluid",
    "row", "one", "two", "three", "row_break", "row_item",
    "PercentSize", "autocol", "col", "margin", "offset", "padding"
)


# -- Variables
# -----------------------------------------------------------------------------


ColumnSize = Union[int, str]
"""
Column size type. Valid values for arguments of this type are integers in the
[1, 12] interval (in integer or string form) and the string `auto`.
"""


MarginSize = Union[int, str]
"""
Margin size type. Values values for arguments of this type integers in the
[0, 5] interval (in integer or string form) and the string `auto`.
"""


PaddingSize = Union[int, str]
"""
Padding size type. Values values for arguments of this type integers in the
[0, 5] interval (in integer or string form) and the string `auto`.
"""


_side_names: Tuple[str, str, str, str, str, str, str] = ("", "t", "b", "l", "r", "x", "y")
"""
The ordered list of side names for spacing and margin definitions.
"""


_size_names: Tuple[str, str, str, str, str] = ("xs", "sm", "md", "lg", "xl")
"""
The ordered list of Bootstrap size identifier strings.
"""


# -- Containers
# -----------------------------------------------------------------------------


def container(*args: ElementType, class_: Optional[str] = None) -> div:
    """
    Bootstrap container element.

    ```HTML
    <div class="container {class_}">
        {positional arguments as children elements}
    </div>
    ```

    Arguments:
        class_: Additional classes to add to the `container` `div` that wraps the given elements.
    """
    return div(*args, class_=f"container {class_}" if class_ else "container")


def container_fluid(*args: ElementType, class_: Optional[str] = None) -> div:
    """
    Bootstrap fluid container element.

    ```HTML
    <div class="container-fluid {class_}">
        {positional arguments as children elements}
    </div>
    ```

    Arguments:
        class_: Additional classes to add to the `container` `div` that wraps the given elements.
    """
    return div(*args, class_=f"container-fluid {class_}" if class_ else "container-fluid")


# -- Rows
# -----------------------------------------------------------------------------


def row(*args: ElementType, class_: Optional[str] = None) -> div:
    """
    Bootstrap container row element.

    ```HTML
    <div class="row {class_}">
        {positional arguments as children elements}
    </div>
    ```

    Arguments:
        class_: Additional classes to add to the `row` `div` that wraps the given elements.
    """
    return div(*args, class_=f"row {class_}" if class_ else "row")


def one(item: ElementType,
        *,
        class_: Optional[str] = None,
        xs: Optional[ColumnSize] = None,
        sm: Optional[ColumnSize] = None,
        md: Optional[ColumnSize] = None,
        lg: Optional[ColumnSize] = None,
        xl: Optional[ColumnSize] = None) -> div:
    """
    Creates a row with a single item in it.

    ```HTML
    <div class="row {class_}">
        {item element with size specification}
    </div>
    ```

    Arguments:
        item: The element the row should contain.
        class_: Additional classes to add to the `row` `div` that wraps the element.
        xs: Column size for extra small screens.
        sm: Column size for small screens.
        md: Column size for mid-sized screens.
        lg: Column size for large screens.
        xl: Column size for extra large screens.
    """
    return row(
        row_item(item, xs=xs, sm=sm, md=md, lg=lg, xl=xl),
        class_=class_
    )


def two(left: ElementType,
        right: ElementType,
        *,
        class_: Optional[str] = None,
        xs: Optional[Tuple[ColumnSize, ColumnSize]] = None,
        sm: Optional[Tuple[ColumnSize, ColumnSize]] = None,
        md: Optional[Tuple[ColumnSize, ColumnSize]] = None,
        lg: Optional[Tuple[ColumnSize, ColumnSize]] = None,
        xl: Optional[Tuple[ColumnSize, ColumnSize]] = None,
        reverse: bool = False) -> div:
    """
    Creates a row of two elements with the specified column sizes.

    ```HTML
    <div class="row {class_}">
        {left element with size specification}
        {right element with size specification}
    </div>
    ```

    Arguments:
        left: The element on the left side of the row.
        right: The element on the right side of the row.
        class_: Additional classes to add to the `row` `div` that wraps the given elements.
        xs: Tuple of column sizes for extra small screens.
        sm: Tuple of column sizes for small screens.
        md: Tuple of column sizes for mid-sized screens.
        lg: Tuple of column sizes for large screens.
        xl: Tuple of column sizes for extra large screens.
        reverse: Whether to reverse the order of the items within the row.
    """
    missing = (None, None)
    # The zip() object must be converted to a tuple, because it's iterated multiple times.
    # Another solution would be to use `cols = lambda: zip(...)` to create a new zip
    # iterator every time, but this is more straigthforward and the list is short anyway.
    cols = tuple(zip(_size_names, (xs or missing, sm or missing, md or missing, lg or missing, xl or missing)))
    left, right, indices = (right, left, (1, 0)) if reverse else (left, right, (0, 1))
    return row(
        row_item(left, **{k: v[indices[0]] for k, v in cols}),
        row_item(right, **{k: v[indices[1]] for k, v in cols}),
        class_=class_
    )


def three(left: ElementType,
          middle: ElementType,
          right: ElementType,
          *,
          class_: Optional[str] = None,
          xs: Optional[Tuple[ColumnSize, ColumnSize, ColumnSize]] = None,
          sm: Optional[Tuple[ColumnSize, ColumnSize, ColumnSize]] = None,
          md: Optional[Tuple[ColumnSize, ColumnSize, ColumnSize]] = None,
          lg: Optional[Tuple[ColumnSize, ColumnSize, ColumnSize]] = None,
          xl: Optional[Tuple[ColumnSize, ColumnSize, ColumnSize]] = None,
          reverse: bool = False) -> div:
    """
    Creates a row of three elements with the specified column sizes.

    ```HTML
    <div class="row {class_}">
        {left element with size specification}
        {middle element with size specification}
        {right element with size specification}
    </div>
    ```

    Arguments:
        left: The element on the left side of the row.
        middle: The element in the middle of the row.
        right: The element on the right side of the row.
        class_: Additional classes to add to the `row` `div` that wraps the given elements.
        xs: Tuple of column sizes for extra small screens.
        sm: Tuple of column sizes for small screens.
        md: Tuple of column sizes for mid-sized screens.
        lg: Tuple of column sizes for large screens.
        xl: Tuple of column sizes for extra large screens.
        reverse: Whether to reverse the order of the items within the row.
    """
    missing = (None, None, None)
    # The zip() object must be converted to a tuple, because it's iterated multiple times.
    # Another solution would be to use `cols = lambda: zip(...)` to create a new zip
    # iterator every time, but this is more straigthforward and the list is short anyway.
    cols = tuple(zip(_size_names, (xs or missing, sm or missing, md or missing, lg or missing, xl or missing)))
    left, right, indices = (right, left, (2, 1, 0)) if reverse else (left, right, (0, 1, 2))
    return row(
        row_item(left, **{k: v[indices[0]] for k, v in cols}),
        row_item(middle, **{k: v[indices[1]] for k, v in cols}),
        row_item(right, **{k: v[indices[2]] for k, v in cols}),
        class_=class_
    )


# -- Row items
# -----------------------------------------------------------------------------


def row_break() -> div:
    """
    Returns a `div` that always spans a full row and as a result adds a
    line-break between row items.
    """
    return div(class_=PercentSize.width_100)


def row_item(*args: ElementType,
             class_: Optional[str] = None,
             xs: Optional[ColumnSize] = None,
             sm: Optional[ColumnSize] = None,
             md: Optional[ColumnSize] = None,
             lg: Optional[ColumnSize] = None,
             xl: Optional[ColumnSize] = None) -> div:
    """
    Bootstrap row item element: `<div class="{column-size-classes}"></div>`

    ```HTML
    <div class="{size specification and {class_}}">
        {positional arguments as children elements}
    </div>
    ```

    Arguments:
        class_: Additional classes to add to the `div` (row item) that wraps `content`.
        xs: Column size for extra small screens.
        sm: Column size for small screens.
        md: Column size for mid-sized screens.
        lg: Column size for large screens.
        xl: Column size for extra large screens.

    Returns:
        A `div` with that wraps `content` and has the required column size classes.
    """
    class_ = f"{autocol(xs, sm, md, lg, xl)} {class_}"\
        if class_ else autocol(xs, sm, md, lg, xl)
    return div(*args, class_=class_)


# -- Utilities
# -----------------------------------------------------------------------------


class PercentSize(object):
    """
    CSS class names for defining an element's width and height in percentage
    relative to its parent element.
    """

    height_25: str = "h-25"

    height_50: str = "h-50"

    height_75: str = "h-75"

    height_100: str = "h-100"

    width_25: str = "w-25"

    width_50: str = "w-50"

    width_75: str = "w-75"

    width_100: str = "w-100"


def autocol(xs: Optional[ColumnSize] = None,
            sm: Optional[ColumnSize] = None,
            md: Optional[ColumnSize] = None,
            lg: Optional[ColumnSize] = None,
            xl: Optional[ColumnSize] = None) -> str:
    """
    Formats the specified column sizes into a class string of `col-{brakpoint}-{size}` items.

    Arguments:
        xs: Column size for extra small screens.
        sm: Column size for small screens.
        md: Column size for mid-sized screens.
        lg: Column size for large screens.
        xl: Column size for extra large screens.

    Returns:
        The formatted class string or `col` if no sizes were specified.
    """
    return col(xs, sm, md, lg, xl) or "col"


def col(xs: Optional[ColumnSize] = None,
        sm: Optional[ColumnSize] = None,
        md: Optional[ColumnSize] = None,
        lg: Optional[ColumnSize] = None,
        xl: Optional[ColumnSize] = None) -> Optional[str]:
    """
    Formats the specified column sizes into a class string of `col-{brakpoint}-{size}` items.

    Arguments:
        xs: Column size for extra small screens.
        sm: Column size for small screens.
        md: Column size for mid-sized screens.
        lg: Column size for large screens.
        xl: Column size for extra large screens.

    Returns:
        The formatted class string or `None` if no sizes were specified.
    """
    return " ".join(f"col-{c}-{w}" for c, w in zip(_size_names, (xs, sm, md, lg, xl)) if w) or None


def margin(around: Optional[MarginSize] = None,
           *,
           top: Optional[MarginSize] = None,
           bottom: Optional[MarginSize] = None,
           left: Optional[MarginSize] = None,
           right: Optional[MarginSize] = None,
           x: Optional[MarginSize] = None,
           y: Optional[MarginSize] = None) -> Optional[str]:
    """
    Formats the specified margin sizes into a class string of `m{side}-{size}` items.

    Arguments:
        around: Margin size on all sides.
        top: Margin size on the top.
        bottom: Margin size at the bottom.
        left: Margin size on the left side.
        right: Margin size on the right side.
        x: Margin size on the X axis (both left and right side).
        y: Margin size on the Y axis (both top and bottom).

    Returns:
        The formatted class string or `None` if no sizes were specified.
    """
    return " ".join(f"m{s}-{m}" for s, m in zip(_side_names, (around, top, bottom, left, right, x, y)) if m or m == 0) or None


def offset(xs: Optional[ColumnSize] = None,
           sm: Optional[ColumnSize] = None,
           md: Optional[ColumnSize] = None,
           lg: Optional[ColumnSize] = None,
           xl: Optional[ColumnSize] = None) -> Optional[str]:
    """
    Arguments:
        xs: Offset (in column count) size for extra small screens.
        sm: Offset (in column count) size for small screens.
        md: Offset (in column count) size for mid-sized screens.
        lg: Offset (in column count) size for large screens.
        xl: Offset (in column count) size for extra large screens.

    Returns:
        The formatted class string or `None` if no sizes were specified.
    """
    return " ".join(f"offset-{c}-{w}" for c, w in zip(_size_names, (xs, sm, md, lg, xl)) if w) or None


def padding(around: Optional[PaddingSize] = None,
            *,
            top: Optional[PaddingSize] = None,
            bottom: Optional[PaddingSize] = None,
            left: Optional[PaddingSize] = None,
            right: Optional[PaddingSize] = None,
            x: Optional[PaddingSize] = None,
            y: Optional[PaddingSize] = None) -> Optional[str]:
    """
    Formats the specified padding sizes into a class string of `p{side}-{size}` items.

    Arguments:
        around: Padding size on all sides.
        top: Padding size on the top.
        bottom: Padding size at the bottom.
        left: Padding size on the left side.
        right: Padding size on the right side.
        x: Padding size on the X axis (both left and right side).
        y: Padding size on the Y axis (both top and bottom).

    Returns:
        The formatted class string or `None` if no sizes were specified.
    """
    return " ".join(f"p{s}-{p}" for s, p in zip(_side_names, (around, top, bottom, left, right, x, y)) if p or p == 0) or None
