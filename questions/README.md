# 📚 Questions Directory - Organized Structure

## 🗂️ Cấu trúc phân cấp theo môn học

```
questions/
├── python/                    (Môn Python)
│   ├── basics.json           (14 câu - Cú pháp cơ bản)
│   ├── data-types.json       (Coming soon)
│   └── functions.json        (Coming soon)
│
├── macroeconomics/           (Môn Kinh tế vĩ mô)
│   ├── gdp-cpi.json         (3 câu - GDP & CPI)
│   └── is-lm.json           (Coming soon)
│
├── data-structures/          (Môn Cấu trúc dữ liệu)
│   ├── basics.json          (3 câu - Stack, Queue)
│   └── trees.json           (Coming soon)
│
└── README.md                 (File này)
```

---

## 🤖 **PROMPT TẠO QUIZ - OUTPUT JSON THUẦN TÚY**

### **Copy prompt này gửi cho AI:**

```
You are an assistant that generates multiple-choice quiz questions for studying.

I will give you a block of English text containing study material.

Your task is:

1. Analyze the text and identify all key topics and concepts.
2. Do not skip any topic in the input text.
3. For each concept, generate at least 2–3 questions covering different aspects (definition, notation, example, application).
4. Ensure questions are evenly distributed across all topics so the whole text is fully covered.
5. Each question must have 4 options: one correct and three plausible distractors.
6. Generate questions at different difficulty levels:
   - Easy: basic definitions and simple facts.
   - Medium: applying concepts in examples or problem situations.
   - Hard: extended reasoning, comparisons, or less direct questions.

---

**OUTPUT FORMAT - PURE JSON ARRAY:**

Generate ONLY a valid JSON array (NOT JavaScript). Output must be copy-pasteable directly into a .json file.

**CRITICAL RULES:**
- ✅ Output ONLY: `[...]` (pure JSON array)
- ✅ Use DOUBLE quotes for all strings (JSON standard)
- ✅ NO template literals (backticks)
- ✅ NO trailing commas
- ✅ Valid JSON syntax only

**JSON Structure:**

[
    {
        "id": 1,
        "question": "Your question text here (with Vietnamese translations for difficult terms)",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct": 0,
        "explanation": "Brief explanation of why this answer is correct",
        "difficulty": "easy",
        "topic": "Main topic name"
    },
    {
        "id": 2,
        "question": "Second question...",
        "options": ["...", "...", "...", "..."],
        "correct": 2,
        "explanation": "...",
        "difficulty": "medium",
        "topic": "..."
    }
]

---

**CODE BLOCK FORMATTING:**

For questions with code, use HTML tags with proper JSON escaping:

**Example 1: Simple code**
```json
{
    "id": 1,
    "question": "What is the output?<pre class=\"code-block\">x = 5\\ny = 10\\nprint(x + y)</pre>",
    "options": ["5", "10", "15", "Error"],
    "correct": 2,
    "explanation": "x + y = 5 + 10 = 15",
    "difficulty": "easy",
    "topic": "Basic Operations"
}
```

**Example 2: Multi-line code**
```json
{
    "id": 2,
    "question": "What does this function return?<pre class=\"code-block\">def calculate(a, b):\\n    if a > b:\\n        return a - b\\n    else:\\n        return a + b\\n\\nresult = calculate(5, 3)</pre>",
    "options": ["2", "8", "5", "3"],
    "correct": 0,
    "explanation": "Since 5 > 3, it returns 5 - 3 = 2",
    "difficulty": "medium",
    "topic": "Functions"
}
```

**JSON Escaping Rules:**
- `\"` for double quotes
- `\\n` for newlines
- `\\` for backslashes
- NO single quotes (use double quotes only)

---

**VALIDATION CHECKLIST:**

Before submitting, verify:
- [ ] Output is PURE JSON (starts with `[`, ends with `]`)
- [ ] All strings use double quotes (not single quotes or backticks)
- [ ] All code blocks use `<pre class=\"code-block\">` with proper escaping
- [ ] All `correct` indices are valid (0-3)
- [ ] All `difficulty` values are: "easy", "medium", or "hard"
- [ ] NO trailing comma after last object
- [ ] Valid JSON syntax (test with json.org validator)
- [ ] All questions have non-empty `explanation`
- [ ] IDs increment sequentially from 1

---

**COMMON MISTAKES TO AVOID:**

❌ **WRONG - JavaScript syntax:**
```javascript
const questions = [...]  // ❌ NO! This is JavaScript
```

✅ **CORRECT - Pure JSON:**
```json
[...]  // ✅ YES! Pure JSON array
```

❌ **WRONG - Single quotes:**
```json
{'question': 'text'}  // ❌ JSON requires double quotes
```

✅ **CORRECT - Double quotes:**
```json
{"question": "text"}  // ✅ Valid JSON
```

❌ **WRONG - Trailing comma:**
```json
[
    {...},
    {...},  // ❌ Last comma breaks JSON
]
```

✅ **CORRECT - No trailing comma:**
```json
[
    {...},
    {...}   // ✅ No comma after last item
]
```

❌ **WRONG - Unescaped newlines:**
```json
{"question": "Line 1
Line 2"}  // ❌ Literal newline breaks JSON
```

✅ **CORRECT - Escaped newlines:**
```json
{"question": "Line 1\\nLine 2"}  // ✅ Escaped \\n
```

---

**QUALITY CHECK:**

After generating all questions, verify:

1. **Coverage:** "Does this quiz cover ALL main concepts from the input text?"
   - If NO → Add more questions for missing topics

2. **Distribution:** "Are questions evenly spread?" (aim: 40% easy, 40% medium, 20% hard)
   - If NO → Adjust difficulty levels

3. **Validity:** "Can I copy-paste this into a .json file without ANY edits?"
   - If NO → Fix JSON syntax errors

4. **Completeness:** "Would a student understand all key concepts by studying these questions?"
   - If NO → Add clarifying questions

---

**LANGUAGE:**
- Questions: English with Vietnamese translations for technical terms
  - Example: "linear programming (quy hoạch tuyến tính)"
- Explanations: Brief but clear (1-2 sentences)

---

**PERFORMANCE:**
Generate ALL questions before ending output. Do not truncate or summarize.

---

**OUTPUT ONLY:**
A valid JSON array that can be directly saved to a .json file.
NO explanatory text before or after the array.
NO markdown code blocks wrapping the output.
```

---

## 📝 **CÁCH SỬ DỤNG PROMPT**

### **Bước 1: Copy prompt trên**

### **Bước 2: Gửi cho AI kèm tài liệu:**
```
[PASTE PROMPT TRÊN]

Tài liệu đính kèm: [paste slide/text ở đây]
```

### **Bước 3: Copy output và lưu vào file:**
```bash
# AI trả về:
[
    {"id": 1, "question": "...", ...},
    {"id": 2, "question": "...", ...}
]

# Copy và paste vào file:
questions/python/new-topic.json
```

### **Bước 4: Validate JSON:**
```bash
# Kiểm tra JSON hợp lệ
python -m json.tool questions/python/new-topic.json

# Nếu OK → Generate manifest
python generate_manifest.py
```

---

## ✅ **LỢI ÍCH CỦA PROMPT MỚI**

1. ✅ **Output thuần JSON** - Copy-paste trực tiếp
2. ✅ **Không cần edit** - Đúng format ngay từ đầu
3. ✅ **Validation tự động** - AI tự check trước khi output
4. ✅ **Giảm sai sót** - Không cần convert từ JS sang JSON

---

**ZERO CONFIG - CHỈ CẦN:**
1. Tạo file JSON từ AI output
2. `python generate_manifest.py`
3. **XONG!** ✨
