from typing import Dict

from markyp import IElement

from markyp_bootstrap4 import alerts
from markyp_bootstrap4 import badges
from markyp_bootstrap4 import breadcrumbs
from markyp_bootstrap4 import cards
from markyp_bootstrap4 import carousels
from markyp_bootstrap4 import collapses
from markyp_bootstrap4 import dropdowns
from markyp_bootstrap4 import forms
from markyp_bootstrap4 import input_groups
from markyp_bootstrap4 import jumbotrons
from markyp_bootstrap4 import list_groups
from markyp_bootstrap4 import modals
from markyp_bootstrap4 import navbars
from markyp_bootstrap4 import navs
from markyp_bootstrap4 import pagination
from markyp_bootstrap4 import req
from markyp_bootstrap4 import scrollspy
from markyp_bootstrap4 import tabs
from markyp_bootstrap4.buttons import a_button, a_toggle,\
                                      b_button, b_toggle,\
                                      i_button, i_toggle,\
                                      l_button, l_toggle,\
                                      ButtonStyle
from markyp_bootstrap4.colors import bg, text
from markyp_bootstrap4.layout import container_fluid, margin, offset, row, row_break, row_item, one, two, three, col, PercentSize

from markyp_highlightjs import python, js as hljs, themes as hlthemes

from markyp_html import meta, join, style, webpage
from markyp_html.block import div, hr, nav
from markyp_html.forms import form
from markyp_html.inline import a, code, em, img, strong
from markyp_html.text import h1, h2, h3, h4, h5, p

button_margin = margin(x=1, y=1)

lipsum = (
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat orci turpis, "
    "eget euismod elit suscipit quis. Integer rutrum finibus diam et sodales. Integer dignissim "
    "erat urna, a sollicitudin augue egestas quis. Quisque a iaculis urna. Donec ac tortor quis "
    "est fermentum tincidunt at sed enim. Suspendisse sagittis neque nec laoreet imperdiet. "
    "Suspendisse interdum posuere sem auctor commodo. Pellentesque habitant morbi tristique "
    "senectus et netus et malesuada fames ac turpis egestas. Phasellus pulvinar risus dictum "
    "sapien lacinia, a vehicula felis fringilla. Quisque rhoncus erat eros, sit amet luctus mi "
    "vestibulum ac. Vivamus lobortis laoreet lacus nec ullamcorper. Phasellus pulvinar turpis "
    "molestie, accumsan justo vitae, vulputate lectus. Class aptent taciti sociosqu ad litora "
    "torquent per conubia nostra, per inceptos himenaeos."),
    ("Curabitur massa ligula, auctor tempor libero in, pretium venenatis dolor. Donec feugiat "
    "facilisis libero, eu condimentum justo sagittis quis. Nullam arcu ante, porta a lacus sed, "
    "elementum venenatis leo. Nulla efficitur ornare semper. Aliquam mattis mollis ultricies. "
    "Integer imperdiet mauris tortor, ac congue nulla molestie id. Sed quis varius lorem. Orci "
    "varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam "
    "magna diam, varius eget ligula ac, vestibulum venenatis lectus. Aliquam egestas pretium gravida. "
    "Vivamus bibendum ipsum magna, a vestibulum orci imperdiet a. Nam luctus ac odio vitae fringilla."),
    ("Proin ornare sapien tellus. Duis accumsan consectetur consequat. Morbi vel enim pretium, "
    "rhoncus augue a, rutrum nisl. Nam tempus tellus interdum velit vestibulum, quis feugiat orci "
    "mollis. Pellentesque libero enim, sodales iaculis consectetur in, volutpat sit amet magna. "
    "Praesent bibendum mollis nibh, ut feugiat velit consectetur vel. Curabitur pellentesque "
    "suscipit tincidunt. Praesent mattis purus arcu, id interdum dui commodo non. Nulla imperdiet "
    "massa a nulla pharetra pretium. Mauris fermentum euismod scelerisque. Quisque ante justo, "
    "iaculis at consequat eu, fringilla non sem. Vivamus feugiat nibh quis ante porta imperdiet. "
    "Vivamus ultricies augue vel enim finibus, ut viverra sapien tempus. Aliquam eleifend tellus "
    "sed tincidunt lobortis."),
    ("Ut id tempor enim, a fermentum orci. Aliquam lacinia, nulla at lacinia feugiat, tellus metus "
    "efficitur erat, eu porttitor tellus risus ac nisl. Nullam volutpat diam nec facilisis viverra. "
    "Ut fringilla metus at nisi pretium, in mattis lacus hendrerit. Nunc varius gravida quam nec "
    "vestibulum. Morbi vehicula eleifend diam, sit amet fermentum massa. Quisque sit amet pulvinar "
    "justo. Aliquam risus sem, commodo at erat cursus, interdum tempor leo. Praesent id orci eget "
    "orci eleifend sollicitudin. Sed quam arcu, faucibus vitae facilisis vel, volutpat quis eros. "
    "Nullam ullamcorper venenatis ligula at blandit.")
)


custom_css = style(
    """
    .section-anchor {
        margin-top: -54px;
        display: block;
        height: 54px;
        visibility: hidden;
        position: relative;
    }

    .sidebar-nav {
        position: fixed;
        top: 0;
        bottom: 0;
        z-index: 100;
        box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
    }

    .sidebar-sticky {
        position: relative;
        top: 0;
        height: calc(100vh - 56px);
        padding-top: 100px;
        overflow-x: hidden;
        overflow-y: auto;
    }

    @supports ((position: -webkit-sticky) or (position: sticky)) {
        .sidebar-sticky {
            position: -webkit-sticky;
            position: sticky;
        }
    }
    """
)

class SectionRegistry(object):

    class Dropdown(IElement):

        __slots__ = ("_registry",)

        def __init__(self, registry):
            self._registry = registry

        def __str__(self) -> str:
            button_id = "section-list-dropdown-button"
            return dropdowns.dropdown(
                dropdowns.dropdown_button.light("Sections", id=button_id, class_=text.dark),
                dropdowns.menu(
                    *[dropdowns.menu_item(name, factory=a, href=f"#{section_id}")
                        for name, section_id in self._registry.items()],
                    button_id=button_id
                )
            ).markup

    class SidebarNav(IElement):

        __slots__ = ("_registry",)

        def __init__(self, registry):
            self._registry = registry

        def __str__(self) -> str:
            return navs.nav(
                navs.nav_item(h4("Table of Contents")),
                *[navs.nav_item(navs.nav_link(name, href=f"#{section_id}", class_=text.dark))
                    for name, section_id in self._registry.items()],
                class_="flex-column",
                nav_style=navs.NavStyle.PILLS
            ).markup

    def __init__(self):
        self._registry: Dict = {}

    @property
    def dropdown(self):
        return SectionRegistry.Dropdown(self)

    @property
    def sidebar_nav(self):
        return SectionRegistry.SidebarNav(self)

    def items(self):
        return self._registry.items()

    def section(self, title):
        element_id = self._get_id(title)
        self._registry[title] = element_id
        return two(
            div(class_="section-anchor", id=element_id),
            h3(title, id=element_id, class_=margin(top=4, bottom=3)),
            md=(12, 12)
        )

    def subsection(self, *args):
        # Don't register subsections for now, the section list is long enough in itself.
        return one(h4(*args), class_=margin(top=3, bottom=2), md=12)

    def _get_id(self, key: str) -> str:
        base = key.lower().replace(" ", "-")
        if base not in self._registry:
            return base

        index = 0
        while f"{base}-{index}" in self._registry:
            index += 1

        return f"{base}-{index}"

section_registry = SectionRegistry()

def get_alert():
    return alerts.alert.primary(
        h4("Alert with", badges.span_badge.primary("primary"), "context."),
        hr(),
        python(
            'from markyp_html.text import h3\n'
            'from markyp_bootstrap4.alerts import alert\n'
            'from markyp_bootstrap4.badges import span_badge\n\n'
            'alert.primary(h3("Alert with", span_badge.primary("primary"), "context."))'
        )
    )

def get_dismissable_alert():
    return alerts.dismissable.danger(
        h4("Dismissable alert with", badges.span_badge.danger("danger"), "context."),
        hr(),
        python(
            'from markyp_html.text import h3\n'
            'from markyp_bootstrap4.alerts import dismissable\n'
            'from markyp_bootstrap4.badges import span_badge\n\n'
            'dismissable.danger(h3("Dismissable alert with", span_badge.danger("danger"), "context."))'
        )
    )

def get_breadcrumb():
    return breadcrumbs.breadcrumb(
        a(strong("Home"), href="#"),
        a("Topic", href="#"),
        a("Subtopic", href="#"),
        em("Current page")
    )

def get_breadcrumb_code():
    return python(
        'from markyp_bootstrap4.breadcrumbs import breadcrumb\n'
        'from markyp_html.inline import a, em, strong\n\n'
        'breadcrumb(\n'
        '    a(strong("Home"), href="#"),\n'
        '    a("Topic", href="#"),\n'
        '    a("Subtopic", href="#"),\n'
        '    em("Current page")\n)'
    )

def get_buttons():
    return row(
        h5("Active:"),
        row_break(),
        l_button.primary("Primary", active=True, class_=button_margin),
        l_button.secondary("Secondary", active=True, class_=button_margin),
        l_button.success("Success", active=True, class_=button_margin),
        l_button.danger("Danger", active=True, class_=button_margin),
        l_button.warning("Warning", active=True, class_=button_margin),
        l_button.info("Info", active=True, class_=button_margin),
        l_button.light("Light", active=True, class_=button_margin),
        l_button.dark("Dark", active=True, class_=button_margin),
        l_button.link("Link", active=True, class_=button_margin),
        class_=col(md=12)
    )

def get_buttons_large():
    return row(
        h5("Large:"),
        row_break(),
        b_button.primary("Primary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.secondary("Secondary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.success("Success", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.danger("Danger", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.warning("Warning", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.info("Info", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.light("Light", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.dark("Dark", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.link("Link", class_=join(ButtonStyle.LARGE, button_margin)),
        class_=col(md=12)
    )

def get_buttons_small():
    return row(
        h5("Small:"),
        row_break(),
        i_button.primary("Primary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.secondary("Secondary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.success("Success", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.danger("Danger", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.warning("Warning", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.info("Info", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.light("Light", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.dark("Dark", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.link("Link", class_=join(ButtonStyle.SMALL, button_margin)),
        class_=col(md=12)
    )

def get_buttons_disabled():
    return row(
        h5("Disabled:"),
        row_break(),
        b_button.primary("Primary", disabled=True, class_=button_margin),
        b_button.secondary("Secondary", disabled=True, class_=button_margin),
        b_button.success("Success", disabled=True, class_=button_margin),
        b_button.danger("Danger", disabled=True, class_=button_margin),
        b_button.warning("Warning", disabled=True, class_=button_margin),
        b_button.info("Info", disabled=True, class_=button_margin),
        b_button.light("Light", disabled=True, class_=button_margin),
        b_button.dark("Dark", disabled=True, class_=button_margin),
        b_button.link("Link", disabled=True, class_=button_margin),
        class_=col(md=12)
    )

def get_buttons_block():
    return row(
        h5("Block:"),
        row_break(),
        a_button.primary("Primary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.secondary("Secondary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.success("Success", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.danger("Danger", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.warning("Warning", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.info("Info", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.light("Light", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.dark("Dark", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.link("Link", class_=join(ButtonStyle.BLOCK, button_margin)),
        class_=col(md=12)
    )

def get_outline_buttons():
    return row(
        h5("Active:"),
        row_break(),
        l_button.primary_outline("Primary", active=True, class_=button_margin),
        l_button.secondary_outline("Secondary", active=True, class_=button_margin),
        l_button.success_outline("Success", active=True, class_=button_margin),
        l_button.danger_outline("Danger", active=True, class_=button_margin),
        l_button.warning_outline("Warning", active=True, class_=button_margin),
        l_button.info_outline("Info", active=True, class_=button_margin),
        l_button.light_outline("Light", active=True, class_=button_margin),
        l_button.dark_outline("Dark", active=True, class_=button_margin),
        l_button.link_outline("Link", active=True, class_=button_margin),
        class_=col(md=12)
    )

def get_outline_buttons_large():
    return row(
        h5("Large:"),
        row_break(),
        b_button.primary_outline("Primary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.secondary_outline("Secondary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.success_outline("Success", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.danger_outline("Danger", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.warning_outline("Warning", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.info_outline("Info", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.light_outline("Light", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.dark_outline("Dark", class_=join(ButtonStyle.LARGE, button_margin)),
        b_button.link_outline("Link", class_=join(ButtonStyle.LARGE, button_margin)),
        class_=col(md=12)
    )

def get_outline_buttons_small():
    return row(
        h5("Small:"),
        row_break(),
        i_button.primary_outline("Primary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.secondary_outline("Secondary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.success_outline("Success", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.danger_outline("Danger", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.warning_outline("Warning", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.info_outline("Info", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.light_outline("Light", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.dark_outline("Dark", class_=join(ButtonStyle.SMALL, button_margin)),
        i_button.link_outline("Link", class_=join(ButtonStyle.SMALL, button_margin)),
        class_=col(md=12)
    )

def get_outline_buttons_disabled():
    return row(
        h5("Disabled:"),
        row_break(),
        b_button.primary_outline("Primary", disabled=True, class_=button_margin),
        b_button.secondary_outline("Secondary", disabled=True, class_=button_margin),
        b_button.success_outline("Success", disabled=True, class_=button_margin),
        b_button.danger_outline("Danger", disabled=True, class_=button_margin),
        b_button.warning_outline("Warning", disabled=True, class_=button_margin),
        b_button.info_outline("Info", disabled=True, class_=button_margin),
        b_button.light_outline("Light", disabled=True, class_=button_margin),
        b_button.dark_outline("Dark", disabled=True, class_=button_margin),
        b_button.link_outline("Link", disabled=True, class_=button_margin),
        class_=col(md=12)
    )

def get_outline_buttons_block():
    return row(
        h5("Block:"),
        row_break(),
        a_button.primary_outline("Primary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.secondary_outline("Secondary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.success_outline("Success", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.danger_outline("Danger", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.warning_outline("Warning", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.info_outline("Info", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.light_outline("Light", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.dark_outline("Dark", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_button.link_outline("Link", class_=join(ButtonStyle.BLOCK, button_margin)),
        class_=col(md=12)
    )

def get_toggle_buttons():
    return row(
        h5("Active:"),
        row_break(),
        l_toggle.primary("Primary", active=True, class_=button_margin),
        l_toggle.secondary("Secondary", active=True, class_=button_margin),
        l_toggle.success("Success", active=True, class_=button_margin),
        l_toggle.danger("Danger", active=True, class_=button_margin),
        l_toggle.warning("Warning", active=True, class_=button_margin),
        l_toggle.info("Info", active=True, class_=button_margin),
        l_toggle.light("Light", active=True, class_=button_margin),
        l_toggle.dark("Dark", active=True, class_=button_margin),
        l_toggle.link("Link", active=True, class_=button_margin),
        class_=col(md=12)
    )

def get_toggle_buttons_large():
    return row(
        h5("Large:"),
        row_break(),
        b_toggle.primary("Primary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.secondary("Secondary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.success("Success", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.danger("Danger", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.warning("Warning", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.info("Info", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.light("Light", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.dark("Dark", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.link("Link", class_=join(ButtonStyle.LARGE, button_margin)),
        class_=col(md=12)
    )

def get_toggle_buttons_small():
    return row(
        h5("Small:"),
        row_break(),
        i_toggle.primary("Primary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.secondary("Secondary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.success("Success", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.danger("Danger", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.warning("Warning", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.info("Info", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.light("Light", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.dark("Dark", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.link("Link", class_=join(ButtonStyle.SMALL, button_margin)),
        class_=col(md=12)
    )

def get_toggle_buttons_disabled():
    return row(
        h5("Disabled:"),
        row_break(),
        b_toggle.primary("Primary", disabled=True, class_=button_margin),
        b_toggle.secondary("Secondary", disabled=True, class_=button_margin),
        b_toggle.success("Success", disabled=True, class_=button_margin),
        b_toggle.danger("Danger", disabled=True, class_=button_margin),
        b_toggle.warning("Warning", disabled=True, class_=button_margin),
        b_toggle.info("Info", disabled=True, class_=button_margin),
        b_toggle.light("Light", disabled=True, class_=button_margin),
        b_toggle.dark("Dark", disabled=True, class_=button_margin),
        b_toggle.link("Link", disabled=True, class_=button_margin),
        class_=col(md=12)
    )

def get_toggle_buttons_block():
    return row(
        h5("Block:"),
        row_break(),
        a_toggle.primary("Primary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.secondary("Secondary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.success("Success", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.danger("Danger", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.warning("Warning", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.info("Info", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.light("Light", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.dark("Dark", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.link("Link", class_=join(ButtonStyle.BLOCK, button_margin)),
        class_=col(md=12)
    )

def get_outline_toggle_buttons():
    return row(
        h5("Active:"),
        row_break(),
        l_toggle.primary_outline("Primary", active=True, class_=button_margin),
        l_toggle.secondary_outline("Secondary", active=True, class_=button_margin),
        l_toggle.success_outline("Success", active=True, class_=button_margin),
        l_toggle.danger_outline("Danger", active=True, class_=button_margin),
        l_toggle.warning_outline("Warning", active=True, class_=button_margin),
        l_toggle.info_outline("Info", active=True, class_=button_margin),
        l_toggle.light_outline("Light", active=True, class_=button_margin),
        l_toggle.dark_outline("Dark", active=True, class_=button_margin),
        l_toggle.link_outline("Link", active=True, class_=button_margin),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_large():
    return row(
        h5("Large:"),
        row_break(),
        b_toggle.primary_outline("Primary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.secondary_outline("Secondary", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.success_outline("Success", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.danger_outline("Danger", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.warning_outline("Warning", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.info_outline("Info", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.light_outline("Light", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.dark_outline("Dark", class_=join(ButtonStyle.LARGE, button_margin)),
        b_toggle.link_outline("Link", class_=join(ButtonStyle.LARGE, button_margin)),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_small():
    return row(
        h5("Small:"),
        row_break(),
        i_toggle.primary_outline("Primary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.secondary_outline("Secondary", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.success_outline("Success", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.danger_outline("Danger", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.warning_outline("Warning", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.info_outline("Info", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.light_outline("Light", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.dark_outline("Dark", class_=join(ButtonStyle.SMALL, button_margin)),
        i_toggle.link_outline("Link", class_=join(ButtonStyle.SMALL, button_margin)),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_disabled():
    return row(
        h5("Disabled:"),
        row_break(),
        b_toggle.primary_outline("Primary", disabled=True, class_=button_margin),
        b_toggle.secondary_outline("Secondary", disabled=True, class_=button_margin),
        b_toggle.success_outline("Success", disabled=True, class_=button_margin),
        b_toggle.danger_outline("Danger", disabled=True, class_=button_margin),
        b_toggle.warning_outline("Warning", disabled=True, class_=button_margin),
        b_toggle.info_outline("Info", disabled=True, class_=button_margin),
        b_toggle.light_outline("Light", disabled=True, class_=button_margin),
        b_toggle.dark_outline("Dark", disabled=True, class_=button_margin),
        b_toggle.link_outline("Link", disabled=True, class_=button_margin),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_block():
    return row(
        h5("Block:"),
        row_break(),
        a_toggle.primary_outline("Primary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.secondary_outline("Secondary", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.success_outline("Success", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.danger_outline("Danger", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.warning_outline("Warning", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.info_outline("Info", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.light_outline("Light", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.dark_outline("Dark", class_=join(ButtonStyle.BLOCK, button_margin)),
        a_toggle.link_outline("Link", class_=join(ButtonStyle.BLOCK, button_margin)),
        class_=col(md=12)
    )

def get_card_left():
    return cards.card(
        cards.header.h5("Hungary"),
        cards.Image.top("https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/EU-Hungary.svg/500px-EU-Hungary.svg.png"),
        cards.body(
            cards.text.p(
                "Hungary is a country in Central Europe, spanning 93,030 square kilometres "
                "in the Carpathian Basin. With about 10 million inhabitants, Hungary is a "
                "medium-sized member state of the European Union. The official language is "
                "Hungarian, which is the most widely spoken Uralic language in the world..."
            )
        ),
        cards.footer_div(cards.link("Learn more", href="http://www.wikiwand.com/en/Hungary")),
        class_=join(bg.light, text.dark, cards.TextAlign.LEFT, PercentSize.height_100)
    )

def get_card_center():
    return cards.card(
        cards.header.h5("Hungarian History"),
        cards.body(
            cards.text.p(
                "The foundations of the Hungarian state were established in the late ninth "
                "century CE by the Hungarian grand prince Árpád following the conquest of "
                "the Carpathian Basin. His great-grandson Stephen I ascended the  throne "
                "in 1000, converting his realm to a Christian kingdom. By the 12th century, "
                "Hungary became a regional power, reaching its cultural and  political "
                "height in the 15th century..."
            )
        ),
        cards.Image.bottom("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Istvan-ChroniconPictum.jpg/340px-Istvan-ChroniconPictum.jpg"),
        cards.footer_div(cards.link("Learn more", href="http://www.wikiwand.com/en/Budapest#/History")),
        class_=join(bg.light, text.dark, cards.TextAlign.CENTER, PercentSize.height_100)
    )

def get_card_right():
    return cards.card(
        cards.header.h5("Budapest"),
        cards.Image.top("https://images.pexels.com/photos/59701/pexels-photo-59701.jpeg"),
        cards.body(
            cards.text.p(
                "The history of Budapest began when an early Celtic settlement transformed "
                "into the Roman town of Aquincum, the capital of Lower Pannonia. The Hungarians "
                "arrived in the territory in the late 9th century. The area was pillaged by "
                "the Mongols in 1241. Buda, the settlements on the west bank of the river, "
                "became one of the centres of Renaissance humanist culture by the 15th century..."
            )
        ),
        cards.footer_div(cards.link("Learn more", href="http://www.wikiwand.com/en/Budapest")),
        class_=join(bg.light, text.dark, cards.TextAlign.RIGHT, PercentSize.height_100)
    )

def get_carousel():
    imports = "\n".join([
        "from markyp_bootstrap4.carousels import carousel, item_caption",
        "from markyp_html.block import div",
        "from markyp_html.inline import img",
        "from markyp_html.text import h4"
    ])
    slides = "\n".join([
        '    div(',
        '       img.placeholder(4*160, 4*90, text=f"Slide 1", class_="d-block w-100"),',
        '       item_caption(h4("Slide 1"))',
        '    ),',
        '    div(',
        '       img.placeholder(4*160, 4*90, text=f"Slide 2", class_="d-block w-100"),',
        '       item_caption(h4("Slide 2"))',
        '    ),',
        '    div(',
        '       img.placeholder(4*160, 4*90, text=f"Slide 3", class_="d-block w-100"),',
        '       item_caption(h4("Slide 3"))',
        '    ),'
    ])
    c_full = "\n".join([
        'carousel(',
        slides,
        '    identifier="full-carousel"',
        ')'
    ])
    c_controls_only = "\n".join([
        'carousel(',
        slides,
        '    add_indicators=False,',
        '    identifier="controls-only-carousel"',
        ')'
    ])
    c_indicators_only = "\n".join([
        'carousel(',
        slides,
        '    add_controls=False,',
        '    identifier="indicators-only-carousel"',
        ')'
    ])
    c_empty = "\n".join([
        'carousel(',
        slides,
        '    add_controls=False,',
        '    add_indicators=False,',
        '    identifier="controlless-carousel"',
        ')'
    ])
    return carousels.carousel(
        one(div(
            python(
                f"{imports}\n\n{c_empty}",
                class_=join(col(md=8), offset(md=2), margin(bottom=5))
            ),
            carousels.item_caption(h4("Carousel without controls and indicators"))
        )),
        one(div(
            python(
                f"{imports}\n\n{c_controls_only}",
                class_=join(col(md=8), offset(md=2), margin(bottom=5))
            ),
            carousels.item_caption(h4("Carousel with controls"))
        )),
        one(div(
            python(
                f"{imports}\n\n{c_indicators_only}",
                class_=join(col(md=8), offset(md=2), margin(bottom=5))
            ),
            carousels.item_caption(h4("Carousel with indicators"))
        )),
        one(div(
            python(
                f"{imports}\n\n{c_full}",
                class_=join(col(md=8), offset(md=2), margin(bottom=5))
            ),
            carousels.item_caption(h4("Carousel with controls and indicators"))
        )),
        identifier="Carousel-1"
    )

def get_collapse():
    collapse_id = "collapse-1"
    collapse_shown = True
    button_args = collapses.button_args_for(collapse_id, expanded=collapse_shown)
    button_args["_class"] = button_margin
    return div(
        div(
            b_button.primary("Primary", **button_args),
            b_button.secondary("Secondary", **button_args),
            b_button.success("Success", **button_args),
            b_button.danger("Danger", **button_args),
            b_button.warning("Warning", **button_args),
            b_button.info("Info", **button_args),
            b_button.light("Light", **button_args),
            b_button.dark("Dark", **button_args),
            b_button.link("Link", **button_args),
            class_=margin(bottom=2)
        ),
        row_break(),
        collapses.collapse(
            python(
                'from markyp_bootstrap4 import collapses\n'
                'from markyp_bootstrap4.buttons import b_button\n'
                'from markyp_bootstrap4.layout import row_break\n'
                'from markyp_html.block import div\n\n'
                'collapse_id = "collapse-1"\n'
                'div(\n'
                '    b_button.primary("Toggle collapse", class_="mb-2", **collapses.button_args_for(collapse_id)),\n'
                '    row_break(),\n'
                '    collapses.collapse(\n'
                '        "Collapse content, closed by default.",\n'
                '        identifier=collapse_id\n'
                '    )\n'
                ')'
            ),
            identifier=collapse_id,
            show=collapse_shown
        )
    )

def get_accordion():
    acc_id = "acc-1"
    titles = ["First", "Second", "Third", "Fourth", "Fifth"]
    contents = [f"Content of {title.lower()} collapse within the accordion ..." for title in titles]
    items = [
        cards.card(
            cards.title.h5(b_button.link(ttl, class_=text.light), **collapses.button_args_for(f"{acc_id}-{ttl}")),
            collapses.collapse(
                cards.body(cnt, class_=join(bg.light, text.dark)),
                identifier=f"{acc_id}-{ttl}",
                accordion_id=acc_id
            ),
            class_=join(bg.dark, text.light)
        ) for ttl, cnt in zip(titles, contents)
    ]
    return div(*items, id=acc_id)

def get_dropdown():
    menu_items = (
        dropdowns.menu_header.h5("Group 1"),
        dropdowns.menu_item("Action 1"),
        dropdowns.menu_item("Action 2"),
        dropdowns.menu_divider(),
        dropdowns.menu_header.h5("Group 2"),
        dropdowns.menu_item("Action 3", disabled=True),
        dropdowns.menu_item("Action 4")
    )
    return (
        dropdowns.dropdown(
            dropdowns.dropdown_button.primary_outline("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        ),
        dropdowns.dropdown(
            dropdowns.dropdown_button.secondary("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        ),
        dropdowns.dropdown(
            dropdowns.dropdown_button.success_outline("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        ),
        dropdowns.dropdown(
            dropdowns.dropdown_button.danger("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        ),
        dropdowns.dropdown(
            dropdowns.dropdown_button.warning_outline("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        ),
        dropdowns.dropdown(
            dropdowns.dropdown_button.info("Dropdown button", id="dropdown-button-1", class_=button_margin),
            dropdowns.menu(*menu_items, button_id="dropdown-button-1")
        )
    )

def get_multiline_login_form():
    return form(
        forms.form_group(
            forms.text.h5("Email"),
            forms.input_.email(placeholder="Enter your email address")
        ),
        forms.form_group(
            forms.text.h5("Password"),
            forms.input_.password(placeholder="Enter your password")
        ),
        forms.form_check(
            forms.input_.checkbox(),
            forms.form_check_label("Remember Me")
        ),
        b_button.primary("Sign In", type="submit")
    )

def get_grid_login_form():
    return form(
        forms.form_group(
            forms.text.h5("Email", class_=col(md=2)),
            forms.input_.email(placeholder="Enter your email address", class_=col(md=10)),
            row=True
        ),
        forms.form_group(
            forms.text.h5("Password", class_=col(md=2)),
            forms.input_.password(placeholder="Enter your password", class_=col(md=10)),
            row=True
        ),
        forms.form_check(
            forms.input_.checkbox(),
            forms.form_check_label("Remember Me")
        ),
        b_button.primary("Sign In", type="submit")
    )

def get_inline_login_form():
    return forms.inline_form(
        input_groups.input_group(
            input_groups.pre_group(input_groups.text.p("@")),
            forms.input_.text(placeholder="Username"),
            class_=margin(right=2)
        ),
        forms.input_.password(placeholder="Password", class_=margin(right=2)),
        forms.form_check(
            forms.input_.checkbox(),
            forms.form_check_label("Remember Me"),
            class_=margin(right=2)
        ),
        b_button.primary("Sign In", type="submit")
    )

def get_jumbotron():
    return jumbotrons.jumbotron(
        h1("Example jumbotron",class_=text.dark),
        python(
            'from markyp_html.text import h1, p\n\n'
            'from markyp_bootstrap4.jumbotrons import jumbotron\n\n'
            'jumbotron(\n'
            '    h1("Jumbotron"),\n'
            '    p("With a lengthy description...")\n'
            ')'
        )
    )

def get_input_groups():
    return (
        input_groups.input_group(
            input_groups.pre_group(input_groups.text.p("First and last name:")),
            forms.input_.text(placeholder="First name"),
            forms.input_.text(placeholder="Last name"),
            class_=margin(bottom=2)
        ),
        row_break(),
        input_groups.input_group(
            input_groups.pre_group(input_groups.text.p("Email address:")),
            forms.input_.text(placeholder="username"),
            input_groups.post_group(input_groups.text.p("@markyp-bootstrap4.org")),
            class_=margin(bottom=2)
        ),
        row_break(),
        input_groups.input_group(
            input_groups.pre_group(b_button.light_outline("Submit your application")),
            forms.textarea(placeholder="Write your comments here.", class_="form-control"),
            class_=margin(bottom=2)
        )
    )

def get_list_group():
    list_id = "tab-list-1"
    tab_id = "tab-content-1"
    return (
        list_groups.list_group(
            list_groups.list_group_item(
                "First",
                id=f"{list_id}-1", href=f"#{tab_id}-1",
                role="tab", **{"data-toggle": "list"},
                factory=a, action=True, active=True
            ),
            list_groups.list_group_item(
                "Second",
                id=f"{list_id}-2", href=f"#{tab_id}-2",
                role="tab", **{"data-toggle": "list"},
                factory=a, action=True
            ),
            list_groups.list_group_item(
                "Third",
                id=f"{list_id}-3", href=f"#{tab_id}-3",
                role="tab", **{"data-toggle": "list"},
                factory=a, action=True
            ),
            factory=div,
            id=list_id,
            role="tablist"
        ),
        tabs.tab_content(
            tabs.tab_pane(lipsum[1], id=f"{tab_id}-1", active=True),
            tabs.tab_pane(lipsum[2], id=f"{tab_id}-2"),
            tabs.tab_pane(lipsum[3], id=f"{tab_id}-3"),
            id=tab_id
        )
    )

def get_modal():
    modal_id = "modal-1"
    return div(
        modals.toggle_button.primary("Show modal with example code", modal_id=modal_id),
        modals.modal(
            python("\n".join((
                'from markyp_html.block import hr',
                'from markyp_html.inline import img',
                'from markyp_bootstrap4 import modals\n',
                'modal_id = "example-modal-1"',
                '\n# Toggle button for the modal.',
                'modals.toggle_button.primary("Show modal", modal_id=modal_id),',
                '\n# The modal itself.',
                'modals.modal(',
                '    "Modal content...", hr(), img.placeholder(300, 200), hr(), "More modal content...",',
                '    title=modals.title.h4("Example modal"),',
                '    footer=modals.close_button.primary("Close"),',
                '    id=modal_id',
                ')'
            ))),
            title=modals.title.h4("Modal example"),
            footer=modals.close_button.primary("Close"),
            id=modal_id,
            content_class=join(bg.light, text.dark)
        )
    )

def get_navbar(*, fixed = True):
    collapse_id = "main-navbar-collapse"
    return navbars.navbar(
        container_fluid(
            navbars.brand("markyp-bootstrap4"),
            navbars.navbar_toggler(collapse_id=collapse_id),
            navbars.collapse(
                navs.nav_link("GitHub", href="https://github.com/volfpeter/markyp-bootstrap4", target="_blank", is_nav_item=True),
                navs.nav_link("PyPI", href="https://pypi.org/project/markyp-bootstrap4", target="_blank", is_nav_item=True),
                navs.nav_link("Bootstrap 4", href="https://getbootstrap.com/", target="_blank", is_nav_item=True),
                section_registry.dropdown,
                id=collapse_id,
                nav_factory=div
            )
        ),
        expand_point=navbars.ExpandPoint.LG,
        theme=navbars.Theme.LIGHT,
        class_=join("fixed-top" if fixed else None, bg.light)
    )

def get_navbar_example_code():
    return python("\n".join((
        'from markyp_bootstrap4 import navbars',
        'from markyp_bootstrap4 import navs',
        'from markyp_html.block import div\n',
        'collapse_id = "main-navbar-collapse"\n',
        'navbars.navbar(',
        '    navbars.brand("markyp-bootstrap4"),',
        '    navbars.navbar_toggler(collapse_id=collapse_id),',
        '    navbars.collapse(',
        '        navs.nav_link("GitHub", href="https://github.com/volfpeter/markyp-bootstrap4", target="_blank", is_nav_item=True),',
        '        navs.nav_link("PyPI", href="https://pypi.org/project/markyp-bootstrap4", target="_blank", is_nav_item=True),',
        '        navs.nav_link("Bootstrap 4", href="https://getbootstrap.com/", target="_blank", is_nav_item=True),',
        '        id=collapse_id,',
        '        nav_factory=div,',
        '    ),',
        '    expand_point=navbars.ExpandPoint.LG,',
        '    theme=navbars.Theme.DARK',
        ')'
    )), class_=margin(top=3))

def get_nav():
    example_code = python("\n".join((
        "from markyp_bootstrap4 import navs",
        "navs.navigated_tabs(",
        "    (\"First\", \"First tab content\"),",
        "    (\"Second\", \"Second tab content\"),",
        "    (\"Third\", \"Third tab content\"),",
        "    id=\"navigated-tabs-example\",",
        "    nav_fill=True,",
        "    nav_justified=True",
        ")"
    )))
    return navs.navigated_tabs(
        ("First", div(lipsum[0], example_code)),
        ("Second", div(lipsum[1], example_code)),
        ("Third", div(lipsum[2], example_code)),
        id="navigated-tabs-example",
        nav_fill=True,
        nav_justified=True
    )

def get_pagination():
    def create(position, size):
        return pagination.pagination(
            *(pagination.page_item(item, active=index==3, href="#pagination")
                for index, item in enumerate(("Previous", "1", "2", "3", "4", "5", "Next"))),
            aria_label="Pagination example",
            position=position,
            size=size
        )
    return (
        create(pagination.PaginationPosition.LEFT, pagination.PaginationSize.SMALL),
        create(pagination.PaginationPosition.CENTER, pagination.PaginationSize.DEFAULT),
        create(pagination.PaginationPosition.END, pagination.PaginationSize.LARGE)
    )

def get_pagination_example_code():
    return python("\n".join((
        'from markyp_bootstrap4 import pagination\n',
        'pagination.pagination(',
        '    *(pagination.page_item(item, active=index==3, href="#page-ref")',
        '        for index, item in enumerate(("Previous", "1", "2", "3", "Next"))),',
        '    aria_label="Pagination example",',
        '    position=pagination.PaginationPosition.CENTER,',
        '    size=pagination.PaginationSize.SMALL',
        ')'
    )))

page = webpage(
    get_navbar(),
    container_fluid(row(
        nav(
            div(section_registry.sidebar_nav, class_="sidebar-sticky"),
            class_=join("sidebar-nav d-none d-md-block", col(md=2), bg.light, text.dark),
            id="sidebar-navbar"
        ),
        row_item(
            container_fluid(
                one(
                    h3(
                        "Building web pages with Python,",
                        a(code("markyp"), href="https://github.com/volfpeter/markyp"), ",",
                        a(code("markyp-html"), href="https://github.com/volfpeter/markyp-html"), "and",
                        a(code("markyp-bootstrap4"), href="https://github.com/volfpeter/markyp-bootstrap4")
                    ),
                    md=12,
                    style="margin-top: 100px;"
                ),
                section_registry.section("Alerts and badges"),
                one(get_alert(), md=12),
                one(get_dismissable_alert(), md=12),
                section_registry.section("Breadcrumbs"),
                one(get_breadcrumb(), md=12),
                one(get_breadcrumb_code(), md=12),
                section_registry.section("Buttons"),
                section_registry.subsection("Buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"),
                get_buttons(),
                hr(),
                get_buttons_small(),
                hr(),
                get_buttons_large(),
                hr(),
                get_buttons_disabled(),
                hr(),
                get_buttons_block(),
                section_registry.subsection("Outline buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"),
                get_outline_buttons(),
                hr(),
                get_outline_buttons_small(),
                hr(),
                get_outline_buttons_large(),
                hr(),
                get_outline_buttons_disabled(),
                hr(),
                get_outline_buttons_block(),
                section_registry.subsection("Toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"),
                get_toggle_buttons(),
                hr(),
                get_toggle_buttons_small(),
                hr(),
                get_toggle_buttons_large(),
                hr(),
                get_toggle_buttons_disabled(),
                hr(),
                get_toggle_buttons_block(),
                section_registry.subsection("Outline toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"),
                get_outline_toggle_buttons(),
                hr(),
                get_outline_toggle_buttons_small(),
                hr(),
                get_outline_toggle_buttons_large(),
                hr(),
                get_outline_toggle_buttons_disabled(),
                hr(),
                get_outline_toggle_buttons_block(),
                section_registry.section("Cards"),
                three(
                    get_card_left(), get_card_center(), get_card_right(),
                    md=(4, 4, 4)
                ),
                section_registry.section("Carousels"),
                one(get_carousel(), md=12),
                section_registry.section("Collapses"),
                section_registry.subsection("Collapse with multiple toggle buttons"),
                one(get_collapse(), md=12),
                section_registry.subsection("Accordion"),
                one(get_accordion(), md=12),
                section_registry.section("Dropdowns"),
                row(*get_dropdown(), class_=col(md=12)),
                section_registry.section("Forms"),
                section_registry.subsection("Multiline login form"),
                one(get_multiline_login_form(), md=10, class_=offset(md=1)),
                section_registry.subsection("Grid login form"),
                one(get_grid_login_form(), md=10, class_=offset(md=1)),
                section_registry.subsection("Inline login form"),
                one(get_inline_login_form(), md=10, class_=offset(md=1)),
                section_registry.section("Input groups"),
                row(*get_input_groups(), class_=col(md=12)),
                section_registry.section("Jumbotrons"),
                one(get_jumbotron(), md=12),
                section_registry.section("List groups with tabs"),
                two(*get_list_group(), md=(4, 8)),
                section_registry.section("Modals"),
                one(get_modal(), md=12),
                section_registry.section("Navs and navigated tabs"),
                two(*get_nav(), md=(12, 12)),
                section_registry.section("Navbars"),
                one(get_navbar(fixed=False), md=12),
                one(get_navbar_example_code(), md=12),
                section_registry.section("Pagination"),
                three(*get_pagination(), md=(12, 12, 12)),
                one(get_pagination_example_code(), md=12)
            ),
            md=10
        )
    )),
    page_title="markyp-bootstrap4 demo page",
    head_elements=[
        custom_css,
        req.bootstrap_css,
        hlthemes.github
    ],
    metadata=[
        meta.author("Website Author"),
        meta.charset("UTF-8"),
        meta.description("markyp-bootstrap4 demo"),
        meta.keywords("markyp-html,markyp-bootstrap4,markup,Python,HTML,Bootstrap"),
        meta.viewport("width=device-width, initial-scale=1.0")
    ],
    javascript=[
        *req.all_js,
        *hljs.js
    ],
    class_=text.light,
    style="background-color: #41474D; position: relative;",
    **scrollspy.spied_by("sidebar-navbar", offset=1)
)


# Get the actual HTML markup.
html = str(page)  # or page.markup
print(html)
