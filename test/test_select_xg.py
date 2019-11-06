import pytest
import io
from spodgi import XgStore

from rdflib.namespace import RDF
from rdflib.store import Store
from rdflib import Graph
from rdflib import plugin
from rdflib.collection import Collection

def test_open_odgi():
    plugin.register('XgStore', Store,'spodgi.XgStore', 'XgStore')
    s = plugin.get('XgStore', Store)(base="http://example.org/test/")
    spodgi = Graph(store=s)
    spodgi.open('./test/t.xg', create=False)
    count=0;
    for t in spodgi.triples((None, None, None)):
        (s, p, o) = t
        assert s != None
        assert p != None
        assert o != None
        count=count+1
    assert count > 40
    spodgi.close()

def test_count_all():
    plugin.register('XgStore', Store,'spodgi.XgStore', 'XgStore')
    s = plugin.get('XgStore', Store)(base="http://example.org/test/")
    spodgi = Graph(store=s)
    spodgi.open('./test/t.xg', create=False)
    for r in spodgi.query('SELECT (count(*) as ?count) WHERE {?s ?p ?o}'):
        assert r[0].value == 91
        
    spodgi.close()
    assert True

def test_select_specific_step():
    plugin.register('XgStore', Store,'spodgi.XgStore', 'XgStore')
    s = plugin.get('XgStore', Store)(base="http://example.org/test/")
    spodgi = Graph(store=s)
    spodgi.open('./test/t.xg', create=False)
    for r in spodgi.query('SELECT ?rank WHERE {<path/x/step/2> <http://biohackathon.org/resource/VG#rank> ?rank}'):
        assert r[0].value == 2
        
    spodgi.close()
    assert True