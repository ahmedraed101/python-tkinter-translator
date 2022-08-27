def detect_lang(t, text):
    response = t.detect(text)
    return response.lang


def translate(t, text, src, dest):
    if text.strip() == "":
        return ""
    text_ls = text.strip().split("\n")
    trans_text_ls = t.translate(text_ls, src=src, dest=dest)
    return "\n".join([i.text for i in trans_text_ls])
