

    def search(self,key):
        length=len(key)
        trav=self.root
        for i in range(length):
            if key[i]==trav.children[self.getIndex(key[i])]:
                trav=trav.children[self.getIndex(key[i])]
            else:
             return False
        return True
