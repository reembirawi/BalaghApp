from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ("pending", "قيد الانتظار"),
        ("in_progress", "قيد العمل"),
        ("resolved", "تم الحل"),
    ]

    title = models.CharField(max_length=100, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints', verbose_name="صاحب الشكوى")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="الحالة")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "شكوى"
        verbose_name_plural = "الشكاوى"
    
    def __str__(self):
        return f"{self.title} - {self.owner.username}"
    
class Suggestion(models.Model):
    STATUS_CHOICES = [
        ("pending", "قيد الانتظار"),
        ("in_progress", "قيد العمل"),
        ("resolved", "تم الحل"),
    ]

    title = models.CharField(max_length=100, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suggestions', verbose_name="صاحب الاقتراح")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="الحالة")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "اقتراح"
        verbose_name_plural = "الاقتراحات"
    
    def __str__(self):
        return f"{self.title} - {self.owner.username}"