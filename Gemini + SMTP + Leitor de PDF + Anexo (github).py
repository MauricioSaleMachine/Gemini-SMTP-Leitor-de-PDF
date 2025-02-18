import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import google.generativeai as genai  # Biblioteca do Gemini
import PyPDF2  # Biblioteca para ler PDFs

# Configurações do Gemini
GEMINI_API_KEY = ''  # Chave API

# Configurações do Gmail
GMAIL_USER = ''
GMAIL_PASSWORD = ''  # Senha de aplicativo do Gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Configurar a API do Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Função para fazer uma pergunta ao Gemini
def perguntar_ao_gemini(pergunta):
    try:
        # Inicializa o modelo do Gemini
        model = genai.GenerativeModel('gemini-pro')  # Usando o modelo Gemini Pro
        response = model.generate_content(pergunta)
        return response.text
    except Exception as e:
        return f"Erro ao consultar a API do Gemini: {e}"

# Função para enviar e-mail com anexo
def enviar_email(destinatario, assunto, corpo, caminho_do_pdf):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Adiciona o arquivo PDF como anexo
    try:
        with open(caminho_do_pdf, 'rb') as anexo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())
            encoders.encode_base64(part)  # Codifica o anexo em base64
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={caminho_do_pdf.split("/")[-1]}'  # Nome do arquivo
            )
            msg.attach(part)
    except Exception as e:
        print(f"Erro ao anexar o arquivo PDF: {e}")
        return

    # Envia o e-mail
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para ler um arquivo PDF
def ler_pdf(caminho_do_pdf):
    try:
        with open(caminho_do_pdf, 'rb') as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)  # Usando PdfReader em vez de PdfFileReader
            texto = ''
            for pagina in leitor.pages:  # Itera sobre as páginas do PDF
                texto += pagina.extract_text()
            return texto
    except Exception as e:
        return f"Erro ao ler o arquivo PDF: {e}"

# Função principal
def main():
    # Caminho do arquivo PDF
    caminho_do_pdf = '***'

    # Ler o conteúdo do PDF
    texto_do_pdf = ler_pdf(caminho_do_pdf)
    print(f"Conteúdo do PDF: {texto_do_pdf}")

    # Pergunta ao Gemini com base no conteúdo do PDF
    pergunta = f"Com base no seguinte texto de um PDF, escreva um e-mail formal de no mínimo 30 linhas que resuma o conteudo do PDF, iniciando com 'Prezado(a) ***' finalizando com um 'Atenciosamente: ***'. Aqui está o PDF:\n\n{texto_do_pdf}"
    resposta = perguntar_ao_gemini(pergunta)
    print(f"Resposta do Gemini: {resposta}")

    # Enviar a resposta por e-mail com o PDF anexado
    destinatario = ''
    assunto = 'Resumo da reunião - (13/02/2025)'
    enviar_email(destinatario, assunto, resposta, caminho_do_pdf)

if __name__ == "__main__":
    main()