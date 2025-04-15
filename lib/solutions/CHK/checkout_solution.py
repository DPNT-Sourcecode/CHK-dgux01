
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # assume string is just string of ABCs
        # Need to keep track of item: price
        # need to find out how many, maybe lookup in dictionary
        # Need to apply special discount, maybe % and //
        allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if not skus:
            return -1
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        count = dict()

        for sku in skus:
            if sku not in allowed:
                return -1
            count[sku] = count.get(sku, 0) + 1
        total = 0
        for item, freq in count.items():
            if freq == 0:
                continue
            if item == "A":
                multiples = freq // 3
                singles = freq % 3
                total += multiples * 130
                total += singles * 50
            elif item == "B":
                multiples = freq // 2
                singles = freq % 3
                total += multiples * 45
                total += singles * 30
            else:
                total += prices.get(item)
        return total

