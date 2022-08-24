from django.db import models
from django.utils import timezone


modality =[('1', 'MRI'),
    ('2','CT'),
    ('3','超音波検査'),
    ('4','基本検査'),
    ('5','医師①'),
    ('6','医師②(内視鏡)'),
    ('7','医師③'),
    ]


class Book(models.Model):
    reservation_id = models.CharField	('予約ID' , max_length=20)
    reservation_date = models.DateField('予約日付')
    reservation_time = models.TimeField('予約時間')
    book_staff= models.CharField('予約担当', max_length=20)
    book_time = models.DateTimeField('日付', default=timezone.now)
    # patient_id=models.ForeignKey(Patients, to_field='patient_id',null=True,on_delete=models.CASCADE, blank=True, related_name='patient_id')
    purpose = models.CharField('目的', max_length=10)
    color= models.CharField('色', max_length=10)
    # course_id =models.ForeignKey(Courses, to_field='course_id',null=True,on_delete=models.CASCADE, blank=True, related_name='course_id')
    modality = models.CharField('検査モダリティ', choices = modality, max_length=10)
    part =models.CharField('検査部位', max_length=10)
    memo = models.TextField('メモ')

    def __str__(self):
        return self.reservation_id