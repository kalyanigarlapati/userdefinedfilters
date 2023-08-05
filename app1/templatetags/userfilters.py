from django import template
register=template.Library()




@register.filter('swapping')
def swap(data):
    return data.swapcase()


@register.filter('remove')
def remove(data,arg):
    return data.replace(arg,'')




register.filter('swap',swap)
register.filter('remove',remove)