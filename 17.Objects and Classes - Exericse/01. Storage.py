class Storage:
    def __init__(self,capacity) -> None:
        self.storage = []
        self.capacity = int(capacity)

    def add_product(self,product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self) -> list:
        return self.storage


# Test class
storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())