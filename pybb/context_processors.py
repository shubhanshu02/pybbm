# -*- coding: utf-8 -*-


from pybb import defaults

__author__ = "zeus"


def processor(request):
    context = {}
    for i in (
        "PYBB_TEMPLATE",
        "PYBB_TEMPLATE_MAIL_HTML",
        "PYBB_TEMPLATE_MAIL_TXT",
        "PYBB_DEFAULT_AVATAR_URL",
        "PYBB_MARKUP",
        "PYBB_DEFAULT_TITLE",
        "PYBB_ENABLE_ANONYMOUS_POST",
        "PYBB_ATTACHMENT_ENABLE",  # deprecated, should be used pybb_may_attach_files filter, will be removed
        "PYBB_AVATAR_WIDTH",
        "PYBB_AVATAR_HEIGHT",
    ):
        context[i] = getattr(defaults, i, None)
    context["PYBB_AVATAR_DIMENSIONS"] = "%sx%s" % (
        defaults.PYBB_AVATAR_WIDTH,
        defaults.PYBB_AVATAR_WIDTH,
    )
    return context
