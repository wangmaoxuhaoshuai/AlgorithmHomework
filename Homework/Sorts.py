import numpy as np
import math
import sys
sys.setrecursionlimit(1000000)

class Sort:
    def __init__(self,initial_list):
        self.initial_list_ = initial_list
        self.len_ = initial_list.shape[0]

    def bubble_sort(self):
        assert self.len_ > 0,\
            "initial_list can not be empty"

        for i in range(self.len_ - 1):
            for j in range(self.len_ - i - 1):
                if self.initial_list_[j] > self.initial_list_[j+1]:
                    max = self.initial_list_[j]
                    self.initial_list_[j] = self.initial_list_[j+1]
                    self.initial_list_[j+1] = max
        return self

    def quick_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def quick_sort_func(array):
            if len(array) < 2:
                return array
            else:
                key = array[0]
                less_than_key_array = [m for m in array[1:] if m < key]
                equal_to_key_array = [w for w in array if w == key]
                greater_than_key_array = [n for n in array[1:] if n > key]
            return quick_sort_func(less_than_key_array) + equal_to_key_array + quick_sort_func(greater_than_key_array)

        self.initial_list_ = np.array(quick_sort_func(self.initial_list_))
        return self

    def batcher_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"
        pass

    # 2018-11-7算法作业：选择排序、树选择、堆排序、归并排序、自然归并排序
    # 简单选择排序
    def selection_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def swap(a,b):
            return b,a

        for i in range(self.len_-1):
            min = self.initial_list_[i]
            iter = i
            for j in range(i+1,self.len_):
                if self.initial_list_[j] < self.initial_list_[iter]:
                    iter = j
            if (iter != i):
                self.initial_list_[iter],self.initial_list_[i] = swap(self.initial_list_[iter],self.initial_list_[i])

    # 树选择排序（锦标赛排序）
    def tree_selection_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"
        DATA_MAX = 11

        nodetype = np.dtype({
            'names': ['data', 'tree_arr_index'],
            'formats': ['i', 'i']
        })

        # 满二叉树的叶子节点数
        LeafNodeSize = 1
        # 满二叉树的高度
        height = 1
        # 循环结束后，满二叉树叶子节点应该是2的幂
        while (LeafNodeSize < self.len_):
            LeafNodeSize *= 2
            height += 1

        # 满二叉树所有节点个数正好是叶子个数的两倍
        TreeSize = LeafNodeSize * 2 - 1

        tree_array = np.array([(0, i) for i in range(TreeSize)], dtype=nodetype)
        IndexLeafStart = LeafNodeSize - 1

        IndexArr = 0
        for i in range(IndexLeafStart,TreeSize):
            if (IndexArr < self.len_):
                tree_array[i]['data'] = self.initial_list_[IndexArr]
                tree_array[i]['tree_arr_index'] = IndexArr
                IndexArr += 1
            else:
                tree_array[i]['data'] = DATA_MAX
                tree_array[i]['tree_arr_index'] = -1

        for k in range(TreeSize - 1, 1, -2):
            if (tree_array[k - 1]['data'] <= tree_array[k]['data']):
                tree_array[int(k / 2 - 1)]['data'] = tree_array[k - 1]['data']
                tree_array[int(k / 2 - 1)]['tree_arr_index'] = tree_array[k - 1]['tree_arr_index']
            else:
                tree_array[int(k / 2 - 1)]['data'] = tree_array[k]['data']
                tree_array[int(k / 2 - 1)]['tree_arr_index'] = tree_array[k]['tree_arr_index']

        # 从上次胜出的节点中开始更新
        def UpdateTree(index):
            while (index):
                # 如果是左孩子
                if (index % 2):
                    # 左孩子小于右孩子
                    if (tree_array[index]['data'] <= tree_array[index + 1]['data']):
                        # 更新父节点的值和在该值在树中的索引
                        tree_array[int((index - 1) / 2)]['data'] = tree_array[index]['data']
                        tree_array[int((index - 1) / 2)]['tree_arr_index'] = tree_array[index]['tree_arr_index']
                    else:
                        tree_array[int((index - 1) / 2)]['data'] = tree_array[index + 1]['data']
                        tree_array[int((index - 1) / 2)]['tree_arr_index'] = tree_array[index + 1]['tree_arr_index']
                    # 更新索引，准备比较上一层父节点及其兄弟
                    index = int(index / 2)
                # 如果是右孩子
                else:
                    # 左孩子小于右孩子
                    if (tree_array[index - 1]['data'] <= tree_array[index]['data']):
                        # 更新父节点的值和在该值在树中的索引
                        tree_array[int(index / 2 - 1)]['data'] = tree_array[index - 1]['data']
                        tree_array[int(index / 2 - 1)]['tree_arr_index'] = tree_array[index - 1]['tree_arr_index']
                    else:
                        tree_array[int(index / 2 - 1)]['data'] = tree_array[index]['data']
                        tree_array[int(index / 2 - 1)]['tree_arr_index'] = tree_array[index]['tree_arr_index']
                    # 更新索引，准备比较上一层父节点及其兄弟
                    index = int(index / 2 - 1)

        for m in range(self.len_ - 1):
            self.initial_list_[m] = tree_array[0]['data']
            winIndex = tree_array[0]['tree_arr_index'] + IndexLeafStart
            tree_array[winIndex]['data'] = DATA_MAX
            UpdateTree(winIndex)

        self.initial_list_[self.len_ - 1] = tree_array[0]['data']

    # 堆排序
    def heap_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def swap(a,b):
            return b,a

        def Update(index, len_arr):
            # 非叶子节点,即存在左孩子
            if (index * 2 + 1 < len_arr):
                # 存在右孩子
                if (index * 2 + 2 < len_arr):
                    # 左孩子大于右孩子
                    if (self.initial_list_[index * 2 + 1] > self.initial_list_[index * 2 + 2]):
                        # 左孩子大于父节点
                        if (self.initial_list_[index * 2 + 1] > self.initial_list_[index]):
                            # 交换左孩子和父节点
                            self.initial_list_[index], self.initial_list_[index * 2 + 1] = swap(self.initial_list_[index], self.initial_list_[index * 2 + 1])
                            # 更新左孩子
                            Update(index * 2 + 1,len_arr)
                        # 左孩子小于父节点，不交换
                        else:
                            pass
                    # 右孩子大于左孩子
                    else:
                        # 右孩子大于父节点
                        if (self.initial_list_[index * 2 + 2] > self.initial_list_[index]):
                            # 交换
                            self.initial_list_[index], self.initial_list_[index * 2 + 2] = swap(self.initial_list_[index], self.initial_list_[index * 2 + 2])
                            Update(index * 2 + 2, len_arr)
                        else:
                            pass
                # 不存在右孩子
                else:
                    # 左孩子大于父节点
                    if (self.initial_list_[index * 2 + 1] > self.initial_list_[index]):
                        # 交换左孩子和父节点
                        self.initial_list_[index], self.initial_list_[index * 2 + 1] = swap(self.initial_list_[index],self.initial_list_[index * 2 + 1])
                        Update(index * 2 + 1, len_arr)

        def MakeHeap(index,len_arr):
            Update(index,len_arr)

            if(index > 0):
                index = index - 1
                MakeHeap(index, len_arr)

        for i in range(self.len_ - 1):
            len_i = self.len_ - i
            index = int((self.len_ - i) / 2 - 1)
            MakeHeap(index,len_i)
            self.initial_list_[0], self.initial_list_[self.len_ - i - 1] = swap(self.initial_list_[0],self.initial_list_[self.len_ - i -1])
    # 归并排序
    def merge_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def MergeFunc(arr1,arr2,arr):
            index1 = 0
            index2 = 0
            index = 0
            while(index < arr.shape[0]):
                while(index1 < arr1.shape[0]):
                    if(arr1[index1] < arr2[index2]):
                        arr[index] = arr1[index1]
                        index1 += 1
                        index += 1
                    else:
                        break

                if(index1 == arr1.shape[0]):
                    for i in range(index2,arr2.shape[0]):
                        arr[index] = arr2[i]
                        index += 1
                    break

                while(index2 < arr2.shape[0]):
                    if(arr2[index2] <= arr1[index1]):
                        arr[index] = arr2[index2]
                        index2 += 1
                        index += 1
                    else:
                        break

                if(index2 == arr2.shape[0]):
                    for i in range(index1,arr1.shape[0]):
                        arr[index] = arr1[i]
                        index += 1
                    break

        def Merge(left,right):
            if(left < right):
                center = int((left + right) / 2)
                Merge(left,center)
                Merge(center + 1,right)
                temp_list = np.copy(self.initial_list_)
                MergeFunc(temp_list[left:center + 1],temp_list[center + 1:right + 1],self.initial_list_[left:right + 1])

        Merge(0,self.len_ - 1)

    # 自然归并排序
    def nature_merge_sort(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def MergeFunc(arr1,arr2,arr):
            index1 = 0
            index2 = 0
            index = 0
            while(index < arr.shape[0]):
                while(index1 < arr1.shape[0] and index2 < arr2.shape[0]):
                    if(arr1[index1] < arr2[index2]):
                        arr[index] = arr1[index1]
                        index1 += 1
                        index += 1
                    else:
                        break

                if(index1 == arr1.shape[0]):
                    for i in range(index2,arr2.shape[0]):
                        arr[index] = arr2[i]
                        index += 1
                    break

                while(index2 < arr2.shape[0] and index1 < arr1.shape[0]):
                    if(arr2[index2] <= arr1[index1]):
                        arr[index] = arr2[index2]
                        index2 += 1
                        index += 1
                    else:
                        break

                if(index2 == arr2.shape[0]):
                    for i in range(index1,arr1.shape[0]):
                        arr[index] = arr1[i]
                        index += 1
                    break


        def Merge(arr):
            if(arr.shape[0] > 0):
                temp_arr = np.array([0 for i in range(int((arr.shape[0] + 1) / 2 - 1))])
                index_j = 0
                # 分成了偶数个片段
                if(arr.shape[0] % 2):
                    # MergeFunc(self.initial_list_[0:arr[0] + 1],self.initial_list_[arr[0] + 1,arr[1] + 1])
                    for i in range(0,arr.shape[0],2):
                        temp_list = np.copy(self.initial_list_)
                        if(i == arr.shape[0] - 1):
                            if(i != 0):
                                MergeFunc(temp_list[arr[i - 1] + 1:arr[i] + 1],temp_list[arr[i] + 1:self.len_], self.initial_list_[arr[i - 1] + 1:self.len_])
                            else:
                                MergeFunc(temp_list[0:arr[i] + 1], temp_list[arr[i] + 1:self.len_],self.initial_list_[0:self.len_])
                        elif(i == 0):
                            MergeFunc(temp_list[0:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1],self.initial_list_[0:arr[i + 1] + 1])
                            temp_arr[index_j] = arr[i + 1]
                            index_j += 1
                        else:
                            MergeFunc(temp_list[arr[i - 1] + 1:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1],self.initial_list_[arr[i - 1] + 1:arr[i + 1] + 1])
                            temp_arr[index_j] = arr[i + 1]
                            index_j += 1
                # 分成了奇数个片段
                else:
                    for i in range(0,arr.shape[0],2):
                        temp_list = np.copy(self.initial_list_)
                        if(i == arr.shape[0] - 2):
                            if(i != 0):
                                MergeFunc(temp_list[arr[i-1] + 1:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1], self.initial_list_[arr[i-1] + 1:arr[i+1] + 1])
                                temp_list = np.copy(self.initial_list_)
                                MergeFunc(temp_list[arr[i-1] + 1:arr[i+1] + 1],temp_list[arr[i+1] + 1:self.len_],self.initial_list_[arr[i-1] + 1:self.len_])
                            else:
                                MergeFunc(temp_list[0:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1],self.initial_list_[0:arr[i + 1] + 1])
                                temp_list = np.copy(self.initial_list_)
                                MergeFunc(temp_list[0:arr[i + 1] + 1],temp_list[arr[i + 1] + 1:self.len_],self.initial_list_[0:self.len_])
                        elif(i == 0):
                            MergeFunc(temp_list[0:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1],self.initial_list_[0:arr[i + 1] + 1])
                            temp_arr[index_j] = arr[i + 1]
                            index_j += 1
                        else:
                            MergeFunc(temp_list[arr[i - 1] + 1:arr[i] + 1], temp_list[arr[i] + 1:arr[i + 1] + 1],self.initial_list_[arr[i - 1] + 1:arr[i + 1] + 1])
                            temp_arr[index_j] = arr[i + 1]
                            index_j += 1


                Merge(temp_arr)

        index_array = np.array([i for i in range(self.len_ - 1) if self.initial_list_[i+1] < self.initial_list_[i]])

        Merge(index_array)






    def __repr__(self):
        return "Sort()"



