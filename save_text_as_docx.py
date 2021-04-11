def save_as_docx(input_text, file_type):
    with open(f'docx.{file_type}', 'w', encoding='utf-8') as file:
        file.write(input_text)

