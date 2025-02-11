
class Product:
    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume


class Warehouse:
    def __init__(self, kapacity: float):
        self.kapacity = kapacity
        self.products = []
        self.available_space = kapacity

    def add(self, product: Product):
        if product.volume > self.available_space:
            return -1
        else:
            self.products.append(product)
            self.available_space -= product.volume
            return self.available_space


if __name__ == "__main__":
    pass






