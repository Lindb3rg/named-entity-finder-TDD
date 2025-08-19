import unittest

from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):
    
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents,dict)
    
    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Hello this is a sentence!")
        self.assertIsInstance(ents,dict)
    
    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Billy Bob','label_':'PERSON'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'Billy Bob','label':'Person'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])
    
    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Lithuanian','label_':'NORP'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'Lithuanian','label':'Group'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])
    
    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'The city','label_':'LOC'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'The city','label':'Location'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])
    
    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'American Sign language','label_':'LANGUAGE'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'American Sign language','label':'Language'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])
    
    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Australia','label_':'GPE'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'Australia','label':'Location'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])
    
    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Australia','label_':'GPE'},{'text':'Conny Bob','label_':'PERSON'}]
        ner = NamedEntityClient(model)
        model.returns_doc_ents(doc_ents)
        result = ner.get_ents(".....")
        expected_results = {'ents':[{'ent':'Australia','label':'Location'},
                                    {'ent':'Conny Bob','label':'Person'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])