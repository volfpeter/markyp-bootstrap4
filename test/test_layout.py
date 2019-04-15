from markyp_bootstrap4.layout import _size_names,\
                                     container,\
                                     container_fluid,\
                                     row,\
                                     one,\
                                     two,\
                                     three,\
                                     row_item,\
                                     autocol,\
                                     col,\
                                     margin,\
                                     padding

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

def test_autocol():
    assert autocol() == "col-sm"
    assert autocol(xs=None, sm=None, md=None, lg=None, xl=None) == "col-sm"
    assert autocol(None, None, None, None, None) == "col-sm"
    assert autocol(xs="", sm="", md="", lg="", xl="") == "col-sm"
    assert autocol("", "", "", "", "") == "col-sm"

def test_col():
    assert col() is None
    assert col(xs=None, sm=None, md=None, lg=None, xl=None) is None
    assert col(None, None, None, None, None) is None
    assert col(xs="", sm="", md="", lg="", xl="") is None
    assert col("", "", "", "", "") is None

    assert col(xs=6) == "col-xs-6"
    assert col(6) == "col-xs-6"
    assert col(sm=5) == "col-sm-5"
    assert col(None, 5) == "col-sm-5"
    assert col(md=4) == "col-md-4"
    assert col(None, None, 4) == "col-md-4"
    assert col(lg=3) == "col-lg-3"
    assert col(None, None, None, 3) == "col-lg-3"
    assert col(xl=2) == "col-xl-2"
    assert col(None, None, None, None, 2) == "col-xl-2"

    assert col(xs="auto") == "col-xs-auto"
    assert col("auto") == "col-xs-auto"
    assert col(sm="auto") == "col-sm-auto"
    assert col(None, "auto") == "col-sm-auto"
    assert col(md="auto") == "col-md-auto"
    assert col(None, None, "auto") == "col-md-auto"
    assert col(lg="auto") == "col-lg-auto"
    assert col(None, None, None, "auto") == "col-lg-auto"
    assert col(xl="auto") == "col-xl-auto"
    assert col(None, None, None, None, "auto") == "col-xl-auto"

    assert col(xs=9, sm=8, md=7, lg=6, xl=5) ==\
        "col-xs-9 col-sm-8 col-md-7 col-lg-6 col-xl-5"
    assert col(xs=9, sm="auto", md=7, lg=6, xl="auto") ==\
        "col-xs-9 col-sm-auto col-md-7 col-lg-6 col-xl-auto"

def test_margin():
    assert margin() is None
    assert margin(top=None, bottom=None, left=None, right=None, x=None, y=None) is None
    assert margin(None, None, None, None, None, None) is None
    assert margin(top="", bottom="", left="", right="", x="", y="") is None
    assert margin("", "", "", "", "", "") is None

    assert margin(3) == "mt-3"
    assert margin(top=3) == "mt-3"
    assert margin(None, 3) == "mb-3"
    assert margin(bottom=3) == "mb-3"
    assert margin(None, None, 3) == "ml-3"
    assert margin(left=3) == "ml-3"
    assert margin(None, None, None, 3) == "mr-3"
    assert margin(right=3) == "mr-3"
    assert margin(None, None, None, None, 3) == "mx-3"
    assert margin(x=3) == "mx-3"
    assert margin(None, None, None, None, None, 3) == "my-3"
    assert margin(y=3) == "my-3"

    assert margin("auto") == "mt-auto"
    assert margin(top="auto") == "mt-auto"
    assert margin(None, "auto") == "mb-auto"
    assert margin(bottom="auto") == "mb-auto"
    assert margin(None, None, "auto") == "ml-auto"
    assert margin(left="auto") == "ml-auto"
    assert margin(None, None, None, "auto") == "mr-auto"
    assert margin(right="auto") == "mr-auto"
    assert margin(None, None, None, None, "auto") == "mx-auto"
    assert margin(x="auto") == "mx-auto"
    assert margin(None, None, None, None, None, "auto") == "my-auto"
    assert margin(y="auto") == "my-auto"

    assert margin(0, 1, 2, 3, 4, 5) == "mt-0 mb-1 ml-2 mr-3 mx-4 my-5"
    assert margin("auto", "auto", 2, 3, "auto", "auto") == "mt-auto mb-auto ml-2 mr-3 mx-auto my-auto"

def test_padding():
    assert padding() is None
    assert padding(top=None, bottom=None, left=None, right=None, x=None, y=None) is None
    assert padding(None, None, None, None, None, None) is None
    assert padding(top="", bottom="", left="", right="", x="", y="") is None
    assert padding("", "", "", "", "", "") is None

    assert padding(3) == "pt-3"
    assert padding(top=3) == "pt-3"
    assert padding(None, 3) == "pb-3"
    assert padding(bottom=3) == "pb-3"
    assert padding(None, None, 3) == "pl-3"
    assert padding(left=3) == "pl-3"
    assert padding(None, None, None, 3) == "pr-3"
    assert padding(right=3) == "pr-3"
    assert padding(None, None, None, None, 3) == "px-3"
    assert padding(x=3) == "px-3"
    assert padding(None, None, None, None, None, 3) == "py-3"
    assert padding(y=3) == "py-3"

    assert padding("auto") == "pt-auto"
    assert padding(top="auto") == "pt-auto"
    assert padding(None, "auto") == "pb-auto"
    assert padding(bottom="auto") == "pb-auto"
    assert padding(None, None, "auto") == "pl-auto"
    assert padding(left="auto") == "pl-auto"
    assert padding(None, None, None, "auto") == "pr-auto"
    assert padding(right="auto") == "pr-auto"
    assert padding(None, None, None, None, "auto") == "px-auto"
    assert padding(x="auto") == "px-auto"
    assert padding(None, None, None, None, None, "auto") == "py-auto"
    assert padding(y="auto") == "py-auto"

    assert padding(0, 1, 2, 3, 4, 5) == "pt-0 pb-1 pl-2 pr-3 px-4 py-5"
    assert padding("auto", "auto", 2, 3, "auto", "auto") == "pt-auto pb-auto pl-2 pr-3 px-auto py-auto"
