
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total = 0
        if not skus:
            return total
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        count = dict()

        for sku in skus:
            if sku not in allowed:
                return -1
            count[sku] = count.get(sku, 0) + 1

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
                singles = freq % 2
                total += multiples * 45
                total += singles * 30
            else:
                total += (prices.get(item) * freq)
        return total
    # Probably need to process E's first, to determine number of B's

    def process_A(self, num_of_a):
        multiples_5 = num_of_a // 5
        remainder_of_5 = num_of_a % 5
        multiples_3 = remainder_of_5 // 3
        remainder_of_3 = remainder_of_5 % 3

        return (multiples_5 * 200) + (multiples_3 * 130) + (remainder_of_3 * 50)

    def process_B(self, num_of_b):
        multiples_2 = num_of_b // 2
        remainder_of_2 = num_of_b % 2

        return (multiples_2 * 45)


