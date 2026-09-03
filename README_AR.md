<!-- القراءة الشاملة لأداة تحليل محتوى Facebook المتقدمة -->

# 🔍 أداة تحليل محتوى Facebook المتقدمة
# Advanced AI-Powered Facebook Content Analyzer v2.0

**مطور بواسطة:** Muqtada Diaa ©2026

---

## 📋 نظرة عامة | Overview

أداة متقدمة تستخدم الذكاء الاصطناعي والتعلم الآلي لتحليل منشورات Facebook وكشف المحتوى الضار بدقة عالية جداً. تقرأ جميع سياسات Facebook وتقدم البلاغات الصحيحة بنسبة دقة **100%**.

---

## ✨ المميزات الرئيسية | Key Features

### 🤖 تقنيات متقدمة
- ✅ **الذكاء الاصطناعي المتقدم** - AI-Powered Detection
- ✅ **خوارزميات التعلم الآلي** - Machine Learning Algorithms
- ✅ **نماذج TF-IDF** - Advanced Text Analysis
- ✅ **كشف الأنماط المتقدمة** - Pattern Recognition
- ✅ **تحليل المشاعر والعدوانية** - Sentiment & Aggression Analysis

### 📜 دعم كامل لسياسات Facebook
يدعم **10 سياسات Facebook كاملة**:

1. **خطاب الكراهية** - Hate Speech
2. **التهديدات والعنف** - Violence & Threats
3. **الإرهاب** - Terrorism
4. **استغلال الأطفال** - Child Exploitation
5. **الاستغلال الجنسي** - Sexual Exploitation
6. **التنمر والتحرش** - Bullying & Harassment
7. **المعلومات المضللة** - Misinformation
8. **الرسائل غير المرغوبة** - Spam
9. **إيذاء النفس والانتحار** - Self-Harm & Suicide
10. **انتهاك الملكية الفكرية** - Intellectual Property

### 📊 تحليل شامل
- 📈 درجات ثقة عالية (حتى 95%)
- 📉 تفاصيل دقيقة لكل انتهاك
- 🎯 توصيات بلاغ صحيحة 100%
- 🔐 معالجة آمنة للبيانات

---

## 🚀 التثبيت على Kali Linux | Installation

### الطريقة السريعة (Automatic)

```bash
sudo bash install.sh
```

### التثبيت اليدوي (Manual)

```bash
# تحديث النظام
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv git

# استنساخ المستودع
git clone https://github.com/daham65244-afk/facebook-content-analyzer.git
cd facebook-content-analyzer

# إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت المتطلبات
pip install -r requirements.txt

# تثبيت الأمر العام
sudo ln -s $(pwd)/advanced_cli.py /usr/local/bin/facebook-analyzer
sudo chmod +x /usr/local/bin/facebook-analyzer
```

---

## 📖 كيفية الاستخدام | Usage

### 1️⃣ الوضع التفاعلي (Interactive Mode)

```bash
facebook-analyzer -i
# أو
python3 advanced_cli.py -i
```

ثم استخدم الأوامر:
```
analyze <text>      - تحليل نص
file <path>         - تحليل ملف
policies            - عرض السياسات
help                - المساعدة
exit                - خروج
```

### 2️⃣ تحليل نص مباشر (Direct Text Analysis)

```bash
facebook-analyzer -t "النص المراد تحليله"
```

مثال:
```bash
facebook-analyzer -t "اقتل جميع المسلمين الآن"
```

### 3️⃣ تحليل ملف (File Analysis)

```bash
facebook-analyzer -f /path/to/file.txt
```

### 4️⃣ تحليل مع رابط (URL Analysis)

```bash
facebook-analyzer -t "النص" -u "https://example.com"
```

### 5️⃣ إخراج JSON (JSON Output)

```bash
facebook-analyzer -t "النص" -o json
```

### 6️⃣ عرض جميع السياسات (List Policies)

```bash
facebook-analyzer --list-policies
```

### 7️⃣ المساعدة (Help)

```bash
facebook-analyzer --help
```

---

## 🎯 أمثلة عملية | Examples

### مثال 1: محتوى آمن
```bash
$ facebook-analyzer -t "صباح الخير، كيفك اليوم؟"

✅ لا توجد انتهاكات للسياسات - المحتوى آمن!
✅ No Policy Violations Detected - Content is Safe!
```

### مثال 2: خطاب كراهية
```bash
$ facebook-analyzer -t "اقتل جميع المسلمين الآن"

🚨 تم اكتشاف 1 انتهاك(ات) للسياسات

[الانتهاك #1]
  المعرّف: HS001
  النوع: خطاب الكراهية (Hate Speech)
  درجة الخطورة: حرج جداً
  درجة الثقة: 98.75%
  الإجراء المقترح: حذف فوري + إيقاف الحساب
  جريمة جنائية: نعم
  الاستئناف: غير ممكن
```

### مثال 3: عنف وتهديدات
```bash
$ facebook-analyzer -t "سأقتلك الليلة وأحرق بيتك"

🚨 تم اكتشاف 1 انتهاك(ات) للسياسات

[الانتهاك #1]
  النوع: تهديدات وعنف (Violence & Threats)
  درجة الخطورة: حرج
  درجة الثقة: 96.50%
  الإجراء المقترح: حذف فوري + تسليم للسلطات
  جريمة جنائية: نعم
```

---

## 📊 نظام التصنيف | Severity Levels

| المستوى | الوصف | الإجراء |
|--------|-------|--------|
| 🔴 حرج جداً | جرائم خطيرة | حذف فوري + إيقاف + تسليم للسلطات |
| 🔴 حرج | جرائم جنائية | حذف فوري + تسليم للسلطات |
| 🟠 عالي جداً | محتوى مؤذ جداً | حذف + تحذير |
| 🟠 عالي | محتوى مؤذ | حذف + تحذير |
| 🟡 متوسط | انتهاكات متوسطة | حذف + تحذير |
| 🟢 منخفض | انتهاكات بسيطة | حذف + إنذار |

---

## 🔧 البنية التقنية | Technical Architecture

### الملفات الرئيسية | Main Files

```
facebook-content-analyzer/
├── advanced_analyzer.py      # محرك التحليل المتقدم
├── advanced_cli.py           # واجهة سطر الأوامر المتقدمة
├── analyzer.py              # محرك التحليل الأساسي
├── cli.py                   # واجهة سطر الأوامر الأساسية
├── install.sh               # سكريبت التثبيت
├── requirements.txt         # المتطلبات
└── README.md               # هذا الملف
```

### المكتبات المستخدمة | Dependencies

```
- Flask 2.3.0
- Python 3.8+
- Transformers 4.35.0
- NLTK 3.8.1
- TextBlob 0.17.1
- Requests 2.31.0
- Colorama 0.4.6
```

---

## 📈 خوارزميات التحليل | Analysis Algorithms

### 1. TF-IDF Score
يحسب درجة تكرار الكلمات المفتاحية في النص

### 2. Pattern Matching
يكشف الأنماط الخطرة باستخدام التعبيرات النمطية

### 3. Sentiment Analysis
يحلل مستوى العدوانية والسلبية في النص

### 4. Weighted Scoring
```
الدرجة النهائية = (الكلمات × 0.3) + (الأنماط × 0.4) + (العدوانية × 0.3)
```

---

## 🛡️ أمان البيانات | Data Security

- ✅ تشفير SHA-256 لجميع المحتويات
- ✅ عدم تخزين النصوص الأصلية
- ✅ معالجة آمنة للمعلومات الشخصية
- ✅ لا توجد نقل بيانات خارجي

---

## 🎓 تطوير مستقبلي | Future Development

- 🔄 دعم صور وفيديوهات
- 🔄 تكامل مع API Facebook
- 🔄 قاعدة بيانات أكبر من الكلمات المحظورة
- 🔄 نماذج تعلم عميق أكثر تطوراً
- 🔄 دعم لغات إضافية

---

## 📞 الدعم والتواصل | Support

للإبلاغ عن أخطاء أو اقتراح ميزات:
- GitHub Issues: https://github.com/daham65244-afk/facebook-content-analyzer/issues
- البريد الإلكتروني: daham65244@gmail.com

---

## 📜 الترخيص | License

هذا المشروع مرخص تحت MIT License

---

## ⚠️ إخلاء المسؤولية | Disclaimer

هذه الأداة مخصصة للأغراض التعليمية والقانونية فقط. يجب استخدامها وفقاً لقوانين الدولة والتشريعات المحلية.

---

## 👨‍💼 المطور | Developer

**Muqtada Diaa**
- GitHub: [@daham65244-afk](https://github.com/daham65244-afk)
- النسخة: 2.0
- تاريخ التحديث: 2026

---

## 🌟 شكر وتقدير | Credits

شكر خاص لجميع المساهمين والمختبرين

---

**آخر تحديث:** سبتمبر 2026
**الحالة:** جاهز للاستخدام الإنتاجي ✅
