from markyp_bootstrap4.colors import bg, text, mix

def test_bg():
    assert bg.primary == "bg-primary"
    assert bg.secondary == "bg-secondary"
    assert bg.success == "bg-success"
    assert bg.danger == "bg-danger"
    assert bg.warning == "bg-warning"
    assert bg.info == "bg-info"
    assert bg.light == "bg-light"
    assert bg.dark == "bg-dark"
    assert bg.white == "bg-white"

def test_text():
    assert text.primary == "text-primary"
    assert text.secondary == "text-secondary"
    assert text.success == "text-success"
    assert text.danger == "text-danger"
    assert text.warning == "text-warning"
    assert text.info == "text-info"
    assert text.light == "text-light"
    assert text.dark == "text-dark"
    assert text.muted == "text-muted"
    assert text.white == "text-white"

def test_mix():
    assert mix() == ""
    assert mix(bg.primary) == "bg-primary"
    assert mix(text.success) == "text-success"
    assert mix(bg.primary, text.light) == "bg-primary text-light"
    assert mix(text.light, bg.primary) == "text-light bg-primary"

    # Duplicates are permitted, user error
    assert mix(text.light, bg.primary, text.light) == "text-light bg-primary text-light"
    assert mix(text.light, bg.primary, bg.primary) == "text-light bg-primary bg-primary"
    assert mix(text.light, bg.primary, bg.success) == "text-light bg-primary bg-success"
