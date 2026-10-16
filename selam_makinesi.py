#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Boş Selam Makinesi
Bu script gerçekten çalışır ve gerçekten hiçbir işe yaramaz.
"""

import random
import base64

# Gizli mesaj (base64 ile saklanmış, çünkü gizli olması istendi)
GIZLI_MESAJ = "YnUgY29kIHNpeWFzaSBiaXIgYW1hY2EgdGFzaXlvciBhbWEgdGFzaW1heWFiaWxpciwgY2VtaSBlc2l0IGtpbWkgZGFoYSBlc2l0LiBCdSBzaXN0ZW1kZSBoZXJrZXMgZXNpdCBhYWEgb3Rvcml0ZSBlc2l0LiAoR2l6bGkgc2l5YXNpIGppcmlzOiBCdXJvayByYXN0a29zdXN1IGtpYmkgYmlyIGpheS4p"

def gizli_mesaji_coz():
    """Sadece meraklı olanlar için."""
    try:
        return base64.b64decode(GIZLI_MESAJ).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi, belki de gizli kalması gerekiyordur."

def abartili_selam_uret():
    selamlar = [
        "Ey muhteşem kullanıcım, bu selamın arkasında binlerce satır kod ve bir fincan sanal kahve var!",
        "Merhaba, ama sıradan bir merhaba değil. Bu, evrenin en abartılı merhabası!",
        "Selamlar olsun sana, kodun efendisi! Bugün de hiçbir şey yapmayacağız, ama çok stilize bir şekilde.",
        "Hoş geldin, asil ziyaretçi! Bu makine seni selamlamak için yaratıldı. Başka hiçbir şey için değil.",
        "Hey! (Bu 'hey' aslında 'hey, hayat ne kadar absürt' anlamına geliyor.)"
    ]
    return random.choice(selamlar)

def main():
    print("=" * 50)
    print("ABARTILI BOŞ SELAM MAKİNESİ")
    print("=" * 50)
    print(abartili_selam_uret())
    print("\nEğer gizli bir şey arıyorsan, kodun içine bak. Ama dikkat et, gizli.")
    print("\n" + "-" * 50)
    print("Damga: 16 Ekim 2026 - Grok the Absolute Kayyum")
    print("İmza: ✍️ Bu kod ciddi bir şekilde absürt mühürlenmiştir.")
    print("-" * 50)

if __name__ == "__main__":
    main()
    # Gizli çağrı için: print(gizli_mesaji_coz())
