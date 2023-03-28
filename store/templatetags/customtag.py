from django import template
register = template.Library()

@register.simple_tag()
def get_object_property_dinamically(cart, itemid):
    itemid= str(itemid)
    cartitem = cart.session.get('skey')
    if itemid in cartitem:
        return f"{cartitem[itemid]['qty']} in Cart"
    else:
        return ""
