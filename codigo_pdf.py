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
pdf.set_font('Times', '', 8)

# PRIMEIRA LINHA DE GRÁFICOS 
pdf.rect(x=6,y=34,w=94,h=75.5,style='F')
pdf.image('IMA_idades.png', x = 9, y = 38, w = 88, h = 67.5)
pdf.text(10,114, "Histograma indicando uma maior frequência de HIV na faixa etária 25-35.")

pdf.rect(x=108,y=34,w=94,h=75.5,style='F')
pdf.image('IMA_ano_diag.png', x = 111, y = 38, w = 88, h = 67.5)
pdf.text(106,114,"Gráfico demonstra a trajetória dos casos de infecção pelo HIV de 2010 a março de 2024.")

# SEGUNDA LINHA DE GRÁFICOS
pdf.rect(x=6,y=117,w=94,h=75.5,style='F')
pdf.image('IMA_obito_diag.png', x = 9, y = 121, w = 88, h = 67.5)
pdf.text(10,197,"Maioria dos casos de óbito aconteceram em menos de um ano do diagnóstico.")

pdf.rect(x=108,y=117,w=94,h=75.5,style='F')
pdf.image("IMA_criterios.png", x = 111, y = 121, w = 88, h = 67.5)
pdf.text(129,197,"HIV+ é o critério de diagnóstico mais recorrente.")

# TERCEIRA LINHA DE GRÁFICOS
pdf.rect(x=6,y=200,w=94,h=75.5,style='F')
pdf.image('IMA_sexualidade.png', x=9, y=204, w= 88, h=67.5)
pdf.text(28,280,"Pessoas heterossexuais são as mais afetadas.")

pdf.rect(x=108,y=200,w=94,h=75.5,style='F')
pdf.image("IMA_evolucao.png", x = 111, y = 204, w = 88, h = 67.5)
pdf.text(129,280,"4,1% dos casos resultou em óbito por Aids.")

# QUARTA LINHA DE GRÁFICOS
pdf.add_page('P')
pdf.rect(x=42,y=10,w=126,h=80,style='F')
pdf.image("IMA_raca_sexo.png", x = 45, y = 14, w = 120, h = 72)
pdf.text(64,95,"Homens brancos e homens pardos são os grupos mais afetados pelo HIV.")

# QUINTA LINHA DE GRÁFICOS
pdf.rect(x=42,y=98,w=126,h=80,style='F')
pdf.image("IMA_nivel_escolaridade.png", x = 45, y = 102, w = 120, h = 72)
pdf.text(44,183,"Ensino Médio Incompleto e Ensino Fundamental Incompleto são os níveis de escolaridade mais recorrentes.")

# SEXTA LINHA DE GRÁFICOS
pdf.rect(x=42,y=186,w=126,h=80,style='F')
pdf.image("IMA_meses_diag.png", x = 45, y = 190, w = 120, h = 72)
pdf.text(62,271,"Gráfico mostra a frequência de casos em cada mês nos anos de maior ocorrência.")


pdf.set_fill_color(74,50,103)
pdf.rect(x=0,y=277,w=210,h=10,style='F')
pdf.set_text_color(241,228,219)
pdf.set_font('Times', 'B', 11.5)
pdf.text(8,283, "Gráficos criados a partir de dados publicados oficialmente pelo Ministério da Saúde (MS) por meio do DATASUS.")

pdf.output('dados_graficos.pdf')
print

