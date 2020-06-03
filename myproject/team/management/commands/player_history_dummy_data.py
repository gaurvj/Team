from django.core.management.base import BaseCommand, CommandError
from team.models import *


"""This command is used to insert 
   data into userInfo and ActivityPeriod table"""
class Command(BaseCommand):
    help = 'create dummy data for players history model'


    def handle(self, *args, **options):
            PlayerHistory.objects.bulk_create([PlayerHistory(team_id=1, match_id=1, player_id=1,  fifty=2,
                                                              hundred=1,
                                                             high_score=120, total_run=220
                                                             ),
                                               PlayerHistory(team_id=1, match_id=1, player_id=2, fifty=1,
                                                             hundred=2,
                                                             high_score=100, total_run=250
                                                             ),
                                               PlayerHistory(team_id=1, match_id=1, player_id=3, fifty=1,
                                                             hundred=0,
                                                             high_score=52, total_run=52
                                                             )
                                               ])
            print('data inserted successfully')