from django.db import models

# Create your models here.
class Post_copy(models.Model):
    """title dan body ini akan di simpan sebagai kolom dan di konversi menjadi tabel MySQL"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default="user@domain.com", unique=False)
    posting_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Supaya judul posting di halaman admin akan sesuai title"""
        return f"{self.title}"
