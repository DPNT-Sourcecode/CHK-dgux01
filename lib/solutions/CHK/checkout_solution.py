
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
        products = ["E", "A", "B", "C", "D"]

        free_b, amount_e = self.process_E(count.get("E"))
        amount_a = self.process_A(count.get("A"))
        amount_b = self.process_B(count.get("B") - free_b)
        amount_c = self.process_C(count.get("C"))
        amount_d = self.process_D(count.get("D"))

        total += sum(amount_a, amount_b, amount_c, amount_d, amount_e)
        return total
    # Probably need to process E's first, to determine number of B's

    def process_A(self, num_of_a):
        multiples_5 = num_of_a // 5
        remainder_of_5 = num_of_a % 5
        multiples_3 = remainder_of_5 // 3
        remainder_of_3 = remainder_of_5 % 3

        return (multiples_5 * 200) + (multiples_3 * 130) + (remainder_of_3 * 50)

    def process_B(self, num_of_b):
        # What if number of B is less than 0
        if num_of_b < 1:
            return 0
        multiples_2 = num_of_b // 2
        remainder_of_2 = num_of_b % 2

        return (multiples_2 * 45) + (remainder_of_2 * 30)

    def process_E(self, num_of_e):
        num_free_b = num_of_e // 2
        return num_free_b, num_of_e * 40

    def process_C(self, num_of_c):
        return num_of_c * 20

    def process_D(self, num_of_d):
        return num_of_d * 15


