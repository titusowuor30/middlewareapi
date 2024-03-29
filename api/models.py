from operator import mod
from tabnanny import verbose
from unicodedata import category
from venv import create
from django.db import models

# indicators


class indicators(models.Model):
    facility = models.CharField(
        max_length=500, blank=True, null=True)
    ward = models.CharField(
        max_length=500, blank=True, null=True)
    subcounty = models.CharField(max_length=500, blank=True, null=True)
    county = models.CharField(max_length=500, blank=True, null=True)
    MOH_UID = models.CharField(max_length=255, blank=True, null=True)
    MOH_Indicator_ID = models.CharField(max_length=500)
    MOH_Indicator_Name = models.CharField(
        max_length=500, blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    shortName = models.CharField(max_length=500, blank=True, null=True)
    displayName = models.CharField(max_length=500, blank=True, null=True)
    displayShortName = models.CharField(max_length=500, blank=True, null=True)
    displayNumeratorDescription = models.CharField(
        max_length=500, blank=True, null=True)
    denominatorDescription = models.CharField(
        max_length=500, blank=True, null=True)
    displayDenominatorDescription = models.CharField(
        max_length=500, blank=True, null=True)
    numeratorDescription = models.CharField(
        max_length=500, blank=True, null=True)
    dimensionItem = models.CharField(max_length=500, blank=True, null=True)
    displayFormName = models.CharField(max_length=500, blank=True, null=True)
    numerator = models.CharField(max_length=2500, blank=True, null=True)
    denominator = models.CharField(max_length=2500, blank=True, null=True)
    dimensionItemType = models.CharField(max_length=500, blank=True, null=True)
    indicatorType = models.ForeignKey(
        'indicatorType', on_delete=models.CASCADE, related_name='indicators', blank=True, null=True)
    indicatorGroups = models.ManyToManyField(
        'indicatorGroups', blank=True, null=True)
    khis_data = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.MOH_Indicator_ID

    class Meta:
        db_table = 'moh_indicators'
        verbose_name_plural = 'indicators'


class indicator_category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'indicator_category'
        verbose_name_plural = 'Indicator Categories'


class counties(models.Model):
    name = models.CharField(max_length=100)
    subcounties=models.ManyToManyField("subcounties",blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'counties'
        verbose_name_plural = 'Counties'

class subcounties(models.Model):
    name = models.CharField(max_length=100)
    wards=models.ManyToManyField("ward",blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subcounties'
        verbose_name_plural = 'Sub Counties'

class ward(models.Model):
    name = models.CharField(max_length=100)
    facilities = models.ManyToManyField("Facilities",blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ward'
        verbose_name_plural = 'Wards'

class Facilities(models.Model):
    name = models.CharField(max_length=255, default='Mulele', blank=True,null=True)
    uid = models.CharField(max_length=255, default='xxxxxxxxx', blank=True,null=True)
    mfl_code=models.CharField(max_length=255, default='0000', blank=True,null=True)
    level=models.CharField(max_length=5,default=5, blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'facilities'
        verbose_name_plural = 'Facilities'

class indicatorType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'moh_indicator_types'
        verbose_name_plural = 'indicators types'


class indicatorGroups(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    lastUpdated = models.DateTimeField()
    created = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'moh_indicator_groups'
        verbose_name_plural = 'indicators groups'


class middleware_settings(models.Model):
    syncdata = models.BooleanField(default=False)
    client_url = models.URLField(
        default="https://test.hiskenya.org/dhiske/", blank=True, null=True)

    def __str__(self):
        return "Data Sync Settings"

    class Meta:
        db_table = 'middleware_settings'
        verbose_name_plural = 'Data Sync Settings'


class schedule_settings(models.Model):
    sync_time = models.DateTimeField()
    shedule_description = models.CharField(
        default="Weekely  data sync", max_length=255, blank=True, null=True)

    def __str__(self):
        return "Schedule Settings"

    class Meta:
        db_table = 'schedule_settings'
        verbose_name_plural = 'Schedule Settings'


class total_records(models.Model):
    records = models.IntegerField(default=0)

    def __str__(self):
        return str(self.records) if self.records is not None or '' else "No Files yet!"

    class Meta:
        db_table = 'khis_total_records'
        verbose_name_plural = 'Total Records'


class Data_Mapping_Files(models.Model):
    mapping_file = models.FileField(upload_to='mapping_files/%Y')

    def __str__(self):
        return self.mapping_files.url

    class Meta:
        db_table = 'data_mapping_files'
        verbose_name_plural = 'Data Mapping Files'


class mapped_data(models.Model):
    Date_Mapped = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    DATIM_Indicator_Category = models.CharField(
        max_length=255, blank=True, null=True)
    DATIM_Indicator_ID = models.CharField(
        max_length=500, blank=True, null=True)
    DATIM_Disag_Name = models.CharField(max_length=255, blank=True, null=True)
    DATIM_Disag_ID = models.CharField(max_length=255, blank=True, null=True)
    Operation = models.CharField(max_length=20, blank=True, null=True)
    MOH_Indicator_Name = models.CharField(
        max_length=1500, blank=True, null=True)
    MOH_Indicator_ID = models.CharField(max_length=500, blank=True, null=True)
    # MOH_Disag_Name = models.CharField(max_length=255, blank=True, null=True)
    # MOH_Disag_ID = models.CharField(max_length=255, blank=True, null=True)
    Disaggregation_Type = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.DATIM_Disag_Name

    class Meta:
        verbose_name_plural = 'Mapped Data'


class final_comparison_data(models.Model):
    create_date = models.DateField(blank=True, null=True)
    facility = models.CharField(
        max_length=500, blank=True, null=True)
    ward = models.CharField(
        max_length=500, blank=True, null=True)
    subcounty = models.CharField(max_length=500, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    MOH_FacilityID = models.CharField(max_length=500, blank=True, null=True)
    DATIM_Disag_ID = models.CharField(max_length=500, blank=True, null=True)
    MOH_IndicatorCode = models.CharField(max_length=500, blank=True, null=True)
    indicators = models.CharField(
        max_length=1500, blank=True, null=True)
    category = models.CharField(
        max_length=1500, blank=True, null=True)
    DATIM_Disag_Name = models.CharField(
        max_length=1500, blank=True, null=True)
    khis_data = models.CharField(
        max_length=255, blank=True, null=True)
    datim_data = models.CharField(
        max_length=255, blank=True, null=True)
    weight = models.FloatField(
        max_length=255, blank=True, null=True)
    concodance = models.FloatField(
        max_length=255, blank=True, null=True)
    khis_minus_datim = models.IntegerField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.indicators

    class Meta:
        db_table = 'final_comparison_data'
        verbose_name_plural = 'Final Comparison Data'


class Concodance(models.Model):
    county = models.ForeignKey(
        counties, on_delete=models.CASCADE, related_name='concodance')
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)
    indicator_name = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.DecimalField(
        max_digits=10, decimal_places=2, default=90.00)

    def __str__(self):
        return self.county.name

    class Meta:
        db_table = 'concodance'
        verbose_name_plural = 'Concodance'
