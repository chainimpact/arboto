from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from arboto.settings import DEBUG

from django.core.management.base import BaseCommand

# not useful anymore because we don't have to execute outside files anymore.
# if DEBUG:
#     ENV_PATH = '/home/felipe/.virtualenvs/arboto'
# else:
#     # TODO
#     ENV_PATH = ''


class Command(BaseCommand):
    help = 'getting prices from pyarboto data files'

    def handle(self, *args, **options):
        for data_file in os.listdir('../../../pyarboto/data'):
            if not data_file.endswith('placeholder'):
                with open(os.path.join('../../../pyarboto/data', data_file)) as f:
                    content = f.read()
