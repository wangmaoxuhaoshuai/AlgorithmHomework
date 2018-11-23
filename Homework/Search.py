import numpy as np

# 顺序查找 快速顺序查找 顺序查找在排序表中 折半查找 均匀查找 二叉树查找
class Search:
    def __init__(self,array,num):
        self.initial_array_ = array
        self.len_ = len(array)
        self.num_ = num

    def sequential_search(self):
        result_array = np.array([i for i in range(self.len_) if self.initial_array_[i] == self.num_])
        return  result_array

    def quick_sequential_search(self):
        result_array = []
        i = 0
        if (self.initial_array_[0] == self.num_):
            result_array.append(0)
        i = i + 1
        while(i < self.len_):
            if (self.initial_array_[i] == self.num_):
                result_array.append(i)
            i = i + 1
        return  result_array