class NerModelTestDouble:
    """
    Test Double for spaCy NLP Model
    """
    def __init__(self,model):
        self.model = model
        
    def returns_doc_ents(self,ents):
        self.ents = ents
    
    def __call__(self,sent):
        return DocTestDouble(sent, self.ents)


class DocTestDouble:
    """
    Test Double for spaCy Doc
    """
    def __init__(self,sent,ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]
    
    def patch_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self,attr,patched)
        return self

class SpanTestDouble:
    """
    Test Double for spaCy Span
    """
    def __init__(self,text,label):
        self.text = text
        self.label_ = label