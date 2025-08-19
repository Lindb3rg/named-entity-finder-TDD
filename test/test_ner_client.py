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
        expected_results = {'ents':[{'text':'Billy Bob','label':'Person'}], 'html':""}
        self.assertListEqual(result['ents'],expected_results['ents'])