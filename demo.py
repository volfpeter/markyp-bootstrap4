from markyp_bootstrap4 import alerts
from markyp_bootstrap4 import cards
from markyp_bootstrap4 import carousels
from markyp_bootstrap4 import collapses
from markyp_bootstrap4 import dropdowns
from markyp_bootstrap4 import forms
from markyp_bootstrap4 import input_groups
from markyp_bootstrap4 import jumbotrons
from markyp_bootstrap4 import req
from markyp_bootstrap4.badges import span_badge
from markyp_bootstrap4.breadcrumbs import breadcrumb
from markyp_bootstrap4.buttons import a_button, a_toggle,\
                                      b_button, b_toggle,\
                                      i_button, i_toggle,\
                                      l_button, l_toggle,\
                                      ButtonStyle
from markyp_bootstrap4.colors import bg, text
from markyp_bootstrap4.layout import container, margin, offset, padding, row, row_break, row_item, one, two, three, col, PercentSize

from markyp_highlightjs import highlight, js as hljs, themes as hlthemes

from markyp_html import meta, join, webpage
from markyp_html.block import div, hr
from markyp_html.forms import form
from markyp_html.inline import a, code, em, img, strong
from markyp_html.text import h1, h2, h3, h4, p

button_margin = margin(x=1, y=1)

def section_header(*args):
    return one(h2(*args, md=12, class_=padding(top=5)))

def subsection_header(*args):
    return one(h3(*args, md=12, class_=padding(top=3)))

def get_alert():
    return alerts.alert.primary(
        h3("Alert with", span_badge.primary("primary"), "context."),
        hr(),
        highlight(
            'from markyp_html.text import h3\n'
            'from markyp_bootstrap4.alerts import alert\n'
            'from markyp_bootstrap4.badges import span_badge\n\n'
            'alert.primary(h3("Alert with", span_badge.primary("primary"), "context."))',
            language="python"
        )
    )

def get_dismissable_alert():
    return alerts.dismissable.danger(
        h3("Dismissable alert with", span_badge.danger("danger"), "context."),
        hr(),
        highlight(
            'from markyp_html.text import h3\n'
            'from markyp_bootstrap4.alerts import dismissable\n'
            'from markyp_bootstrap4.badges import span_badge\n\n'
            'dismissable.danger(h3("Dismissable alert with", span_badge.danger("danger"), "context."))',
            language="python"
        )
    )

def get_breadcrumb():
    return breadcrumb(
        a(strong("Home"), href="#"),
        a("Topic", href="#"),
        a("Subtopic", href="#"),
        em("Current page")
    )

def get_breadcrumb_code():
    return highlight(
        'from markyp_bootstrap4.breadcrumbs import breadcrumb\n'
        'from markyp_html.inline import a, em, strong\n\n'
        'breadcrumb(\n'
        '    a(strong("Home"), href="#"),\n'
        '    a("Topic", href="#"),\n'
        '    a("Subtopic", href="#"),\n'
        '    em("Current page")\n)',
        language="python"
    )

def get_buttons():
    return row(
        h4("Active:"),
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
        h4("Large:"),
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
        h4("Small:"),
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
        h4("Disabled:"),
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
        h4("Block:"),
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
        h4("Active:"),
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
        h4("Large:"),
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
        h4("Small:"),
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
        h4("Disabled:"),
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
        h4("Block:"),
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
        h4("Active:"),
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
        h4("Large:"),
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
        h4("Small:"),
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
        h4("Disabled:"),
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
        h4("Block:"),
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
        h4("Active:"),
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
        h4("Large:"),
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
        h4("Small:"),
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
        h4("Disabled:"),
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
        h4("Block:"),
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
            highlight(
                f"{imports}\n\n{c_empty}",
                language="python",
                class_=join(col(md=8), offset(md=2), padding(bottom=5))
            ),
            carousels.item_caption(h4("Carousel without controls and indicators"))
        )),
        one(div(
            highlight(
                f"{imports}\n\n{c_controls_only}",
                language="python",
                class_=join(col(md=8), offset(md=2), padding(bottom=5))
            ),
            carousels.item_caption(h4("Carousel with controls"))
        )),
        one(div(
            highlight(
                f"{imports}\n\n{c_indicators_only}",
                language="python",
                class_=join(col(md=8), offset(md=2), padding(bottom=5))
            ),
            carousels.item_caption(h4("Carousel with indicators"))
        )),
        one(div(
            highlight(
                f"{imports}\n\n{c_full}",
                language="python",
                class_=join(col(md=8), offset(md=2), padding(bottom=5))
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
            highlight(
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
                ')',
                language="python"
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
            cards.title.h4(b_button.link(ttl), **collapses.button_args_for(f"{acc_id}-{ttl}")),
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
        dropdowns.menu_header.h4("Group 1"),
        dropdowns.menu_item("Action 1"),
        dropdowns.menu_item("Action 2"),
        dropdowns.menu_divider(),
        dropdowns.menu_header.h4("Group 2"),
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
        highlight(
            'from markyp_html.text import h1, p\n\n'
            'from markyp_bootstrap4.jumbotrons import jumbotron\n\n'
            'jumbotron(\n'
            '    h1("Jumbotron"),\n'
            '    p("With a lengthy description...")\n'
            ')',
            language="python"
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

page = webpage(
    container(
        one(
            h1(
                "Building web pages with", em("Python"), ",",
                a(code("markyp"), href="https://github.com/volfpeter/markyp"), ",",
                a(code("markyp-html"), href="https://github.com/volfpeter/markyp-html"), ", and",
                a(code("markyp-bootstrap4"), href="https://github.com/volfpeter/markyp-bootstrap4")
            ),
            md=12
        ),
        section_header("Alerts and badges"),
        one(get_alert(), md=12),
        one(get_dismissable_alert(), md=12),
        section_header("Breadcrumbs"),
        one(get_breadcrumb(), md=12),
        one(get_breadcrumb_code(), md=12),
        section_header("Buttons"),
        subsection_header("Buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"),
        get_buttons(),
        hr(),
        get_buttons_small(),
        hr(),
        get_buttons_large(),
        hr(),
        get_buttons_disabled(),
        hr(),
        get_buttons_block(),
        subsection_header("Outline buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"),
        get_outline_buttons(),
        hr(),
        get_outline_buttons_small(),
        hr(),
        get_outline_buttons_large(),
        hr(),
        get_outline_buttons_disabled(),
        hr(),
        get_outline_buttons_block(),
        subsection_header("Toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"),
        get_toggle_buttons(),
        hr(),
        get_toggle_buttons_small(),
        hr(),
        get_toggle_buttons_large(),
        hr(),
        get_toggle_buttons_disabled(),
        hr(),
        get_toggle_buttons_block(),
        subsection_header("Outline toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"),
        get_outline_toggle_buttons(),
        hr(),
        get_outline_toggle_buttons_small(),
        hr(),
        get_outline_toggle_buttons_large(),
        hr(),
        get_outline_toggle_buttons_disabled(),
        hr(),
        get_outline_toggle_buttons_block(),
        section_header("Cards"),
        three(
            get_card_left(), get_card_center(), get_card_right(),
            md=(4, 4, 4)
        ),
        section_header("Carousels"),
        one(get_carousel(), md=12),
        section_header("Collapses"),
        subsection_header("Collapse with multiple toggle buttons"),
        one(get_collapse(), md=12),
        subsection_header("Accordion"),
        one(get_accordion(), md=12),
        section_header("Dropdowns"),
        row(*get_dropdown(), class_=col(md=12)),
        section_header("Forms"),
        subsection_header("Multiline login form"),
        one(get_multiline_login_form(), md=10, class_=offset(md=1)),
        subsection_header("Grid login form"),
        one(get_grid_login_form(), md=10, class_=offset(md=1)),
        subsection_header("Inline login form"),
        one(get_inline_login_form(), md=10, class_=offset(md=1)),
        section_header("Input groups"),
        row(*get_input_groups(), class_=col(md=12)),
        section_header("Jumbotrons"),
        one(get_jumbotron(), md=12),
        class_=padding(y=5)
    ),
    page_title="markyp-bootstrap4 demo page",
    head_elements=[
        req.bootstrap_css,
        *req.all_js,
        hlthemes.github,
    ],
    metadata=[
        meta.author("Website Author"),
        meta.charset("UTF-8"),
        meta.description("markyp-bootstrap4 demo"),
        meta.keywords("markyp-html,markyp-bootstrap4,markup,Python,HTML,Bootstrap"),
        meta.viewport("width=device-width, initial-scale=1.0")
    ],
    javascript=[
        *hljs.js
    ],
    class_=join(bg.dark, text.light)
)


# Get the actual HTML markup.
html = str(page)  # or page.markup
print(html)
