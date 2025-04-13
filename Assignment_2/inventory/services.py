from .models import Item, Purchase, Sell

class ItemService:
    @staticmethod
    def create_item(code, name, unit, description):
        item = Item(code=code, name=name, unit=unit, description=description)
        item.save()
        return item

    @staticmethod
    def update_item(code, **kwargs):
        item = Item.objects.get(code=code)
        for key, value in kwargs.items():
            setattr(item, key, value)
        item.save()
        return item

    @staticmethod
    def delete_item(code):
        item = Item.objects.get(code=code)
        item.is_deleted = True
        item.save()

class PurchaseService:
    @staticmethod
    def create_purchase(code, date, description):
        purchase = Purchase(code=code, date=date, description=description)
        purchase.save()
        return purchase

class SellService:
    @staticmethod
    def create_sell(code, date, description):
        sell = Sell(code=code, date=date, description=description)
        sell.save()
        return sell