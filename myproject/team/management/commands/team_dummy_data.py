from django.core.management.base import BaseCommand, CommandError
from team.models import *


"""This command is used to insert 
   data into userInfo and ActivityPeriod table"""
class Command(BaseCommand):
    help = 'create dummy data for team  model'


    def handle(self, *args, **options):
        Team.objects.bulk_create([Team(name='India', logo_url='https://previews.123rf.com/images/inkdrop/inkdrop1711/inkdrop171100532/90225939-india-national-flag-football-crest-a-logo-type.jpg', club_state='Delhi'),
                                  Team(name='FC Barcelona',  logo_url='https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/83.png', club_state='Barcelona'),
                                  Team(name='Juventus F.C.', logo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTmx8Amn2qkFK_UREDuMktFos7E6mOYLTkzppKj4kmaVBd9KJpj&usqp=CAU', club_state='Turin')
                                  ])
        print('data inserted successfully')

