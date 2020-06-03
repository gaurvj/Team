from django.core.management.base import BaseCommand, CommandError
from team.models import *


"""This command is used to insert 
   data into userInfo and ActivityPeriod table"""
class Command(BaseCommand):
    help = 'create dummy data for points'


    def handle(self, *args, **options):
        Point.objects.bulk_create([Point(match_id=1, team_id=1, point=2),
                                   Point(match_id=1, team_id=2, point=1)]
                                  )

        print('data inserted successfully')