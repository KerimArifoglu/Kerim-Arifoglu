# XSS (Cross-Site Scripting) Zafiyeti Demonstrasyonu

Bu repository, XSS (Cross-Site Scripting) güvenlik açığını gösteren basit bir Flask web uygulamasını içermektedir. Uygulama, kullanıcıların yorum bırakabildiği ve bu yorumların listelenebildiği basit bir sistemdir.

## Zafiyet detayları
OWASP Kategorisi: A7:2021 - Cross-Site Scripting (XSS)
Referans: OWASP XSS
## CVSS Skoru
Base Score: 6.1 (Medium)
Vector String: CVSS:3.1/AV/AC/PR/UI/S/C/I/A

## Zafiyet Açıklaması
Bu uygulamadaki XSS zafiyeti, kullanıcı tarafından girilen yorumların hiçbir sanitizasyon işlemi uygulanmadan doğrudan web sayfasında görüntülenmesinden kaynaklanmaktadır. Zafiyet içeren kodda (vulnerable_app.py), kullanıcı tarafından girilen yorumlar, Jinja2 şablonunda |safe filtresinden geçirilerek HTML'e dönüştürülmeden doğrudan yerleştirilmektedir. Bu durum, kötü niyetli kullanıcıların HTML ve JavaScript kodu enjekte etmesine olanak tanır.
