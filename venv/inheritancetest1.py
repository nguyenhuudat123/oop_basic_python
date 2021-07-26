class sieunhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
class sieunhangao(sieunhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_sieu_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        #dongf ở super là kế thừa thoi. cho self vào là tạch
        self.sieu_thu = para_sieu_thu
    @classmethod
    def infor_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac, sieu_thu = new_lst
        return cls(ten, vu_khi, mau_sac, sieu_thu)
sieu_nhan_A = sieunhangao.infor_string("a-b-c-d")
print(sieu_nhan_A.__dict__)
