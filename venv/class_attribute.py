class SieuNhan:
    stt = 6
    so_thu_tu = 1
    suc_manh = 50
    dame = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "sieu nhan "+ para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1

        self.dame = SieuNhan.suc_manh
        SieuNhan.suc_manh += 10
    def xin_chao(self):
        print(f"xin chao, ta la sieu nhan  {self.ten}")
sieu_nhan_A = SieuNhan("trang", "riu", "nga voi")
sieu_nhan_B = SieuNhan("xanh", "sung", "da troi")

print(sieu_nhan_A.stt, sieu_nhan_A.dame)
print(sieu_nhan_B.stt, sieu_nhan_B.dame)
print(SieuNhan.so_thu_tu, SieuNhan.suc_manh)
sieu_nhan_A.xin_chao()
