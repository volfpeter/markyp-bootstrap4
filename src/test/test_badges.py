from markyp.elements import Element
from markyp_bootstrap4.badges import BadgeFactory, a_badge, span_badge

def test_BadgeFactory():
    class e(Element):
        __slots__ = ()

        @property
        def inline_children(self) -> bool:
            return True

    e_badge = BadgeFactory(e)

    assert e_badge.primary("value").markup ==\
        '<e class="badge badge-primary">value</e>'
    assert e_badge.primary("value", class_="my-badge").markup ==\
        '<e class="badge badge-primary my-badge">value</e>'
    assert e_badge.primary("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-primary my-badge">value</e>'
    assert e_badge.primary_pill("value").markup ==\
        '<e class="badge badge-pill badge-primary">value</e>'
    assert e_badge.primary_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-primary my-badge">value</e>'
    assert e_badge.primary_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-primary my-badge">value</e>'

    assert e_badge.secondary("value").markup ==\
        '<e class="badge badge-secondary">value</e>'
    assert e_badge.secondary("value", class_="my-badge").markup ==\
        '<e class="badge badge-secondary my-badge">value</e>'
    assert e_badge.secondary("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-secondary my-badge">value</e>'
    assert e_badge.secondary_pill("value").markup ==\
        '<e class="badge badge-pill badge-secondary">value</e>'
    assert e_badge.secondary_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-secondary my-badge">value</e>'
    assert e_badge.secondary_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-secondary my-badge">value</e>'

    assert e_badge.success("value").markup ==\
        '<e class="badge badge-success">value</e>'
    assert e_badge.success("value", class_="my-badge").markup ==\
        '<e class="badge badge-success my-badge">value</e>'
    assert e_badge.success("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-success my-badge">value</e>'
    assert e_badge.success_pill("value").markup ==\
        '<e class="badge badge-pill badge-success">value</e>'
    assert e_badge.success_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-success my-badge">value</e>'
    assert e_badge.success_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-success my-badge">value</e>'

    assert e_badge.danger("value").markup ==\
        '<e class="badge badge-danger">value</e>'
    assert e_badge.danger("value", class_="my-badge").markup ==\
        '<e class="badge badge-danger my-badge">value</e>'
    assert e_badge.danger("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-danger my-badge">value</e>'
    assert e_badge.danger_pill("value").markup ==\
        '<e class="badge badge-pill badge-danger">value</e>'
    assert e_badge.danger_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-danger my-badge">value</e>'
    assert e_badge.danger_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-danger my-badge">value</e>'

    assert e_badge.warning("value").markup ==\
        '<e class="badge badge-warning">value</e>'
    assert e_badge.warning("value", class_="my-badge").markup ==\
        '<e class="badge badge-warning my-badge">value</e>'
    assert e_badge.warning("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-warning my-badge">value</e>'
    assert e_badge.warning_pill("value").markup ==\
        '<e class="badge badge-pill badge-warning">value</e>'
    assert e_badge.warning_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-warning my-badge">value</e>'
    assert e_badge.warning_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-warning my-badge">value</e>'

    assert e_badge.info("value").markup ==\
        '<e class="badge badge-info">value</e>'
    assert e_badge.info("value", class_="my-badge").markup ==\
        '<e class="badge badge-info my-badge">value</e>'
    assert e_badge.info("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-info my-badge">value</e>'
    assert e_badge.info_pill("value").markup ==\
        '<e class="badge badge-pill badge-info">value</e>'
    assert e_badge.info_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-info my-badge">value</e>'
    assert e_badge.info_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-info my-badge">value</e>'

    assert e_badge.light("value").markup ==\
        '<e class="badge badge-light">value</e>'
    assert e_badge.light("value", class_="my-badge").markup ==\
        '<e class="badge badge-light my-badge">value</e>'
    assert e_badge.light("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-light my-badge">value</e>'
    assert e_badge.light_pill("value").markup ==\
        '<e class="badge badge-pill badge-light">value</e>'
    assert e_badge.light_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-light my-badge">value</e>'
    assert e_badge.light_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-light my-badge">value</e>'

    assert e_badge.dark("value").markup ==\
        '<e class="badge badge-dark">value</e>'
    assert e_badge.dark("value", class_="my-badge").markup ==\
        '<e class="badge badge-dark my-badge">value</e>'
    assert e_badge.dark("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-dark my-badge">value</e>'
    assert e_badge.dark_pill("value").markup ==\
        '<e class="badge badge-pill badge-dark">value</e>'
    assert e_badge.dark_pill("value", class_="my-badge").markup ==\
        '<e class="badge badge-pill badge-dark my-badge">value</e>'
    assert e_badge.dark_pill("value", class_="my-badge", attr=42).markup ==\
        '<e attr="42" class="badge badge-pill badge-dark my-badge">value</e>'

def test_a_badge():
    assert a_badge.primary("value").markup ==\
        '<a class="badge badge-primary">value</a>'
    assert a_badge.primary("value", class_="my-badge").markup ==\
        '<a class="badge badge-primary my-badge">value</a>'
    assert a_badge.primary("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-primary my-badge">value</a>'
    assert a_badge.primary_pill("value").markup ==\
        '<a class="badge badge-pill badge-primary">value</a>'
    assert a_badge.primary_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-primary my-badge">value</a>'
    assert a_badge.primary_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-primary my-badge">value</a>'

    assert a_badge.secondary("value").markup ==\
        '<a class="badge badge-secondary">value</a>'
    assert a_badge.secondary("value", class_="my-badge").markup ==\
        '<a class="badge badge-secondary my-badge">value</a>'
    assert a_badge.secondary("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-secondary my-badge">value</a>'
    assert a_badge.secondary_pill("value").markup ==\
        '<a class="badge badge-pill badge-secondary">value</a>'
    assert a_badge.secondary_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-secondary my-badge">value</a>'
    assert a_badge.secondary_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-secondary my-badge">value</a>'

    assert a_badge.success("value").markup ==\
        '<a class="badge badge-success">value</a>'
    assert a_badge.success("value", class_="my-badge").markup ==\
        '<a class="badge badge-success my-badge">value</a>'
    assert a_badge.success("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-success my-badge">value</a>'
    assert a_badge.success_pill("value").markup ==\
        '<a class="badge badge-pill badge-success">value</a>'
    assert a_badge.success_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-success my-badge">value</a>'
    assert a_badge.success_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-success my-badge">value</a>'

    assert a_badge.danger("value").markup ==\
        '<a class="badge badge-danger">value</a>'
    assert a_badge.danger("value", class_="my-badge").markup ==\
        '<a class="badge badge-danger my-badge">value</a>'
    assert a_badge.danger("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-danger my-badge">value</a>'
    assert a_badge.danger_pill("value").markup ==\
        '<a class="badge badge-pill badge-danger">value</a>'
    assert a_badge.danger_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-danger my-badge">value</a>'
    assert a_badge.danger_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-danger my-badge">value</a>'

    assert a_badge.warning("value").markup ==\
        '<a class="badge badge-warning">value</a>'
    assert a_badge.warning("value", class_="my-badge").markup ==\
        '<a class="badge badge-warning my-badge">value</a>'
    assert a_badge.warning("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-warning my-badge">value</a>'
    assert a_badge.warning_pill("value").markup ==\
        '<a class="badge badge-pill badge-warning">value</a>'
    assert a_badge.warning_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-warning my-badge">value</a>'
    assert a_badge.warning_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-warning my-badge">value</a>'

    assert a_badge.info("value").markup ==\
        '<a class="badge badge-info">value</a>'
    assert a_badge.info("value", class_="my-badge").markup ==\
        '<a class="badge badge-info my-badge">value</a>'
    assert a_badge.info("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-info my-badge">value</a>'
    assert a_badge.info_pill("value").markup ==\
        '<a class="badge badge-pill badge-info">value</a>'
    assert a_badge.info_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-info my-badge">value</a>'
    assert a_badge.info_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-info my-badge">value</a>'

    assert a_badge.light("value").markup ==\
        '<a class="badge badge-light">value</a>'
    assert a_badge.light("value", class_="my-badge").markup ==\
        '<a class="badge badge-light my-badge">value</a>'
    assert a_badge.light("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-light my-badge">value</a>'
    assert a_badge.light_pill("value").markup ==\
        '<a class="badge badge-pill badge-light">value</a>'
    assert a_badge.light_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-light my-badge">value</a>'
    assert a_badge.light_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-light my-badge">value</a>'

    assert a_badge.dark("value").markup ==\
        '<a class="badge badge-dark">value</a>'
    assert a_badge.dark("value", class_="my-badge").markup ==\
        '<a class="badge badge-dark my-badge">value</a>'
    assert a_badge.dark("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-dark my-badge">value</a>'
    assert a_badge.dark_pill("value").markup ==\
        '<a class="badge badge-pill badge-dark">value</a>'
    assert a_badge.dark_pill("value", class_="my-badge").markup ==\
        '<a class="badge badge-pill badge-dark my-badge">value</a>'
    assert a_badge.dark_pill("value", class_="my-badge", href="#").markup ==\
        '<a href="#" class="badge badge-pill badge-dark my-badge">value</a>'

def test_span_badge():
    assert span_badge.primary("value").markup ==\
        '<span class="badge badge-primary">value</span>'
    assert span_badge.primary("value", class_="my-badge").markup ==\
        '<span class="badge badge-primary my-badge">value</span>'
    assert span_badge.primary("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-primary my-badge">value</span>'
    assert span_badge.primary_pill("value").markup ==\
        '<span class="badge badge-pill badge-primary">value</span>'
    assert span_badge.primary_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-primary my-badge">value</span>'
    assert span_badge.primary_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-primary my-badge">value</span>'

    assert span_badge.secondary("value").markup ==\
        '<span class="badge badge-secondary">value</span>'
    assert span_badge.secondary("value", class_="my-badge").markup ==\
        '<span class="badge badge-secondary my-badge">value</span>'
    assert span_badge.secondary("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-secondary my-badge">value</span>'
    assert span_badge.secondary_pill("value").markup ==\
        '<span class="badge badge-pill badge-secondary">value</span>'
    assert span_badge.secondary_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-secondary my-badge">value</span>'
    assert span_badge.secondary_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-secondary my-badge">value</span>'

    assert span_badge.success("value").markup ==\
        '<span class="badge badge-success">value</span>'
    assert span_badge.success("value", class_="my-badge").markup ==\
        '<span class="badge badge-success my-badge">value</span>'
    assert span_badge.success("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-success my-badge">value</span>'
    assert span_badge.success_pill("value").markup ==\
        '<span class="badge badge-pill badge-success">value</span>'
    assert span_badge.success_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-success my-badge">value</span>'
    assert span_badge.success_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-success my-badge">value</span>'

    assert span_badge.danger("value").markup ==\
        '<span class="badge badge-danger">value</span>'
    assert span_badge.danger("value", class_="my-badge").markup ==\
        '<span class="badge badge-danger my-badge">value</span>'
    assert span_badge.danger("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-danger my-badge">value</span>'
    assert span_badge.danger_pill("value").markup ==\
        '<span class="badge badge-pill badge-danger">value</span>'
    assert span_badge.danger_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-danger my-badge">value</span>'
    assert span_badge.danger_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-danger my-badge">value</span>'

    assert span_badge.warning("value").markup ==\
        '<span class="badge badge-warning">value</span>'
    assert span_badge.warning("value", class_="my-badge").markup ==\
        '<span class="badge badge-warning my-badge">value</span>'
    assert span_badge.warning("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-warning my-badge">value</span>'
    assert span_badge.warning_pill("value").markup ==\
        '<span class="badge badge-pill badge-warning">value</span>'
    assert span_badge.warning_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-warning my-badge">value</span>'
    assert span_badge.warning_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-warning my-badge">value</span>'

    assert span_badge.info("value").markup ==\
        '<span class="badge badge-info">value</span>'
    assert span_badge.info("value", class_="my-badge").markup ==\
        '<span class="badge badge-info my-badge">value</span>'
    assert span_badge.info("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-info my-badge">value</span>'
    assert span_badge.info_pill("value").markup ==\
        '<span class="badge badge-pill badge-info">value</span>'
    assert span_badge.info_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-info my-badge">value</span>'
    assert span_badge.info_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-info my-badge">value</span>'

    assert span_badge.light("value").markup ==\
        '<span class="badge badge-light">value</span>'
    assert span_badge.light("value", class_="my-badge").markup ==\
        '<span class="badge badge-light my-badge">value</span>'
    assert span_badge.light("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-light my-badge">value</span>'
    assert span_badge.light_pill("value").markup ==\
        '<span class="badge badge-pill badge-light">value</span>'
    assert span_badge.light_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-light my-badge">value</span>'
    assert span_badge.light_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-light my-badge">value</span>'

    assert span_badge.dark("value").markup ==\
        '<span class="badge badge-dark">value</span>'
    assert span_badge.dark("value", class_="my-badge").markup ==\
        '<span class="badge badge-dark my-badge">value</span>'
    assert span_badge.dark("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-dark my-badge">value</span>'
    assert span_badge.dark_pill("value").markup ==\
        '<span class="badge badge-pill badge-dark">value</span>'
    assert span_badge.dark_pill("value", class_="my-badge").markup ==\
        '<span class="badge badge-pill badge-dark my-badge">value</span>'
    assert span_badge.dark_pill("value", class_="my-badge", attr="something").markup ==\
        '<span attr="something" class="badge badge-pill badge-dark my-badge">value</span>'
