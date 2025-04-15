
class CheckoutSolution:

    # skus = unicode string
    # If more products, might need to make a super process, then do case match
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

        free_b, amount_e = self.process_E(count.get("E"))
        amount_a = self.process_A(count.get("A"))
        total += amount_e
    # Probably need to process E's first, to determine number of B's

    def process_A(self, num_of_a):
        multiples_5 = num_of_a // 5
        remainder_of_5 = num_of_a % 5
        multiples_3 = remainder_of_5 // 3
        remainder_of_3 = remainder_of_5 % 3

        return (multiples_5 * 200) + (multiples_3 * 130) + (remainder_of_3 * 50)

    def process_B(self, num_of_b):
        # Maybe process E here?
        multiples_2 = num_of_b // 2
        remainder_of_2 = num_of_b % 2

        return (multiples_2 * 45) + (remainder_of_2 * 30)

    def process_E(self, num_of_e):
        num_free_b = num_of_e // 2
        return num_free_b, num_of_e * 40




