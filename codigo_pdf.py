from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")

pdf.add_page()

# TÍTULO
pdf.set_x(x=0)
pdf.set_font('Times', 'B', 20)
pdf.set_fill_color(74,50,103)
pdf.set_text_color(241,228,219)
pdf.multi_cell(220, 10, 'DADOS DE HIV ENTRE 2010 E 2024 \n NO ESTADO DE MINAS GERAIS',
                align = 'C', fill=True)

# CORES E FONTE
pdf.set_fill_color(241,228,219)
pdf.set_text_color(74,50,103)
pdf.set_font('Times', '', 11)

# PRIMEIRA LINHA DE GRÁFICOS 
pdf.set_xy(x=6, y=34)
pdf.cell(94, 75.5, ln= 0, align = 'C', fill=True)
pdf.image('distribuicao_idades.png', x = 9, y = 38, w = 88, h = 67.5)

pdf.set_x(x=108)
pdf.cell(94, 75.5, ln= 1, align = 'C', fill=True)
pdf.image('ano_DIA.png', x = 111, y = 38, w = 88, h = 67.5)

# SEGUNDA LINHA DE GRÁFICOS

pdf.set_xy(x=6, y=114)
pdf.cell(94, 75.5, ln= 0, align = 'C', fill=True)
pdf.image('diferenca_DIA_OB.png', x = 9, y = 118, w = 88, h = 67.5)

pdf.set_x(x=108)
pdf.cell(94, 75.5, ln= 1, align = 'C', fill=True)
pdf.image("casos_CRI.png", x = 111, y = 118, w = 88, h = 67.5)

# TERCEIRA LINHA DE GRÁFICOS

pdf.set_xy(x=6, y=195)
pdf.cell(196, 81, ln= 2, align = 'C', fill=True)
pdf.image('distribuicao_idades.png', x=9, y=199, w= 94, h=73)
pdf.image("nivel_escolaridade.png", x = 105, y = 199, w = 94, h = 73)

pdf.output('teste.pdf')
print

