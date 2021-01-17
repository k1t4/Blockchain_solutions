from django import template
register = template.Library()

@register.filter(name="my_filter_name")
def mod(value, arg):
    return value % arg

register.filter('mod', mod)
