from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_sum():
        assert (CheckoutSolution().checkout("AAAAA"), 230)
        assert (CheckoutSolution().checkout("BBB"), 75)
        assert (CheckoutSolution().checkout("CD"), 35)
        assert (CheckoutSolution().checkout(""), -1)
        assert (CheckoutSolution().checkout("123abc"), -1)
