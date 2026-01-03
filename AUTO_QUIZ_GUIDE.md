# 🎯 AUTO-QUIZ SYSTEM - ZERO CONFIG!

## ✨ **CÁCH SỬ DỤNG CỰC ĐƠN GIẢN**

### **Chỉ cần 2 bước:**

#### **Bước 1: Tạo file JSON**
```bash
# Tạo file quiz mới ở đâu cũng được trong questions/
questions/python/data-types.json
questions/python/functions.json
questions/macroeconomics/is-lm.json
```

#### **Bước 2: Chạy script**
```bash
python generate_manifest.py
```

**XONG!** 🎉 Không cần sửa code gì cả!

---

## 🚀 **WORKFLOW HOÀN CHỈNH**

```bash
# 1. Tạo file JSON mới
# Ví dụ: questions/python/loops.json

# 2. Generate manifest
python generate_manifest.py

# 3. Test local
python -m http.server 8000
# Mở http://localhost:8000/index.html

# 4. Push lên GitHub
git add .
git commit -m "Add new quiz"
git push
```

**Dropdown tự động cập nhật!** ✨

---

## 📂 **NAMING CONVENTION**

File name sẽ tự động convert thành display name:

| **File** | **Hiển thị** |
|----------|--------------|
| `basics.json` | Basics |
| `data-types.json` | Data Types |
| `is-lm-model.json` | Is Lm Model |
| `gdp-cpi.json` | Gdp Cpi |

**Subject** được lấy từ tên folder:
- `python/` → 🐍 Python
- `macroeconomics/` → 📊 Macroeconomics  
- `data-structures/` → 🗂️ Data Structures

---

## 🎨 **CUSTOM EMOJI**

Muốn thêm emoji cho môn mới? Edit `generate_manifest.py`:

```python
subject_emojis = {
    'python': '🐍',
    'macroeconomics': '📊',
    'data-structures': '🗂️',
    'calculus': '📐',        # ← THÊM MỚI
    'statistics': '📈',      # ← THÊM MỚI
    'default': '📚'
}
```

---

## ✅ **LỢI ÍCH**

1. ✅ **Zero config** - Không cần sửa index.html
2. ✅ **Auto-detect** - Tự động tìm file JSON
3. ✅ **Auto-count** - Tự động đếm số câu hỏi
4. ✅ **Auto-dropdown** - Tự động build dropdown
5. ✅ **Giảm sai sót** - Không cần thao tác thủ công

---

## 🔧 **TROUBLESHOOTING**

### **Lỗi: "Failed to load manifest"**
```bash
# Chạy lại script
python generate_manifest.py
```

### **Quiz không xuất hiện trong dropdown**
```bash
# Kiểm tra file JSON có valid không
python -m json.tool questions/python/new-quiz.json

# Generate lại manifest
python generate_manifest.py
```

### **Emoji không hiển thị**
Thêm vào `subject_emojis` trong `generate_manifest.py`

---

## 🎯 **VÍ DỤ THỰC TẾ**

### **Thêm 3 quiz Python mới:**

```bash
# 1. Tạo file
echo [] > questions/python/data-types.json
echo [] > questions/python/functions.json  
echo [] > questions/python/oop.json

# 2. Thêm câu hỏi vào file (dùng AI hoặc tự viết)

# 3. Generate manifest
python generate_manifest.py

# 4. Reload browser
# → Thấy 3 quiz mới trong dropdown Python! ✨
```

---

## 🚀 **ADVANCED: AUTO-DEPLOY**

Thêm vào `.github/workflows/deploy.yml`:

```yaml
- name: Generate quiz manifest
  run: python generate_manifest.py

- name: Deploy to GitHub Pages
  run: |
    git add questions/manifest.json
    git commit -m "Auto-update manifest" || true
    git push
```

**Mỗi lần push → tự động update manifest!** 🎉

---

**Enjoy zero-config quiz creation! 🚀**
