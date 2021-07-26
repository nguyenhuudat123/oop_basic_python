class sieunhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    #def bien_hinh(self):
     #   print(f"sieu nhan {sieunhan.ten} bien hinh")
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')      #xóa dấu gạch ngang nế  có
        new_lst = [st.strip() for st in lst]        #xóa khoảng trắng thừa nếu có
        ten, vu_khi, mau_sac = new_lst              #gán vào từng cặp cho đr cấi trúc dict
        return cls(ten, vu_khi, mau_sac)           # trả về bằng ga o thức cls
    @staticmethod
    def bien_hinh():
        print("sieu nhan bien hinh")
    # nêu bỏ #staticmethod đi thì phải là bien_hinh(self)
    def xin_chao(self):
        print(f"xin chao, ta la sieu nhan  {self.ten}")
    def bien_hinh_2(self):
        print(f"xin chao, ta la {self.ten} bien hinh")
infor_str = "do - kiem - do vl"
sieu_nhan_A = sieunhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)
print(sieu_nhan_A.ten)
#kiểu dư liệu dicttionary, dưu từng cặp dữ liệu, sẽ trả về ngoặc nhọn
sieu_nhan_A.bien_hinh()
sieu_nhan_A.xin_chao()
sieu_nhan_A.bien_hinh_2()
