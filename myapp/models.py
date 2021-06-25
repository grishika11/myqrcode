from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.
class Qrcode(models.Model):
	data = models.CharField(max_length=200)
	qr_code=models.ImageField(upload_to='media/qr_codes',blank=True)

	def __str__(self):
		return str(self.data)

	