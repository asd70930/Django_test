from django.test import TestCase

# Create your tests here.


def check_vip_stock(fun):
    def wrapper(re):
        print("id:", re['id'])
        print("vip:", re['vip'])
        xx = (True, 10)
        fun(re, xx)
    return wrapper

@check_vip_stock
def add_order(re, ans):
    print("yo")
    print(ans)


# x = {"id": 1, "vip": True}
#
# add_order(x)
# print()
#
#
# y = (1,2)
#
# y1 ,y2 = y
# print(y1,y2)


def add_val_to_list(val, list=[]):
    list.append(val)
    return list


list1 = add_val_to_list(321)
list2 = add_val_to_list(123, [])
list3 = add_val_to_list('a')

print('list1:', list1)
print('list2:', list2)
print('list3:', list3)

