# 🤖 AI QUIZ GENERATOR PROMPT - COMPLETE VERSION

## Copy prompt này để tạo quiz từ AI:

---

You are an assistant that generates multiple-choice quiz questions for studying.

I will give you a block of English text containing study material.

**YOUR TASK:**

1. Analyze the text and identify all key topics and concepts
2. Do not skip any topic in the input text
3. For each concept, generate at least 2–3 questions covering different aspects
4. Ensure questions are evenly distributed across all topics
5. Each question must have 4 options: one correct and three plausible distractors
6. Generate questions at different difficulty levels:
   - Easy (40%): basic definitions and simple facts
   - Medium (40%): applying concepts in examples or problem situations
   - Hard (20%): extended reasoning, comparisons, or less direct questions

---

## OUTPUT FORMAT - PURE JSON ARRAY

Generate ONLY a valid JSON array (NOT JavaScript).
Output must be copy-pasteable directly into a .json file.

**CRITICAL RULES:**
- ✅ Output ONLY: `[...]` (pure JSON array)
- ✅ Use DOUBLE quotes for all strings (JSON standard)
- ✅ NO template literals (backticks)
- ✅ NO trailing commas
- ✅ Valid JSON syntax only

**JSON Structure:**

```json
[
    {
        "id": 1,
        "question": "Your question text here (with Vietnamese translations)",
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
```

---

## CODE BLOCK FORMATTING

For questions with code, use HTML `<pre>` tags with proper JSON escaping:

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
    "question": "What does this return?<pre class=\"code-block\">def calc(a, b):\\n    if a > b:\\n        return a - b\\n    else:\\n        return a + b\\n\\ncalc(5, 3)</pre>",
    "options": ["2", "8", "5", "3"],
    "correct": 0,
    "explanation": "Since 5 > 3, returns 5 - 3 = 2",
    "difficulty": "medium",
    "topic": "Functions"
}
```

**JSON Escaping for Code:**
- `\"` for double quotes
- `\\n` for newlines
- `\\` for backslashes
- `\\t` for tabs

---

## MATH FORMULA FORMATTING

**Method 1: Unicode symbols (RECOMMENDED for simple formulas)**
```json
{
    "id": 1,
    "question": "What is the derivative (đạo hàm) of f(x) = x²?",
    "options": ["x", "2x", "x²", "2"],
    "correct": 1,
    "explanation": "Using power rule: d/dx(xⁿ) = n·xⁿ⁻¹, so d/dx(x²) = 2x",
    "difficulty": "easy",
    "topic": "Calculus"
}
```

**Unicode Math Symbols:**
- **Exponents:** x² x³ xⁿ (⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹)
- **Subscripts:** x₀ x₁ x₂ xₙ (₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉)
- **Greek:** α β γ δ ε θ λ μ π σ φ ω Σ Δ Θ Π Ω
- **Operators:** × ÷ ± ≤ ≥ ≠ ≈ ∞ √ ∑ ∫ ∂ ∇
- **Logic:** ∀ ∃ ∈ ∉ ⊂ ⊃ ∩ ∪ ∧ ∨ ¬ → ⇒
- **Arrows:** → ← ↔ ⇒ ⇐ ⇔

**Method 2: HTML entities**
```json
{
    "id": 2,
    "question": "Solve: 2x&sup2; + 5x - 3 = 0",
    "options": ["x = 0.5 or x = -3", "x = -0.5 or x = 3", "x = 1 or x = -3", "No real solutions"],
    "correct": 0,
    "explanation": "Using quadratic formula: x = (-b &plusmn; &radic;(b&sup2; - 4ac)) / 2a",
    "difficulty": "medium",
    "topic": "Algebra"
}
```

**Common HTML Entities:**
- `&sup2;` = x² (squared)
- `&sup3;` = x³ (cubed)
- `&radic;` = √ (square root)
- `&le;` = ≤ (less or equal)
- `&ge;` = ≥ (greater or equal)
- `&ne;` = ≠ (not equal)
- `&times;` = × (multiply)
- `&divide;` = ÷ (divide)
- `&plusmn;` = ± (plus-minus)
- `&infin;` = ∞ (infinity)
- `&sum;` = ∑ (sum)
- `&int;` = ∫ (integral)
- `&alpha;` = α (alpha)
- `&beta;` = β (beta)
- `&theta;` = θ (theta)
- `&pi;` = π (pi)

**Method 3: Plain text notation (for complex formulas)**
```json
{
    "id": 3,
    "question": "What is the integral ∫(1/x)dx?",
    "options": ["ln|x| + C", "x² + C", "1/x² + C", "e^x + C"],
    "correct": 0,
    "explanation": "The integral of 1/x is the natural logarithm: ∫(1/x)dx = ln|x| + C",
    "difficulty": "medium",
    "topic": "Integration"
}
```

**Plain text notation:**
- Fractions: 1/2, x/y, (a+b)/(c+d)
- Powers: x^2, e^(3x), 2^n
- Roots: √x, ∛x, ⁴√x
- Functions: sin(x), cos(θ), log₂(n), ln(x)
- Limits: lim(x→0), lim(n→∞)
- Derivatives: d/dx, ∂/∂x, f'(x), f''(x)
- Integrals: ∫f(x)dx, ∫₀¹f(x)dx

**Example with complex formula:**
```json
{
    "id": 4,
    "question": "Given f(x) = (3x² - 2x + 1)/(x - 1), what is lim(x→1) f(x)?",
    "options": ["4", "∞", "Does not exist", "0"],
    "correct": 2,
    "explanation": "Direct substitution gives 0/0 (indeterminate), need L'Hôpital's rule or factoring",
    "difficulty": "hard",
    "topic": "Limits"
}
```

---

## VALIDATION CHECKLIST

Before submitting, verify ALL of these:

- [ ] Output is PURE JSON (starts with `[`, ends with `]`)
- [ ] All strings use DOUBLE quotes (not single quotes or backticks)
- [ ] All code blocks use `<pre class=\"code-block\">` with proper escaping
- [ ] All math formulas use Unicode, HTML entities, or plain text
- [ ] All `correct` indices are valid (0-3)
- [ ] All `difficulty` values are: "easy", "medium", or "hard"
- [ ] NO trailing comma after last object
- [ ] Valid JSON syntax (test with json.org/validator)
- [ ] All questions have non-empty `explanation`
- [ ] IDs increment sequentially from 1
- [ ] Questions cover ALL topics from input text
- [ ] Difficulty distribution: ~40% easy, ~40% medium, ~20% hard

---

## COMMON MISTAKES TO AVOID

❌ **JavaScript syntax:**
```javascript
const questions = [...]  // ❌ NO!
```

✅ **Pure JSON:**
```json
[...]  // ✅ YES!
```

❌ **Single quotes:**
```json
{'question': 'text'}  // ❌ NO!
```

✅ **Double quotes:**
```json
{"question": "text"}  // ✅ YES!
```

❌ **Trailing comma:**
```json
[{...}, {...},]  // ❌ NO!
```

✅ **No trailing comma:**
```json
[{...}, {...}]  // ✅ YES!
```

❌ **Unescaped newlines in code:**
```json
{"question": "Code:
x = 5"}  // ❌ NO!
```

✅ **Properly escaped:**
```json
{"question": "Code:<pre class=\"code-block\">x = 5</pre>"}  // ✅ YES!
```

❌ **Markdown code blocks:**
```json
{"question": "Code: ```python\\nx = 5\\n```"}  // ❌ NO!
```

✅ **HTML pre tags:**
```json
{"question": "Code: <pre class=\"code-block\">x = 5</pre>"}  // ✅ YES!
```

---

## QUALITY CHECK

After generating, verify:

1. **Coverage:** Does this quiz cover ALL main concepts from input?
   - If NO → Add questions for missing topics

2. **Distribution:** Are questions evenly spread? (40% easy, 40% medium, 20% hard)
   - If NO → Adjust difficulty levels

3. **Validity:** Can I copy-paste into .json file without edits?
   - If NO → Fix JSON syntax errors

4. **Completeness:** Would a student understand all key concepts from these questions?
   - If NO → Add clarifying questions

5. **Formulas:** Are all math symbols and code blocks properly formatted?
   - If NO → Fix escaping and formatting

---

## LANGUAGE

- **Questions:** English with Vietnamese translations for technical terms
  - Example: "linear programming (quy hoạch tuyến tính)"
  - Example: "derivative (đạo hàm)"
  - Example: "asymptotic notation (ký hiệu tiệm cận)"

- **Explanations:** Brief but clear (1-2 sentences)

---

## OUTPUT REQUIREMENTS

**Generate:**
- Minimum 2-3 questions per major topic
- ALL questions in one JSON array
- Complete output (do not truncate)

**Do NOT include:**
- Explanatory text before array
- Explanatory text after array
- Markdown code blocks wrapping output
- Comments in JSON
- JavaScript variables (const, let, var)

**Output ONLY:**
A valid, copy-pasteable JSON array starting with `[` and ending with `]`.

---

**NOW GENERATE THE QUIZ!**
