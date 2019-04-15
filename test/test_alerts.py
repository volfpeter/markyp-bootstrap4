from markyp_bootstrap4.alerts import alert, dismissable

def test_alert():
    assert alert("Message", "Description", context="primary").markup ==\
        '<div role="alert" class="alert alert-primary">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="primary", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-primary my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.primary("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-primary">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.primary("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-primary my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="secondary").markup ==\
        '<div role="alert" class="alert alert-secondary">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="secondary", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-secondary my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.secondary("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-secondary">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.secondary("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-secondary my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="success").markup ==\
        '<div role="alert" class="alert alert-success">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="success", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-success my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.success("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-success">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.success("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-success my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="danger").markup ==\
        '<div role="alert" class="alert alert-danger">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="danger", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-danger my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.danger("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-danger">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.danger("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-danger my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="warning").markup ==\
        '<div role="alert" class="alert alert-warning">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="warning", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-warning my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.warning("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-warning">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.warning("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-warning my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="info").markup ==\
        '<div role="alert" class="alert alert-info">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="info", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-info my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.info("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-info">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.info("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-info my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="light").markup ==\
        '<div role="alert" class="alert alert-light">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="light", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-light my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.light("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-light">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.light("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-light my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

    assert alert("Message", "Description", context="dark").markup ==\
        '<div role="alert" class="alert alert-dark">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert("Message", "Description", context="dark", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-dark my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.dark("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-dark">\n'\
        'Message\nDescription\n'\
        '</div>'
    assert alert.dark("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-dark my-alert">\n'\
        'Message\nDescription\n'\
        '</div>'

def test_dismissable():
    assert dismissable("Message", "Description", context="primary").markup ==\
        '<div role="alert" class="alert alert-primary alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="primary", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-primary alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.primary("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-primary alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.primary("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-primary alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="secondary").markup ==\
        '<div role="alert" class="alert alert-secondary alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="secondary", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-secondary alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.secondary("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-secondary alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.secondary("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-secondary alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="success").markup ==\
        '<div role="alert" class="alert alert-success alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="success", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-success alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.success("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-success alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.success("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-success alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="danger").markup ==\
        '<div role="alert" class="alert alert-danger alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="danger", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-danger alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.danger("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-danger alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.danger("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-danger alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="warning").markup ==\
        '<div role="alert" class="alert alert-warning alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="warning", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-warning alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.warning("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-warning alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.warning("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-warning alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="info").markup ==\
        '<div role="alert" class="alert alert-info alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="info", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-info alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.info("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-info alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.info("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-info alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="light").markup ==\
        '<div role="alert" class="alert alert-light alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="light", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-light alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.light("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-light alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.light("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-light alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'

    assert dismissable("Message", "Description", context="dark").markup ==\
        '<div role="alert" class="alert alert-dark alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable("Message", "Description", context="dark", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-dark alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.dark("Message", "Description").markup ==\
        '<div role="alert" class="alert alert-dark alert-dismissible fade show">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
    assert dismissable.dark("Message", "Description", class_="my-alert").markup ==\
        '<div role="alert" class="alert alert-dark alert-dismissible fade show my-alert">\n'\
        'Message\nDescription\n'\
        '<button data-dismiss="alert" type="button" aria-label="Close" class="close">'\
        '<span aria-hidden="true">&times;</span>'\
        '</button>\n'\
        '</div>'
