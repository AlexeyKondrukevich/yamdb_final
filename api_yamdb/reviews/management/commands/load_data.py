from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

DATA_TABLE = {
    User: "users.csv",
    Category: "category.csv",
    Genre: "genre.csv",
    Title: "titles.csv",
    Review: "review.csv",
    Comment: "comments.csv",
}


class Command(BaseCommand):
    help = "Loads data from static/data"

    def handle(self, *args, **options):
        for model, csv_file in DATA_TABLE.items():
            with open(
                f"{settings.BASE_DIR}/static/data/{csv_file}",
                "r",
                encoding="utf-8",
            ) as file:
                reader = DictReader(file)
                model.objects.bulk_create(model(**data) for data in reader)
        self.stdout.write(
            self.style.SUCCESS("***Data was succesfully loaded***")
        )
