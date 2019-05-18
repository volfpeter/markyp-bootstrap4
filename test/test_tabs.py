from markyp_bootstrap4.tabs import *

def test_tab_content():
    assert tab_content().markup ==\
        '<div class="tab-content"></div>'
    assert tab_content("First", "Second").markup ==\
        '<div class="tab-content">\nFirst\nSecond\n</div>'
    assert tab_content("First", "Second", class_="my-tc", attr=42).markup ==\
        '<div attr="42" class="tab-content my-tc">\nFirst\nSecond\n</div>'

def test_tab_pane():
    assert tab_pane().markup ==\
        '<div role="tabpanel" class="tab-pane fade"></div>'
    assert tab_pane("First", "Second").markup ==\
        '<div role="tabpanel" class="tab-pane fade">\nFirst\nSecond\n</div>'
    assert tab_pane("First", "Second", active=True).markup ==\
        '<div role="tabpanel" class="tab-pane fade show active">\nFirst\nSecond\n</div>'
    assert tab_pane("First", "Second", fade=False).markup ==\
        '<div role="tabpanel" class="tab-pane">\nFirst\nSecond\n</div>'
    assert tab_pane("First", "Second", class_="my-tp", attr=42).markup ==\
        '<div role="tabpanel" attr="42" class="tab-pane fade my-tp">\nFirst\nSecond\n</div>'
