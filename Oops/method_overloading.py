#   *args= tuple
#   **args= dict




class opreations:
    def perform_add(self,*args):
        total=sum([arg for arg in args if isinstance(arg,(int,float))])

        return total
    
    def perform_max(self,*args):

        total=max([arg for arg in args if isinstance(arg,(int,float))])


        return total
    

math=opreations()

print(math.perform_add(10,20.5))
print(math.perform_max(10,20,30,70.6))
    
