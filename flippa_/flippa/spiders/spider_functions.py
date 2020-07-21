import re
class functions():
    newlist = []
    newl = []
    newl2 = []
    newl3 = []
    newl4 = []

    empty1 = []
    empty2 =[]
    empty3 = []
    empty4 = []

    def pp_to_int(i):
        i = int(re.sub(r'[^\w]','',i))
        newlist.append(i)
        return newlist  

    def monthly_net_to_int(n):
        for i in n:
            i = re.sub(r'[^\w]','',i)
            i = re.sub(r"[a-zA-Z]+", "",i)
            i = int(i)
            newl.append(i)
        return newl

    def age_to_int(a):
        for i in a:
            i = re.sub(r'[^\w]','',i)
            i = re.sub(r"[a-zA-Z]+", "",i)
            i = int(i)
            newl2.append(i)
        return newl2

    def site_type_lst(s):
        for i in s:
            i = i.strip(' \n ')
            newl3.append(i)
        return newl3

    def multiple_mo(m):
        m = m[0]
        empty1.append(m)
        for i in empty1:
            i = i.strip(' \n ')
            i = i.strip('Multiple x')
            i = float(i)
            empty2.append(i)
        return empty2


    def multiple_yr(m):
        m= m[0]
        empty3.append(m)
        for i in empty3:
            i = i.strip(' \n ')
            i = i.strip('Multiple x')
            i = float(i)
            i = round(i*12,2)
            empty4.append(i)
        return empty4


    def pf_lst(pf):
        for i in pf:
            i = i.strip(' \n ')
            newl4.append(i)
        return newl4
