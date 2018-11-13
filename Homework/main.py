import numpy as np
from Sorts import Sort

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
