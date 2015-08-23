from django import template
from django.contrib.auth import get_user_model

register = template.Library()


@register.inclusion_tag("chatboxclient.html", takes_context=True)
def engage(context):
    return context


@register.inclusion_tag("chatboxadmin.html", takes_context=True)
def engageadmin(context):
    return context


@register.inclusion_tag("admin/engage_list_result.html")
def result_list_custom(cl):
    """
    Displays the headers and data list together
    """

    return {'users': get_user_model().objects.all()}
