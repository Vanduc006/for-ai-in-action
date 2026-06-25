# Viết hàm clean_and_count(text) thực hiện đúng pipeline tiền xử lý:

# Chuẩn hóa khoảng trắng thừa (gộp nhiều space về 1, bỏ space đầu/cuối).
# Chuyển toàn bộ về chữ thường.
# Loại bỏ ký tự đặc biệt / dấu câu (chỉ giữ chữ và khoảng trắng).
# Tách từ (tokenize).
# Trả về dict đếm tần suất xuất hiện của mỗi từ, và in ra từ xuất hiện nhiều nhất.

def clean_and_count(text):
    text_dict = {}
    for i in text.split(" "):
        if (i != ''):
            # print(i)
            clean_word = "".join([char for char in i if char.isalpha()])
            
            word = clean_word.lower()
            # print(clean_word)
            if word in text_dict:
                text_dict[word] += 1
            else:
                text_dict[word] = 1
    return text_dict
    
raw = "  Khách HÀNG rất hài lòng!! Sản phẩm tốt, sản phẩm bền... Giao hàng NHANH.  "
result_dict = clean_and_count(raw)

most_frequent_word = max(result_dict, key=result_dict.get)
max_count = result_dict[most_frequent_word]
print(f"{most_frequent_word} : {max_count}")
