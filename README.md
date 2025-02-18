# Gemini-SMTP-Leitor-de-PDF
Este código é um script Python que automatiza a leitura de um arquivo PDF, consulta a API do Gemini (um modelo de linguagem generativa) para gerar um resumo formal do conteúdo do PDF e, em seguida, envia esse resumo por e-mail com o PDF anexado.



Este código é um exemplo de automação que combina a leitura de arquivos PDF, a geração de conteúdo usando inteligência artificial (IA) e o envio de e-mails com anexos. Ele foi projetado para facilitar tarefas repetitivas, como resumir documentos e compartilhá-los de forma automatizada. Abaixo está uma explicação detalhada do funcionamento do código:

1. Leitura de PDF
O código utiliza a biblioteca PyPDF2 para ler o conteúdo de um arquivo PDF. A função ler_pdf abre o arquivo, extrai o texto de todas as páginas e retorna o conteúdo como uma string. Essa etapa é essencial para que o conteúdo do PDF possa ser processado posteriormente.

2. Geração de Resumo com Gemini
O Gemini, um modelo de linguagem generativa da Google, é utilizado para criar um resumo formal do conteúdo do PDF. A função perguntar_ao_gemini envia o texto extraído do PDF para a API do Gemini, junto com uma instrução específica para gerar um e-mail formal. O modelo processa o texto e retorna um resumo estruturado, que começa com "Prezado(a) Mauricio" e termina com "Atenciosamente: SESMT Digital".

3. Envio de E-mail com Anexo
O código utiliza a biblioteca smtplib para enviar o resumo gerado por e-mail. A função enviar_email configura o e-mail com um assunto, corpo e anexa o arquivo PDF original. O e-mail é enviado via servidor SMTP do Gmail, utilizando autenticação com uma senha de aplicativo.

4. Fluxo Principal
A função main orquestra todo o processo:

Define o caminho do PDF a ser lido.

Extrai o texto do PDF.

Envia o texto para o Gemini e recebe o resumo.

Envia o resumo por e-mail, com o PDF anexado.

Aplicações Práticas
Este código pode ser útil em diversas situações, como:

Automatização de relatórios: Resumir documentos longos e enviá-los para equipes ou gestores.

Comunicação formal: Gerar e-mails profissionais com base em conteúdos técnicos ou burocráticos.

Integração com IA: Utilizar modelos de linguagem para processar e resumir informações de forma eficiente.

Considerações de Segurança
Chaves de API e Senhas: As credenciais, como a chave da API do Gemini e a senha do Gmail, estão embutidas no código. Em um ambiente de produção, é recomendável armazenar essas informações em variáveis de ambiente ou usar um gerenciador de segredos.

Senhas de Aplicativo: O Gmail exige o uso de uma senha de aplicativo para autenticação em scripts, garantindo maior segurança.

Tecnologias Utilizadas
PyPDF2: Para leitura de PDFs.

Google Gemini API: Para geração de conteúdo com IA.

smtplib: Para envio de e-mails via SMTP.

MIME: Para formatar e anexar arquivos em e-mails.

Conclusão
Este código é uma solução eficiente para automatizar tarefas que envolvem leitura de documentos, processamento de texto e comunicação por e-mail. Ele demonstra como a integração de ferramentas modernas, como IA generativa, pode simplificar processos complexos e aumentar a produtividade.
