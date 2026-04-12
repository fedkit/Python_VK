from parameter_deco import retry_deco


# 1
@retry_deco(2)
def add(a, b):
    return a + b


assert add(2, 3) == 5
assert add(a=10, b=5) == 15


# 2 
@retry_deco(3)
def always_ok():
    return 'ok'

assert always_ok() == 'ok'


# 3
counter = {'c': 0}

@retry_deco(2)
def fail_value_error():
    counter['c'] += 1
    raise ValueError()

try:
    fail_value_error()
    assert False 
except ValueError:
    assert counter['c'] == 3  

# 4
counter_4 = {'c': 0}

@retry_deco(3)
def flaky_success():
    counter_4['c'] += 1
    if counter_4['c'] < 3:
        raise RuntimeError()
    return 'done'

assert flaky_success() == 'done'
assert counter_4['c'] == 3

# 5
counter_5 = {'c': 0}

@retry_deco(5, [ValueError])
def expected_error():
    counter_5['c'] += 1
    raise ValueError()

try:
    expected_error()
    assert False
except ValueError:
    assert counter_5['c'] == 1

# 6
counter_6 = {'c': 0}

@retry_deco(0)
def fail_once():
    counter_6['c'] += 1
    raise RuntimeError()

try:
    fail_once()
    assert False
except RuntimeError:
    assert counter_6['c'] == 1