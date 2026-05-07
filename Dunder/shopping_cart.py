class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Product {self.name} with price: ${self.price}"

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"


class Cart:
    def __init__(self) -> None:
        self.items: list[Product] = []

    def __str__(self) -> str:
        if not self.items:
            return "Your cart is empty!"

        item_string: list[str] = [f"- {str(item)}" for item in self.items]

        return "\n".join(item_string)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, key: int) -> Product:
        return self.items[key]

    def __contains__(self, item_name: str) -> bool:
        return any(p.name == item_name for p in self.items)

    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented

        new_cart = Cart()
        new_cart.items = self.items + other.items

        return new_cart

    def __iadd__(self, other):
        if isinstance(other, Product):
            self.items.append(other)
            return self

        raise ValueError("Can only add Product objects")

    def __call__(self, discount: float = 0) -> float:
        total = sum(p.price for p in self.items)

        return total * (1 - discount)

    def __bool__(self) -> bool:
        return bool(self.items)


product1 = Product(name="Gaming Laptop", price=1499.99)
product2 = Product(name="Smartphone", price=599.99)
product3 = Product(name="Console", price=899.99)

cart1 = Cart()
cart2 = Cart()

cart1 += product1
cart1 += product2
cart2 += product3

print(f"Cart 1: \n{cart1}\n")
print(f"Cart 2: \n{cart2}\n")

new_cart = cart1 + cart2
print(f"New Cart: \n{new_cart}")

discount = new_cart(discount=0.5)
print(f"{discount:.2f}")
