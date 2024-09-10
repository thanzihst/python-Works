
class operations:
    # def get_persion(**kwargs):
    #     print(kwargs.get("name"))
    #     print(kwargs.get("w_place"))

    # get_persion(name="hari",w_place="tvm",n_place="kakkanad")


    def flat_list(self,*args):
        flat=[]

        for arg in args:
            if isinstance(arg,list):

                flat.extend(flat_list(*args))

            else:

                flat.append(arg)

        return flat
    

print(flat_list(10,20[100,200],[1000[100]]))
