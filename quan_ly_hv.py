class KhoaHoc:  
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):  
        self.maKhoaHoc = maKhoaHoc  
        self.tenKhoaHoc = tenKhoaHoc  
        self.hinhThuc = hinhThuc  
        self.hocPhi = hocPhi  

    def thongTinKhoaHoc(self):  
        return f"Mã khóa học: {self.maKhoaHoc}, Tên khóa học: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi}"  


class HocVien:  
    def __init__(self, maHV, tenHV, ngaySinh):  
        self.maHV = maHV  
        self.tenHV = tenHV  
        self.ngaySinh = ngaySinh  
        self.khoaHoc = []  

    def dangKyKhoaHoc(self, khoaHoc):  
        self.khoaHoc.append(khoaHoc)  

    def hienThiKhoaHoc(self):  
        if not self.khoaHoc:  
            return "Chưa đăng ký khóa học nào."  
        return [khoaHoc.thongTinKhoaHoc() for khoaHoc in self.khoaHoc]  


khoaHoc1 = KhoaHoc("KH001", "Lập trình Python", "Trực tuyến", 2000000)  
khoaHoc2 = KhoaHoc("KH002", "Phát triển Web", "Trực tiếp", 3000000)  

hocVien1 = HocVien("HV001", "Nguyễn Văn A", "2000-01-01")  
hocVien2 = HocVien("HV002", "Trần Thị B", "2001-02-02")  
 
hocVien1.dangKyKhoaHoc(khoaHoc1)  
hocVien1.dangKyKhoaHoc(khoaHoc2)  
hocVien2.dangKyKhoaHoc(khoaHoc1)  

print(f"Học viên: {hocVien1.tenHV} đã đăng ký các khóa học:")  
print(hocVien1.hienThiKhoaHoc())  

print(f"Học viên: {hocVien2.tenHV} đã đăng ký các khóa học:")  
print(hocVien2.hienThiKhoaHoc())