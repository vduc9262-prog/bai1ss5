branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3


for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch} ,tháng {month}: "))
    print()


for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        print(f"Chi nhánh {branch} ,tháng {month} : {revenue} triệu đồng")

# Vì sao cách duyệt này khiến báo cáo không gom dữ liệu theo từng chi nhánh?
# vì thiếu print() ở vòng lặp month 

# Vì vòng lặp ngoài là tháng, nên chương trình nhập và in theo tháng trước.

# Theo yêu cầu nghiệp vụ, vòng lặp ngoài nên duyệt theo chi nhánh hay theo tháng?
# Vòng lặp trong nên duyệt theo chi nhánh hay theo tháng?
# Vòng lặp ngoài nên duyệt theo Chi nhánh
# Vòng lặp trong nên duyệt theo Tháng
