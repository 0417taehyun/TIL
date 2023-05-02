if __name__ == "__main__":
    import time
    
    
    start: float = time.time()
    eager_evaluation: list[int] = []
    for number in range(1, 10000001):
        eager_evaluation.append(number * number)
    print("Eager Evaluation: ", time.time() - start)

        
    start: float = time.time()
    lazy_evaluation: list[int] = list(
        map(lambda number: number * number, range(1, 10000001))
    )
    print("Lazy Evaluation: ",  time.time() - start)
    
    
    start: float = time.time()
    eager_evaluation: list[int] = [
        number * number for number in range(1, 10000001)
    ]
    print("List Comprehension: ", time.time() - start)
    