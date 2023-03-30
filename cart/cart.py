from store.models import ShopeeItem
from decimal import Decimal


class Cart():

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, item, qty):
        itemid = str(item.itemid)
        stock = str(item.stock)
        st = int(qty)*int(item.price)
        if itemid in self.cart:
            nqty = self.cart[str(itemid)]['qty']+ int(qty)
            if nqty > int(stock):
                st = int(stock)*int(item.price)
                self.cart[itemid] = {'price':item.price,'qty':int(stock),'stock':stock,'subtotal':st}
            else:
                self.cart[itemid] = {'price':item.price,'qty':nqty,'stock':stock,'subtotal':st}
        else:
            self.cart[itemid] = {'price':item.price,'qty':qty,'stock':stock,'subtotal':st}
        self.save()
    
    def update(self, item, qty):
        itemid = str(item.itemid)
        stock = str(item.stock)
        nqty = int(qty)
        st = nqty*int(item.price)
        if itemid in self.cart:
            self.cart[itemid] = {'price':item.price,'qty':nqty,'stock':stock,'subtotal':st}
        else:
            self.cart[itemid] = {'price':item.price,'qty':nqty,'stock':stock,'subtotal':st}
        self.save()

    def __iter__(self):
        itemid = self.cart.keys()
        orditems = ShopeeItem.manager.filter(itemid__in=itemid)
        cart = self.cart.copy()
        
        for item in orditems:
            cart[str(item.itemid)]['product'] = item
        
        for i in cart.values():
            i['price'] = Decimal(i['price'])
            i['total_cost'] = i['price'] * i['qty']
            yield i

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def stock_check(self,itemid):
        return self.cart[str(itemid)]['qty']
    
    def cart_item_check(self, itemid):
        return str(itemid) in self.cart
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def delete(self, item):
        itemid = str(item)

        if itemid in self.cart:
            del self.cart[itemid]
            self.save()
            
    def clear(self):
        # Remove basket from session
        del self.session['skey']
        new_key = self.cart.pop()
        self.save()
        
    
    def save(self):
        self.session.modified = True