

def adder(initial):
    value = initial

    def add(delta):
        nonlocal value

        value += delta
        if hasattr(add, "max_value"):
            if value >= add.max_value:
                add.event_max(value)

        return add
    
    def max_(maxv, event):
        add.max_value = maxv
        add.event_max = event
        return add

    add.max = max_

    return add


def max_reached_test(val):
    print(f"Max value was reached: {val}")


a = adder(1)
a(5)(100).max(100, max_reached_test)(0)
a(-100)
a(100)