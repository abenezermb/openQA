import ktrain
from ktrain import text

# # input data
# docs = []

# # create a search index
# INDEXDIR = '/tmp/myindex'
# text.SimpleQA.initialize_index(INDEXDIR)
# text.SimpleQA.index_from_list(docs,INDEXDIR,commit_every=len(docs))

# # create QA instance
# qa = text.SimpleQA(INDEXDIR)

# # asking questions
# question = ""
# answers = qa.ask('')
# answers = answers[:5] # return the first five answers

def loadModel(docs):
    # create a search index
    INDEXDIR = '/tmp/myindex'
    text.SimpleQA.initialize_index(INDEXDIR)
    text.SimpleQA.index_from_list(docs,INDEXDIR,commit_every=len(docs))
    # create QA instance
    qa = text.SimpleQA(INDEXDIR)
    return qa

def askQuestion(qa,question):
    answers = qa.ask(question)
    return answers[:5]