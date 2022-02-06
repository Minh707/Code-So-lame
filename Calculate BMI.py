#vietnames
print("Chào mừng bạn đến với máy tính BMI của Minh707.")

# Cung cấp chuyển đổi đo lường
Offer_Conversions = input("Bạn có muốn chuyển đổi đơn vị đo lường feet sang hệ mét không? (yes / no): ")

if Offer_Conversions == "yes":
    Imperial_Weight = input("Cân nặng của bạn tính bằng bao nhiêu?: ")
    Imperial_Height = input("Chiều cao của bạn tính bằng feet là bao nhiêu(Hệ thập phân)?: ")

    Imperial_Weight = float(Imperial_Weight)
    Imperial_Height = float(Imperial_Height)

    Metric_Converted_Weight = Imperial_Weight * 2.205
    Metric_Converted_Height = Imperial_Height * 30.48

    Metric_Converted_Weight = str(Metric_Converted_Weight)
    Metric_Converted_Height = str(Metric_Converted_Height)

    print("Trọng lượng chỉ số của bạn là " + Metric_Converted_Weight + " kg, hãy lưu ý điều này cho giai đoạn tiếp theo.")
    print("Chiều cao chỉ số của bạn là " + Metric_Converted_Height + " cm, hãy lưu ý điều này cho giai đoạn tiếp theo.")
    print("--")
elif Offer_Conversions == "no":
    print("--")

# Thu thập dữ liệu

Age = input("Đặt tuổi của bạn: ")
Weight = input("Tính trọng lượng của bạn tính bằng KG: ")
Height = input("Đặt chiều cao của bạn trong CM: ")

# Tính công thức BMI

Weight = float(Weight)
Height = float(Height)

Height_Squared = Height * Height
BMI_Formula_Assisted = Weight / Height_Squared
BMI_Formula_Completed = BMI_Formula_Assisted * 10000

# Hiển thị biểu đồ sức khỏe

BMI_Formula_Completed =  str(BMI_Formula_Completed)

print("Bạn có chỉ số BMI là " + BMI_Formula_Completed + ".")

BMI_Formula_Completed = float(BMI_Formula_Completed)

if BMI_Formula_Completed <= 18.5:
    print("Bạn đang thiếu cân, hãy cân nhắc tăng cân để đưa chỉ số BMI của bạn từ 20 đến 25.")
elif BMI_Formula_Completed <= 25:
    print("Bạn hoàn toàn khỏe mạnh với chỉ số BMI nằm trong khoảng từ 20 đến 25.")
elif BMI_Formula_Completed <= 30:
    print("Bạn đang thừa cân, hãy nói chuyện với bác sĩ về việc đặt cho mình một chỉ số BMI mục tiêu mới từ 20 đến 25.")
elif BMI_Formula_Completed >= 30.1:
    print("Bạn bị béo phì, bạn cần giảm chỉ số BMI của mình xuống từ 20 đến 25, nếu không bạn có thể gặp rủi ro.")
print("Program by Minh707.")
