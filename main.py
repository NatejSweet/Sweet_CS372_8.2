import threading

def main():
    values = [[10,20], [1,5], [70,80], [27,92], [0,16]]
    threads = []
    results = []
    for value in values:
        t = threading.Thread(target=sum_range, args=(value, results), daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    sum = 0
    for n in results:
        sum += n
    print(results)
    print(sum)
    values = None

    
def sum_range(values, results):
    r = range(values[0], values[1] + 1)
    results.append(sum(r))
if __name__ == "__main__":
    main()
