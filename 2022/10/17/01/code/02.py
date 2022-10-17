def dynamic_programming(number: int) -> int:
    f1, f2 = 1, 1
    for _ in range(3, number + 1):
        result: int = f1 + f2
        f1, f2 = f2, result
    
    return result


def lazy_loading_dp(number: int) -> int:
    f1, f2 = 1, 1
    while True:
        result: int = f1 + f2
        yield result
        f1, f2 = f2, result
        

if __name__ == "__main__":
    import gc
    import psutil
    
    
    def calculate_memory_usage():
        gc.collect()
        process = psutil.Process()
        rss = process.memory_info().rss / 2 ** 20
        
        return rss
    
    
    before: float = calculate_memory_usage()
    result: int = dynamic_programming(number=10000)
    print("Dynamic Programming: ", result)
    print(
        "After Dynamic Programming: ",
        calculate_memory_usage() - before
    )
    
    
    before: float = calculate_memory_usage()
    fibonacci = lazy_loading_dp(number=10000)
    for _ in range(3, 10001):
        result: int = next(fibonacci)
    print("Dynamic Programming: ", result)
    print(
        "After Lazy Loading Dynamic Programming: ",
        calculate_memory_usage() - before
    )
    