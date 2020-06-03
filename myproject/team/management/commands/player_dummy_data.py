from django.core.management.base import BaseCommand, CommandError
from team.models import *


"""This command is used to insert 
   data into userInfo and ActivityPeriod table"""
class Command(BaseCommand):
    help = 'create dummy data for players model'


    def handle(self, *args, **options):
            Player.objects.bulk_create([Player(team_id=1, first_name='Vijay', last_name='Gaur',
                                               image_url='https://imgprod65.hobbylobby.com/8/da/9a/8da9a93891a5eadd3558097dd33b2aee8835c35d/700Wx700H-193359-0320-px.jpg',
                                               player_jersy_number=1,
                                               country='India'
                                               ),
                                        Player(team_id=1, first_name='Vicky', last_name='M',
                                               image_url='https://imgprod65.hobbylobby.com/8/da/9a/8da9a93891a5eadd3558097dd33b2aee8835c35d/700Wx700H-193359-0320-px.jpg',
                                               player_jersy_number=2,
                                               country='India'
                                               ),
                                        Player(team_id=1, first_name='Akash.', last_name='Neil',
                                               image_url='https://www.nationalarchives.gov.uk/wp-content/uploads/2015/06/logo-a-tna-600x315.jpg',
                                               player_jersy_number=3,
                                               country='India')
                                        ])
            print('data inserted successfully')