
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # assume string is just string of ABCs
        # Need to keep track of item: price
        # need to find out how many, maybe lookup in dictionary
        # Need to apply special discount, maybe % and //
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        count = dict()

        for sku in skus:
            count[sku] = count.get(sku, 0) + 1


