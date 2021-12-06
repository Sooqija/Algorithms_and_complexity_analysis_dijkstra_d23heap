from dijkstra_dheap import graph_generator, dijkstra_dheap
from time import time

if __name__ == "__main__":
    ################### test 1. case 1.a
    case = "1.a"
    n_start = 1
    n_end = 10002
    n_step = 100
    q = 1
    r = 1000000
    possibility = ( n_end**2 / 10 ) / ( n_end * (n_end - 1) )
    if possibility > 1:
        possibility = 1

    file_1 = open('case_1a_result.txt', 'w')
    for vertex_count in range(n_start, n_end, n_step):
        print("Start vertex_count = " + str(vertex_count) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_1.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(vertex_count) + '\n')
    file_1.close()
    print("Processing Done for case ", case)


    ################### test 1. case 1.b
    case = "1.b"
    n_start = 1
    n_end = 10002
    n_step = 100
    q = 1
    r = 1000000
    possibility = ( n_end**2 ) / ( n_end * (n_end - 1) )
    if possibility > 1:
        possibility = 1

    file_2 = open('case_1b_result.txt', 'w')
    for vertex_count in range(n_start, n_end, n_step):
        print("Start vertex_count = " + str(vertex_count) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_2.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(vertex_count) + '\n')
    file_2.close()
    print("Processing Done for case ", case)


    ################### test 2. case 2.a
    case = "2.a"
    n_start = 101
    n_end = 10002
    n_step = 100
    q = 1
    r = 1000000
    possibility = ( 100 * n_end ) / ( n_end * (n_end - 1) )
    if possibility > 1:
        possibility = 1

    file_3 = open('case_2a_result.txt', 'w')
    for vertex_count in range(n_start, n_end, n_step):
        print("Start vertex_count = " + str(vertex_count) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_3.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(vertex_count) + '\n')
    file_3.close()
    print("Processing Done for case ", case)


    ################### test 2. case 2.b
    case = "2.b"
    n_start = 101
    n_end = 10002
    n_step = 100
    q = 1
    r = 1000000
    possibility = ( 1000 * n_end ) / ( n_end * (n_end - 1) )
    if possibility > 1:
        possibility = 1

    file_4 = open('case_2b_result.txt', 'w')
    for vertex_count in range(n_start, n_end, n_step):
        print("Start vertex_count = " + str(vertex_count) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_4.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(vertex_count) + '\n')
    file_4.close()
    print("Processing Done for case ", case)


    ################### test 3. case 2
    case = "3"
    n = 10001
    e_start = 0
    e_end = 10000000
    e_step = 100000
    q = 1
    r = 1000000

    file_5 = open('case_3_result.txt', 'w')
    for edges_count in range(e_start, e_end, e_step):
        possibility = ( edges_count ) / ( n * (n - 1) )
        if possibility > 1:
            possibility = 1

        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        print("Start edges_count = " + str(edges_count) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_5.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(edges_count) + '\n')
    file_5.close()
    print("Processing Done for case ", case)


    ################### test 4. case 4.a
    case = "4.a"
    n = 10001
    q = 1
    r_start = 1
    r_end = 200
    r_step = 1
    possibility = ( n **2 ) / ( n * (n - 1) )
    if possibility > 1:
        possibility = 1

    file_6 = open('case_4a_result.txt', 'w')
    for weight in range(r_start, r_end, r_step):
        print("Start weight = " + str(weight) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_6.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(weight) + '\n')
    file_6.close()
    print("Processing Done for case ", case)


    ################### test 4. case 4.b
    case = "4.b"
    n = 10001
    q = 1
    r_start = 1
    r_end = 200
    r_step = 1
    possibility = ( 1000 * n ) / ( n * (n - 1) )
    if possibility > 1:
        possibility = 1

    file_7 = open('case_4b_result.txt', 'w')
    for weight in range(r_start, r_end, r_step):
        print("Start weight = " + str(weight) + " test. Case", case)
        adj_matrix = graph_generator(possibility, vertex_count, q, r)
        d2_heap_tstart = time()
        d2_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 2, start = 0)
        d2_heap_tend = time() - d2_heap_tstart
        d3_heap_tstart = time()
        d3_heap_res = dijkstra_dheap(adj_matrix, vertex_count, d = 3, start = 0)
        if d2_heap_res == d3_heap_res:
            print("Passed")
        d3_heap_tend = time() - d3_heap_tstart
        file_7.write(str(d2_heap_tend) + ' ' + str(d3_heap_tend) + ' ' + str(weight) + '\n')
    file_7.close()
    print("Processing Done for case ", case)