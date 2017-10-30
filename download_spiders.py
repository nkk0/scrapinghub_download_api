import json
import sys

from scrapinghub import ScrapinghubClient


# Scrapy Cloud API key and project number
apikey = ''
project_number = 0

def get_jsons(starting_spider_number, ending_spider_number):
    number_of_items = ending_spider_number - starting_spider_number + 1
    client = ScrapinghubClient(apikey)

    for i in range(number_of_items):
        depth = 1
        job = client.get_job('{}/{}/{}'.format(project_number, i + starting_spider_number, depth))

        while not job.items.list() and depth < 10:
            depth += 1
            print()
            print('Depth is now {}.'.format(depth))
            job = client.get_job('{}/{}/{}'.format(project_number, i + starting_spider_number, depth))

        if job.items.list():
            print('Writing {}.'.format(dict(job.metadata.list()).get('spider')))
            with open('{}.json'.format(dict(job.metadata.list()).get('spider')), 'w+') as f:
                json.dump(job.items.list(), f)
        else:
            print('Spider not found.')

get_jsons(int(sys.argv[1]),int(sys.argv[2]))
