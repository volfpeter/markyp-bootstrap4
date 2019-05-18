from markyp_html.block import div
from markyp_html.inline import a
from markyp_html.lists import li, ul
from markyp_bootstrap4.list_groups import *

def test_ItemContext():
    assert ItemContext.PRIMARY == "primary"
    assert ItemContext.SECONDARY == "secondary"
    assert ItemContext.SUCCESS == "success"
    assert ItemContext.DANGER == "danger"
    assert ItemContext.WARNING == "warning"
    assert ItemContext.INFO == "info"
    assert ItemContext.LIGHT == "light"
    assert ItemContext.DARK == "dark"

    assert ItemContext.get_class() is None
    assert ItemContext.get_class("") is None
    assert ItemContext.get_class(ItemContext.PRIMARY) == "list-group-item-primary"
    assert ItemContext.get_class(ItemContext.SECONDARY) == "list-group-item-secondary"
    assert ItemContext.get_class(ItemContext.SUCCESS) == "list-group-item-success"
    assert ItemContext.get_class(ItemContext.DANGER) == "list-group-item-danger"
    assert ItemContext.get_class(ItemContext.WARNING) == "list-group-item-warning"
    assert ItemContext.get_class(ItemContext.INFO) == "list-group-item-info"
    assert ItemContext.get_class(ItemContext.LIGHT) == "list-group-item-light"
    assert ItemContext.get_class(ItemContext.DARK) == "list-group-item-dark"

def test_list_group():
    assert list_group().markup ==\
        '<ul class="list-group"></ul>'
    assert list_group("First", "Second").markup ==\
        '<ul class="list-group">\nFirst\nSecond\n</ul>'
    assert list_group("First", "Second", class_="my-lg").markup ==\
        '<ul class="list-group my-lg">\nFirst\nSecond\n</ul>'
    assert list_group(factory=ul).markup ==\
        '<ul class="list-group"></ul>'
    assert list_group("First", "Second", factory=ul).markup ==\
        '<ul class="list-group">\nFirst\nSecond\n</ul>'
    assert list_group("First", "Second", factory=ul, class_="my-lg").markup ==\
        '<ul class="list-group my-lg">\nFirst\nSecond\n</ul>'
    assert list_group(factory=div).markup ==\
        '<div class="list-group"></div>'
    assert list_group("First", "Second", factory=div).markup ==\
        '<div class="list-group">\nFirst\nSecond\n</div>'
    assert list_group("First", "Second", factory=div, class_="my-lg").markup ==\
        '<div class="list-group my-lg">\nFirst\nSecond\n</div>'
    assert list_group("First", "Second", factory=div, class_="my-lg", attr=42).markup ==\
        '<div attr="42" class="list-group my-lg">\nFirst\nSecond\n</div>'

    assert list_group(flush=True).markup ==\
        '<ul class="list-group list-group-flush"></ul>'
    assert list_group("First", "Second", flush=True).markup ==\
        '<ul class="list-group list-group-flush">\nFirst\nSecond\n</ul>'
    assert list_group("First", "Second", flush=True, class_="my-lg").markup ==\
        '<ul class="list-group list-group-flush my-lg">\nFirst\nSecond\n</ul>'
    assert list_group(factory=ul, flush=True).markup ==\
        '<ul class="list-group list-group-flush"></ul>'
    assert list_group("First", "Second", factory=ul, flush=True).markup ==\
        '<ul class="list-group list-group-flush">\nFirst\nSecond\n</ul>'
    assert list_group("First", "Second", factory=ul, flush=True, class_="my-lg").markup ==\
        '<ul class="list-group list-group-flush my-lg">\nFirst\nSecond\n</ul>'
    assert list_group(factory=div, flush=True).markup ==\
        '<div class="list-group list-group-flush"></div>'
    assert list_group("First", "Second", factory=div, flush=True).markup ==\
        '<div class="list-group list-group-flush">\nFirst\nSecond\n</div>'
    assert list_group("First", "Second", factory=div, flush=True, class_="my-lg", attr=42).markup ==\
        '<div attr="42" class="list-group list-group-flush my-lg">\nFirst\nSecond\n</div>'

def test_list_group_item():
    assert list_group_item().markup ==\
        '<li class="list-group-item"></li>'
    assert list_group_item("First", "Second").markup ==\
        '<li class="list-group-item">First Second</li>'
    assert list_group_item("First", "Second", class_="my-lgi", action=True).markup ==\
        '<li class="list-group-item list-group-item-action my-lgi">First Second</li>'
    assert list_group_item("First", "Second", class_="my-lgi", active=True).markup ==\
        '<li class="list-group-item active my-lgi">First Second</li>'
    assert list_group_item("First", "Second", class_="my-lgi", disabled=True).markup ==\
        '<li class="list-group-item disabled my-lgi">First Second</li>'
    assert list_group_item("First", "Second", class_="my-lgi", disabled=True, attr=42).markup ==\
        '<li attr="42" class="list-group-item disabled my-lgi">First Second</li>'

    assert list_group_item(factory=a).markup ==\
        '<a class="list-group-item"></a>'
    assert list_group_item("First", "Second", factory=a).markup ==\
        '<a class="list-group-item">First Second</a>'
    assert list_group_item("First", "Second", factory=a, class_="my-lgi", action=True).markup ==\
        '<a class="list-group-item list-group-item-action my-lgi">First Second</a>'
    assert list_group_item("First", "Second", factory=a, class_="my-lgi", active=True).markup ==\
        '<a class="list-group-item active my-lgi">First Second</a>'
    assert list_group_item("First", "Second", factory=a, class_="my-lgi", disabled=True).markup ==\
        '<a class="list-group-item disabled my-lgi">First Second</a>'
    assert list_group_item("First", "Second", factory=a, class_="my-lgi", disabled=True, attr=42).markup ==\
        '<a attr="42" class="list-group-item disabled my-lgi">First Second</a>'

    assert list_group_item("First", "Second", context=ItemContext.PRIMARY).markup ==\
        '<li class="list-group-item list-group-item-primary">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.SECONDARY).markup ==\
        '<li class="list-group-item list-group-item-secondary">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.SUCCESS).markup ==\
        '<li class="list-group-item list-group-item-success">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.DANGER).markup ==\
        '<li class="list-group-item list-group-item-danger">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.WARNING).markup ==\
        '<li class="list-group-item list-group-item-warning">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.INFO).markup ==\
        '<li class="list-group-item list-group-item-info">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.LIGHT).markup ==\
        '<li class="list-group-item list-group-item-light">First Second</li>'
    assert list_group_item("First", "Second", context=ItemContext.DARK).markup ==\
        '<li class="list-group-item list-group-item-dark">First Second</li>'
