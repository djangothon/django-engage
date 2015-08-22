from django import template

register = template.Library()


@register.inclusion_tag("chatbox.html", takes_context=True)
def engage(context):
    request = context['request']
    return context
