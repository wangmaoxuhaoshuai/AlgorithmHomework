import numpy as np
from Sorts import Sort
from Search import Search

sortorsearch = int(input("Please enter 1 for sort or 2 for search or 0 for quit: "))
while (sortorsearch != 0):
    # 排序算法测试
    if (sortorsearch == 1):
        len_list = int(input("Please enter a number as the length of random list (0 for quit!): "))
        while (len_list != 0):
            list = np.random.randint(0,10,size=len_list)

            for i in range(len_list):
                print(list[i],end=' ')

            sort_func = input("\nPlease choose a sort for list"
                              "('b' for bubble sort,"
                              "'q' for quick sort,"
                              "'s' for selection sort,"
                              "'t' for tree selection sort,"
                              "'h' for heap sort,"
                              "'g' for merge sort,"
                              "'n' for natural merge sort"
                              "):")
            while ((sort_func != 'b')
                   & (sort_func != 'q')
                   & (sort_func != 's')
                   & (sort_func != 't')
                   & (sort_func != 'h')
                   & (sort_func != 'g')
                   & (sort_func != 'n')

            ):
                sort_func = input("\nPlease choose a sort for list"
                                  "('b' for bubble sort,"
                                  "'q' for quick sort,"
                                  "'s' for selection sort,"
                                  "'t' for tree selection sort,"
                                  "'h' for heap sort,"
                                  "'g' for merge sort,"
                                  "'n' for natural merge sort"
                                  "): ")

            sort_test = Sort(list)
            if (sort_func == 'b'):
                sort_test.bubble_sort()
            if (sort_func == 'q'):
                sort_test.quick_sort()
            if (sort_func == 's'):
                sort_test.selection_sort()
            if (sort_func == 't'):
                sort_test.tree_selection_sort()
            if (sort_func == 'h'):
                sort_test.heap_sort()
            if (sort_func == 'g'):
                sort_test.merge_sort()
            if (sort_func == 'n'):
                sort_test.nature_merge_sort()

            for i in range(len_list):
                print(sort_test.initial_list_[i],end=' ')
            len_list = int(input("\nPlease enter a number as the length of random list (0 for quit!): "))
        sortorsearch = int(input("Please enter 1 for sort or 2 for search or 0 for quit: "))
    # 查找算法测试
    elif (sortorsearch == 2):
        pass
        len_list = int(input("Please enter a number as the length of random list (0 for quit!): "))
        while (len_list != 0):
            list = np.random.randint(0, 100, size=len_list)
            list = np.sort(list)
            for i in range(len_list):
                print(list[i], end=' ')
            num = int(input("\nPlease enter a num that u want search: "))
            search_func = input("Please choose a sort for list"
                              "('s' for sequential search,"
                              "'q' for quick sequential search,"
                              "'b' for binary search,"
                              "'u' for uniform binary search,"
                              "'t' for tree search,"
                              "):")

            while ((search_func != 's')
                & (search_func != 'q')
                & (search_func != 'b')
                & (search_func != 'u')
                & (search_func != 't')
            ):
                search_func = input("Please choose a sort for list"
                                  "('s' for sequential search,"
                                  "'q' for quick sequential search,"
                                  "'b' for binary search,"
                                  "'u' for uniform binary search,"
                                  "'t' for tree search,"
                                  "): ")

            search_test = Search(list,num)
            if (search_func == 's'):
                search_test.sequential_search()
            if (search_func == 'q'):
                search_test.quick_sequential_search()
            if (search_func == 'b'):
                search_test.binary_search()
            if (search_func == 'u'):
                search_test.uniform_binary_search()
            if (search_func == 't'):
                search_test.tree_search()

            index = search_test.index_
            if (index != len(list)):
                print("The " + str(num) + " is in index : " + str(index))
            else:
                print("The " + str(num) + " is not in the array.")

            len_list = int(input("\nPlease enter a number as the length of random list (0 for quit!): "))

        sortorsearch = int(input("Please enter 1 for sort or 2 for search or 0 for quit: "))
    else:
        sortorsearch = int(input("Please enter 1 for sort or 2 for search or 0 for quit: "))
