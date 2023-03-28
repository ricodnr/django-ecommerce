import json
from pydantic import BaseModel
# store api
# https://shopee.vn/api/v4/shop/get_shop_base?entry_point=ShopByPDP&need_cancel_rate=true&request_source=shop_home_page&username=chukongngai&version=1
# item api
# https://shopee.vn/api/v4/shop/search_items?offset=0&limit=100&order=desc&filter_sold_out=3&use_case=1&sort_by=sales&order=sales&shopid=203699428
# class ShopeeItem(BaseModel):
#     itemid : str
#     shopid : int
#     name: str
#     currency : str
#     stock : int
#     sold: int
#     historical_sold: int
#     liked_count: int
#     brand: str
#     cmt_count: int
#     item_status: str
#     price: int
#     price_min: int
#     price_max: int
#     price_before_discount: int
#     show_discount: int
#     raw_discount: int
#     is_official_shop: bool
#     image: str
#     shop_location: str

with open("search_items.json", "r") as read_file:
    data = json.load(read_file)
# print(data["items"][0]["item_basic"]["images"][0])
js=[]
jsimage=[]
c=0
for i in data["items"]:
    jsdictitem={}
    fielddictitem={}
    ii = i["item_basic"]
    jsdictitem["model"] = "store.ShopeeItem"
    fielddictitem["itemid"] = ii["itemid"]
    fielddictitem["shopid"] = ii["shopid"]
    fielddictitem["name"] = ii["name"]
    fielddictitem["currency"] = ii["currency"]
    fielddictitem["stock"] = ii["stock"]
    fielddictitem["sold"] = ii["sold"]
    fielddictitem["historical_sold"] = ii["historical_sold"]
    fielddictitem["liked_count"] = ii["liked_count"]
    fielddictitem["brand"] = ii["brand"]
    fielddictitem["cmt_count"] = ii["cmt_count"]
    fielddictitem["item_status"] = ii["item_status"]
    fielddictitem["price"] = int(ii["price"]/100000)
    fielddictitem["price_min"] = int(ii["price_min"]/100000)
    fielddictitem["price_max"] = int(ii["price_max"]/100000)
    fielddictitem["price_before_discount"] = int(ii["price_before_discount"]/100000)
    fielddictitem["show_discount"] = ii["show_discount"]
    fielddictitem["raw_discount"] = ii["raw_discount"]
    fielddictitem["is_official_shop"] = ii["is_official_shop"]
    fielddictitem["avatar"] = ii["image"]
    fielddictitem["shop_location"] = ii["shop_location"]
    jsdictitem["fields"] = fielddictitem.copy()
    js.append(jsdictitem.copy())

    for img in ii["images"]:
        c+=1
        jsdictimage = {}
        fielddictimage = {}
        jsdictimage["model"] = "store.ItemImage"
        jsdictimage["pk"] = c
        fielddictimage["itemid"] = ii["itemid"]
        fielddictimage["image"] = img
        jsdictimage["fields"] = fielddictimage.copy()
        js.append(jsdictimage.copy())

    

# print(js[0]["fields"]["price"])
with open("shopeeitems.json","w") as w:
    json.dump(js,w,indent=4)