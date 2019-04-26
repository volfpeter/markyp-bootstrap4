from markyp_bootstrap4.elements import *

def test_close_icon():
    assert close_icon().markup ==\
        '<button type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>'
