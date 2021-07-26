class sieunhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def cap_nhap_suc_manh(cls, dame):
        cls.suc_manh = dame
sieu_nhan_A = sieunhan("vang", "kiem", "choe")
sieu_nhan_B = sieunhan("hong", "xuong", "canh sen")
print(sieunhan.suc_manh)
print(sieu_nhan_A.suc_manh)

sieu_nhan_A.cap_nhap_suc_manh(40)
print(sieunhan.suc_manh)
print(sieu_nhan_A.suc_manh)
print(sieu_nhan_B.suc_manh)

#cập nhập sức mạnh bằng object thay vì class. thay đổi hết tất cả sức manh của các object liên qun đến clasas này.
