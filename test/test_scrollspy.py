from markyp_bootstrap4.scrollspy import *

def test_spied_by():
    assert spied_by("identifier") == {
        "data-spy": "scroll",
        "data-target": "#identifier",
        "data-offset": 0
    }

    assert spied_by(".identifier") == {
        "data-spy": "scroll",
        "data-target": ".identifier",
        "data-offset": 0
    }

    assert spied_by("#identifier") == {
        "data-spy": "scroll",
        "data-target": "#identifier",
        "data-offset": 0
    }

    assert spied_by("identifier", offset=42) == {
        "data-spy": "scroll",
        "data-target": "#identifier",
        "data-offset": 42
    }
