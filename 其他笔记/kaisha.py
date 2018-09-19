import urllib
from urllib import parse

def str2url(s):
    #s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = int(strlen/rows)
    right_rows = strlen % rows
    new_s = list(s[num_loc:])
    output = ''
    for i in range(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[int(p)]
    return parse.unquote(output).replace('^', '0')


def main():
    s = "8h28n132885333_55E9953tF.e%112%%66%k3E-%f32t%xt26%355843e7%%561bp2i%F356EE%1Fy455Eb76%Fa231E%5655a%1EEf72f3mmF7%326_E.u32--455eA1i6229F311mtD4%c76bd%2.39F41859ph1%57d34a"
    result_str = str2url(s)
    print(result_str)

main()
