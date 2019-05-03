from markyp_bootstrap4.input_groups import *

def test_text():
    assert text.p("Value").markup ==\
        '<p class="input-group-text">Value</p>'
    assert text.p("Value", attr=42, class_="my-igt").markup ==\
        '<p attr="42" class="input-group-text my-igt">Value</p>'

    assert text.h1("Value").markup ==\
        '<h1 class="input-group-text">Value</h1>'
    assert text.h1("Value", attr=42, class_="my-igt").markup ==\
        '<h1 attr="42" class="input-group-text my-igt">Value</h1>'

    assert text.h2("Value").markup ==\
        '<h2 class="input-group-text">Value</h2>'
    assert text.h2("Value", attr=42, class_="my-igt").markup ==\
        '<h2 attr="42" class="input-group-text my-igt">Value</h2>'

    assert text.h3("Value").markup ==\
        '<h3 class="input-group-text">Value</h3>'
    assert text.h3("Value", attr=42, class_="my-igt").markup ==\
        '<h3 attr="42" class="input-group-text my-igt">Value</h3>'

    assert text.h4("Value").markup ==\
        '<h4 class="input-group-text">Value</h4>'
    assert text.h4("Value", attr=42, class_="my-igt").markup ==\
        '<h4 attr="42" class="input-group-text my-igt">Value</h4>'

    assert text.h5("Value").markup ==\
        '<h5 class="input-group-text">Value</h5>'
    assert text.h5("Value", attr=42, class_="my-igt").markup ==\
        '<h5 attr="42" class="input-group-text my-igt">Value</h5>'

    assert text.h6("Value").markup ==\
        '<h6 class="input-group-text">Value</h6>'
    assert text.h6("Value", attr=42, class_="my-igt").markup ==\
        '<h6 attr="42" class="input-group-text my-igt">Value</h6>'

def test_InputGroupStyle():
    assert InputGroupStyle.SMALL == "input-group-sm"
    assert InputGroupStyle.LARGE == "input-group-lg"

def test_input_group():
    assert input_group().markup ==\
        '<div class="input-group"></div>'
    assert input_group("First", "Second").markup ==\
        '<div class="input-group">\nFirst\nSecond\n</div>'
    assert input_group("First", "Second", class_=InputGroupStyle.LARGE).markup ==\
        '<div class="input-group input-group-lg">\nFirst\nSecond\n</div>'
    assert input_group("First", "Second", class_=InputGroupStyle.LARGE, attr=42).markup ==\
        '<div attr="42" class="input-group input-group-lg">\nFirst\nSecond\n</div>'

def test_pre_group():
    assert pre_group().markup ==\
        '<div class="input-group-prepend"></div>'
    assert pre_group("First", "Second").markup ==\
        '<div class="input-group-prepend">\nFirst\nSecond\n</div>'
    assert pre_group("First", "Second", class_="my-pre").markup ==\
        '<div class="input-group-prepend my-pre">\nFirst\nSecond\n</div>'
    assert pre_group("First", "Second", class_="my-pre", attr=42).markup ==\
        '<div attr="42" class="input-group-prepend my-pre">\nFirst\nSecond\n</div>'

def test_post_group():
    assert post_group().markup ==\
        '<div class="input-group-append"></div>'
    assert post_group("First", "Second").markup ==\
        '<div class="input-group-append">\nFirst\nSecond\n</div>'
    assert post_group("First", "Second", class_="my-post").markup ==\
        '<div class="input-group-append my-post">\nFirst\nSecond\n</div>'
    assert post_group("First", "Second", class_="my-post", attr=42).markup ==\
        '<div attr="42" class="input-group-append my-post">\nFirst\nSecond\n</div>'
