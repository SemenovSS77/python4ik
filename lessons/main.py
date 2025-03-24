def countdown(n):
    def step():
        nonlocal n
        print(n if n > 0 else  "done")
        n -= 1
    return step

do_step = countdown(7)

