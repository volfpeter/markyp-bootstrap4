[![Build Status](https://travis-ci.org/volfpeter/markyp-bootstrap4.svg?branch=master)](https://travis-ci.org/volfpeter/markyp-bootstrap4)
[![Downloads](https://pepy.tech/badge/markyp-bootstrap4)](https://pepy.tech/project/markyp-bootstrap4)
[![Downloads](https://pepy.tech/badge/markyp-bootstrap4/month)](https://pepy.tech/project/markyp-bootstrap4/month)
[![Downloads](https://pepy.tech/badge/markyp-bootstrap4/week)](https://pepy.tech/project/markyp-bootstrap4/week)

# markyp-bootstrap4

Create Bootstrap 4 web pages using purely Python.

The project is built on [markyp](https://github.com/volfpeter/markyp) and [markyp-html](https://github.com/volfpeter/markyp-html).

## Installation

The project is listed on the Python Package Index, it can be installed simply by executing `pip install markyp-bootstrap4`.

## Getting started

If you are not familiar with the basic concepts of `markyp`, please start by having a look at its documentation [here](https://github.com/volfpeter/markyp).

For a demo of the capabilities of `markyp-bootstrap4`, head over to the project's [GitHub Pages](https://volfpeter.github.io/markyp-bootstrap4). The source code of that page was generated by the `demo.py` script that you can find at the root of this repository.

The following example shows how to create a login form using `markyp-bootstrap4`.

```Python
from markyp_html import webpage
from markyp_html.forms import form

from markyp_bootstrap4 import req
from markyp_bootstrap4.layout import container, one, col, margin, offset
from markyp_bootstrap4.buttons import b_button
from markyp_bootstrap4.forms import form_group, form_check, form_check_label, input_, text

def login():
    return form(
        form_group(
            text.h5("Email"),
            input_.email(placeholder="Enter your email address")
        ),
        form_group(
            text.h5("Password"),
            input_.password(placeholder="Enter your password")
        ),
        form_check(
            input_.checkbox(),
            form_check_label("Remember Me"),
            class_=margin(bottom=2)
        ),
        b_button.primary("Sign In", type="submit")
    )

page = webpage(
    container(
        one(
            login(),
            md=6,
            class_=offset(md=3)
        )
    ),
    page_title="markyp-bootstrap4 example",
    head_elements=[
        req.bootstrap_css,
        *req.all_js
    ]
)

print(page)
```

Here is a list of things to notice in the example:

- Bootstrap 4's requirements can be import with `from markyp_bootstrap4 import req`, and the required CSS and JavaScript imports should be added to the `head_elements` of the webpage.
- The `layout` module contains the components you can use to define the layout of the webpage.
- `markyp_bootstrap4` components are grouped the same way as components in Bootstrap 4's documentation. The only difference is here every module name is in plural form.

## Related projects

- [markyp-html](https://github.com/volfpeter/markyp-html): Create custom or non-Bootstrap 4 components for you webpage.
- [markyp-fontawesome](https://github.com/volfpeter/markyp-fontawesome): Add Font Awesome 5 icons to your webpage.
- [markyp-highlightjs](https://github.com/volfpeter/markyp-highlightjs): Add syntax-highlighted code to your webpage.

## Community guidelines

In general, please treat each other with respect and follow the below guidelines to interact with the project:

- _Questions, feedback_: Open an issue with a `[Question] <issue-title>` title.
- _Bug reports_: Open an issue with a `[Bug] <issue-title>` title, an adequate description of the bug, and a code snippet that reproduces the issue if possible.
- _Feature requests and ideas_: Open an issue with an `[Enhancement] <issue-title>` title and a clear description of the enhancement proposal.

## Contribution guidelines

Every form of contribution is welcome, including documentation improvements, tests, bug fixes, and feature implementations.

Please follow these guidelines to contribute to the project:

- Make sure your changes match the documentation and coding style of the project, including [PEP 484](https://www.python.org/dev/peps/pep-0484/) type annotations.
- `mypy` is used to type-check the codebase, submitted code should not produce typing errors. See [this page](http://mypy-lang.org/) for more information on `mypy`.
- _Small_ fixes can be submitted simply by creating a pull request.
- Non-trivial changes should have an associated [issue](#community-guidelines) in the issue tracker that commits must reference (typically by adding `#refs <issue-id>` to the end of commit messages).
- Please write [tests](#testing) for the changes you make (if applicable).

If you have any questions about contributing to the project, please contact the project owner.

As mentioned in the [contribution guidelines](#contribution-guidelines), the project is type-checked using `mypy`, so first of all, the project must pass `mypy`'s static code analysis.

The project is tested using `pytest`. The chosen test layout is that tests are outside the application code, see [this page](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code) for details on what it means in practice.

If `pytest` is installed, the test set can be executed using the `pytest test` command from within the project directory.

If `pytest-cov` is also installed, a test coverage report can be generated by executing `pytest test --cov markyp_bootstrap4` from the root directory of the project.

## License - MIT

The library is open-sourced under the conditions of the MIT [license](https://choosealicense.com/licenses/mit/).
