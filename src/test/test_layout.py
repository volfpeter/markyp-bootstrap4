from markyp_bootstrap4.layout import _size_names,\
                                     container,\
                                     container_fluid,\
                                     row,\
                                     one,\
                                     two,\
                                     three,\
                                     row_item,\
                                     format_column_sizes

def test_size_names():
    assert _size_names == ("xs", "sm", "md", "lg", "xl")

def test_container():
    assert container("first", "second", "third").markup ==\
        '<div class="container">\nfirst\nsecond\nthird\n</div>'
    assert container("first", "second", "third", class_="").markup ==\
        '<div class="container">\nfirst\nsecond\nthird\n</div>'
    assert container("first", "second", "third", class_="fancy-container").markup ==\
        '<div class="container fancy-container">\nfirst\nsecond\nthird\n</div>'

def test_container_fluid():
    assert container_fluid("first", "second", "third").markup ==\
        '<div class="container-fluid">\nfirst\nsecond\nthird\n</div>'
    assert container_fluid("first", "second", "third", class_="").markup ==\
        '<div class="container-fluid">\nfirst\nsecond\nthird\n</div>'
    assert container_fluid("first", "second", "third", class_="fancy-container").markup ==\
        '<div class="container-fluid fancy-container">\nfirst\nsecond\nthird\n</div>'

def test_row():
    assert row("foo", "bar").markup == '<div class="row">\nfoo\nbar\n</div>'
    assert row("foo", "bar", class_="").markup == '<div class="row">\nfoo\nbar\n</div>'
    assert row("foo", "bar", class_="fancy-row").markup == '<div class="row fancy-row">\nfoo\nbar\n</div>'

    assert row(row_item("first", md=8), row_item("second", md=4)).markup ==\
        '<div class="row">\n'\
        '<div class="col-md-8">\nfirst\n</div>\n'\
        '<div class="col-md-4">\nsecond\n</div>\n'\
        '</div>'

def test_one():
    assert one("item").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nitem\n</div>\n'\
        '</div>'
    assert one("item", class_="").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nitem\n</div>\n'\
        '</div>'
    assert one("item", class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm">\nitem\n</div>\n'\
        '</div>'

    assert one("item", md=8).markup ==\
        '<div class="row">\n'\
        '<div class="col-md-8">\nitem\n</div>\n'\
        '</div>'
    assert one("item", md=8, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-md-8">\nitem\n</div>\n'\
        '</div>'

    assert one("item", sm="auto", md=8).markup ==\
        '<div class="row">\n'\
        '<div class="col-sm-auto col-md-8">\nitem\n</div>\n'\
        '</div>'
    assert one("item", sm="auto", md=8, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm-auto col-md-8">\nitem\n</div>\n'\
        '</div>'

def test_two():
    assert two("left", "right").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", class_="").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", reverse=True, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '</div>'

    assert two("left", "right", md=(8, 4)).markup ==\
        '<div class="row">\n'\
        '<div class="col-md-8">\nleft\n</div>\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", md=(8, 4), class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-md-8">\nleft\n</div>\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", md=(8, 4), reverse=True, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '<div class="col-md-8">\nleft\n</div>\n'\
        '</div>'

    assert two("left", "right", sm=("auto", 6), md=(8, 4)).markup ==\
        '<div class="row">\n'\
        '<div class="col-sm-auto col-md-8">\nleft\n</div>\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", sm=("auto", 6), md=(8, 4), class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm-auto col-md-8">\nleft\n</div>\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '</div>'
    assert two("left", "right", sm=("auto", 6), md=(8, 4), reverse=True, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '<div class="col-sm-auto col-md-8">\nleft\n</div>\n'\
        '</div>'

def test_three():
    assert three("left", "middle", "right").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nmiddle\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", class_="").markup ==\
        '<div class="row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nmiddle\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '<div class="col-sm">\nmiddle\n</div>\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", class_="fancy-row", reverse=True).markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm">\nright\n</div>\n'\
        '<div class="col-sm">\nmiddle\n</div>\n'\
        '<div class="col-sm">\nleft\n</div>\n'\
        '</div>'

    assert three("left", "middle", "right", md=(2, 6, 4)).markup ==\
        '<div class="row">\n'\
        '<div class="col-md-2">\nleft\n</div>\n'\
        '<div class="col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", md=(2, 6, 4), class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-md-2">\nleft\n</div>\n'\
        '<div class="col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", md=(2, 6, 4), reverse=True, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-md-4">\nright\n</div>\n'\
        '<div class="col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-md-2">\nleft\n</div>\n'\
        '</div>'

    assert three("left", "middle", "right", sm=("auto", 2, 6), md=(2, 6, 4)).markup ==\
        '<div class="row">\n'\
        '<div class="col-sm-auto col-md-2">\nleft\n</div>\n'\
        '<div class="col-sm-2 col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", sm=("auto", 2, 6), md=(2, 6, 4), class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm-auto col-md-2">\nleft\n</div>\n'\
        '<div class="col-sm-2 col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '</div>'
    assert three("left", "middle", "right", sm=("auto", 2, 6), md=(2, 6, 4), reverse=True, class_="fancy-row").markup ==\
        '<div class="row fancy-row">\n'\
        '<div class="col-sm-6 col-md-4">\nright\n</div>\n'\
        '<div class="col-sm-2 col-md-6">\nmiddle\n</div>\n'\
        '<div class="col-sm-auto col-md-2">\nleft\n</div>\n'\
        '</div>'

def test_row_item():
    assert row_item("foo", "bar").markup == '<div class="col-sm">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", class_="").markup == '<div class="col-sm">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", class_="fancy-div").markup == '<div class="col-sm fancy-div">\nfoo\nbar\n</div>'

    assert row_item("foo", "bar", xs=6).markup == '<div class="col-xs-6">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", xs=6, class_="fancy-div").markup == '<div class="col-xs-6 fancy-div">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", sm=6).markup == '<div class="col-sm-6">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", sm=6, class_="fancy-div").markup == '<div class="col-sm-6 fancy-div">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", md=6).markup == '<div class="col-md-6">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", md=6, class_="fancy-div").markup == '<div class="col-md-6 fancy-div">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", lg=6).markup == '<div class="col-lg-6">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", lg=6, class_="fancy-div").markup == '<div class="col-lg-6 fancy-div">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", xl=6).markup == '<div class="col-xl-6">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", xl=6, class_="fancy-div").markup == '<div class="col-xl-6 fancy-div">\nfoo\nbar\n</div>'

    assert row_item("foo", "bar", xs=12, sm=11, md=10, lg=9, xl=8).markup ==\
        '<div class="col-xs-12 col-sm-11 col-md-10 col-lg-9 col-xl-8">\nfoo\nbar\n</div>'
    assert row_item("foo", "bar", class_="fancy-div", xs=12, sm=11, md=10, lg=9, xl=8).markup ==\
        '<div class="col-xs-12 col-sm-11 col-md-10 col-lg-9 col-xl-8 fancy-div">\nfoo\nbar\n</div>'

def test_format_column_sizes():
    assert format_column_sizes() == "col-sm"
    assert format_column_sizes(xs=None, sm=None, md=None, lg=None, xl=None) == "col-sm"
    assert format_column_sizes(xs="", sm="", md="", lg="", xl="") == "col-sm"

    assert format_column_sizes(xs=6) == "col-xs-6"
    assert format_column_sizes(sm=5) == "col-sm-5"
    assert format_column_sizes(md=4) == "col-md-4"
    assert format_column_sizes(lg=3) == "col-lg-3"
    assert format_column_sizes(xl=2) == "col-xl-2"

    assert format_column_sizes(xs="auto") == "col-xs-auto"
    assert format_column_sizes(sm="auto") == "col-sm-auto"
    assert format_column_sizes(md="auto") == "col-md-auto"
    assert format_column_sizes(lg="auto") == "col-lg-auto"
    assert format_column_sizes(xl="auto") == "col-xl-auto"

    assert format_column_sizes(xs=9, sm=8, md=7, lg=6, xl=5) ==\
        "col-xs-9 col-sm-8 col-md-7 col-lg-6 col-xl-5"
    assert format_column_sizes(xs=9, sm="auto", md=7, lg=6, xl="auto") ==\
        "col-xs-9 col-sm-auto col-md-7 col-lg-6 col-xl-auto"
