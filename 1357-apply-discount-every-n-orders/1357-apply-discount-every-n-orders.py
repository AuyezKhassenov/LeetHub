class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.product_price = dict(zip(products, prices))
        self.n = n
        self.cnt_cust = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(len(product)):
            total += self.product_price[product[i]] * amount[i]
        self.cnt_cust += 1
        if not self.cnt_cust % self.n:
            total = total * ((100 - self.discount) / 100)
        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)