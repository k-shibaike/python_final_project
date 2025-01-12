# inventory/inventory_manager.py
try:
    # パッケージとして実行される場合（main.pyから）
    from . import product
except ImportError:
    # 直接実行される場合
    import product


def all_stock_info():
    for product_info in product.products:
        print(product_info.name, product_info.stock)


def add_stock(id, quantity):
    for product_info in product.products:
        # try:
        if product_info.id == id:
            product_info.stock += quantity
            break
    else:
        print("商品IDがありません")
        # except Exception as e:


if __name__ == "__main__":
    all_stock_info()
