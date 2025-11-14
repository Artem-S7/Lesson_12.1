import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text_without_tags = []
    inside_tag = False

    for ch in html:
        if ch == '<':
            inside_tag = True
            continue
        if ch == '>':
            inside_tag = False
            continue
        if not inside_tag:
            text_without_tags.append(ch)

    cleaned = ''.join(text_without_tags)
    lines = cleaned.splitlines()
    non_empty = [line.strip() for line in lines if line.strip()]
    result_text = '\n'.join(non_empty)

    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write(result_text)
delete_html_tags('draft.html')





