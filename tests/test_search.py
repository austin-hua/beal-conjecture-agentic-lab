from beal_lab import Solution, search


def test_solution_properties() -> None:
    solution = Solution(2, 3, 3, 3, 1, 4)
    assert solution.equation_holds is False
    assert solution.pairwise_coprime is True


def test_search_rejects_invalid_bounds() -> None:
    try:
        search(max_base=1)
    except ValueError as error:
        assert "max_base" in str(error)
    else:
        raise AssertionError("expected ValueError")


def test_small_search_has_no_primitive_solution() -> None:
    assert search(max_base=20, max_exponent=5) == []
