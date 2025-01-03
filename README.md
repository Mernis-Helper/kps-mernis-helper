# kps-mernis-helper
kps hizmetlerini dışarıdan ücret ödemeden kullanabilirsiniz. 2025 yılına gelmeden gerekli dosyalar eklenecektir. sunucunuz üzerinde servisi aktif hale getirmeniz yeterli olacaktır.




# Kullanımı
  -Mernis dosyası içerisindeki uygulamayı sunucuda aktif hale getirin. ardından istediğiniz dilde aşağıdaki gibi post etmeniz yeterli olacaktır. örnekler incelenebilir.
   *** Headerda mutlaka "Content-Type": "application/json" gönderilmelidir.
   !! servisler kpsden kullanıma izin verilen servisler için geçerlidir. bu sebeple kps üzerindeki servislerden isteğiniz olması halinde uygulamaya eklenir ve kps üzerinden aktif şekilde kullanabilirsiniz.

## Bileşik Kütük Sorgulama ##
Json Post Edilmelidir
{
    "kullaniciAdi": "kullaniciAdiniz",
    "sifre": "Şifreniz",
    "kimlikNo": "123123123123",
    "dogumGun": 21,
    "dogumAy": 1,
    "dogumYil": 2003
}
