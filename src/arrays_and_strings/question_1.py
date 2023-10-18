# Implement an algorithm that determines whether all characters in a string occur
# only once. What if it is forbidden to use additional
# data structures?

any_str = 'ddog'
length_ascii = 256


def get_count_symbs_in_st(st, length_ascii_alphabet):
    f = False
    if len(st) >= length_ascii_alphabet:
        f = True
        return f
    d = dict()

    for el in st:
        if el not in d:
            d[el] = 1
        else:
            f = True
            return f
    return f


result = get_count_symbs_in_st(any_str, length_ascii)
print("Occured more than once" if result else "Occured once" )
