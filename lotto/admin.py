from django.contrib import admin
from lotto.models import GuessNumbers # .models -> admin파일과 같은 폴더에 있는 models파일

# Register your models here.
admin.site.register(GuessNumbers)
