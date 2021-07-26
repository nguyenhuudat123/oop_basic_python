class kter:
    def __init__(self, para_ho, para_ten):
        self.ten = para_ten
        self.ho = para_ho
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)
    @property
    def email(self):
        return f'{self.ho}_{self.ten}@gmail.com'

    @ho_va_ten.setter
    def ho_va_ten(self, ten_m):
        ho_moi, ten_moi = ten_m.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi

kter_1 = kter('nguyen', 'nam')
print(kter_1.__dict__)
print(kter_1.ho_va_ten)
print(kter_1.email)

kter_1.ho_va_ten = "vu van"
print(kter_1.ho)