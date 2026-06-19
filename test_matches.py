import zipfile
import xml.etree.ElementTree as ET

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

with zipfile.ZipFile('_posts/到台湾去.docx') as docx:
    xml_content = docx.read('word/document.xml')
    root = ET.fromstring(xml_content)
    
    with open('docx_paragraphs.txt', 'w', encoding='utf-8') as f:
        for p in root.findall('.//w:p', namespaces):
            # Find style
            style_elem = p.find('.//w:pPr/w:pStyle', namespaces)
            style = style_elem.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if style_elem is not None else None
            
            # Find text
            texts = [t.text for t in p.findall('.//w:t', namespaces) if t.text]
            text = "".join(texts)
            if text.strip():
                f.write(f"Style: {style} | Text: {text}\n")
