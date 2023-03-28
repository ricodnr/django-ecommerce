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
        if itemid in self.cart:
            nqty = self.cart[str(itemid)]['qty']+ int(qty)
            if nqty > int(stock):
                self.cart[itemid] = {'price':item.price,'qty':int(stock),'stock':stock}
            else:
                self.cart[itemid] = {'price':item.price,'qty':nqty,'stock':stock}
        else:
            self.cart[itemid] = {'price':item.price,'qty':qty,'stock':stock}
        self.save()
    
    def update(self, item, qty):
        itemid = str(item.itemid)
        stock = str(item.stock)
        nqty = int(qty)
        if itemid in self.cart:
            self.cart[itemid] = {'price':item.price,'qty':nqty,'stock':stock}
        else:
            self.cart[itemid] = {'price':item.price,'qty':int(qty),'stock':stock}
        self.save()

    def __iter__(self):
        itemid = self.cart.keys()
        orditems = ShopeeItem.manager.filter(itemid__in=itemid)
        cart = self.cart.copy()
        
        for item in orditems:
            cart[str(item.itemid)]['product'] = item
            sqty = cart[str(item.itemid)]['qty']
            stock = item.stock
            if sqty > stock : self.cart[str(item.itemid)]['status'] = "invalid"
            else: self.cart[str(item.itemid)]['status'] = "valid"
        
        for i in cart.values():
            i['price'] = Decimal(i['price'])
            i['total_cost'] = i['price'] * i['qty']
            yield i

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def stock_check(self,itemid):
        return self.cart[str(itemid)]['qty']
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def delete(self, item):
        itemid = str(item)
        print(itemid)
        if itemid in self.cart:
            del self.cart[itemid]
            self.save()
            
    
    def save(self):
        self.session.modified = True