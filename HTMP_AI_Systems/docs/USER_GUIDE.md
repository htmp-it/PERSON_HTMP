# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG GIÁM SÁT CÔNG NHÂN (WARDEN AI)

Tài liệu hướng dẫn thao tác vận hành dành cho người dùng trên giao diện Web.

---

## 1. Đăng nhập & Tổng quan Giao diện (Dashboard)

1. Mở trình duyệt web và truy cập địa chỉ hệ thống (ví dụ: `http://localhost:5000` hoặc IP máy chủ).
2. Giao diện chính hiển thị danh sách các Camera đang giám sát thời gian thực kèm các thẻ thống kê vi phạm.

```text
┌────────────────────────────────────────────────────────┐
│ [🖼️ HÌNH ẢNH 1: Giao diện tổng quan Dashboard chính]    │
│ (Chụp toàn màn hình Dashboard với lưới camera & stats)  │
└────────────────────────────────────────────────────────┘
```

---

## 2. Xem trực tiếp Camera (Live View)

- **Xem nhiều camera:** Hệ thống mặc định hiển thị dạng lưới (Grid View).
- **Phóng to 1 camera:** Nhấp vào khung camera muốn quan sát chi tiết để mở **Focused View**.
- **Quay lại danh sách:** Nhấp nút **"Thu nhỏ" / "Quay lại"**.

```text
┌────────────────────────────────────────────────────────┐
│ [🖼️ HÌNH ẢNH 2: Chế độ xem chi tiết 1 Camera]           │
│ (Chụp giao diện Focused View của một camera)            │
└────────────────────────────────────────────────────────┘
```

---

## 3. Cấu hình Vùng Giám Sát Máy (Vẽ ROI Đa giác)

Dùng khi cần thiết lập hoặc điều chỉnh vị trí đứng làm việc của công nhân tại từng máy:

1. Tại khung camera cần chỉnh, chọn **"Cấu hình vùng"** (hoặc mở bảng vẽ đa giác).
2. **Chấm điểm:** Nhấp **Chuột TRÁI** lần lượt quanh vị trí máy/khu vực đứng của công nhân.
3. **Khép kín vùng:** Nhấp **Chuột PHẢI** để hoàn tất nối điểm cuối về điểm đầu.
4. **Đặt tên máy:** Nhập mã máy vào ô tên theo định dạng chuẩn (ví dụ: `may_1`, `may_7`).
5. **Thêm máy khác (nếu có):** Bấm nút **"Vẽ thêm"** nếu camera quan sát nhiều máy.
6. **Lưu cấu hình:** Bấm nút **"Lưu cấu hình"** màu xanh để AI bắt đầu áp dụng ngay.

```text
┌────────────────────────────────────────────────────────┐
│ [🖼️ HÌNH ẢNH 3: Thao tác chấm điểm vẽ vùng đa giác]    │
│ (Chụp ảnh các điểm nối màu và ô nhập tên máy)          │
└────────────────────────────────────────────────────────┘
```

---

## 4. Tra cứu Lịch sử Vi phạm (History)

1. Nhấp vào tab **"Lịch sử"** (History) trên thanh điều hướng bên trái.
2. **Bộ lọc:**
   - Chọn **Khoảng ngày** cần tra cứu.
   - Chọn **Vị trí / Máy** cần kiểm tra.
3. **Xem bằng chứng vi phạm:**
   - Bấm icon **Xem ảnh** 🖼️: Mở pop-up ảnh chụp khoảnh khắc vi phạm (có nút **Tải ảnh về**).
   - Bấm icon **Xem video** ▶️: Mở cửa sổ phát lại video clip ngắn thời điểm vi phạm (hỗ trợ tua/tải video).

```text
┌────────────────────────────────────────────────────────┐
│ [🖼️ HÌNH ẢNH 4: Bảng danh sách lịch sử & Pop-up video] │
│ (Chụp bảng lịch sử lọc và modal xem lại clip vi phạm)   │
└────────────────────────────────────────────────────────┘
```

---

## 5. Báo cáo & Phân tích Thống kê (Analytics)

1. Nhấp vào tab **"Phân tích"** (Analysis).
2. Chọn khoảng thời gian hoặc máy cụ thể để xem:
   - Biểu đồ số lượt vi phạm theo khung giờ / ngày.
   - Tỷ lệ tuân thủ vị trí làm việc giữa các máy.

```text
┌────────────────────────────────────────────────────────┐
│ [🖼️ HÌNH ẢNH 5: Biểu đồ thống kê vi phạm Analytics]     │
│ (Chụp màn hình biểu đồ cột / đường trong tab Analysis) │
└────────────────────────────────────────────────────────┘
```

---

> 💡 **Mẹo thao tác nhanh:**
> - **Chuột Trái:** Thêm điểm mốc đa giác.
> - **Chuột Phải:** Đóng kín khung đa giác.
> - **Đặt tên chuẩn:** Luôn đặt theo mẫu `may_X` (viết thường, dấu gạch dưới).
