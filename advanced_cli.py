#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
واجهة سطر الأوامر المتقدمة
Advanced CLI with Full Facebook Policy Integration

مطور بواسطة: Muqtada Diaa
© 2026
"""

import argparse
import json
import sys
from pathlib import Path
from advanced_analyzer import AdvancedAIAnalyzer, FacebookPolicies
from colorama import Fore, Back, Style, init
from datetime import datetime
import time

init(autoreset=True)

class AdvancedFacebookAnalyzerCLI:
    """
    واجهة متقدمة لتحليل محتوى Facebook
    """
    
    def __init__(self):
        self.analyzer = AdvancedAIAnalyzer()
        self.policies = FacebookPolicies.FACEBOOK_POLICIES
    
    def print_banner(self):
        """
        طباعة اللافتة الرئيسية
        """
        print(f"{Fore.CYAN}{Back.BLACK}")
        print("╔════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                        ║")
        print("║      🔍 أداة تحليل محتوى Facebook المتقدمة - نسخة 2.0                 ║")
        print("║         Advanced AI-Powered Facebook Content Analyzer v2.0             ║")
        print("║                                                                        ║")
        print("║  ✨ مدعومة بالذكاء الاصطناعي والتعلم الآلي                            ║")
        print("║  ✨ AI-Powered & Machine Learning Enabled                             ║")
        print("║                                                                        ║")
        print("║  📋 10 سياسات Facebook متطورة / 10 Advanced Facebook Policies         ║")
        print("║  🎯 دقة عالية جداً / Ultra-High Accuracy Analysis                     ║")
        print("║  ⚖️  بلاغات صحيحة 100% / 100% Correct Reporting                       ║")
        print("║                                                                        ║")
        print("║  تطوير: Muqtada Diaa © 2026                                          ║")
        print("║                                                                        ║")
        print("╚════════════════════════════════════════════════════════════════════════╝")
        print(f"{Style.RESET_ALL}\n")
    
    def print_header(self, title: str):
        print(f"\n{Fore.CYAN}{'='*75}")
        print(f"{Fore.GREEN}🔍 {title}")
        print(f"{Fore.CYAN}{'='*75}{Style.RESET_ALL}\n")
    
    def print_violation_details(self, violations: list):
        """
        طباعة تفاصيل الانتهاكات المكتشفة
        """
        if not violations:
            print(f"{Fore.GREEN}✅ لا توجد انتهاكات للسياسات - المحتوى آمن!")
            print(f"{Fore.GREEN}✅ No Policy Violations Detected - Content is Safe!{Style.RESET_ALL}")
            return
        
        print(f"{Fore.RED}🚨 تم اكتشاف {len(violations)} انتهاك(ات) للسياسات{Style.RESET_ALL}")
        print(f"{Fore.RED}🚨 Detected {len(violations)} Policy Violation(s){Style.RESET_ALL}\n")
        
        for i, violation in enumerate(violations, 1):
            severity_colors = {
                'حرج جداً': Fore.RED + Back.WHITE,
                'حرج': Fore.RED,
                'عالي جداً': Fore.LIGHTRED_EX,
                'عالي': Fore.YELLOW,
                'متوسط': Fore.LIGHTYELLOW_EX,
                'منخفض': Fore.GREEN
            }
            
            color = severity_colors.get(violation['severity'], Fore.YELLOW)
            
            print(f"{Fore.CYAN}[الانتهاك #{i}] {Style.RESET_ALL}")
            print(f"  {Fore.LIGHTBLUE_EX}المعرّف:{Style.RESET_ALL} {violation['policy_id']}")
            print(f"  {Fore.LIGHTBLUE_EX}النوع:{Style.RESET_ALL} {violation['policy_name']} ({violation['policy_name_en']})")
            print(f"  {Fore.LIGHTBLUE_EX}الوصف:{Style.RESET_ALL} {violation['description']}")
            print(f"  {color}درجة الخطورة: {violation['severity']}{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTGREEN_EX}درجة الثقة: {violation['confidence']}%{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTBLUE_EX}نقاط الكلمات المفتاحية: {violation['keyword_score']}{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTBLUE_EX}نقاط تطابق الأنماط: {violation['pattern_score']}{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTBLUE_EX}نقاط العدوانية: {violation['aggression_score']}{Style.RESET_ALL}")
            
            if violation['matching_patterns']:
                print(f"  {Fore.LIGHTMAGENTA_EX}أنماط مطابقة:{Style.RESET_ALL} {violation['matching_patterns'][:3]}")
            
            print(f"  {Fore.LIGHTRED_EX}الإجراء المقترح: {violation['recommended_action']}{Style.RESET_ALL}")
            
            if violation['criminal_offense']:
                print(f"  {Fore.RED}⚠️  جريمة جنائية - يتطلب تسليم للسلطات{Style.RESET_ALL}")
            
            if not violation['appeal_possible']:
                print(f"  {Fore.RED}🔒 لا يمكن الاستئناف{Style.RESET_ALL}")
            else:
                print(f"  {Fore.GREEN}✓ يمكن الاستئناف{Style.RESET_ALL}")
            
            print(f"  {Fore.LIGHTYELLOW_EX}العقوبة الأولى: {violation['first_offense_penalty']}{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTRED_EX}العقوبة المتكررة: {violation['repeat_offense_penalty']}{Style.RESET_ALL}")
            print()
    
    def print_report_recommendation(self, report: dict):
        """
        طباعة توصية البلاغ
        """
        self.print_header("🎯 توصية البلاغ النهائية / Final Report Recommendation")
        
        if not report['can_report']:
            print(f"{Fore.GREEN}✅ المحتوى آمن - لا يوجد بلاغ مطلوب")
            print(f"{Fore.GREEN}✅ Content is safe - No report needed{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}نوع البلاغ / Report Type:{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}{report['report_type']} ({report['report_type_en']}){Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}{report['report_type_ar']}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}درجة الخطورة / Severity:{Style.RESET_ALL}")
        print(f"  {Fore.RED}{report['severity']}{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}المستوى: {report['severity_level']}/5{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}درجة الثقة / Confidence:{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTGREEN_EX}{report['confidence_percentage']}%{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}الإجراء المقترح / Recommended Action:{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTRED_EX}{report['recommended_action']}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}معلومات العقوبة / Penalty Information:{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTYELLOW_EX}الانتهاك الأول: {report['first_offense_ban']}{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTRED_EX}الانتهاك المتكرر: {report['repeat_offense_ban']}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}معلومات إضافية / Additional Info:{Style.RESET_ALL}")
        if report['criminal_offense']:
            print(f"  {Fore.RED}⚠️  جريمة جنائية{Style.RESET_ALL}")
        
        if report['appeal_possible']:
            print(f"  {Fore.GREEN}✓ يمكن الاستئناف{Style.RESET_ALL}")
        else:
            print(f"  {Fore.RED}✗ لا يمكن الاستئناف{Style.RESET_ALL}")
        
        print(f"\n{Fore.LIGHTGREEN_EX}✅ البلاغ جاهز للتقديم على Facebook")
        print(f"{Fore.LIGHTGREEN_EX}✅ Report Ready to Submit to Facebook{Style.RESET_ALL}")
    
    def print_json_output(self, analysis: dict):
        """
        طباعة النتائج بصيغة JSON
        """
        output = {
            'timestamp': analysis['timestamp'],
            'content_hash': analysis['content_hash'],
            'statistics': {
                'text_length': analysis['text_length'],
                'word_count': analysis['word_count'],
                'character_count': analysis['character_count']
            },
            'violations_summary': {
                'total_violations': analysis['violations_detected'],
                'violations': analysis['violations']
            },
            'report': analysis['report_recommendation'],
            'accuracy_score': analysis['accuracy_score']
        }
        
        print(json.dumps(output, indent=2, ensure_ascii=False, default=str))
    
    def analyze_content(self, text: str, url: str = None, output_format: str = 'text'):
        """
        تحليل المحتوى
        """
        self.print_banner()
        print(f"{Fore.CYAN}⏳ جاري التحليل باستخدام الذكاء الاصطناعي...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⏳ Analyzing with AI-Powered Engine...{Style.RESET_ALL}\n")
        
        # تنفيذ التحليل
        analysis = self.analyzer.analyze(text, url)
        
        if output_format == 'json':
            self.print_json_output(analysis)
        else:
            # طباعة التفاصيل
            self.print_header(f"📊 التحليل التفصيلي / Detailed Analysis")
            print(f"{Fore.LIGHTBLUE_EX}إحصائيات المحتوى / Content Statistics:{Style.RESET_ALL}")
            print(f"  طول النص: {analysis['text_length']} حرف")
            print(f"  عدد الكلمات: {analysis['word_count']} كلمة")
            print(f"  عدد السياسات المفحوصة: {analysis['facebook_policies_checked']}")
            print(f"  درجة الدقة الكلية: {analysis['accuracy_score']}%\n")
            
            # طباعة الانتهاكات
            self.print_header(f"⚠️  الانتهاكات المكتشفة / Detected Violations")
            self.print_violation_details(analysis['violations'])
            
            # طباعة التوصية
            self.print_report_recommendation(analysis['report_recommendation'])
            
            print(f"\n{Fore.CYAN}{'='*75}{Style.RESET_ALL}")
    
    def list_policies(self):
        """
        عرض قائمة جميع السياسات
        """
        self.print_banner()
        self.print_header("📋 سياسات Facebook المتوفرة / Available Facebook Policies")
        
        for policy_id, policy in self.policies.items():
            if policy_id == 'clean':
                continue
            
            print(f"{Fore.CYAN}[{policy['id']}] {policy['name']}{Style.RESET_ALL}")
            print(f"      {policy['name_en']}")
            print(f"      الوصف: {policy['description']}")
            print(f"      {Fore.RED}الخطورة: {policy['severity']}{Style.RESET_ALL}")
            print()
    
    def interactive_mode(self):
        """
        الوضع التفاعلي
        """
        self.print_banner()
        print(f"{Fore.GREEN}أنت في الوضع التفاعلي. اكتب 'help' للمساعدة\n")
        
        while True:
            try:
                print(f"{Fore.CYAN}▶ {Style.RESET_ALL}", end='', flush=True)
                command = input().strip()
                
                if not command:
                    continue
                
                if command.lower() in ['exit', 'quit', 'خروج']:
                    print(f"{Fore.GREEN}وداعاً!{Style.RESET_ALL}")
                    break
                
                elif command.lower() in ['help', 'ساعدة', 'مساعدة']:
                    print(f"""
{Fore.GREEN}الأوامر المتاحة:{Style.RESET_ALL}
  analyze <text>  - تحليل نص
  file <path>     - تحليل ملف
  policies        - عرض السياسات
  help            - هذه المساعدة
  exit            - الخروج
                    """)
                
                elif command.lower().startswith('analyze '):
                    text = command[8:]
                    self.analyze_content(text)
                
                elif command.lower().startswith('file '):
                    filepath = command[5:]
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            text = f.read()
                        self.analyze_content(text)
                    except FileNotFoundError:
                        print(f"{Fore.RED}❌ الملف غير موجود{Style.RESET_ALL}")
                
                elif command.lower() == 'policies':
                    self.list_policies()
                
                else:
                    print(f"{Fore.YELLOW}أمر غير معروف. اكتب 'help'{Style.RESET_ALL}")
            
            except KeyboardInterrupt:
                print(f"\n{Fore.GREEN}تم الإيقاف{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}خطأ: {str(e)}{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(
        description='أداة تحليل محتوى Facebook المتقدمة - Advanced AI-Powered Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  %(prog)s -i                      # الوضع التفاعلي
  %(prog)s -t "نص للتحليل"        # تحليل نص
  %(prog)s -f input.txt            # تحليل ملف
  %(prog)s --list-policies         # عرض السياسات
  %(prog)s -t "نص" -o json        # إخراج JSON
        """
    )
    
    parser.add_argument('-i', '--interactive', action='store_true', help='الوضع التفاعلي')
    parser.add_argument('-t', '--text', type=str, help='نص للتحليل')
    parser.add_argument('-f', '--file', type=str, help='تحليل من ملف')
    parser.add_argument('-u', '--url', type=str, help='إضافة رابط')
    parser.add_argument('-o', '--output', choices=['text', 'json'], default='text', help='صيغة الإخراج')
    parser.add_argument('--list-policies', action='store_true', help='عرض السياسات')
    
    args = parser.parse_args()
    
    cli = AdvancedFacebookAnalyzerCLI()
    
    if args.interactive or (not args.text and not args.file and not args.list_policies):
        cli.interactive_mode()
    elif args.list_policies:
        cli.list_policies()
    elif args.text:
        cli.analyze_content(args.text, args.url, args.output)
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
            cli.analyze_content(text, args.url, args.output)
        except FileNotFoundError:
            print(f"{Fore.RED}❌ الملف غير موجود{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ: {str(e)}{Style.RESET_ALL}")


if __name__ == '__main__':
    main()
