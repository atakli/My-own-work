
# ya bazı doc'ların içinde resimler olduğu için bu scripti kullanmadım şimdilik
import os
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)
yol = r'C:\Users\Emre\Downloads\Quiz2'
for i in os.listdir(yol):
	print(	'****************************************'+'\n'+
			"***********"+" SIRADAKİ: "+i+"***********"+
			'\n'+'****************************************')
	print(get_docx_text(yol+'\\'+i))
	
	