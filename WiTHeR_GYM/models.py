from django.db import models
from datetime import *

class Client(models.Model):
    """Клиенты"""
    surname_c = models.CharField("Фамилия клиента", max_length=15, primary_key=True)
    name_c = models.CharField("Имя клиента", max_length=15)
    patronymic_c = models.CharField("Отчество клиента", max_length=15)
    birthdate_c = models.DateField("Дата рождения клиента")
    phonenumber_c = models.CharField("Номер телефона клиента", max_length=12)
    sex_c = models.CharField("Пол клиента", max_length=5)
    address_c = models.CharField("Адрес клиента", max_length=100)

    def __str__(self):
        return f'{self.surname_c} {self.name_c} {self.patronymic_c}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class PriceList(models.Model):
    """Цена"""
    price = models.IntegerField("Цена")

    def __str__(self):
        return f'{self.price}'

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

class Abonement(models.Model):
    """Абонемент"""
    name_abonement = models.CharField("Название абонемента", max_length=20, primary_key=True)
    price = models.ForeignKey(PriceList, verbose_name="Цена", on_delete=models.SET_NULL, null=True)
    number_of_visits = models.IntegerField("Количество посещений")
    number_of_days = models.IntegerField("Количество дней")

    def __str__(self):
        return f'{self.name_abonement}'

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"

class SaleAbonements(models.Model):
    """Продажа абонемента"""
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    name_abonement = models.ForeignKey(Abonement, verbose_name="Абонемент", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата активации абонемента")
    finish_date = models.DateField("Дата деактивации абонемента")

    def __str__(self):
        return f'{self.client} - {self.name_abonement}'

    class Meta:
        verbose_name = "Продажа абонемента"
        verbose_name_plural = "Продажа абонементов"

class Premises(models.Model):
    """Помещение"""
    premises = models.CharField("Помещение", max_length=30)

    def __str__(self):
        return f'{self.premises}'

    class Meta:
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

class TypesOfTraining(models.Model):
    """Тип тренировки"""
    type_training = models.CharField("Тип тренировки", max_length=50)

    def __str__(self):
        return f'{self.type_training}'

    class Meta:
        verbose_name = "Тип тренировки"
        verbose_name_plural = "Типы тренировок"

class Services(models.Model):
    """Услуга"""
    service = models.CharField("Услуга", max_length=20, primary_key=True)
    type_training = models.ForeignKey(TypesOfTraining, verbose_name="Тип тренировки", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Employes(models.Model):
    """Тренер"""
    surname_e = models.CharField("Фамилия тренера", max_length=15, primary_key=True)
    name_e = models.CharField("Имя тренера", max_length=15)
    patronymic_e = models.CharField("Отчество тренера", max_length=15)
    birthdate_e = models.DateField("Дата рождения тренера")
    address_e = models.CharField("Адрес тренера", max_length=100)
    salary_e = models.IntegerField("Оклад клиента")

    def __str__(self):
        return f'{self.surname_e} {self.name_e} {self.patronymic_e}'

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

class SpecEmployes(models.Model):
    """Тренер - Услуга"""
    employee = models.ForeignKey(Employes, verbose_name="Тренер", on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.employee} - {self.service}'

    class Meta:
        verbose_name = "Тренер - Услуга"
        verbose_name_plural = "Тренеры - Услуги"

class Schedule(models.Model):
    """Расписание"""
    date_r = models.DateField("Дата тренировки")
    start_time = models.TimeField("Время начала тренировки")
    finish_time = models.TimeField("Время окончания тренировки")
    employee = models.ForeignKey(Employes, verbose_name="Тренер", on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.SET_NULL, null=True)
    premises = models.ForeignKey(Premises, verbose_name="Помещение", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.employee} - {self.service}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

class TrackingVisits(models.Model):
    """Учёт посещений"""
    card_number = models.ForeignKey(SaleAbonements, verbose_name="Продажа абонемента", on_delete=models.SET_NULL, null=True)
    schedule_number = models.ForeignKey(Schedule, verbose_name="Расписание", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.card_number} - {self.schedule_number}'

    class Meta:
        verbose_name = "Учёт посещений"
        verbose_name_plural = "Учёт посещений"
