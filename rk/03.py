import time

def timeit_last_k(k, limit):
    def dec(func):
        time_history = []

        def wrap(*args, **kwargs):
            start = time.perf_counter()
            answer = func(*args, **kwargs)
            runtime = time.perf_counter() - start

            if runtime > limit:
                time_history.append(runtime)
                if len(time_history) > k:
                    time_history.pop(0)

                avg_time = sum(time_history) / len(time_history)
                print(avg_time)

            return answer

        return wrap
    return dec


@timeit_last_k(2, limit=10)
def sleeper(n):
    time.sleep(n)
    return n


sleeper(4)    # ничего не выведет (<=10)
sleeper(12)   # 12
sleeper(5)    # 12
sleeper(20)   # 16