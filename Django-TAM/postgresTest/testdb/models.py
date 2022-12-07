from django.db import models
from django.forms import ModelForm
from django import forms



# Create your models here.
class Stocks(models.Model):
    id = models.BigIntegerField(blank=True, primary_key= True)
    index = models.TextField(blank=True, null=True)
    donen_varliklar = models.FloatField(blank=True, null=True)
    nakit_ve_nakit_benzerleri = models.FloatField(blank=True, null=True)
    finansal_yatirimlar_donen = models.FloatField(blank=True, null=True)
    ticari_alacaklar_donen = models.FloatField(blank=True, null=True)
    finans_sektoru_faaliyetlerinden_alacaklar_donen = models.FloatField(blank=True, null=True)
    diger_alacaklar_donen = models.FloatField(blank=True, null=True)
    musteri_sozlesmelerinden_dogan_varliklar_donen = models.FloatField(blank=True, null=True)
    stoklar_donen = models.FloatField(blank=True, null=True)
    canli_varliklar_donen = models.FloatField(blank=True, null=True)
    diger_donen_varliklar = models.FloatField(blank=True, null=True)
    ara_toplam_donen = models.FloatField(blank=True, null=True)
    satis_amaciyla_elde_tutulan_duran_varliklar = models.FloatField(blank=True, null=True)
    duran_varliklar = models.FloatField(blank=True, null=True)
    ticari_alacaklar_duran = models.FloatField(blank=True, null=True)
    finans_sektoru_faaliyetlerinden_alacaklar_duran = models.FloatField(blank=True, null=True)
    diger_alacaklar_duran = models.FloatField(blank=True, null=True)
    musteri_sozlesmelerinden_dogan_varliklar_duran = models.FloatField(blank=True, null=True)
    finansal_yatirimlar_duran = models.FloatField(blank=True, null=True)
    ozkaynak_yontemiyle_degerlenen_yatirimlar = models.FloatField(blank=True, null=True)
    canli_varliklar_duran = models.FloatField(blank=True, null=True)
    yatirim_amacli_gayrimenkuller = models.FloatField(blank=True, null=True)
    stoklar_duran = models.FloatField(blank=True, null=True)
    kullanim_hakki_varliklari = models.FloatField(blank=True, null=True)
    maddi_duran_varliklar = models.FloatField(blank=True, null=True)
    serefiye = models.FloatField(blank=True, null=True)
    maddi_olmayan_duran_varliklar = models.FloatField(blank=True, null=True)
    ertelenmis_vergi_varligi = models.FloatField(blank=True, null=True)
    diger_duran_varliklar = models.FloatField(blank=True, null=True)
    toplam_varliklar = models.FloatField(blank=True, null=True)
    kaynaklar = models.FloatField(blank=True, null=True)
    kisa_vadeli_yukumlulukler = models.FloatField(blank=True, null=True)
    finansal_borclar_kisa = models.FloatField(blank=True, null=True)
    diger_finansal_yukumlulukler_kisa = models.FloatField(blank=True, null=True)
    ticari_borclar_kisa = models.FloatField(blank=True, null=True)
    diger_borclar_kisa = models.FloatField(blank=True, null=True)
    musteri_soz_dogan_yuk_field = models.FloatField(db_column='musteri_soz._dogan_yuk.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finans_sektoru_faaliyetlerinden_borclar_kisa = models.FloatField(blank=True, null=True)
    devlet_tesvik_ve_yardimlari_kisa = models.FloatField(blank=True, null=True)
    ertelenmis_gelirler_musteri_soz_dogan_yuk_dis_kal_field = models.FloatField(db_column='ertelenmis_gelirler_musteri_soz._dogan_yuk._dis.kal.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    donem_kari_vergi_yukumlulugu = models.FloatField(blank=True, null=True)
    borc_karsiliklari = models.FloatField(blank=True, null=True)
    diger_kisa_vadeli_yukumlulukler = models.FloatField(blank=True, null=True)
    ara_toplam_kisa = models.FloatField(blank=True, null=True)
    uzun_vadeli_yukumlulukler = models.FloatField(blank=True, null=True)
    finansal_borclar = models.FloatField(blank=True, null=True)
    diger_finansal_yukumlulukler_uzun = models.FloatField(blank=True, null=True)
    ticari_borclar_uzun = models.FloatField(blank=True, null=True)
    diger_borclar_uzun = models.FloatField(blank=True, null=True)
    musteri_soz_dogan_yuk_field_0 = models.FloatField(db_column='musteri_soz.dogan_yuk.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    finans_sektoru_faaliyetlerinden_borclar_uzun = models.FloatField(blank=True, null=True)
    devlet_tesvik_ve_yardimlari_uzun = models.FloatField(blank=True, null=True)
    ertelenmis_gelirler_musteri_soz_dogan_yuk_dis_kal_field_0 = models.FloatField(db_column='ertelenmis_gelirler_musteri_soz.dogan_yuk._dis.kal.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    uzun_vadeli_karsiliklar = models.FloatField(blank=True, null=True)
    ertelenmis_vergi_yukumlulugu = models.FloatField(blank=True, null=True)
    diger_uzun_vadeli_yukumlulukler = models.FloatField(blank=True, null=True)
    ozkaynaklar = models.FloatField(blank=True, null=True)
    ana_ortakliga_ait_ozkaynaklar = models.FloatField(blank=True, null=True)
    odenmis_sermaye = models.FloatField(blank=True, null=True)
    deger_artis_fonlari = models.FloatField(blank=True, null=True)
    yabanci_para_cevrim_farklari = models.FloatField(blank=True, null=True)
    kardan_ayrilan_kisitlanmis_yedekler = models.FloatField(blank=True, null=True)
    gecmis_yillar_kar_zararlari = models.FloatField(db_column='gecmis_yillar_kar/zararlari', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    donem_net_kar_zarari = models.FloatField(db_column='donem_net_kar/zarari', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    diger_ozsermaye_kalemleri = models.FloatField(blank=True, null=True)
    azinlik_paylaribilanco = models.FloatField(blank=True, null=True)
    toplam_kaynaklar = models.FloatField(blank=True, null=True)
    surdurulen_faaliyetler = models.FloatField(blank=True, null=True)
    satis_gelirleri = models.FloatField(blank=True, null=True)
    satislarin_maliyeti_field = models.FloatField(db_column='satislarin_maliyeti_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ticari_faaliyetlerden_diger_kar_zarar = models.FloatField(blank=True, null=True)
    ticari_faaliyetlerden_brut_kar_zarar = models.FloatField(blank=True, null=True)
    faiz_ucret_prim_komisyon_ve_diger_gelirler = models.FloatField(db_column='faiz,_ucret,_prim,_komisyon_ve_diger_gelirler', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    faiz_ucret_prim_komisyon_ve_diger_giderler_field = models.FloatField(db_column='faiz,_ucret,_prim,_komisyon_ve_diger_giderler_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finans_sektoru_faaliyetlerinden_diger_kar_zarar = models.FloatField(blank=True, null=True)
    finans_sektoru_faaliyetlerinden_brut_kar_zarar = models.FloatField(blank=True, null=True)
    diger_gelir_ve_giderlerbilanco = models.FloatField(blank=True, null=True)
    brut_kar_zarar = models.FloatField(blank=True, null=True)
    pazarlama_satis_ve_dagitim_giderleri_field = models.FloatField(db_column='pazarlama,_satis_ve_dagitim_giderleri_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    genel_yonetim_giderleri_field = models.FloatField(db_column='genel_yonetim_giderleri_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arastirma_ve_gelistirme_giderleri_field = models.FloatField(db_column='arastirma_ve_gelistirme_giderleri_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    diger_faaliyet_gelirleri = models.FloatField(blank=True, null=True)
    diger_faaliyet_giderleri_field = models.FloatField(db_column='diger_faaliyet_giderleri_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    faaliyet_kari_oncesi_diger_gelir_ve_giderler = models.FloatField(blank=True, null=True)
    net_faaliyet_kar_zarari = models.FloatField(db_column='net_faaliyet_kar/zarari', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    yatirim_faaliyetlerinden_gelirler = models.FloatField(blank=True, null=True)
    yatirim_faaliyetlerinden_giderler_field = models.FloatField(db_column='yatirim_faaliyetlerinden_giderler_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    diger_gelir_ve_giderlergt = models.FloatField(blank=True, null=True)
    ozkaynak_yontemiyle_degerlenen_yatirimlarin_kar_zararlarindaki_field = models.FloatField(db_column='ozkaynak_yontemiyle_degerlenen_yatirimlarin_kar/zararlarindaki_', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    finansman_gideri_oncesi_faaliyet_kari_zarari = models.FloatField(db_column='finansman_gideri_oncesi_faaliyet_kari/zarari', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    esas_faaliyet_disi_finansal_gelirler = models.FloatField(blank=True, null=True)
    esas_faaliyet_disi_finansal_giderler_field = models.FloatField(db_column='esas_faaliyet_disi_finansal_giderler_-', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vergi_oncesi_diger_gelir_ve_giderler = models.FloatField(blank=True, null=True)
    surdurulen_faaliyetler_vergi_geliri_gideri = models.FloatField(blank=True, null=True)
    donem_vergi_geliri_gideri = models.FloatField(blank=True, null=True)
    ertelenmis_vergi_geliri_gideri = models.FloatField(blank=True, null=True)
    diger_vergi_geliri_gideri = models.FloatField(blank=True, null=True)
    durdurulan_faaliyetler_vergi_sonrasi_donem_kari_zarari = models.FloatField(blank=True, null=True)
    donem_kari_zarari = models.FloatField(blank=True, null=True)
    donem_kar_zararinin_dagilimi = models.FloatField(db_column='donem_kar/zararinin_dagilimi', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    azinlik_paylarigt = models.FloatField(blank=True, null=True)
    ana_ortaklik_paylari = models.FloatField(blank=True, null=True)
    hisse_basina_kazanc = models.FloatField(blank=True, null=True)
    seyreltilmis_hisse_basina_kazanc = models.FloatField(blank=True, null=True)
    surdurulen_faaliyetlerden_hisse_basina_kazanc = models.FloatField(blank=True, null=True)
    surdurulen_faaliyetlerden_seyreltilmis_hisse_basina_kazanc = models.FloatField(blank=True, null=True)
    amortisman_giderleri = models.FloatField(blank=True, null=True)
    kidem_tazminati = models.FloatField(blank=True, null=True)
    finansman_giderleri = models.FloatField(blank=True, null=True)
    yurtici_satislar = models.FloatField(blank=True, null=True)
    yurtdisi_satislar = models.FloatField(blank=True, null=True)
    net_yabanci_para_pozisyonu = models.FloatField(blank=True, null=True)
    parasal_net_yabanci_para_varlik_yukumluluk_pozisyonu = models.FloatField(db_column='parasal_net_yabanci_para_varlik/yukumluluk_pozisyonu', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    net_ypp_hedge_dahil = models.FloatField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    ceyreklik_satislar = models.FloatField(blank=True, null=True)
    ceyreklik_donem_kari = models.FloatField(blank=True, null=True)
    ceyreklik_faaliyet_kari = models.FloatField(blank=True, null=True)
    ceyreklik_brut_kar = models.FloatField(blank=True, null=True)
    ceyreklik_finansman_geliri = models.FloatField(blank=True, null=True)
    ceyreklik_finansman_gideri = models.FloatField(blank=True, null=True)
    ceyreklik_psd_giderleri = models.FloatField(blank=True, null=True)
    ceyreklik_genel_yonetim_giderleri = models.FloatField(blank=True, null=True)
    ceyreklik_diger_faaliyet_gelirleri = models.FloatField(blank=True, null=True)
    ceyreklik_diger_faaliyet_giderleri = models.FloatField(blank=True, null=True)
    ceyreklik_satislarin_maliyeti = models.FloatField(blank=True, null=True)
    ceyreklik_yatirim_faaliyeti_geliri = models.FloatField(blank=True, null=True)
    ceyreklik_yatirim_faaliyeti_gideri = models.FloatField(blank=True, null=True)
    ceyreklik_net_finansman = models.FloatField(blank=True, null=True)
    favok = models.FloatField(blank=True, null=True)
    ceyreklik_favok = models.FloatField(blank=True, null=True)
    ceyreklik_finansman_oncesi_kar_zarar = models.FloatField(blank=True, null=True)
    ceyreklik_vergi_oncesi_kar_zarar = models.FloatField(blank=True, null=True)
    ceyreklik_vergi = models.FloatField(blank=True, null=True)
    ceyreklik_amortisman = models.FloatField(blank=True, null=True)
    ceyreklik_esas_faaliyet_kari = models.FloatField(blank=True, null=True)
    ceyreklik_arge_gideri = models.FloatField(blank=True, null=True)
    yilliklandirilmis_donem_kari = models.TextField(blank=True, null=True)
    yilliklandirilmis_satislar = models.TextField(blank=True, null=True)
    yilliklandirilmis_esas_faaliyet_kari = models.TextField(blank=True, null=True)
    yilliklandirilmis_faaliyet_kari = models.TextField(blank=True, null=True)
    stock = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.stock} - {self.year}/{self.month}'

    class Meta:
        managed = False
        db_table = 'stocks_2'

