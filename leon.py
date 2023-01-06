from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def extraire_texte_page(page, fichier_texte):
    """
    Extrait le texte d'une page PDF et l'écrit dans un fichier texte.
    """
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    interpreter.process_page(page)
    converter.close()
    texte = output.getvalue()
    output.close()
    fichier_texte.write(texte)

def extraire_texte_pdf(fichier_pdf):
    """
    Extrait le texte de chaque page d'un fichier PDF et écrit chaque page
    dans un fichier texte séparé.
    """
    infile = open(fichier_pdf, 'rb')
    for num_page, page in enumerate(PDFPage.get_pages(infile)):
        # Ouvre un fichier texte pour chaque page
        with open(f'page_{num_page + 1}.txt', 'w', encoding='utf-8') as fichier_texte:
            extraire_texte_page(page, fichier_texte)
    infile.close()

# Utilisation de la fonction
extraire_texte_pdf('mon_fichier.pdf')
