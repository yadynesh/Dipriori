from django.core.management.base import BaseCommand, CommandError
from shortener.models import MagicUrl

class Command(BaseCommand):
    help = 'Run the client to calculate association-rules'

    # def add_arguments(self, parser):
    #     parser.add_argument('--items', type=int) 
    #     #if I specify -- here then I have to specify it while giving the arguments
    #     #i.e python manage.py runclient --items 5
        

    def handle(self, *args, **options):
        print(options)
        return MagicUrl.objects.refresh_shortcodes(items = options['items'])