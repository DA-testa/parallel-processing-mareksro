# python3
import heapq
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread = [(0,i) for i in range(n)]
    heapq.heapify(thread)
    for darbs in enumerate(data):
        finish, x = heapq.heappop(thread)
        output.append((x, finish))
        finish+=darbs
        heapq.heappush(thread,(finish,x))


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int,input().split())
    data = list(map(int,input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
   
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    
    for i, j in result:
        print(i,j)

if __name__ == "__main__":
    main()
