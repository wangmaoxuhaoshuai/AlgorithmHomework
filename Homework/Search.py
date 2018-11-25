import numpy as np

# 顺序查找 快速顺序查找 折半查找 均匀折半查找 二叉树查找
class Search:
    def __init__(self,array,num):
        # 待查找数组
        self.initial_array_ = array
        self.len_ = len(array)
        # 待查找数
        self.num_ = num
        # 待查找数的索引
        self.index_ = self.len_

    # 顺序查找
    def sequential_search(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        for i in range(self.len_):
            if (self.num_ == self.initial_array_[i]):
                self.index_ = i
                break

    # 快速顺序查找
    def quick_sequential_search(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        for i in range(self.len_):
            if (self.initial_array_[i] <= self.num_):
                if (self.num_ == self.initial_array_[i]):
                    self.index_ = i
                    break
            else:
                break

    # 二分查找
    def binary_search(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def find(left_index,right_index):
            if (left_index >= 0 and left_index < self.len_ and right_index >= 0 and right_index < self.len_):
                mid_index = int((left_index + right_index) / 2)
                if (self.num_ == self.initial_array_[mid_index]):
                    self.index_ = mid_index
                    return
                elif (self.num_ > self.initial_array_[mid_index]):
                    left_index = mid_index + 1
                    find(left_index,right_index)
                else:
                    right_index = mid_index - 1
                    find(left_index,right_index)

        find(0,self.len_ - 1)

    # 均匀折半查找
    def uniform_binary_search(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"

        def find(i,m):
            if (self.num_ == self.initial_array_[i]):
                self.index_ = i
                return
            else:
                if (m == 0):
                    return
                if (self.num_ < self.initial_array_[i]):
                    i = i - int(np.ceil(m / 2))
                else:
                    i = i + int(np.ceil(m / 2))
                m = int(np.floor(m / 2))
                find(i,m)

        find(int(np.ceil(self.len_ / 2)),int(np.floor(self.len_ / 2)))

    # 二叉树查找
    def tree_search(self):
        assert self.len_ > 0, \
            "initial_list can not be empty"
        if (self.len_ == 1):
            self.index_ = 0
        else:
            # 分别记录： 节点左子树下标 节点的值在给定数组中的下标 节点右子树下标 （初始化记录第一个节点）
            tree_array = np.array([0,0,0])

            # 记录每一次插入到tree_array的节点的下标
            index_tree_add = 0

            # 构造二叉树
            for i in range(1,self.len_):

                def insert(value,root):

                    # 小于等于根节点
                    if (self.initial_array_[value] <= self.initial_array_[root]):
                        # 若根节点左子树不存在，则将节点作为根节点左子树
                        if (tree_array[root][0] == 0):
                            # 将节点插入到树中
                            tree_array = np.vstack([tree_array,[0,value,0]])
                            # 修改增加的节点下标
                            index_tree_add += 1
                            # 修改根节点中的左子树下标
                            tree_array[root][0] = index_tree_add
                        # 若根节点左子树下标存在
                        else:
                            # 修改根节点为原来根节点的左子树
                            root = tree_array[root][0]
                            # 递归
                            insert(value,root)
                    # 大于根节点
                    else:
                        # 若根节点的右子树不存在，则将节点作为根节点右子树
                        if (tree_array[root][2] == 0):
                            # 将节点插入到树中
                            tree_array = np.vstack([tree_array, [0, value, 0]])
                            # 修改增加的节点下标
                            index_tree_add += 1
                            tree_array[root][2] = index_tree_add
                        # 若根节点的右子树存在
                        else:
                            root = tree_array[root][2]
                            insert(value,root)

                insert(i,0)

            def search(root):

                # 查找数等于根节点
                if (self.num_ == self.initial_array_[tree_array[root][1]]):
                    self.index_ = tree_array[root][1]
                    return
                # 查找数大于根节点，则比较右子树
                elif (self.num > self.initial_array_[tree_array[root][1]]):
                    # 如果根节点右子树不存在
                    if (tree_array[root][2] == 0):
                        return
                    # 如果右子树存在，修改根节点为右子树
                    else:
                        root = tree_array[root][2]
                        search(root)
                # 查找树小于根节点，则比较左子树
                else:
                    # 如果左子树不存在
                    if (tree_array[root][0] == 0):
                        return
                    else:
                        root = tree_array[root][0]
                        search(root)

            search(0)





