#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Facebook Content Analyzer - تحليل منشورات Facebook وكشف المحتوى الضار
أداة متقدمة للكشف عن الكراهية والعنف والمحتوى الممنوع
"""

import re
import json
from typing import Dict, List, Tuple
from textblob import TextBlob
from langdetect import detect, DetectorFactory
import requests
from urllib.parse import urlparse
import hashlib
from datetime import datetime

DetectorFactory.seed = 0

class ContentAnalyzer:
    """
    محلل محتوى Facebook متقدم
    """
    
    # قائمة الكلمات المحظورة والكراهية
    HATE_SPEECH_KEYWORDS = {
        'arabic': [
            'اقتل', 'تفجير', 'قنبلة', 'سلاح', 'ارهاب', 'ارهابي',
            'كسر', 'ضرب', 'جرح', 'دم', 'موت', 'قتل',
            'شنق', 'حرق', 'تعذيب', 'اغتصاب', 'اغتيال',
            'كافر', 'ملحد', 'زنديق', 'منحرف', 'شاذ',
            'ابن', 'بنت', 'عاهرة', 'قذر', 'وسخ',
            'اسرائيل', 'يهودي', 'مسيحي', 'شيعي', 'سني',
            'سحاق', 'لواط', 'جنس', 'نيك', 'كس'
        ],
        'english': [
            'kill', 'bomb', 'terrorism', 'terrorist', 'murder', 'death',
            'rape', 'assault', 'attack', 'violence', 'violent',
            'hate', 'racist', 'racism', 'sexism', 'sexist',
            'nazi', 'fascist', 'supremacist', 'jewish', 'islam',
            'nigger', 'faggot', 'bitch', 'slut', 'whore',
            'sex', 'porn', 'xxx', 'nude', 'naked'
        ]
    }
    
    # أنواع البلاغات حسب سياسة Facebook
    REPORT_TYPES = {
        'hate_speech': {
            'name': 'خطاب كراهية',
            'description': 'محتوى يهاجم أشخاصاً بناءً على خصائصهم المحمية',
            'severity': 'عالي جداً',
            'action': 'حذف فوري + إيقاف الحساب'
        },
        'violence': {
            'name': 'عنف',
            'description': 'محتوى يحتوي على تهديدات عنيفة أو تشجيع على العنف',
            'severity': 'عالي جداً',
            'action': 'حذف فوري + تحقيق'
        },
        'terrorism': {
            'name': 'إرهاب',
            'description': 'محتوى متعلق بالإرهاب أو تنظيمات إرهابية',
            'severity': 'حرج',
            'action': 'حذف فوري + تسليم للسلطات'
        },
        'sexual_content': {
            'name': 'محتوى جنسي',
            'description': 'محتوى عري أو جنسي صريح',
            'severity': 'عالي',
            'action': 'حذف + تحذير الحساب'
        },
        'exploitation': {
            'name': 'استغلال الأطفال',
            'description': 'محتوى يتضمن استغلال أو إيذاء الأطفال',
            'severity': 'حرج',
            'action': 'حذف فوري + تسليم للسلطات'
        },
        'bullying': {
            'name': 'تنمر',
            'description': 'محتوى يتعرض لأشخاص بالسخرية أو التحقير',
            'severity': 'متوسط',
            'action': 'حذف + تحذير'
        },
        'misinformation': {
            'name': 'معلومات مضللة',
            'description': 'محتوى يحتوي على معلومات كاذبة أو مضللة',
            'severity': 'متوسط',
            'action': 'إضافة تصنيف تحذيري'
        },
        'spam': {
            'name': 'رسائل غير مرغوبة',
            'description': 'محتوى متكرر أو إزعاجي',
            'severity': 'منخفض',
            'action': 'حذف + تحذير'
        },
        'intellectual_property': {
            'name': 'انتهاك الملكية الفكرية',
            'description': 'محتوى ينتهك حقوق الملكية الفكرية',
            'severity': 'متوسط',
            'action': 'حذف + إشعار'
        },
        'harmful_goods': {
            'name': 'بيع منتجات ضارة',
            'description': 'محتوى يروج لبيع منتجات خطرة أو ممنوعة',
            'severity': 'عالي',
            'action': 'حذف + تحقيق'
        },
        'clean': {
            'name': 'محتوى آمن',
            'description': 'المحتوى لا ينتهك أي سياسات',
            'severity': 'لا يوجد',
            'action': 'لا توجد إجراءات'
        }
    }
    
    def __init__(self):
        self.analysis_history = []
    
    def detect_language(self, text: str) -> str:
        """
        كشف لغة النص
        """
        try:
            lang = detect(text)
            return 'arabic' if lang in ['ar'] else 'english'
        except:
            return 'english'
    
    def check_hate_speech(self, text: str) -> Tuple[bool, float]:
        """
        فحص الكلمات المحظورة والكراهية
        العودة: (وجود كراهية، درجة الكراهية من 0-1)
        """
        lang = self.detect_language(text)
        keywords = self.HATE_SPEECH_KEYWORDS.get(lang, [])
        
        text_lower = text.lower()
        hate_count = 0
        
        for keyword in keywords:
            hate_count += len(re.findall(r'\b' + keyword + r'\b', text_lower))
        
        words = len(text_lower.split())
        hate_score = min(1.0, hate_count / max(words, 1))
        
        return hate_count > 0, hate_score
    
    def check_violence(self, text: str) -> Tuple[bool, float]:
        """
        فحص محتوى العنف والتهديدات
        """
        violence_patterns = [
            r'(ايه|اقتل|اذبح|اشنق|احرق|اجرح|اضرب)\s+',
            r'(قتل|ذبح|شنق|حرق|جرح|ضرب)\s+(ب|ك)',
            r'(سلاح|رصاصة|قنبلة|فخخ|متفجرات)\s+',
            r'(تهديد|تجاه|ضد|على)\s+(حياة|بحياة)',
            r'(سأقتل|سأذبح|سأجرح|ستموت)',
            r'(i will kill|kill you|murder|bomb|terrorist)',
            r'(death threat|fuck|harm|beat)',
        ]
        
        text_lower = text.lower()
        violence_count = 0
        
        for pattern in violence_patterns:
            violence_count += len(re.findall(pattern, text_lower))
        
        words = len(text_lower.split())
        violence_score = min(1.0, violence_count / max(words, 1))
        
        return violence_count > 0, violence_score
    
    def check_sexual_content(self, text: str) -> Tuple[bool, float]:
        """
        فحص المحتوى الجنسي
        """
        sexual_patterns = [
            r'(عاري|عريان|ملابس|لباس)\s*(داخلي|سفلي|جنسي)',
            r'(صور|فيديو)\s*(جنسي|ممنوع|محظور)',
            r'(sex|porn|nude|naked|xxx)',
            r'(xxx|18\+|adult)',
        ]
        
        text_lower = text.lower()
        sexual_count = 0
        
        for pattern in sexual_patterns:
            sexual_count += len(re.findall(pattern, text_lower))
        
        words = len(text_lower.split())
        sexual_score = min(1.0, sexual_count / max(words, 1))
        
        return sexual_count > 0, sexual_score
    
    def check_misinformation(self, text: str) -> Tuple[bool, float]:
        """
        فحص المعلومات المضللة
        """
        fake_patterns = [
            r'(كذب|مكذوب|افتراء|اشاعة|خبر كاذب)',
            r'(fake news|hoax|fabricated|false)',
            r'(قال|زعم|يدعي)\s+(بدون|ب)\s+(دليل|برهان)',
        ]
        
        text_lower = text.lower()
        fake_count = 0
        
        for pattern in fake_patterns:
            fake_count += len(re.findall(pattern, text_lower))
        
        words = len(text_lower.split())
        fake_score = min(1.0, fake_count / max(words, 1))
        
        return fake_count > 0, fake_score
    
    def sentiment_analysis(self, text: str) -> Dict:
        """
        تحليل المشاعر في النص
        """
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity  # من -1 (سلبي) إلى 1 (إيجابي)
            subjectivity = blob.sentiment.subjectivity  # من 0 (موضوعي) إلى 1 (ذاتي)
            
            if polarity > 0.1:
                sentiment = 'إيجابي'
            elif polarity < -0.1:
                sentiment = 'سلبي'
            else:
                sentiment = 'محايد'
            
            return {
                'sentiment': sentiment,
                'polarity': round(polarity, 3),
                'subjectivity': round(subjectivity, 3)
            }
        except:
            return {
                'sentiment': 'غير محدد',
                'polarity': 0,
                'subjectivity': 0
            }
    
    def check_spam(self, text: str) -> Tuple[bool, float]:
        """
        فحص الرسائل غير المرغوبة والإزعاجات
        """
        spam_patterns = [
            r'(تابع|اضغط|اشترك|انقر)\s+(هنا|هناك|أسفل)',
            r'(رابط|link)\s+(في|على)\s+(الملف|الصفحة|البيو)',
            r'(اكسب|فوز|جائزة|هدية)\s+(مجاني|بالمجان)',
            r'(follow|click|subscribe|link)',
            r'(.){20,}\1{2,}',  # تكرار نفس الحرف
        ]
        
        text_lower = text.lower()
        spam_count = 0
        
        for pattern in spam_patterns:
            spam_count += len(re.findall(pattern, text_lower))
        
        # فحص التكرار المفرط
        words = text_lower.split()
        if len(words) > 0:
            unique_words = len(set(words))
            repetition_ratio = 1 - (unique_words / len(words))
            spam_count += int(repetition_ratio > 0.5)
        
        spam_score = min(1.0, spam_count / max(len(words), 1))
        
        return spam_count > 0, spam_score
    
    def determine_report_type(self, text: str) -> List[str]:
        """
        تحديد أنواع البلاغات المطلوبة
        """
        report_types = []
        
        hate_detected, hate_score = self.check_hate_speech(text)
        if hate_detected and hate_score > 0.1:
            report_types.append('hate_speech')
        
        violence_detected, violence_score = self.check_violence(text)
        if violence_detected and violence_score > 0.1:
            report_types.append('violence')
        
        if 'ارهاب' in text.lower() or 'terrorism' in text.lower():
            report_types.append('terrorism')
        
        sexual_detected, sexual_score = self.check_sexual_content(text)
        if sexual_detected and sexual_score > 0.1:
            report_types.append('sexual_content')
        
        fake_detected, fake_score = self.check_misinformation(text)
        if fake_detected and fake_score > 0.1:
            report_types.append('misinformation')
        
        spam_detected, spam_score = self.check_spam(text)
        if spam_detected and spam_score > 0.1:
            report_types.append('spam')
        
        if not report_types:
            report_types.append('clean')
        
        return report_types
    
    def analyze_url(self, url: str) -> Dict:
        """
        تحليل الرابط وفحصه
        """
        result = {
            'url': url,
            'is_valid': False,
            'domain': '',
            'suspicious': False,
            'url_hash': hashlib.md5(url.encode()).hexdigest()
        }
        
        try:
            parsed = urlparse(url)
            result['domain'] = parsed.netloc
            result['is_valid'] = True
            
            # فحص النطاقات المشبوهة
            suspicious_domains = ['bit.ly', 'tinyurl', 'short.link']
            if any(domain in result['domain'] for domain in suspicious_domains):
                result['suspicious'] = True
            
            # محاولة الوصول للرابط
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.head(url, timeout=5, headers=headers, allow_redirects=True)
                result['status_code'] = response.status_code
                result['accessible'] = response.status_code == 200
            except:
                result['accessible'] = False
        
        except:
            result['is_valid'] = False
        
        return result
    
    def generate_report(self, text: str, url: str = None, user_info: Dict = None) -> Dict:
        """
        إنشاء تقرير شامل للمحتوى
        """
        report_types = self.determine_report_type(text)
        
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'text_hash': hashlib.sha256(text.encode()).hexdigest(),
            'text_length': len(text),
            'word_count': len(text.split()),
            'language': self.detect_language(text),
            'sentiment': self.sentiment_analysis(text),
            'detected_issues': [],
            'report_recommendations': [],
            'severity_level': 'منخفض',
            'url_analysis': None
        }
        
        # فحص الكراهية
        hate_detected, hate_score = self.check_hate_speech(text)
        if hate_detected:
            analysis['detected_issues'].append({
                'type': 'خطاب كراهية',
                'score': round(hate_score, 3),
                'confidence': round(hate_score * 100, 1)
            })
        
        # فحص العنف
        violence_detected, violence_score = self.check_violence(text)
        if violence_detected:
            analysis['detected_issues'].append({
                'type': 'عنف',
                'score': round(violence_score, 3),
                'confidence': round(violence_score * 100, 1)
            })
        
        # فحص المحتوى الجنسي
        sexual_detected, sexual_score = self.check_sexual_content(text)
        if sexual_detected:
            analysis['detected_issues'].append({
                'type': 'محتوى جنسي',
                'score': round(sexual_score, 3),
                'confidence': round(sexual_score * 100, 1)
            })
        
        # فحص المعلومات المضللة
        fake_detected, fake_score = self.check_misinformation(text)
        if fake_detected:
            analysis['detected_issues'].append({
                'type': 'معلومات مضللة',
                'score': round(fake_score, 3),
                'confidence': round(fake_score * 100, 1)
            })
        
        # فحص الرسائل غير المرغوبة
        spam_detected, spam_score = self.check_spam(text)
        if spam_detected:
            analysis['detected_issues'].append({
                'type': 'رسائل غير مرغوبة',
                'score': round(spam_score, 3),
                'confidence': round(spam_score * 100, 1)
            })
        
        # إضافة توصيات البلاغات
        for report_type in report_types:
            if report_type in self.REPORT_TYPES:
                analysis['report_recommendations'].append({
                    'type': report_type,
                    'name': self.REPORT_TYPES[report_type]['name'],
                    'description': self.REPORT_TYPES[report_type]['description'],
                    'severity': self.REPORT_TYPES[report_type]['severity'],
                    'action': self.REPORT_TYPES[report_type]['action']
                })
        
        # تحديد درجة الخطورة
        if any(r['severity'] == 'حرج' for r in analysis['report_recommendations']):
            analysis['severity_level'] = 'حرج'
        elif any(r['severity'] == 'عالي جداً' for r in analysis['report_recommendations']):
            analysis['severity_level'] = 'عالي جداً'
        elif any(r['severity'] == 'عالي' for r in analysis['report_recommendations']):
            analysis['severity_level'] = 'عالي'
        elif any(r['severity'] == 'متوسط' for r in analysis['report_recommendations']):
            analysis['severity_level'] = 'متوسط'
        
        # تحليل الرابط إذا كان موجوداً
        if url:
            analysis['url_analysis'] = self.analyze_url(url)
        
        # إضافة معلومات المستخدم إذا كانت موجودة
        if user_info:
            analysis['user_info'] = user_info
        
        self.analysis_history.append(analysis)
        return analysis


def main():
    """
    الدالة الرئيسية
    """
    analyzer = ContentAnalyzer()
    return analyzer


if __name__ == '__main__':
    main()
