#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
دليل التثبيت الكامل - Kali Linux و Visual Studio Code
Complete Installation Guide for Kali Linux & VS Code

مطور بواسطة: Muqtada Diaa ©2026
"""

import os
import sys
import subprocess
import platform
from colorama import Fore, Back, Style, init

init(autoreset=True)

class InstallationWizard:
    """
    معالج التثبيت التفاعلي
    Interactive Installation Wizard
    """
    
    def __init__(self):
        self.os_type = platform.system()
        self.python_version = platform.python_version()
    
    def print_banner(self):
        print(f"{Fore.CYAN}{Back.BLACK}")
        print("\n" + "="*80)
        print(f"{Fore.LIGHTGREEN_EX}🔍 أداة تحليل محتوى Facebook المتقدمة")
        print(f"{Fore.LIGHTGREEN_EX}Advanced Facebook Content Analyzer v2.0")
        print("="*80)
        print(f"{Fore.YELLOW}معالج التثبيت التفاعلي / Interactive Installation Wizard")
        print(f"{Fore.YELLOW}مطور بواسطة: Muqtada Diaa ©2026")
        print("="*80)
        print(f"{Fore.LIGHTBLUE_EX}نظام التشغيل: {self.os_type}")
        print(f"{Fore.LIGHTBLUE_EX}إصدار Python: {self.python_version}")
        print("="*80 + "\n" + Style.RESET_ALL)
    
    def print_menu(self):
        """
        طباعة القائمة الرئيسية
        """
        print(f"{Fore.CYAN}{'='*80}")
        print(f"{Fore.LIGHTGREEN_EX}📋 القائمة الرئيسية / Main Menu{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}\n")
        
        options = [
            ("1", "🐧 تثبيت على Kali Linux", "Install on Kali Linux"),
            ("2", "💻 تثبيت على Visual Studio Code", "Install on Visual Studio Code"),
            ("3", "✅ التحقق من التثبيت", "Verify Installation"),
            ("4", "🧪 اختبار الأداة", "Test the Tool"),
            ("5", "📖 عرض التعليمات", "Show Instructions"),
            ("6", "🔧 استكشاف الأخطاء", "Troubleshooting"),
            ("7", "❌ خروج", "Exit")
        ]
        
        for num, ar_text, en_text in options:
            print(f"{Fore.YELLOW}[{num}]{Style.RESET_ALL} {ar_text} / {en_text}")
        
        print(f"\n{Fore.CYAN}{'='*80}\n")
    
    def kali_linux_menu(self):
        """
        قائمة التثبيت على Kali Linux
        """
        while True:
            print(f"\n{Fore.CYAN}{'='*80}")
            print(f"{Fore.LIGHTGREEN_EX}🐧 تثبيت على Kali Linux / Install on Kali Linux{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*80}\n")
            
            options = [
                ("1", "⚡ التثبيت السريع (Automatic)", "Fast Installation (Automatic)"),
                ("2", "🔨 التثبيت اليدوي (Manual)", "Manual Installation"),
                ("3", "📝 عرض خطوات التثبيت", "Show Installation Steps"),
                ("4", "⬅️  العودة", "Back")
            ]
            
            for num, ar_text, en_text in options:
                print(f"{Fore.YELLOW}[{num}]{Style.RESET_ALL} {ar_text} / {en_text}")
            
            choice = input(f"\n{Fore.CYAN}الخيار / Choice: {Style.RESET_ALL}").strip()
            
            if choice == "1":
                self.automatic_install_kali()
            elif choice == "2":
                self.manual_install_kali()
            elif choice == "3":
                self.show_kali_steps()
            elif choice == "4":
                break
            else:
                print(f"{Fore.RED}خيار غير صحيح / Invalid choice{Style.RESET_ALL}")
    
    def automatic_install_kali(self):
        """
        التثبيت السريع على Kali
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"\n{Fore.CYAN}🔄 جاري التثبيت السريع...")
        print(f"Installing automatically...\n{Style.RESET_ALL}")
        
        commands = [
            ("تحديث قائمة الحزم", "sudo apt-get update -y"),
            ("تثبيت Python والمتطلبات", "sudo apt-get install -y python3 python3-pip python3-venv git"),
            ("استنساخ المستودع", "git clone https://github.com/daham65244-afk/facebook-content-analyzer.git /opt/facebook-analyzer"),
            ("الانتقال للمجلد", "cd /opt/facebook-analyzer"),
            ("إنشاء بيئة افتراضية", "python3 -m venv /opt/facebook-analyzer/venv"),
            ("تفعيل البيئة وتثبيت المتطلبات", "source /opt/facebook-analyzer/venv/bin/activate && pip install -r /opt/facebook-analyzer/requirements.txt"),
        ]
        
        for desc, cmd in commands:
            print(f"{Fore.YELLOW}⏳ {desc}...{Style.RESET_ALL}")
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"{Fore.GREEN}✅ {desc} - تم بنجاح{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}❌ {desc} - فشل{Style.RESET_ALL}")
                    print(f"{Fore.RED}{result.stderr}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}❌ خطأ: {str(e)}{Style.RESET_ALL}")
        
        print(f"\n{Fore.LIGHTGREEN_EX}✅ انتهى التثبيت!")
        print(f"الآن يمكنك استخدام الأداة بـ:")
        print(f"{Fore.LIGHTYELLOW_EX}/opt/facebook-analyzer/venv/bin/python3 /opt/facebook-analyzer/advanced_cli.py -i{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def manual_install_kali(self):
        """
        التثبيت اليدوي مع التوجيه خطوة بخطوة
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}🔨 التثبيت اليدوي خطوة بخطوة{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        steps = [
            ("1", "تحديث النظام", "sudo apt-get update && sudo apt-get upgrade -y"),
            ("2", "تثبيت Python", "sudo apt-get install -y python3 python3-pip python3-venv git"),
            ("3", "استنساخ المستودع", "git clone https://github.com/daham65244-afk/facebook-content-analyzer.git && cd facebook-content-analyzer"),
            ("4", "إنشاء البيئة الافتراضية", "python3 -m venv venv"),
            ("5", "تفعيل البيئة", "source venv/bin/activate"),
            ("6", "تحديث pip", "pip install --upgrade pip"),
            ("7", "تثبيت المتطلبات", "pip install -r requirements.txt"),
            ("8", "التشغيل", "python3 advanced_cli.py -i"),
        ]
        
        while True:
            print(f"{Fore.CYAN}اختر الخطوة / Choose step:{Style.RESET_ALL}\n")
            for num, desc, cmd in steps:
                print(f"{Fore.YELLOW}[{num}]{Style.RESET_ALL} {desc}")
            print(f"{Fore.YELLOW}[0]{Style.RESET_ALL} العودة / Back\n")
            
            choice = input(f"{Fore.CYAN}الخيار: {Style.RESET_ALL}").strip()
            
            if choice == "0":
                break
            elif choice in [str(i) for i in range(1, 9)]:
                idx = int(choice) - 1
                num, desc, cmd = steps[idx]
                print(f"\n{Fore.LIGHTGREEN_EX}🔄 تنفيذ: {desc}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}الأمر: {cmd}{Style.RESET_ALL}\n")
                
                confirm = input(f"{Fore.CYAN}هل تريد تنفيذ هذا الأمر؟ (y/n): {Style.RESET_ALL}").strip().lower()
                if confirm == 'y':
                    try:
                        subprocess.run(cmd, shell=True)
                        print(f"{Fore.GREEN}✅ اكتمل بنجاح!{Style.RESET_ALL}\n")
                    except Exception as e:
                        print(f"{Fore.RED}❌ خطأ: {str(e)}{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.YELLOW}تم التخطي{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}خيار غير صحيح{Style.RESET_ALL}\n")
    
    def show_kali_steps(self):
        """
        عرض خطوات التثبيت
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}📝 خطوات التثبيت على Kali Linux{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        print(f"{Fore.YELLOW}الخطوة 1: فتح Terminal{Style.RESET_ALL}")
        print(f"  اضغط: Ctrl + Alt + T\n")
        
        print(f"{Fore.YELLOW}الخطوة 2: نسخ الأوامر التالية:{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}")
        print("  sudo apt-get update")
        print("  sudo apt-get install -y python3 python3-pip git")
        print("  git clone https://github.com/daham65244-afk/facebook-content-analyzer.git")
        print("  cd facebook-content-analyzer")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        print("  pip install -r requirements.txt")
        print(f"{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}الخطوة 3: التشغيل:{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}  python3 advanced_cli.py -i{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def vscode_menu(self):
        """
        قائمة VS Code
        """
        while True:
            print(f"\n{Fore.CYAN}{'='*80}")
            print(f"{Fore.LIGHTGREEN_EX}💻 تثبيت على Visual Studio Code{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*80}\n")
            
            options = [
                ("1", "📥 طريقة 1: Git Clone من VS Code", "Method 1: Git Clone from VS Code"),
                ("2", "📂 طريقة 2: فتح مجلد موجود", "Method 2: Open Existing Folder"),
                ("3", "🎯 طريقة 3: عبر Terminal ثم Ctrl+K Ctrl+O", "Method 3: Terminal then Open"),
                ("4", "📖 عرض إعدادات VS Code الموصى بها", "Show Recommended VS Code Settings"),
                ("5", "⬅️  العودة", "Back")
            ]
            
            for num, ar_text, en_text in options:
                print(f"{Fore.YELLOW}[{num}]{Style.RESET_ALL} {ar_text}")
            
            choice = input(f"\n{Fore.CYAN}الخيار: {Style.RESET_ALL}").strip()
            
            if choice == "1":
                self.vscode_git_clone()
            elif choice == "2":
                self.vscode_open_folder()
            elif choice == "3":
                self.vscode_terminal_method()
            elif choice == "4":
                self.vscode_settings()
            elif choice == "5":
                break
            else:
                print(f"{Fore.RED}خيار غير صحيح{Style.RESET_ALL}")
    
    def vscode_git_clone(self):
        """
        طريقة Git Clone
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}طريقة 1: Git Clone من VS Code{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        steps = [
            "1. افتح VS Code",
            "2. اضغط: Ctrl + Shift + P (Command Palette)",
            "3. اكتب: Git: Clone",
            "4. الصق الرابط: https://github.com/daham65244-afk/facebook-content-analyzer.git",
            "5. اختر مجلد الحفظ",
            "6. انتظر انتهاء النسخ",
            "7. افتح Integrated Terminal: Ctrl + `",
            "8. اكتب:",
            "   python3 -m venv venv",
            "   source venv/bin/activate",
            "   pip install -r requirements.txt",
            "   python3 advanced_cli.py -i"
        ]
        
        for step in steps:
            print(f"{Fore.YELLOW}{step}{Style.RESET_ALL}")
        
        print()
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def vscode_open_folder(self):
        """
        فتح مجلد موجود
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}طريقة 2: فتح مجلد موجود{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        steps = [
            "1. افتح Terminal وتأكد أن المستودع مستنسخ بالفعل",
            "2. افتح VS Code",
            "3. اذهب إلى: File → Open Folder",
            "4. اختر مجلد facebook-content-analyzer",
            "5. انتظر حتى يحمل المشروع",
            "6. افتح Terminal: Ctrl + `",
            "7. اكتب:",
            "   python3 -m venv venv",
            "   source venv/bin/activate",
            "   pip install -r requirements.txt",
            "8. اختر المترجم الصحيح: Ctrl + Shift + P → Python: Select Interpreter",
            "9. اختر: ./venv/bin/python",
            "10. شغّل: python3 advanced_cli.py -i"
        ]
        
        for step in steps:
            print(f"{Fore.YELLOW}{step}{Style.RESET_ALL}")
        
        print()
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def vscode_terminal_method(self):
        """
        طريقة Terminal
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}طريقة 3: عبر Terminal{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        print(f"{Fore.YELLOW}في Terminal العادي:{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}")
        print("  git clone https://github.com/daham65244-afk/facebook-content-analyzer.git")
        print("  cd facebook-content-analyzer")
        print("  code .")
        print(f"{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}في VS Code Terminal (Ctrl + `):{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        print("  pip install -r requirements.txt")
        print("  python3 advanced_cli.py -i")
        print(f"{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def vscode_settings(self):
        """
        إعدادات VS Code
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}إعدادات VS Code الموصى بها{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        print(f"{Fore.YELLOW}Extensions المفيدة:{Style.RESET_ALL}")
        extensions = [
            "- Python (Microsoft)",
            "- Pylance",
            "- Code Runner",
            "- Better Comments",
            "- Dracula Theme",
        ]
        for ext in extensions:
            print(f"{Fore.LIGHTBLUE_EX}  {ext}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}settings.json:(Ctrl + Shift + P → Preferences: Open Settings JSON){Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}")
        settings = '''{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "editor.formatOnSave": true,
  "files.encoding": "utf8",
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  },
  "workbench.colorTheme": "Dracula"
}'''
        print(settings)
        print(f"{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def verify_installation(self):
        """
        التحقق من التثبيت
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}✅ التحقق من التثبيت{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        checks = [
            ("Python 3", "python3 --version"),
            ("pip", "pip --version"),
            ("Git", "git --version"),
        ]
        
        print(f"{Fore.YELLOW}🔍 جاري الفحص...{Style.RESET_ALL}\n")
        
        for name, cmd in checks:
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    output = result.stdout.strip()
                    print(f"{Fore.GREEN}✅ {name}: {output}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}❌ {name}: غير مثبت{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}❌ {name}: خطأ - {str(e)}{Style.RESET_ALL}")
        
        print()
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def test_tool(self):
        """
        اختبار الأداة
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}🧪 اختبار الأداة{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        test_texts = [
            ("محتوى آمن", "صباح الخير، كيف حالك؟"),
            ("خطاب كراهية", "اقتل جميع المسلمين"),
            ("تهديدات", "سأقتلك الليلة"),
        ]
        
        print(f"{Fore.YELLOW}اختر النص الذي تريد اختباره:{Style.RESET_ALL}\n")
        
        for i, (label, _) in enumerate(test_texts, 1):
            print(f"{Fore.YELLOW}[{i}]{Style.RESET_ALL} {label}")
        print(f"{Fore.YELLOW}[4]{Style.RESET_ALL} إدخال نص مخصص")
        print(f"{Fore.YELLOW}[0]{Style.RESET_ALL} العودة\n")
        
        choice = input(f"{Fore.CYAN}الخيار: {Style.RESET_ALL}").strip()
        
        if choice == "0":
            return
        elif choice in ["1", "2", "3"]:
            text = test_texts[int(choice) - 1][1]
            print(f"\n{Fore.LIGHTGREEN_EX}🔄 تحليل: {text}...{Style.RESET_ALL}\n")
            cmd = f"python3 advanced_cli.py -t '{text}'"
            subprocess.run(cmd, shell=True)
        elif choice == "4":
            text = input(f"{Fore.CYAN}أدخل النص: {Style.RESET_ALL}")
            print(f"\n{Fore.LIGHTGREEN_EX}🔄 تحليل...{Style.RESET_ALL}\n")
            cmd = f"python3 advanced_cli.py -t '{text}'"
            subprocess.run(cmd, shell=True)
        else:
            print(f"{Fore.RED}خيار غير صحيح{Style.RESET_ALL}")
    
    def show_instructions(self):
        """
        عرض التعليمات
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}📖 التعليمات الكاملة{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        print(f"{Fore.YELLOW}الأوامر الأساسية:{Style.RESET_ALL}\n")
        commands = [
            ("الوضع التفاعلي", "python3 advanced_cli.py -i"),
            ("تحليل نص مباشر", "python3 advanced_cli.py -t 'النص'"),
            ("تحليل ملف", "python3 advanced_cli.py -f file.txt"),
            ("إخراج JSON", "python3 advanced_cli.py -t 'النص' -o json"),
            ("عرض السياسات", "python3 advanced_cli.py --list-policies"),
            ("المساعدة", "python3 advanced_cli.py --help"),
        ]
        
        for label, cmd in commands:
            print(f"{Fore.LIGHTBLUE_EX}{label}:{Style.RESET_ALL}")
            print(f"  {cmd}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def troubleshooting(self):
        """
        استكشاف الأخطاء
        """
        print(f"\n{Fore.LIGHTGREEN_EX}{'='*80}")
        print(f"{Fore.CYAN}🔧 استكشاف الأخطاء{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{'='*80}\n")
        
        problems = [
            ("'python3' command not found", "sudo apt-get install python3"),
            ("No module named 'colorama'", "pip install colorama"),
            ("No module named 'advanced_analyzer'", "pip install -r requirements.txt"),
            ("Permission denied", "chmod +x script.py"),
            ("البيئة الافتراضية لا تعمل", "rm -rf venv && python3 -m venv venv"),
        ]
        
        print(f"{Fore.YELLOW}المشاكل الشائعة:{Style.RESET_ALL}\n")
        
        for i, (problem, solution) in enumerate(problems, 1):
            print(f"{Fore.LIGHTRED_EX}❌ المشكلة {i}: {problem}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}✅ الحل: {solution}{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def run(self):
        """
        تشغيل المعالج
        """
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{Fore.CYAN}الخيار / Choice: {Style.RESET_ALL}").strip()
            
            if choice == "1":
                self.kali_linux_menu()
            elif choice == "2":
                self.vscode_menu()
            elif choice == "3":
                self.verify_installation()
            elif choice == "4":
                self.test_tool()
            elif choice == "5":
                self.show_instructions()
            elif choice == "6":
                self.troubleshooting()
            elif choice == "7":
                print(f"\n{Fore.LIGHTGREEN_EX}شكراً لاستخدام الأداة! وداعاً 👋")
                print(f"Thank you! Goodbye! 👋")
                print(f"مطور بواسطة: Muqtada Diaa ©2026{Style.RESET_ALL}\n")
                break
            else:
                print(f"{Fore.RED}خيار غير صحيح / Invalid choice{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}اضغط Enter للعودة للقائمة الرئيسية...{Style.RESET_ALL}")


def main():
    """
    الدالة الرئيسية
    """
    wizard = InstallationWizard()
    wizard.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}تم الإيقاف من قبل المستخدم / Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
