from docx import Document


def save_docx_text(file_name, text):
    file = Document()
    file.add_paragraph(text)
    file.save(f'{file_name}.docx')


def save_txt_text(file_name, text):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(text)