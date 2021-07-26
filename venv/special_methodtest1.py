class sieu_nhan:
    def __init__(self, para_ten, para_mau):
        self.ten= para_ten
        self.mau = para_mau

    def __str__(self):
        return 'Day la {}, mau {}'.format(self.ten, self.mau)

    def __repr__(self):
        return 'ten: {}\nmau: {}'.format(self.ten, self.mau)
    def __len__(self):
        return len(self, ten)
sieu_nhan_A = sieu_nhan("do", "do do")
print(sieu_nhan_A)
print('%s'%sieu_nhan_A)
print('%r'%sieu_nhan_A)