from datetime import datetime

from django.db import models

class Incidents(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    description = models.CharField(max_length=255, verbose_name='Описание',)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    taken_measures = models.CharField(max_length=255, verbose_name='Принятые меры по ликвидации', null=True, blank=True)



    #электрики сообщат о происшествии диспетчеру, диспетчер - создание заявки о происшествии

    list_display = ('address','description', )
    search_fields = ['address', 'description']
    class Meta:
        verbose_name = "Происшествие"
        verbose_name_plural = "Происшествия"
        permissions = [
            ("Incidents.incidents_add", "Добавление происшествий"),
            ("Incidents.incidents_change", "Изменение происшествий"),
            ("Incidents.incidents_delete", "Удаление происшествий"),
            ("Incidents.incidents_id", "Просмотр происшествия"),
            ("Incidents.incidents_map", "Просмотр всех происшествий на карте"),

            ("Incidents.incidents_all", "Просмотр всех происшествий в таблице"),
        ]

    def __str__(self):
        return self.address
