from markyp_bootstrap4.jumbotrons import *

def test_jumbotron():
    assert jumbotron().markup ==\
        '<div class="jumbotron"></div>'
    assert jumbotron("First", "Second").markup ==\
        '<div class="jumbotron">\nFirst\nSecond\n</div>'
    assert jumbotron("First", "Second", fluid=False).markup ==\
        '<div class="jumbotron">\nFirst\nSecond\n</div>'
    assert jumbotron("First", "Second", fluid=True).markup ==\
        '<div class="jumbotron jumbotron-fluid">\nFirst\nSecond\n</div>'
    assert jumbotron("First", "Second", class_="my-j", attr=42).markup ==\
        '<div attr="42" class="jumbotron my-j">\nFirst\nSecond\n</div>'

def test_rectangular_jumbotron():
    assert rectangular_jumbotron().markup ==\
        '<div class="jumbotron">\n<div class="container"></div>\n</div>'
    assert rectangular_jumbotron("First", "Second").markup ==\
        '<div class="jumbotron">\n<div class="container">\nFirst\nSecond\n</div>\n</div>'
    assert rectangular_jumbotron("First", "Second", fluid=False).markup ==\
        '<div class="jumbotron">\n<div class="container">\nFirst\nSecond\n</div>\n</div>'
    assert rectangular_jumbotron("First", "Second", fluid=True).markup ==\
        '<div class="jumbotron jumbotron-fluid">\n<div class="container">\nFirst\nSecond\n</div>\n</div>'
    assert rectangular_jumbotron("First", "Second", class_="my-j", attr=42).markup ==\
        '<div attr="42" class="jumbotron my-j">\n<div class="container">\nFirst\nSecond\n</div>\n</div>'
