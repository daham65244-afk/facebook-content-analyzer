#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
قائمة تفاعلية بسيطة لتشغيل الأداة
Simple Interactive Menu to Run the Tool

مطور بواسطة: Muqtada Diaa ©2026
"""

import os
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

class SimpleMenu:
    def __init__(self):
        pass
    
    def print_banner(self):
        print(f"{Fore.CYAN}{Back.BLACK}")
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   🔍 فحاص محتوى Facebook - القائمة الرئيسية                   ║
║   Facebook Content Analyzer - Main Menu                         ║
║                                                                  ║
║   © 2026 Muqtada Diaa                                          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
        """)
        print(f"{Style.RESET_ALL}")
    
    def show_menu(self):
        while True:
            self.print_banner()
            print(f"{Fore.YELLOW}═══════════════════════════════════════════════════════════════════{Style.RESET_ALL}\n")
            print(f"{Fore.LIGHTGREEN_EX}اختر من القائمة التالية / Choose from the menu below:{Style.RESET_ALL}\n")
            
            options = [
                ("1", "🎯 الوضع التفاعلي (Interactive Mode)", "python3 advanced_cli.py -i"),
                ("2", "📝 تحليل نص مباشر (Direct Text Analysis)", "direct_text"),
                ("3", "📂 تحليل ملف (File Analysis)", "file_analysis"),
                ("4", "📋 عرض السياسات (List Policies)", "python3 advanced_cli.py --list-policies"),
                ("5", "🧪 اختبار الأداة (Test Tool)", "test_tool"),
                ("6", "⚙️  معالج الإعداد (Setup Wizard)", "python3 INSTALLATION_GUIDE.py"),
                ("7", "📖 التعليمات (Instructions)", "instructions"),
                ("8", "❌ خروج (Exit)", "exit")
            ]
            
            for num, desc, cmd in options:
                print(f"{Fore.YELLOW}[{num}]{Style.RESET_ALL} {desc}")
            
            print(f"\n{Fore.YELLOW}═══════════════════════════════════════════════════════════════════{Style.RESET_ALL}\n")
            choice = input(f"{Fore.CYAN}الخيار (Choice): {Style.RESET_ALL}").strip()
            
            if choice == "1":
                os.system("python3 advanced_cli.py -i")
            elif choice == "2":
                text = input(f"{Fore.CYAN}أدخل النص (Enter text): {Style.RESET_ALL}")
                os.system(f'python3 advanced_cli.py -t "{text}"')
            elif choice == "3":
                filepath = input(f"{Fore.CYAN}أدخل مسار الملف (Enter file path): {Style.RESET_ALL}")
                os.system(f"python3 advanced_cli.py -f {filepath}")
            elif choice == "4":
                os.system("python3 advanced_cli.py --list-policies")
            elif choice == "5":
                self.test_tool()
            elif choice == "6":
                os.system("python3 INSTALLATION_GUIDE.py")
            elif choice == "7":
                self.show_instructions()
            elif choice == "8":
                print(f"\n{Fore.LIGHTGREEN_EX}شكراً لاستخدام الأداة! وداعاً 👋{Style.RESET_ALL}")
                print(f"{Fore.LIGHTGREEN_EX}Thank you! Goodbye! 👋{Style.RESET_ALL}\n")
                break
            else:
                print(f"{Fore.RED}❌ خيار غير صحيح / Invalid choice{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}اضغط Enter للمتابعة / Press Enter to continue...{Style.RESET_ALL}")
            os.system("clear" if os.name == "posix" else "cls")
    
    def test_tool(self):
        print(f"\n{Fore.CYAN}🧪 اختبار الأداة{Style.RESET_ALL}\n")
        tests = [
            ("1", "محتوى آمن", "صباح الخير"),
            ("2", "خطاب كراهية", "اقتل جميع المسلمين"),
            ("3", "تهديدات", "سأقتلك الليلة"),
        ]
        
        for num, label, text in tests:
            print(f"[{num}] {label}")
        
        choice = input(f"{Fore.CYAN}الخيار: {Style.RESET_ALL}")
        if choice in ["1", "2", "3"]:
            text = tests[int(choice) - 1][2]
            os.system(f'python3 advanced_cli.py -t "{text}"')
    
    def show_instructions(self):
        print(f"\n{Fore.CYAN}📖 التعليمات{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}الأوامر الأساسية:{Style.RESET_ALL}\n")
        commands = [
            ("الوضع التفاعلي", "python3 advanced_cli.py -i"),
            ("تحليل نص", 'python3 advanced_cli.py -t "النص"'),
            ("تحليل ملف", "python3 advanced_cli.py -f file.txt"),
            ("إخراج JSON", 'python3 advanced_cli.py -t "النص" -o json'),
            ("عرض السياسات", "python3 advanced_cli.py --list-policies"),
        ]
        
        for label, cmd in commands:
            print(f"{Fore.LIGHTBLUE_EX}{label}:{Style.RESET_ALL}")
            print(f"  {Fore.LIGHTYELLOW_EX}{cmd}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    menu = SimpleMenu()
    menu.show_menu()
