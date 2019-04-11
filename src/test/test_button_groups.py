from markyp_bootstrap4.button_groups import BGSize,\
                                            button_group,\
                                            toggle_button_group

def test_BGSize():
    assert BGSize.DEFAULT is None
    assert BGSize.SMALL == "sm"
    assert BGSize.LARGE == "lg"

def test_button_group():
    assert button_group("foo", "bar").markup ==\
        '<div class="btn-group">\nfoo\nbar\n</div>'
    assert button_group("foo", "bar", class_="my").markup ==\
        '<div class="btn-group my">\nfoo\nbar\n</div>'
    assert button_group("foo", "bar", class_="my", a="a", b=42).markup ==\
        '<div a="a" b="42" class="btn-group my">\nfoo\nbar\n</div>'
    assert button_group("foo", "bar", class_="my", size=BGSize.DEFAULT, a="a", b=42).markup ==\
        '<div a="a" b="42" class="btn-group my">\nfoo\nbar\n</div>'
    assert button_group("foo", "bar", class_="my", size=BGSize.SMALL, a="a", b=42).markup ==\
        '<div a="a" b="42" class="btn-group-sm my">\nfoo\nbar\n</div>'
    assert button_group("foo", "bar", class_="my", size=BGSize.LARGE, a="a", b=42).markup ==\
        '<div a="a" b="42" class="btn-group-lg my">\nfoo\nbar\n</div>'

def test_toggle_button_group():
    assert toggle_button_group("foo", "bar").markup ==\
        '<div data-toggle="buttons" class="btn-group btn-group-toggle">\nfoo\nbar\n</div>'
    assert toggle_button_group("foo", "bar", class_="my").markup ==\
        '<div data-toggle="buttons" class="btn-group btn-group-toggle my">\nfoo\nbar\n</div>'
    assert toggle_button_group("foo", "bar", class_="my", size=BGSize.DEFAULT, a="a", b=42).markup ==\
        '<div a="a" b="42" data-toggle="buttons" class="btn-group btn-group-toggle my">\nfoo\nbar\n</div>'
    assert toggle_button_group("foo", "bar", class_="my", size=BGSize.SMALL, a="a", b=42).markup ==\
        '<div a="a" b="42" data-toggle="buttons" class="btn-group-sm btn-group-toggle my">\nfoo\nbar\n</div>'
    assert toggle_button_group("foo", "bar", class_="my", size=BGSize.LARGE, a="a", b=42).markup ==\
        '<div a="a" b="42" data-toggle="buttons" class="btn-group-lg btn-group-toggle my">\nfoo\nbar\n</div>'
