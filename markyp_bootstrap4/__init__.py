"""
The basic components that are required to get Bootstrap 4 working.
"""

from typing import Tuple

from markyp_html import link, script


__author__ = "Peter Volf"
__copyright__ = "Copyright 2019, Peter Volf"
__email__ = "do.volfp@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/volfpeter/markyp-bootstrap4"
__version__ = "0.1905.2"


__all__ = ("CDNs", "req")


class CDNs(object):
    """
    CDN definitions for Bootstrap and other libraries it requires.
    """

    __slots__ = ()

    class Bootstrap(object):
        """
        Bootstrap library CDN definition.
        """

        __slots__ = ()

        CDN_URL: str = "https://stackpath.bootstrapcdn.com/bootstrap"

        VERSION: str = "4.3.1"

        @classmethod
        def cdn_url_with_version(cls) -> str:
            """
            Returns the concatenated value of `CDN_URL` and `VERSION`.
            """
            return f"{cls.CDN_URL}/{cls.VERSION}"

        @classmethod
        def css_url(cls) -> str:
            """
            Returns the CDN URL for Bootstrap's CSS.
            """
            return f"{cls.cdn_url_with_version()}/css/bootstrap.min.css"

        @classmethod
        def js_url(cls) -> str:
            """
            Returns the CDN URL for Bootstrap's minified JavaScript component.
            """
            return f"{cls.cdn_url_with_version()}/js/bootstrap.min.js"

        @classmethod
        def js_bundle_url(cls) -> str:
            """
            Returns the CDN URL for bundled Bootstrap library (CSS and JS included).
            """
            return f"{cls.cdn_url_with_version()}/js/bootstrap.bundle.min.js"

    class jQuery(object):
        """
        jQuery library CDN definition.

        Usually the slim and minified version is required, see `slim_minified`.
        """

        __slots__ = ()

        CDN_URL: str = "https://code.jquery.com"

        VERSION: str = "3.3.1"

        @classmethod
        def minified_url(cls) -> str:
            """
            Returns the URL to the minified version of jQuery.
            """
            return f"{cls.CDN_URL}/jquery-{cls.VERSION}.min.js"

        @classmethod
        def uncompressed_url(cls) -> str:
            """
            Returns the URL to the uncompressed version of jQuery.
            """
            return f"{cls.CDN_URL}/jquery-{cls.VERSION}.js"

        @classmethod
        def slim_minified_url(cls) -> str:
            """
            Returns the URL to the slim and minified version of jQuery.

            Using this version should usually be fine.
            """
            return f"{cls.CDN_URL}/jquery-{cls.VERSION}.slim.min.js"

        @classmethod
        def slim_url(cls) -> str:
            """
            Returns the URL to the slim version of jQuery.
            """
            return f"{cls.CDN_URL}/jquery-{cls.VERSION}.slim.js"

    class PopperJS(object):
        """
        Popper.js CDN definition.

        Popper.js is a popup management library required by some Bootstrap elements.
        """

        __slots__ = ()

        CDN_URL: str = "https://cdnjs.cloudflare.com/ajax/libs/popper.js"

        VERSION: str = "1.14.7"

        @classmethod
        def cdn_url_with_version(cls) -> str:
            """
            Returns the concatenated value of `CDN_URL` and `VERSION`.
            """
            return f"{cls.CDN_URL}/{cls.VERSION}"

        @classmethod
        def js_url(cls) -> str:
            """
            Returns the CDN URL of the minified Popper.js library.
            """
            return f"{cls.CDN_URL}/{cls.VERSION}/umd/popper.min.js"


class __BootstrapRequirements(object):
    """
    Components that are required in a page to make Bootstrap fully functional.

    Typically you will need `bootstrap_css` and `all_js`.
    """

    __slots__ = ()

    @property
    def all_js(self) -> Tuple[script, script, script]:
        """
        All the JavaScript elements that are required by Bootstrap.
        """
        # Bootstrap must be the last item on the list (or at least it should come
        # after jQuery), otherwise some components won't work.
        return (
            self.jquery,
            self.popper_js,
            self.bootstrap_js
        )

    @property
    def bootstrap_css(self) -> link:
        """
        Bootstrap CSS import `link` element.
        """
        return link.css(CDNs.Bootstrap.css_url())

    @property
    def bootstrap_js(self) -> script:
        """
        Bootstrap JavaScript import `script` element.
        """
        return script.ref(CDNs.Bootstrap.js_url())

    @property
    def jquery(self) -> script:
        """
        jQuery JavaScript import `script` element.
        """
        return script.ref(CDNs.jQuery.slim_minified_url())

    @property
    def popper_js(self) -> script:
        """
        Popper.js JavaScript import `script` element.
        """
        return script.ref(CDNs.PopperJS.js_url())

req: __BootstrapRequirements = __BootstrapRequirements()
"""
Components that are required in a page to make Bootstrap fully functional.
"""
