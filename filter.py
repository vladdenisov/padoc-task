import sys
import panflute as pf
from requests import head

headers = []

def headerIsExistingFilter(elem, doc):
  if isinstance(elem, pf.Header):
    text = pf.stringify(elem)
    if (text in headers):
      sys.stderr.write("Warning: Header `" + text + "` already exists in document\n")
    else:
      headers.append(text)

def levelHeaderFilter(elem, doc):
  if (isinstance(elem, pf.Header)):
    if (elem.level > 2):
      elem = pf.Plain(pf.Str(pf.stringify(elem).upper()))
      return elem

def boldify(doc):
  doc.replace_keyword('BOLD', pf.Strong(pf.Str('BOLD')))

if __name__ == '__main__':
  pf.run_filters([headerIsExistingFilter, levelHeaderFilter], prepare=boldify)
