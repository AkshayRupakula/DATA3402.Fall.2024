create_new_args = lambda args: [a if isinstance(a, list) and len(a) == max_len else [a] * max_len if not isinstance(a, list) else print("Error: all list arguments must have same length.") or exit() for a in args]
