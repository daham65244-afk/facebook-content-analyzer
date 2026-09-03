#!/bin/bash
# -*- coding: utf-8 -*-
"""
معالج الإعداد السريع
Quick Setup Wizard for Kali Linux

مطور بواسطة: Muqtada Diaa ©2026
"""

echo -e "\033[1;36m"
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  🔍 أداة تحليل محتوى Facebook - معالج الإعداد السريع         ║"
echo "║     Advanced Facebook Content Analyzer - Quick Setup Wizard    ║"
echo "╚═════════════════════════════════════════��══════════════════════╝"
echo -e "\033[0m"

# التحقق من صلاحيات المسؤول
if [[ $EUID -ne 0 ]]; then
   echo -e "\033[1;33m⚠️  سيتم طلب كلمة المرور للعمليات التي تتطلب صلاحيات المسؤول\033[0m\n"
fi

# تحديث النظام
echo -e "\033[1;32m🔄 تحديث قائمة الحزم...\033[0m"
sudo apt-get update -y > /dev/null 2>&1

# تثبيت المتطلبات
echo -e "\033[1;32m📦 تثبيت Python والمتطلبات...\033[0m"
sudo apt-get install -y python3 python3-pip python3-venv git > /dev/null 2>&1

# استنساخ المستودع
echo -e "\033[1;32m📥 استنساخ المستودع...\033[0m"
if [ -d "facebook-content-analyzer" ]; then
    echo -e "\033[1;33m⚠️  المجلد موجود بالفعل، سيتم التحديث...\033[0m"
    cd facebook-content-analyzer
    git pull origin main
else
    git clone https://github.com/daham65244-afk/facebook-content-analyzer.git
    cd facebook-content-analyzer
fi

# إنشاء البيئة الافتراضية
echo -e "\033[1;32m🐍 إنشاء البيئة الافتراضية...\033[0m"
python3 -m venv venv > /dev/null 2>&1

# تفعيل البيئة وتثبيت المتطلبات
echo -e "\033[1;32m📚 تثبيت المكتبات...\033[0m"
source venv/bin/activate
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

echo ""
echo -e "\033[1;32m╔════════════════════════════════════════════════════════════════╗\033[0m"
echo -e "\033[1;32m║         ✅ انتهى الإعداد بنجاح! Setup Complete!               ║\033[0m"
echo -e "\033[1;32m╚════════════════════════════════════════════════════════════════╝\033[0m"

echo ""
echo -e "\033[1;36m📝 كيفية الاستخدام:\033[0m"
echo ""
echo -e "\033[1;33m1️⃣  الوضع التفاعلي:\033[0m"
echo -e "   \033[1;36mpython3 advanced_cli.py -i\033[0m"
echo ""
echo -e "\033[1;33m2️⃣  تحليل نص مباشر:\033[0m"
echo -e "   \033[1;36mpython3 advanced_cli.py -t \"النص المراد تحليله\"\033[0m"
echo ""
echo -e "\033[1;33m3️⃣  تحليل ملف:\033[0m"
echo -e "   \033[1;36mpython3 advanced_cli.py -f /path/to/file.txt\033[0m"
echo ""
echo -e "\033[1;33m4️⃣  عرض السياسات:\033[0m"
echo -e "   \033[1;36mpython3 advanced_cli.py --list-policies\033[0m"
echo ""
echo -e "\033[1;33m5️⃣  المساعدة:\033[0m"
echo -e "   \033[1;36mpython3 advanced_cli.py --help\033[0m"
echo ""
echo -e "\033[1;36m🌐 أو شغّل معالج الإعداد التفاعلي:\033[0m"
echo -e "\033[1;36mpython3 INSTALLATION_GUIDE.py\033[0m"
echo ""
echo -e "\033[1;32m🎉 شكراً لاستخدام الأداة! Enjoy!\033[0m"
echo -e "\033[1;33m© 2026 Muqtada Diaa\033[0m\n"
