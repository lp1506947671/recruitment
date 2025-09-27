import csv

from django.core.management import BaseCommand
from interview.models import Candidate


class Command(BaseCommand):
    # python manage.py import_candidates --path /path/to/your/file.csv
    help = "导入候选人数据"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="CSV文件路径")

    def handle(self, *args, **options):
        path = options["path"]
        with open(path, newline="") as f:
            reader = csv.reader(f, dialect="excel", delimiter=";")
            for row in reader:
                candidate = Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    phone=row[2],
                    bachelor_school=row[3],
                    major=row[4],
                    degree=row[5],
                    test_score_of_general_ability=row[6],
                    paper_score=row[7],
                )
                print(candidate)
