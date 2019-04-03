from markyp_bootstrap4 import CDNs,\
                              req

def test_cdns():
    # -- Bootstrap CDN
    assert CDNs.Bootstrap.cdn_url_with_version() ==\
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1"
    assert CDNs.Bootstrap.css_url() ==\
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    assert CDNs.Bootstrap.js_url() ==\
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    assert CDNs.Bootstrap.js_bundle_url() ==\
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"

    # -- jQuery CDN
    assert CDNs.jQuery.minified_url() == "https://code.jquery.com/jquery-3.3.1.min.js"
    assert CDNs.jQuery.uncompressed_url() == "https://code.jquery.com/jquery-3.3.1.js"
    assert CDNs.jQuery.slim_minified_url() == "https://code.jquery.com/jquery-3.3.1.slim.min.js"
    assert CDNs.jQuery.slim_url() == "https://code.jquery.com/jquery-3.3.1.slim.js"

    # -- Popper.js CDN
    assert CDNs.PopperJS.cdn_url_with_version() ==\
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7"
    assert CDNs.PopperJS.js_url() ==\
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"

def test_req():
    assert req.bootstrap_css.markup ==\
        '<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
    assert req.bootstrap_js.markup ==\
        '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>'
    assert req.jquery.markup ==\
        '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>'
    assert req.popper_js.markup ==\
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>'

    jquery, popper, bs4 = req.all_js
    assert bs4.markup ==\
        '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>'
    assert jquery.markup ==\
        '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>'
    assert popper.markup ==\
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>'
