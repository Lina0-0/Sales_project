class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price*self.quantity

def main():
    p = Product("Laptop", 1000, 3)
    print(p.total_value())

if __name__ == "__main__":
    main()