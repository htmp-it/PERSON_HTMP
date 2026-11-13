# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Page setup (margins)
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Style setup
normal_style = doc.styles['Normal']
normal_style.font.name = 'Calibri'
normal_style.font.size = Pt(11)
normal_style.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

def set_cell_background(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_border(cell, color="94A3B8", sz="12", val="dashed"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders_xml = f'''
    <w:tcBorders {nsdecls("w")}>
        <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
    </w:tcBorders>
    '''
    tcPr.append(parse_xml(borders_xml))

def add_image_box(doc, title, desc):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_border(cell, color="94A3B8", sz="12", val="dashed")
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(f"[{title.upper()}]")
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)
    
    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(20)
    run2 = p2.add_run(f"({desc})")
    run2.font.italic = True
    run2.font.size = Pt(9.5)
    run2.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(0)
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("HƯỚNG DẪN SỬ DỤNG HỆ THỐNG GIÁM SÁT CÔNG NHÂN")
r_title.font.bold = True
r_title.font.size = Pt(18)
r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(14)
r_sub = p_sub.add_run("(WARDEN AI - TÀI LIỆU VẬN HÀNH DÀNH CHO NGƯỜI DÙNG)")
r_sub.font.bold = True
r_sub.font.size = Pt(11)
r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

def add_heading_section(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)
    r = h.add_run(text)
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    return h

# Section 1
add_heading_section(doc, "1. Đăng nhập & Tổng quan Giao diện (Dashboard)")
p1 = doc.add_paragraph()
p1.paragraph_format.space_after = Pt(2)
p1.add_run("1. Mở trình duyệt web (Chrome/Edge) và nhập địa chỉ hệ thống (VD: http://localhost:5000 hoặc IP máy chủ).")
p2 = doc.add_paragraph()
p2.paragraph_format.space_after = Pt(6)
p2.add_run("2. Màn hình Dashboard hiển thị toàn bộ luồng Camera trực tiếp và các thẻ thông số thống kê vi phạm.")
add_image_box(doc, "CHÈN HÌNH ẢNH 1: GIAO DIỆN TỔNG QUAN DASHBOARD", "Chụp toàn màn hình Dashboard với lưới camera và thẻ thống kê vi phạm")

# Section 2
add_heading_section(doc, "2. Xem trực tiếp Camera (Live View)")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run("• Xem nhiều camera: ")
r.font.bold = True
p.add_run("Mặc định hệ thống hiển thị dạng lưới (Grid View).")

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run("• Phóng to 1 camera: ")
r.font.bold = True
p.add_run("Nhấp chuột vào khung camera bất kỳ để mở chế độ xem tập trung (Focused View).")

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(6)
r = p.add_run("• Quay lại danh sách: ")
r.font.bold = True
p.add_run("Bấm nút 'Thu nhỏ' / 'Quay lại'.")
add_image_box(doc, "CHÈN HÌNH ẢNH 2: CHẾ ĐỘ XEM CHI TIẾT 1 CAMERA", "Chụp giao diện Focused View phóng to của 1 camera")

# Section 3
add_heading_section(doc, "3. Cấu hình Vùng Giám Sát Máy (Vẽ ROI Đa giác)")
steps = [
    ("Bước 1:", "Tại camera cần cấu hình, bấm chọn nút 'Cấu hình vùng'."),
    ("Bước 2:", "Nhấp Chuột TRÁI lần lượt vào các góc xung quanh vị trí máy/vùng đứng của công nhân."),
    ("Bước 3:", "Nhấp Chuột PHẢI để hoàn tất và khép kín vùng đa giác."),
    ("Bước 4:", "Nhập tên vùng máy vào ô text theo chuẩn (Ví dụ: may_1, may_7)."),
    ("Bước 5:", "Bấm 'Vẽ thêm' nếu trong khung hình camera có nhiều máy khác cần giám sát."),
    ("Bước 6:", "Bấm nút 'Lưu cấu hình' (màu xanh) để AI cập nhật tọa độ giám sát ngay lập tức.")
]
for step_num, step_desc in steps:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"{step_num} ")
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    p.add_run(step_desc)

p_after = doc.add_paragraph()
p_after.paragraph_format.space_after = Pt(4)
add_image_box(doc, "CHÈN HÌNH ẢNH 3: THAO TÁC CHẤM ĐIỂM VẼ VÙNG ĐA GIÁC", "Chụp ảnh vùng đa giác được vẽ quanh máy kèm ô nhập tên máy và nút Lưu")

# Section 4
add_heading_section(doc, "4. Tra cứu Lịch sử Vi phạm (History)")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
p.add_run("1. Chọn tab 'Lịch sử' (History) trên thanh điều hướng bên trái.")
p2 = doc.add_paragraph()
p2.paragraph_format.space_after = Pt(2)
p2.add_run("2. Bộ lọc: Chọn Khoảng ngày và Vị trí / Máy cần tra cứu.")
p3 = doc.add_paragraph()
p3.paragraph_format.space_after = Pt(6)
p3.add_run("3. Xem bằng chứng: Bấm icon Ảnh để xem/tải ảnh vi phạm độ phân giải cao; Bấm icon Video để phát lại video clip vi phạm (có tua và tải về).")
add_image_box(doc, "CHÈN HÌNH ẢNH 4: BẢNG DANH SÁCH LỊCH SỬ & POP-UP VIDEO", "Chụp bảng lịch sử lọc vi phạm và cửa sổ pop-up phát lại clip bằng chứng")

# Section 5
add_heading_section(doc, "5. Báo cáo & Phân tích Thống kê (Analytics)")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
p.add_run("1. Chọn tab 'Phân tích' (Analysis) trên menu bên trái.")
p2 = doc.add_paragraph()
p2.paragraph_format.space_after = Pt(6)
p2.add_run("2. Theo dõi biểu đồ số lượt vi phạm theo khung giờ/ngày và so sánh tỷ lệ tuân thủ giữa các máy.")
add_image_box(doc, "CHÈN HÌNH ẢNH 5: BIỂU ĐỒ THỐNG KÊ VI PHẠM ANALYTICS", "Chụp màn hình biểu đồ xu hướng vi phạm theo thời gian trong tab Analysis")

# Tip box
tbl_tip = doc.add_table(rows=1, cols=1)
tbl_tip.alignment = WD_TABLE_ALIGNMENT.CENTER
c_tip = tbl_tip.cell(0, 0)
c_tip.width = Inches(6.5)
set_cell_background(c_tip, "EFF6FF")
set_cell_border(c_tip, color="3B82F6", sz="12", val="single")
p_tip = c_tip.paragraphs[0]
p_tip.paragraph_format.space_before = Pt(8)
p_tip.paragraph_format.space_after = Pt(8)
r_tip_icon = p_tip.add_run("GHI NHỚ NHANH THAO TÁC:\n")
r_tip_icon.font.bold = True
r_tip_icon.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
r_tip_content = p_tip.add_run("• Chuột TRÁI: Đặt điểm mốc đa giác.\n• Chuột PHẢI: Hoàn tất khép kín vùng.\n• Định dạng tên máy: Luôn đặt theo dạng may_X (ví dụ: may_1, may_2).")
r_tip_content.font.size = Pt(10)
r_tip_content.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)

output_path = r'c:\Users\it07\Downloads\person_htmp\HTMP_AI_Systems\docs\HUONG_DAN_SU_DUNG.docx'
doc.save(output_path)
print("SUCCESS:", output_path)
