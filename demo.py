from markyp_bootstrap4 import cards
from markyp_bootstrap4 import req
from markyp_bootstrap4.alerts import alert, dismissable
from markyp_bootstrap4.badges import span_badge
from markyp_bootstrap4.breadcrumbs import breadcrumb
from markyp_bootstrap4.buttons import a_button, a_toggle,\
                                      b_button, b_toggle,\
                                      i_button, i_toggle,\
                                      l_button, l_toggle,\
                                      ButtonStyle
from markyp_bootstrap4.colors import bg, text
from markyp_bootstrap4.layout import container, row, row_item, one, two, three, col

from markyp_highlightjs import highlight, js as hljs, themes as hlthemes

from markyp_html import meta, style, join, webpage
from markyp_html.block import div, hr, pre
from markyp_html.inline import a, code, em, strong
from markyp_html.text import h1, h2, h3, p

def get_alert():
    return alert.primary(
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
    return dismissable.danger(
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
        "Active:",
        l_button.primary("Primary", active=True),
        l_button.secondary("Secondary", active=True),
        l_button.success("Success", active=True),
        l_button.danger("Danger", active=True),
        l_button.warning("Warning", active=True),
        l_button.info("Info", active=True),
        l_button.light("Light", active=True),
        l_button.dark("Dark", active=True),
        l_button.link("Link", active=True),
        class_=col(md=12)
    )

def get_buttons_large():
    return row(
        "Large:",
        b_button.primary("Primary", class_=ButtonStyle.LARGE),
        b_button.secondary("Secondary", class_=ButtonStyle.LARGE),
        b_button.success("Success", class_=ButtonStyle.LARGE),
        b_button.danger("Danger", class_=ButtonStyle.LARGE),
        b_button.warning("Warning", class_=ButtonStyle.LARGE),
        b_button.info("Info", class_=ButtonStyle.LARGE),
        b_button.light("Light", class_=ButtonStyle.LARGE),
        b_button.dark("Dark", class_=ButtonStyle.LARGE),
        b_button.link("Link", class_=ButtonStyle.LARGE),
        class_=col(md=12)
    )

def get_buttons_small():
    return row(
        "Small:",
        i_button.primary("Primary", class_=ButtonStyle.SMALL),
        i_button.secondary("Secondary", class_=ButtonStyle.SMALL),
        i_button.success("Success", class_=ButtonStyle.SMALL),
        i_button.danger("Danger", class_=ButtonStyle.SMALL),
        i_button.warning("Warning", class_=ButtonStyle.SMALL),
        i_button.info("Info", class_=ButtonStyle.SMALL),
        i_button.light("Light", class_=ButtonStyle.SMALL),
        i_button.dark("Dark", class_=ButtonStyle.SMALL),
        i_button.link("Link", class_=ButtonStyle.SMALL),
        class_=col(md=12)
    )

def get_buttons_disabled():
    return row(
        "Disabled:",
        b_button.primary("Primary", disabled=True),
        b_button.secondary("Secondary", disabled=True),
        b_button.success("Success", disabled=True),
        b_button.danger("Danger", disabled=True),
        b_button.warning("Warning", disabled=True),
        b_button.info("Info", disabled=True),
        b_button.light("Light", disabled=True),
        b_button.dark("Dark", disabled=True),
        b_button.link("Link", disabled=True),
        class_=col(md=12)
    )

def get_buttons_block():
    return row(
        "Block:",
        a_button.primary("Primary", class_=ButtonStyle.BLOCK),
        a_button.secondary("Secondary", class_=ButtonStyle.BLOCK),
        a_button.success("Success", class_=ButtonStyle.BLOCK),
        a_button.danger("Danger", class_=ButtonStyle.BLOCK),
        a_button.warning("Warning", class_=ButtonStyle.BLOCK),
        a_button.info("Info", class_=ButtonStyle.BLOCK),
        a_button.light("Light", class_=ButtonStyle.BLOCK),
        a_button.dark("Dark", class_=ButtonStyle.BLOCK),
        a_button.link("Link", class_=ButtonStyle.BLOCK),
        class_=col(md=12)
    )

def get_outline_buttons():
    return row(
        "Active:",
        l_button.primary_outline("Primary", active=True),
        l_button.secondary_outline("Secondary", active=True),
        l_button.success_outline("Success", active=True),
        l_button.danger_outline("Danger", active=True),
        l_button.warning_outline("Warning", active=True),
        l_button.info_outline("Info", active=True),
        l_button.light_outline("Light", active=True),
        l_button.dark_outline("Dark", active=True),
        l_button.link_outline("Link", active=True),
        class_=col(md=12)
    )

def get_outline_buttons_large():
    return row(
        "Large:",
        b_button.primary_outline("Primary", class_=ButtonStyle.LARGE),
        b_button.secondary_outline("Secondary", class_=ButtonStyle.LARGE),
        b_button.success_outline("Success", class_=ButtonStyle.LARGE),
        b_button.danger_outline("Danger", class_=ButtonStyle.LARGE),
        b_button.warning_outline("Warning", class_=ButtonStyle.LARGE),
        b_button.info_outline("Info", class_=ButtonStyle.LARGE),
        b_button.light_outline("Light", class_=ButtonStyle.LARGE),
        b_button.dark_outline("Dark", class_=ButtonStyle.LARGE),
        b_button.link_outline("Link", class_=ButtonStyle.LARGE),
        class_=col(md=12)
    )

def get_outline_buttons_small():
    return row(
        "Small:",
        i_button.primary_outline("Primary", class_=ButtonStyle.SMALL),
        i_button.secondary_outline("Secondary", class_=ButtonStyle.SMALL),
        i_button.success_outline("Success", class_=ButtonStyle.SMALL),
        i_button.danger_outline("Danger", class_=ButtonStyle.SMALL),
        i_button.warning_outline("Warning", class_=ButtonStyle.SMALL),
        i_button.info_outline("Info", class_=ButtonStyle.SMALL),
        i_button.light_outline("Light", class_=ButtonStyle.SMALL),
        i_button.dark_outline("Dark", class_=ButtonStyle.SMALL),
        i_button.link_outline("Link", class_=ButtonStyle.SMALL),
        class_=col(md=12)
    )

def get_outline_buttons_disabled():
    return row(
        "Disabled:",
        b_button.primary_outline("Primary", disabled=True),
        b_button.secondary_outline("Secondary", disabled=True),
        b_button.success_outline("Success", disabled=True),
        b_button.danger_outline("Danger", disabled=True),
        b_button.warning_outline("Warning", disabled=True),
        b_button.info_outline("Info", disabled=True),
        b_button.light_outline("Light", disabled=True),
        b_button.dark_outline("Dark", disabled=True),
        b_button.link_outline("Link", disabled=True),
        class_=col(md=12)
    )

def get_outline_buttons_block():
    return row(
        "Block:",
        a_button.primary_outline("Primary", class_=ButtonStyle.BLOCK),
        a_button.secondary_outline("Secondary", class_=ButtonStyle.BLOCK),
        a_button.success_outline("Success", class_=ButtonStyle.BLOCK),
        a_button.danger_outline("Danger", class_=ButtonStyle.BLOCK),
        a_button.warning_outline("Warning", class_=ButtonStyle.BLOCK),
        a_button.info_outline("Info", class_=ButtonStyle.BLOCK),
        a_button.light_outline("Light", class_=ButtonStyle.BLOCK),
        a_button.dark_outline("Dark", class_=ButtonStyle.BLOCK),
        a_button.link_outline("Link", class_=ButtonStyle.BLOCK),
        class_=col(md=12)
    )

def get_toggle_buttons():
    return row(
        "Active:",
        l_toggle.primary("Primary", active=True),
        l_toggle.secondary("Secondary", active=True),
        l_toggle.success("Success", active=True),
        l_toggle.danger("Danger", active=True),
        l_toggle.warning("Warning", active=True),
        l_toggle.info("Info", active=True),
        l_toggle.light("Light", active=True),
        l_toggle.dark("Dark", active=True),
        l_toggle.link("Link", active=True),
        class_=col(md=12)
    )

def get_toggle_buttons_large():
    return row(
        "Large:",
        b_toggle.primary("Primary", class_=ButtonStyle.LARGE),
        b_toggle.secondary("Secondary", class_=ButtonStyle.LARGE),
        b_toggle.success("Success", class_=ButtonStyle.LARGE),
        b_toggle.danger("Danger", class_=ButtonStyle.LARGE),
        b_toggle.warning("Warning", class_=ButtonStyle.LARGE),
        b_toggle.info("Info", class_=ButtonStyle.LARGE),
        b_toggle.light("Light", class_=ButtonStyle.LARGE),
        b_toggle.dark("Dark", class_=ButtonStyle.LARGE),
        b_toggle.link("Link", class_=ButtonStyle.LARGE),
        class_=col(md=12)
    )

def get_toggle_buttons_small():
    return row(
        "Small:",
        i_toggle.primary("Primary", class_=ButtonStyle.SMALL),
        i_toggle.secondary("Secondary", class_=ButtonStyle.SMALL),
        i_toggle.success("Success", class_=ButtonStyle.SMALL),
        i_toggle.danger("Danger", class_=ButtonStyle.SMALL),
        i_toggle.warning("Warning", class_=ButtonStyle.SMALL),
        i_toggle.info("Info", class_=ButtonStyle.SMALL),
        i_toggle.light("Light", class_=ButtonStyle.SMALL),
        i_toggle.dark("Dark", class_=ButtonStyle.SMALL),
        i_toggle.link("Link", class_=ButtonStyle.SMALL),
        class_=col(md=12)
    )

def get_toggle_buttons_disabled():
    return row(
        "Disabled:",
        b_toggle.primary("Primary", disabled=True),
        b_toggle.secondary("Secondary", disabled=True),
        b_toggle.success("Success", disabled=True),
        b_toggle.danger("Danger", disabled=True),
        b_toggle.warning("Warning", disabled=True),
        b_toggle.info("Info", disabled=True),
        b_toggle.light("Light", disabled=True),
        b_toggle.dark("Dark", disabled=True),
        b_toggle.link("Link", disabled=True),
        class_=col(md=12)
    )

def get_toggle_buttons_block():
    return row(
        "Block:",
        a_toggle.primary("Primary", class_=ButtonStyle.BLOCK),
        a_toggle.secondary("Secondary", class_=ButtonStyle.BLOCK),
        a_toggle.success("Success", class_=ButtonStyle.BLOCK),
        a_toggle.danger("Danger", class_=ButtonStyle.BLOCK),
        a_toggle.warning("Warning", class_=ButtonStyle.BLOCK),
        a_toggle.info("Info", class_=ButtonStyle.BLOCK),
        a_toggle.light("Light", class_=ButtonStyle.BLOCK),
        a_toggle.dark("Dark", class_=ButtonStyle.BLOCK),
        a_toggle.link("Link", class_=ButtonStyle.BLOCK),
        class_=col(md=12)
    )

def get_outline_toggle_buttons():
    return row(
        "Active:",
        l_toggle.primary_outline("Primary", active=True),
        l_toggle.secondary_outline("Secondary", active=True),
        l_toggle.success_outline("Success", active=True),
        l_toggle.danger_outline("Danger", active=True),
        l_toggle.warning_outline("Warning", active=True),
        l_toggle.info_outline("Info", active=True),
        l_toggle.light_outline("Light", active=True),
        l_toggle.dark_outline("Dark", active=True),
        l_toggle.link_outline("Link", active=True),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_large():
    return row(
        "Large:",
        b_toggle.primary_outline("Primary", class_=ButtonStyle.LARGE),
        b_toggle.secondary_outline("Secondary", class_=ButtonStyle.LARGE),
        b_toggle.success_outline("Success", class_=ButtonStyle.LARGE),
        b_toggle.danger_outline("Danger", class_=ButtonStyle.LARGE),
        b_toggle.warning_outline("Warning", class_=ButtonStyle.LARGE),
        b_toggle.info_outline("Info", class_=ButtonStyle.LARGE),
        b_toggle.light_outline("Light", class_=ButtonStyle.LARGE),
        b_toggle.dark_outline("Dark", class_=ButtonStyle.LARGE),
        b_toggle.link_outline("Link", class_=ButtonStyle.LARGE),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_small():
    return row(
        "Small:",
        i_toggle.primary_outline("Primary", class_=ButtonStyle.SMALL),
        i_toggle.secondary_outline("Secondary", class_=ButtonStyle.SMALL),
        i_toggle.success_outline("Success", class_=ButtonStyle.SMALL),
        i_toggle.danger_outline("Danger", class_=ButtonStyle.SMALL),
        i_toggle.warning_outline("Warning", class_=ButtonStyle.SMALL),
        i_toggle.info_outline("Info", class_=ButtonStyle.SMALL),
        i_toggle.light_outline("Light", class_=ButtonStyle.SMALL),
        i_toggle.dark_outline("Dark", class_=ButtonStyle.SMALL),
        i_toggle.link_outline("Link", class_=ButtonStyle.SMALL),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_disabled():
    return row(
        "Disabled:",
        b_toggle.primary_outline("Primary", disabled=True),
        b_toggle.secondary_outline("Secondary", disabled=True),
        b_toggle.success_outline("Success", disabled=True),
        b_toggle.danger_outline("Danger", disabled=True),
        b_toggle.warning_outline("Warning", disabled=True),
        b_toggle.info_outline("Info", disabled=True),
        b_toggle.light_outline("Light", disabled=True),
        b_toggle.dark_outline("Dark", disabled=True),
        b_toggle.link_outline("Link", disabled=True),
        class_=col(md=12)
    )

def get_outline_toggle_buttons_block():
    return row(
        "Block:",
        a_toggle.primary_outline("Primary", class_=ButtonStyle.BLOCK),
        a_toggle.secondary_outline("Secondary", class_=ButtonStyle.BLOCK),
        a_toggle.success_outline("Success", class_=ButtonStyle.BLOCK),
        a_toggle.danger_outline("Danger", class_=ButtonStyle.BLOCK),
        a_toggle.warning_outline("Warning", class_=ButtonStyle.BLOCK),
        a_toggle.info_outline("Info", class_=ButtonStyle.BLOCK),
        a_toggle.light_outline("Light", class_=ButtonStyle.BLOCK),
        a_toggle.dark_outline("Dark", class_=ButtonStyle.BLOCK),
        a_toggle.link_outline("Link", class_=ButtonStyle.BLOCK),
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
        class_=join(bg.light, text.dark, cards.TextAlign.LEFT)
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
        class_=join(bg.light, text.dark, cards.TextAlign.CENTER)
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
        class_=join(bg.light, text.dark, cards.TextAlign.RIGHT)
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
        one(h2("Alerts and badges", md=12)),
        one(get_alert(), md=12),
        one(get_dismissable_alert(), md=12),
        one(h2("Breadcrumbs", md=12)),
        one(get_breadcrumb(), md=12),
        one(get_breadcrumb_code(), md=12),
        one(h2("Buttons", md=12)),
        one(h3("Buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"), md=12),
        get_buttons(),
        hr(),
        get_buttons_small(),
        hr(),
        get_buttons_large(),
        hr(),
        get_buttons_disabled(),
        hr(),
        get_buttons_block(),
        one(h3("Outline buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"), md=12),
        get_outline_buttons(),
        hr(),
        get_outline_buttons_small(),
        hr(),
        get_outline_buttons_large(),
        hr(),
        get_outline_buttons_disabled(),
        hr(),
        get_outline_buttons_block(),
        one(h3("Toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"), ", and", code("<input>"), "elements"), md=12),
        get_toggle_buttons(),
        hr(),
        get_toggle_buttons_small(),
        hr(),
        get_toggle_buttons_large(),
        hr(),
        get_toggle_buttons_disabled(),
        hr(),
        get_toggle_buttons_block(),
        one(h3("Outline toggle buttons from", code("<a></a>"), ",", code("<button></button>"), ",", code("<label></label>"),  ", and", code("<input>"), "elements"), md=12),
        get_outline_toggle_buttons(),
        hr(),
        get_outline_toggle_buttons_small(),
        hr(),
        get_outline_toggle_buttons_large(),
        hr(),
        get_outline_toggle_buttons_disabled(),
        hr(),
        get_outline_toggle_buttons_block(),
        one(h2("Cards", md=12)),
        three(
            get_card_left(), get_card_center(), get_card_right(),
            md=(4, 4, 4)
        )
    ),
    page_title="markyp-bootstrap4 demo page",
    head_elements=[
        req.bootstrap_css,
        req.jquery,
        req.bootstrap_js,
        req.popper_js,
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
