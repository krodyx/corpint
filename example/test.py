import logging
from os import path
import corpint

log = logging.getLogger('test')
project = corpint.project('test')

log.info("Creating sample entity...")
origin = project.origin('luke')
origin.emit_entity({
    'uid': origin.uid('calderbank'),
    'type': 'Person',
    'name': 'Damian Calderbank',
    'aliases': ['Damian James Calderbank', 'Damian J. Calderbank'],
    'weight': 5,
    'jurisdiction': 'United Kingdom'
})

log.info("Reading CSV file...")
with open(path.join(path.dirname(__file__), 'test.csv')) as fh:
    origin = project.origin(fh.name)
    origin.clear()
    for entity in corpint.load.csv(fh):
        entity['uid'] = origin.uid(entity['name'])
        entity['weight'] = 1
        origin.emit_entity(entity)

log.info("Data integration...")
# project.integrate(auto_match=True)
# project.enrich('wikipedia')
# project.integrate(auto_match=True)
# project.enrich('wikidata')
project.enrich('aleph')
