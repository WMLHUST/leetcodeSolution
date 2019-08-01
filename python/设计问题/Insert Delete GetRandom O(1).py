class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.cache:
            self.cache[val] = 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.cache:
            del self.cache[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(list(self.cache.keys()))

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()

randomSet = RandomizedSet();

randomSet.insert(1);

randomSet.remove(2);

randomSet.insert(2);

randomSet.getRandom();

randomSet.remove(1);

randomSet.insert(2);

randomSet.getRandom();