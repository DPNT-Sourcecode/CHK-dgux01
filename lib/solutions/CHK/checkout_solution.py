
class CheckoutSolution:

    # skus = unicode string
    # If more products, might need to make a super process, then do case match
    def checkout(self, skus):
        def process_A(num_of_a):
            multiples_5 = num_of_a // 5
            remainder_of_5 = num_of_a % 5
            multiples_3 = remainder_of_5 // 3
            remainder_of_3 = remainder_of_5 % 3

            return (multiples_5 * 200) + (multiples_3 * 130) + (remainder_of_3 * 50)

        def process_B(num_of_b):
            # What if number of B is less than 0
            if num_of_b < 1:
                return 0
            multiples_2 = num_of_b // 2
            remainder_of_2 = num_of_b % 2

            return (multiples_2 * 45) + (remainder_of_2 * 30)

        def process_E(num_of_e):
            num_free_b = num_of_e // 2
            return num_free_b, num_of_e * 40

        def process_C(num_of_c):
            return num_of_c * 20

        def process_D(num_of_d):
            return num_of_d * 15

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
        for p in products:
            if count.get(p) == 0:
                continue
            match p:
                case "E":
                    free_b, amount_e = process_E(count.get("E"))
                    count["B"] -= free_b
                    total += amount_e
                case "A":
                    amount_a = process_A(count.get("A"))
                    total += amount_a
                case "B":
                    amount_b = process_B(count.get("B"))
                    total += amount_b
                case "C":
                    amount_c = process_C(count.get("C"))
                    total += amount_c
                case "D":
                    amount_d = process_D(count.get("D"))
                    total += amount_d

        # can reduce amount of B instead in lookup
        return total
