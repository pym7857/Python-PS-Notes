class LRUCache(object):

    def __init__(self, capacity):
        global dic, order, cp, i
        """
        :type capacity: int
        """
        dic = dict()
        order = dict()
        cp = capacity
        i=0

    def get(self, key):
        global dic, order, cp, i
        """
        :type key: int
        :rtype: int
        """
        try:
            if dic[key]:
                order[key] = i
                i+=1
                return dic[key]
        except:
            return -1
        
        

    def put(self, key, value):
        global dic, order, cp, i
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(dic) == cp:
            if dic.has_key(key): # 꽉 찼는데 동일키가 있을때 -> 동일키의 value만 바꿔줌
                dic[key] = value
                order[key] = i
                i+=1
            else: # 꽉 찼는데 동일키가 없을때
                # 1)LRU 지우고
                sod = sorted(order.items(), key=lambda t:t[1])
                deleteKey = sod[0][0]
                del dic[deleteKey]
                del order[deleteKey]
                
                # 2)새 것 삽입
                dic[key] = value
                order[key] = i
                i+=1
               
        elif len(dic) < cp: # 꽉 안찼을때
            dic[key] = value
            order[key] = i
            i+=1
            
        #print(i, dic)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)