
class CheckoutSolution:

    # skus = unicode string
    # If more products, might need to make a super process, then do case match
    def checkout(self, skus):
        # IDEA: have a cart
        allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total = 0
        if not skus:
            return total
        cart = [[], [], []]  # Freebies, Discounts, everything else
        count = dict()
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35,
                  "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
        # SKU -> [[num, price], [num, price]]
        special_discount = {"A": [[3, 150], [5, 200]], "B": [[2, 45]], "H": [
            [5, 45], [10, 80]], "K": [[2, 150]], "P": [[5, 200]], "Q": [[3, 80]], "V": [[2, 90], [3, 130]]}
        # SKU -> [[num, SKU]]
        special_freebie = {"E": [2, "B"], "F": [2, "F"], "N": [
            3, "M"], "R": [3, "Q"], "U": [3, "U"]}

        for sku in skus:
            if sku not in allowed:
                return -1
            count[sku] = count.get(sku, 0) + 1
            if sku in special_freebie:
                cart[0].append(sku)
            elif sku in special_discount:
                cart[1].append(sku)
            else:
                cart[2].append(sku)

        def process_normal_sku(regular_skus):
            total = 0
            for sku in regular_skus:
                # Need to multiply regular sku freq with price, for each sku
                pass

        def process_discounts(discounts):
            total = 0
            for sku in discounts:
                amount_in_cart = count.get(sku, 0)

                for amount_for_deal, bargain_price in special_discount.get(sku):
                    multiples = amount_in_cart // amount_for_deal
                    amount_in_cart %= amount_for_deal
                    total += (multiples * bargain_price)
                    # List of skus with freebies
                total += amount_in_cart * prices.get(sku, 0)
            return total

        def process_freebies(freebies):
            # Process all the freebie skus to reduce count (acts as cart tracker)
            total = 0
            for sku in freebies:
                num_required_to_buy, free_sku = special_freebie.get(sku)
                multiples = count.get(sku, 0) // num_required_to_buy
                count[free_sku] -= count.get(free_sku, 0) - multiples
                total += count.get(sku, 0) * prices.get(sku, 0)
            return total

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

        def process_F(num_of_f):
            multiples_3 = num_of_f // 3
            return (num_of_f - multiples_3) * 10

        freebies_total = process_freebies(cart[0])
        discounts_total = process_discounts(cart[1])
        regular_total = process_normal_sku(cart[2])

        # can reduce amount of B instead in lookup
        return sum(freebies_total, discounts_total, regular_total)







