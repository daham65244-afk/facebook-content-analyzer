#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
واجهة سطر الأوامر لأداة تحليل Facebook
CLI Interface for Facebook Content Analyzer
"""

import argparse
import json
import sys
from pathlib import Path
from analyzer import ContentAnalyzer
from colorama import Fore, Back, Style, init
from tabulate import tabulate
from datetime import datetime

# تهيئة colorama للألوان على جميع الأنظمة
init(autoreset=True)

class FacebookAnalyzerCLI:
    """
    واجهة سطر الأوامر
    """
    
    def __init__(self):
        self.analyzer = ContentAnalyzer()
    
    def print_header(self):
        """
        طباعة رأس البرنامج
        """
        print(f"{Fore.CYAN}{'='*80}")
        print(f"{Fore.GREEN}🔍 أداة تحليل محتوى Facebook")
        print(f"{Fore.GREEN}Facebook Content Analyzer Tool")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
    
    def print_success(self, message):
        print(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")
    
    def print_error(self, message):
        print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")
    
    def print_warning(self, message):
        print(f"{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}")
    
    def print_info(self, message):
        print(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")
    
    def analyze_text(self, text, url=None, output_format='text'):
        """
        تحليل النص
        """
        print(f"\n{Fore.CYAN}📊 جاري التحليل...{Style.RESET_ALL}")
        
        report = self.analyzer.generate_report(text, url)
        
        if output_format == 'json':
            self.output_json(report)
        elif output_format == 'html':
            self.output_html(report)
        else:
            self.output_text(report)
    
    def output_text(self, report):
        """
        طباعة التقرير بصيغة نصية
        """
        print(f"\n{Fore.CYAN}{'='*80}")
        print(f"{Fore.GREEN}📋 التقرير الكامل")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")
        
        # معلومات التحليل الأساسية
        print(f"{Fore.YELLOW}📌 معلومات أساسية:{Style.RESET_ALL}")
        print(f"  الوقت: {report['timestamp']}")
        print(f"  اللغة: {report['language']}")
        print(f"  عدد الكلمات: {report['word_count']}")
        print(f"  طول النص: {report['text_length']} حرف")
        print(f"  Hash: {report['text_hash'][:16]}...\n")
        
        # تحليل المشاعر
        sentiment = report['sentiment']
        print(f"{Fore.YELLOW}💭 تحليل المشاعر:{Style.RESET_ALL}")
        print(f"  المشاعر: {sentiment['sentiment']}")
        print(f"  درجة الإيجابية: {sentiment['polarity']}")
        print(f"  الذاتية: {sentiment['subjectivity']}\n")
        
        # المشاكل المكتشفة
        if report['detected_issues']:
            print(f"{Fore.RED}🚨 المشاكل المكتشفة:{Style.RESET_ALL}")
            for issue in report['detected_issues']:
                severity_color = Fore.RED if issue['score'] > 0.5 else Fore.YELLOW
                print(f"  {severity_color}• {issue['type']}")
                print(f"    النقاط: {issue['score']:.1%} | الثقة: {issue['confidence']}%{Style.RESET_ALL}")
            print()
        else:
            print(f"{Fore.GREEN}✓ لم يتم اكتشاف مشاكل{Style.RESET_ALL}\n")
        
        # توصيات البلاغات
        if report['report_recommendations']:
            print(f"{Fore.RED}📝 توصيات البلاغات:{Style.RESET_ALL}")
            for i, rec in enumerate(report['report_recommendations'], 1):
                severity_color = Fore.RED if rec['severity'] == 'حرج' else Fore.YELLOW
                print(f"\n  {Fore.CYAN}[البلاغ {i}]{Style.RESET_ALL}")
                print(f"    النوع: {rec['type']}")
                print(f"    الاسم: {rec['name']}")
                print(f"    الوصف: {rec['description']}")
                print(f"    {severity_color}درجة الخطورة: {rec['severity']}{Style.RESET_ALL}")
                print(f"    الإجراء المقترح: {rec['action']}")
            print()
        
        # درجة الخطورة العامة
        severity_color = Fore.RED if report['severity_level'] == 'حرج' else Fore.YELLOW
        print(f"{severity_color}⚠️ درجة الخطورة العامة: {report['severity_level']}{Style.RESET_ALL}\n")
        
        # تحليل الرابط
        if report['url_analysis']:
            print(f"{Fore.YELLOW}🔗 تحليل الرابط:{Style.RESET_ALL}")
            url_info = report['url_analysis']
            print(f"  الرابط: {url_info['url']}")
            print(f"  النطاق: {url_info['domain']}")
            print(f"  صحيح: {url_info['is_valid']}")
            print(f"  مشبوه: {url_info['suspicious']}")
            if 'accessible' in url_info:
                print(f"  يمكن الوصول: {url_info['accessible']}")
            print()
        
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")
    
    def output_json(self, report):
        """
        طباعة التقرير بصيغة JSON
        """
        print(json.dumps(report, indent=2, ensure_ascii=False, default=str))
    
    def output_html(self, report):
        """
        إنشاء تقرير HTML
        """
        html_content = self.generate_html_report(report)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"report_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"{Fore.GREEN}✓ تم حفظ التقرير: {filename}{Style.RESET_ALL}")
    
    def generate_html_report(self, report):
        """
        توليد تقرير HTML
        """
        return f"""
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تقرير تحليل محتوى Facebook</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .content {{
            padding: 30px;
        }}
        .section {{
            margin-bottom: 30px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }}
        .section h2 {{
            color: #333;
            margin-bottom: 15px;
            font-size: 1.5em;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }}
        .info-item {{
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
        }}
        .info-item label {{
            font-weight: bold;
            color: #667eea;
            display: block;
            margin-bottom: 5px;
        }}
        .info-item value {{
            color: #333;
            font-size: 1.1em;
        }}
        .severity-critical {{
            background: #ff4444;
            color: white;
        }}
        .severity-high {{
            background: #ff8800;
            color: white;
        }}
        .severity-medium {{
            background: #ffcc00;
            color: #333;
        }}
        .severity-low {{
            background: #44cc44;
            color: white;
        }}
        .issue-item {{
            background: #fff3cd;
            border-left: 4px solid #ff8800;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }}
        .report-item {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }}
        .report-item h3 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-right: 5px;
        }}
        .timestamp {{
            text-align: center;
            color: #999;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 تقرير تحليل محتوى Facebook</h1>
            <p>Facebook Content Analysis Report</p>
        </div>
        
        <div class="content">
            <!-- معلومات أساسية -->
            <div class="section">
                <h2>📌 معلومات أساسية</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <label>الوقت</label>
                        <value>{report['timestamp']}</value>
                    </div>
                    <div class="info-item">
                        <label>اللغة</label>
                        <value>{report['language']}</value>
                    </div>
                    <div class="info-item">
                        <label>عدد الكلمات</label>
                        <value>{report['word_count']}</value>
                    </div>
                    <div class="info-item">
                        <label>طول النص</label>
                        <value>{report['text_length']} حرف</value>
                    </div>
                </div>
            </div>
            
            <!-- المشاعر -->
            <div class="section">
                <h2>💭 تحليل المشاعر</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <label>المشاعر</label>
                        <value>{report['sentiment']['sentiment']}</value>
                    </div>
                    <div class="info-item">
                        <label>درجة الإيجابية</label>
                        <value>{report['sentiment']['polarity']}</value>
                    </div>
                    <div class="info-item">
                        <label>الذاتية</label>
                        <value>{report['sentiment']['subjectivity']}</value>
                    </div>
                </div>
            </div>
            
            <!-- المشاكل -->
            {self._generate_issues_html(report)}
            
            <!-- البلاغات -->
            {self._generate_reports_html(report)}
            
            <!-- درجة الخطورة -->
            <div class="section">
                <h2>⚠️ درجة الخطورة العامة</h2>
                <div class="badge severity-{self._get_severity_class(report['severity_level'])}">
                    {report['severity_level']}
                </div>
            </div>
            
            <div class="timestamp">
                <p>تم إنشاء هذا التقرير بواسطة أداة تحليل محتوى Facebook</p>
                <p>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </div>
    </div>
</body>
</html>
        """
    
    def _generate_issues_html(self, report):
        if not report['detected_issues']:
            return '<div class="section"><h2>✓ لم يتم اكتشاف مشاكل</h2></div>'
        
        html = '<div class="section"><h2>🚨 المشاكل المكتشفة</h2>'
        for issue in report['detected_issues']:
            html += f"""
            <div class="issue-item">
                <strong>{issue['type']}</strong><br>
                النقاط: {issue['score']:.1%} | الثقة: {issue['confidence']}%
            </div>
            """
        html += '</div>'
        return html
    
    def _generate_reports_html(self, report):
        if not report['report_recommendations']:
            return ''
        
        html = '<div class="section"><h2>📝 توصيات البلاغات</h2>'
        for rec in report['report_recommendations']:
            html += f"""
            <div class="report-item">
                <h3>{rec['name']}</h3>
                <p><strong>الوصف:</strong> {rec['description']}</p>
                <p><strong>درجة الخطورة:</strong> <span class="badge severity-{self._get_severity_class(rec['severity'])}">{rec['severity']}</span></p>
                <p><strong>الإجراء المقترح:</strong> {rec['action']}</p>
            </div>
            """
        html += '</div>'
        return html
    
    def _get_severity_class(self, severity):
        if severity == 'حرج':
            return 'critical'
        elif severity == 'عالي جداً' or severity == 'عالي':
            return 'high'
        elif severity == 'متوسط':
            return 'medium'
        else:
            return 'low'
    
    def interactive_mode(self):
        """
        الوضع التفاعلي
        """
        self.print_header()
        self.print_info("أنت في الوضع التفاعلي. اكتب 'help' للحصول على المساعدة.")
        
        while True:
            try:
                print(f"\n{Fore.CYAN}▶{Style.RESET_ALL} ", end='')
                command = input().strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.print_info("وداعاً!")
                    break
                
                elif command.lower() == 'help':
                    self._print_help()
                
                elif command.lower().startswith('analyze '):
                    text = command[8:]
                    self.analyze_text(text)
                
                elif command.lower().startswith('file '):
                    filepath = command[5:]
                    self._analyze_file(filepath)
                
                else:
                    self.print_warning("أمر غير معروف. اكتب 'help' للمساعدة.")
            
            except KeyboardInterrupt:
                print()
                self.print_info("تم الإيقاف.")
                break
            except Exception as e:
                self.print_error(f"خطأ: {str(e)}")
    
    def _print_help(self):
        """
        طباعة المساعدة
        """
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}الأوامر المتاحة:")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print("  analyze <text>     - تحليل نص معين")
        print("  file <path>        - تحليل محتوى ملف")
        print("  help               - عرض هذه المساعدة")
        print("  exit/quit          - الخروج من البرنامج")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    def _analyze_file(self, filepath):
        """
        تحليل ملف
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            self.print_success(f"تم قراءة الملف: {filepath}")
            self.analyze_text(text)
        except FileNotFoundError:
            self.print_error(f"الملف غير موجود: {filepath}")
        except Exception as e:
            self.print_error(f"خطأ في قراءة الملف: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description='أداة تحليل محتوى Facebook',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  %(prog)s -i                          # الوضع التفاعلي
  %(prog)s -t "نص للتحليل"           # تحليل نص
  %(prog)s -f input.txt               # تحليل ملف
  %(prog)s -u "https://example.com"   # تحليل مع رابط
  %(prog)s -o json -t "نص"           # إخراج JSON
        """
    )
    
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='تشغيل الوضع التفاعلي')
    parser.add_argument('-t', '--text', type=str,
                        help='تحليل نص معين')
    parser.add_argument('-f', '--file', type=str,
                        help='تحليل ملف')
    parser.add_argument('-u', '--url', type=str,
                        help='إضافة رابط للتحليل')
    parser.add_argument('-o', '--output', choices=['text', 'json', 'html'],
                        default='text', help='صيغة الإخراج (الافتراضي: text)')
    
    args = parser.parse_args()
    
    cli = FacebookAnalyzerCLI()
    
    if args.interactive:
        cli.interactive_mode()
    elif args.text:
        cli.print_header()
        cli.analyze_text(args.text, args.url, args.output)
    elif args.file:
        cli.print_header()
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
            cli.analyze_text(text, args.url, args.output)
        except FileNotFoundError:
            cli.print_error(f"الملف غير موجود: {args.file}")
        except Exception as e:
            cli.print_error(f"خطأ: {str(e)}")
    else:
        cli.print_header()
        cli.interactive_mode()


if __name__ == '__main__':
    main()
