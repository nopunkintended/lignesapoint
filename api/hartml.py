import random


def font_head():
    fonts = [('marius1', 'MariusRegular'),
             ('tenderness', 'TendernessRegular'),
             ('penna', 'PennaRegular'),
             ('boxfont-round', 'BoxfontRoundRegular'),
             ('bradley-gratis', 'BradleyGratisRegular'),
             ]

    font = random.choice(fonts)
    font_data = '<link rel="stylesheet" media="screen" href="https://fontlibrary.org/face/'
    font_data += font[0]
    font_data += '" type="text/css"/><style>body {font-family: "'
    font_data += font[1]
    font_data += '"; font-weight: normal; font-style: normal;}</style>'
    return font_data


def art_generate():
    html = '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Lignes à point</title>{}</head><body><h1>Deadbeef</h1></body></html>'.format(font_head())
    return html
