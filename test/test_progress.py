from markyp_bootstrap4.progress import *

def test_progress():
    assert progress(value=42, class_="my-progress", attr=42).markup == "\n".join((
        '<div attr="42" class="progress my-progress">',
            '<div style="width: 42%;" role="progressbar" '
                'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
                'class="progress-bar">'
            '</div>',
        '</div>'
    ))

    assert progress(value=42).markup == "\n".join((
        '<div class="progress">',
            '<div style="width: 42%;" role="progressbar" '
                'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
                'class="progress-bar">'
            '</div>',
        '</div>'
    ))

    assert progress("42%", value=42).markup == "\n".join((
        '<div class="progress">',
            '<div style="width: 42%;" role="progressbar" '
                'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
                'class="progress-bar">',
                '42%',
            '</div>',
        '</div>'
    ))

    assert progress(value=42, animated=True, striped=True, bar_class="my-pb", bar_attributes={"attr": 42}).markup == "\n".join((
        '<div class="progress">',
            '<div attr="42" style="width: 42%;" role="progressbar" '
                'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
                'class="progress-bar progress-bar-striped progress-bar-animated my-pb">'
            '</div>',
        '</div>'
    ))

def test_progress_base():
    assert progress_base().markup == '<div class="progress"></div>'
    assert progress_base("First", "Second", class_="my-progress", attr=42).markup == "\n".join((
        '<div attr="42" class="progress my-progress">',
            'First',
            'Second',
        '</div>'
    ))

def test_progressbar():
    assert progressbar(value=42).markup == (
        '<div style="width: 42%;" role="progressbar" '
            'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
            'class="progress-bar">'
        '</div>'
    )

    assert progressbar(value=42, animated=True, striped=True, class_="my-pb", attr=42).markup == (
        '<div attr="42" style="width: 42%;" role="progressbar" '
            'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
            'class="progress-bar progress-bar-striped progress-bar-animated my-pb">'
        '</div>'
    )

    assert progressbar("42%", value=42, style="height: 0.75rem;").markup == "\n".join((
        '<div style="width: 42%; height: 0.75rem;" role="progressbar" '
            'aria-valuenow="42" aria-valuemin="0" aria-valuemax="100" '
            'class="progress-bar">',
            "42%",
        '</div>'
    ))
