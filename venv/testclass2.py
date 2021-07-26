class sieu_nhan:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):   #chữ init trứcc sau phải 2 gạch. __init__
        self.ten = "sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        return f"xin chao, ta la {self.ten}"
sieu_nhan_A = sieu_nhan("do", "kiem", "do ruc")
print("ta la ", sieu_nhan_A.ten)
print("vu khi", sieu_nhan_A.vu_khi)
print(f"ta co mau {sieu_nhan_A.mau_sac}")
print(sieu_nhan_A.xin_chao())
print(sieu_nhan.xin_chao(sieu_nhan_A))
print(sieu_nhan_A.__dict__)