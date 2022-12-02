# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Takeaway(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    restaurantid = models.BigIntegerField(db_column='RestaurantId', blank=True, null=True)  # Field name made lowercase.
    cityid = models.TextField(db_column='CityId', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='Hour', blank=True, null=True)  # Field name made lowercase.
    dayofweek = models.TextField(db_column='DayOfWeek', blank=True, null=True)  # Field name made lowercase.
    totaldeliverytimeinsec = models.IntegerField(db_column='TotalDeliveryTimeInSec', blank=True, null=True)  # Field name made lowercase.
    neworderorig = models.DateTimeField(db_column='NewOrderOrig', blank=True, null=True)  # Field name made lowercase.
    neworder_assigned = models.IntegerField(db_column='NewOrder_Assigned', blank=True, null=True)  # Field name made lowercase.
    assigned_atrestaurant = models.IntegerField(db_column='Assigned_AtRestaurant', blank=True, null=True)  # Field name made lowercase.
    atrestaurant_leftrestaurant = models.IntegerField(db_column='AtRestaurant_LeftRestaurant', blank=True, null=True)  # Field name made lowercase.
    leftrestaurant_atdoor = models.IntegerField(db_column='LeftRestaurant_AtDoor', blank=True, null=True)  # Field name made lowercase.
    atdoor_delivered = models.IntegerField(db_column='AtDoor_Delivered', blank=True, null=True)  # Field name made lowercase.
    neworderts = models.IntegerField(db_column='NewOrderTS', blank=True, null=True)  # Field name made lowercase.
    assignedts = models.FloatField(db_column='AssignedTS', blank=True, null=True)  # Field name made lowercase.
    atrestaurantts = models.FloatField(db_column='AtRestaurantTS', blank=True, null=True)  # Field name made lowercase.
    leftrestaurantts = models.FloatField(db_column='LeftRestaurantTS', blank=True, null=True)  # Field name made lowercase.
    atdoorts = models.FloatField(db_column='AtDoorTS', blank=True, null=True)  # Field name made lowercase.
    deliveredts = models.IntegerField(db_column='DeliveredTS', blank=True, null=True)  # Field name made lowercase.
    dateindays = models.IntegerField(db_column='DateInDays', blank=True, null=True)  # Field name made lowercase.
    tocinprevhourinrest = models.FloatField(db_column='TOCInPrevHourInRest', blank=True, null=True)  # Field name made lowercase.
    tocinprevhourincity = models.FloatField(db_column='TOCInPrevHourInCity', blank=True, null=True)  # Field name made lowercase.
    tdtinprevhourinrest = models.FloatField(db_column='TDTInPrevHourInRest', blank=True, null=True)  # Field name made lowercase.
    tdtinprevhourincity = models.FloatField(db_column='TDTInPrevHourInCity', blank=True, null=True)  # Field name made lowercase.
    tdtinprevweekinrest = models.FloatField(db_column='TDTInPrevWeekInRest', blank=True, null=True)  # Field name made lowercase.
    tdtinprevweekincity = models.FloatField(db_column='TDTInPrevWeekInCity', blank=True, null=True)  # Field name made lowercase.
    congestion = models.TextField(db_column='Congestion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Takeaway'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Stocks(models.Model):
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
    id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'


class Takeaway(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    restaurantid = models.BigIntegerField(blank=True, null=True)
    cityid = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    dayofweek = models.TextField(blank=True, null=True)
    totaldeliverytimeinsec = models.IntegerField(blank=True, null=True)
    neworderorig = models.DateTimeField(blank=True, null=True)
    neworder_assigned = models.IntegerField(blank=True, null=True)
    assigned_atrestaurant = models.IntegerField(blank=True, null=True)
    atrestaurant_leftrestaurant = models.IntegerField(blank=True, null=True)
    leftrestaurant_atdoor = models.IntegerField(blank=True, null=True)
    atdoor_delivered = models.IntegerField(blank=True, null=True)
    neworderts = models.IntegerField(blank=True, null=True)
    assignedts = models.FloatField(blank=True, null=True)
    atrestaurantts = models.FloatField(blank=True, null=True)
    leftrestaurantts = models.FloatField(blank=True, null=True)
    atdoorts = models.FloatField(blank=True, null=True)
    deliveredts = models.IntegerField(blank=True, null=True)
    dateindays = models.IntegerField(blank=True, null=True)
    tocinprevhourinrest = models.FloatField(blank=True, null=True)
    tocinprevhourincity = models.FloatField(blank=True, null=True)
    tdtinprevhourinrest = models.FloatField(blank=True, null=True)
    tdtinprevhourincity = models.FloatField(blank=True, null=True)
    tdtinprevweekinrest = models.FloatField(blank=True, null=True)
    tdtinprevweekincity = models.FloatField(blank=True, null=True)
    congestion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takeaway'


class Temp1(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp1'


class Temp2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp2'
