from markyp_bootstrap4.breadcrumbs import breadcrumb, breadcrumb_item, custom_breadcrumb

def test_custom_breadcrumb():
    assert custom_breadcrumb(class_="my-bc", attr=42).markup ==\
        '<nav aria-label="breadcrumb">\n'\
        '<ol attr="42" class="breadcrumb my-bc"></ol>\n'\
        '</nav>'
    assert custom_breadcrumb(
        breadcrumb_item("Home"),
        breadcrumb_item("Topic"),
        breadcrumb_item("Subtopic"),
        breadcrumb_item("Current page", active=True)).markup ==\
        '<nav aria-label="breadcrumb">\n'\
        '<ol class="breadcrumb">\n'\
        '<li class="breadcrumb-item">Home</li>\n'\
        '<li class="breadcrumb-item">Topic</li>\n'\
        '<li class="breadcrumb-item">Subtopic</li>\n'\
        '<li class="breadcrumb-item active">Current page</li>\n'\
        '</ol>\n'\
        '</nav>'

def test_breadcrumb():
    assert breadcrumb().markup ==\
        '<nav aria-label="breadcrumb">\n'\
        '<ol class="breadcrumb"></ol>\n'\
        '</nav>'
    assert breadcrumb("Home", "Topic", "Subtopic", "Current page").markup ==\
        '<nav aria-label="breadcrumb">\n'\
        '<ol class="breadcrumb">\n'\
        '<li class="breadcrumb-item">Home</li>\n'\
        '<li class="breadcrumb-item">Topic</li>\n'\
        '<li class="breadcrumb-item">Subtopic</li>\n'\
        '<li class="breadcrumb-item active">Current page</li>\n'\
        '</ol>\n'\
        '</nav>'

def test_breadcrumb_item():
    assert breadcrumb_item().markup ==\
        '<li class="breadcrumb-item"></li>'
    assert breadcrumb_item(active=True).markup ==\
        '<li class="breadcrumb-item active"></li>'
    assert breadcrumb_item(active=True, class_="my-bc-item").markup ==\
        '<li class="breadcrumb-item active my-bc-item"></li>'
    assert breadcrumb_item(active=True, class_="my-bc-item", attr=42).markup ==\
        '<li attr="42" class="breadcrumb-item active my-bc-item"></li>'

    assert breadcrumb_item("Home").markup ==\
        '<li class="breadcrumb-item">Home</li>'
    assert breadcrumb_item("Home", active=True).markup ==\
        '<li class="breadcrumb-item active">Home</li>'
    assert breadcrumb_item("Home", active=True, class_="my-bc-item").markup ==\
        '<li class="breadcrumb-item active my-bc-item">Home</li>'
    assert breadcrumb_item("Home", active=True, class_="my-bc-item", attr=42).markup ==\
        '<li attr="42" class="breadcrumb-item active my-bc-item">Home</li>'

    assert breadcrumb_item("Home", "item").markup ==\
        '<li class="breadcrumb-item">Home item</li>'
    assert breadcrumb_item("Home", "item", active=True).markup ==\
        '<li class="breadcrumb-item active">Home item</li>'
    assert breadcrumb_item("Home", "item", active=True, class_="my-bc-item").markup ==\
        '<li class="breadcrumb-item active my-bc-item">Home item</li>'
    assert breadcrumb_item("Home", "item", active=True, class_="my-bc-item", attr=42).markup ==\
        '<li attr="42" class="breadcrumb-item active my-bc-item">Home item</li>'
