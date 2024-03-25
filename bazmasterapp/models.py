from django.db import models


class Bank(models.Model):
    name_bank = models.CharField(max_length=100, verbose_name="Название банка", unique=True)


class TypeBankAccounts(models.Model):
    name_type_bank_acc = models.CharField(max_length=100, verbose_name="Название типа счета", unique=True)


class BankAccounts(models.Model):
    id_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="Название банка")
    id_type = models.ForeignKey(TypeBankAccounts, on_delete=models.CASCADE, verbose_name="Название типа счета")
    name_bank_acc = models.CharField(max_length=100, verbose_name="Название счета")
    summary = models.FloatField(verbose_name="Сумма")
    create_date = models.DateField(verbose_name="Дата создания")
    close_date = models.DateField(verbose_name="Дата закрытия")
    isActive = models.BooleanField(verbose_name="Активен")


class TypesCategories(models.Model):
    type_name = models.CharField(max_length=100, verbose_name="Название типа категории", unique=True)


class Categories(models.Model):
    id_type = models.ForeignKey(TypesCategories, on_delete=models.CASCADE, verbose_name="Название типа категории")
    name_category = models.CharField(max_length=100, verbose_name="Название категории")


class SubCategories(models.Model):
    id_cat = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Название категории")
    name_sub_cat = models.CharField(max_length=100, verbose_name="Название подкатегории")
