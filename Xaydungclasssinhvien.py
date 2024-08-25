class SinhVien:
    def __init__(self, ma_sv, ten_sv, diem_toan, diem_van, diem_hoa):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_hoa = diem_hoa
    
    def diem_trung_binh(self):
        return (self.diem_toan + self.diem_van + self.diem_hoa) / 3
    
    def thong_tin(self):
        return f"Mã SV: {self.ma_sv}, Tên SV: {self.ten_sv}, Toán: {self.diem_toan}, Văn: {self.diem_van}, Hóa: {self.diem_hoa}, Điểm TB: {self.diem_trung_binh():.2f}"

danh_sach_sinh_vien = [
    SinhVien("SV001", "Nguyen Van A", 6, 7, 5),
    SinhVien("SV002", "Le Thi B", 4, 5, 4),
    SinhVien("SV003", "Tran Van C", 8, 6, 7),
    SinhVien("SV004", "Pham Thi D", 7, 7, 6),
    SinhVien("SV005", "Hoang Van E", 3, 4, 5)
]

print("Các sinh viên có điểm trung bình lớn hơn 5:")
for sv in danh_sach_sinh_vien:
    if sv.diem_trung_binh() > 5:
        print(sv.thong_tin())

print("\nCác sinh viên có điểm hóa dưới 5:")
for sv in danh_sach_sinh_vien:
    if sv.diem_hoa < 5:
        print(sv.thong_tin())