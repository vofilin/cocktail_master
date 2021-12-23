from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.
    """
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    for k in [k for k, v in query.items() if not v]:
        del query[k]
    return query.urlencode()
