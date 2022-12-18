from django.db import models

# Create your models here.
class Post(models.Model):
    """title dan body ini akan di simpan sebagai kolom dan di konversi menjadi tabel MySQL"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default="user@domain.com")

    def __str__(self):
        """Supaya judul posting di halaman admin akan sesuai title"""
        return f"{self.title}"
