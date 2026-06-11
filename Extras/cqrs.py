from typing import TypedDict


class OrderDict(TypedDict):
    order_id: int
    category: str
    amount: float


class OrderWriteStore:
    def __init__(self) -> None:
        self.orders: list[OrderDict] = []

    def save_order(self, order_id: int, category: str, amount: float) -> OrderDict:
        save_dict: OrderDict = {
            "order_id": order_id,
            "category": category,
            "amount": amount,
        }

        self.orders.append(save_dict)

        return save_dict


class DashboardReadStore:
    def __init__(self) -> None:
        self.cached_totals: dict[str, float] = {}

    def get_total_by_category(self, category: str) -> float:
        return self.cached_totals.get(category, 0.0)


def sync_projection(event: OrderDict, read_store: DashboardReadStore) -> None:
    category = event.get("category", "")
    amount = event.get("amount", 0.0)

    current_total = read_store.cached_totals.get(category, 0.0)
    read_store.cached_totals[category] = current_total + amount


if __name__ == "__main__":
    write_store = OrderWriteStore()
    read_store = DashboardReadStore()

    order_1 = write_store.save_order(order_id=1, category="electronics", amount=1.0)
    sync_projection(order_1, read_store)

    order_2 = write_store.save_order(order_id=2, category="appliances", amount=5.0)
    sync_projection(order_2, read_store)

    order_3 = write_store.save_order(order_id=3, category="electronics", amount=3.0)
    sync_projection(order_3, read_store)

    print(read_store.cached_totals)
