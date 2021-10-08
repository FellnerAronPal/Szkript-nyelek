import secret_logic

assert not secret_logic.is_numaric("asd"), "is_numaric with not numaric"
assert secret_logic.is_numaric("123"), "is_numaric with not numaric"

assert not secret_logic.is_supperd_operator("%"), "is_supperd_operator not supported operator"

assert secret_logic.calculate(1, '+', 6) == 7, "calculate + operator"
