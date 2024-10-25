from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SAMPLE_NAME).exists():
            User.objects.create_user(
                username=settings.SAMPLE_NAME,
                email=settings.SAMPLE_EMAIL,
                password=settings.SAMPLE_PASSWORD,
                is_staff=True,
            )
            print("サンプルユーザー作成")
        else:
            print(f"サンプルユーザー[{settings.SAMPLE_NAME}]はすでに存在しています")