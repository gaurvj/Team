from django.contrib import admin
from.models import Match
from django.contrib.auth.models import User, Group


class MatchAdmin(admin.ModelAdmin):

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',  # jquery
            '/static/admin/team/js/match_main.js',  # app static folder
        )

admin.site.register(Match, MatchAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'Match Fixture'


