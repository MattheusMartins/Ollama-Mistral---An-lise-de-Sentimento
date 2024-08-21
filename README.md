# **Documentação do Script de Análise de Sentimento**

![Descrição da Imagem](https://github-production-user-asset-6210df.s3.amazonaws.com/3325447/271034511-d6be0694-eb35-417b-8f08-47d3b6c2a171.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240821%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240821T222506Z&X-Amz-Expires=300&X-Amz-Signature=0b73df8576c3d8798c775049dc32c0e9167ee2932ac17f369e4ce863fd99bb8b&X-Amz-SignedHeaders=host&actor_id=89713193&key_id=0&repo_id=658928958)


## **Descrição Geral**
Este script Python foi desenvolvido para realizar uma análise de sentimento em textos contidos em uma coluna específica de um arquivo Excel (`.xlsx`). O script utiliza o modelo de linguagem **Mistral** da **Ollama** para classificar os textos em "Positivo", "Neutro" ou "Negativo". O resultado da análise é salvo em uma nova coluna do mesmo arquivo, que é então exportado para um novo arquivo Excel.

## **Pré-requisitos**
- **Python 3.x**
- Bibliotecas Python:
  - `pandas` para manipulação de dados
  - `ollama` para interação com o modelo Mistral
- Um arquivo Excel (`.xlsx`) contendo uma coluna de texto chamada "Resumo" que será analisada.

## **Instalação das Dependências**
Certifique-se de que as seguintes bibliotecas estão instaladas:
```bash
pip install pandas ollama
```
```bash
ollama run mistral
```
## **Como o Script Funciona**

1. **Leitura do Arquivo Excel:**
   - O script começa lendo o arquivo Excel (`treino.xlsx`) e carregando os dados em um `DataFrame` do pandas.
   - As colunas disponíveis no `DataFrame` são exibidas para diagnóstico inicial.

2. **Normalização das Colunas:**
   - Os espaços em branco no início e no final dos nomes das colunas são removidos para evitar erros de referência.

3. **Verificação da Coluna 'Resumo':**
   - O script verifica se a coluna "Resumo" está presente no `DataFrame`. 
   - Se a coluna existir, o conteúdo é convertido para o tipo `str` para garantir compatibilidade com a análise de sentimento.

4. **Função de Análise de Sentimento:**
   - A função `analisar_sentimento(texto)` é definida para enviar cada texto da coluna "Resumo" ao modelo Mistral.
   - A função utiliza o método `ollama.generate` para gerar uma resposta do modelo, que classifica o sentimento do texto.
   - O modelo responde com um dos três possíveis resultados: "Positivo", "Neutro" ou "Negativo".

5. **Aplicação da Função de Sentimento:**
   - A função de análise de sentimento é aplicada a cada entrada na coluna "Resumo".
   - Os resultados são armazenados em uma nova coluna chamada "Sentimento" no `DataFrame`.

6. **Exportação dos Resultados:**
   - O `DataFrame` atualizado, incluindo a nova coluna "Sentimento", é salvo em um novo arquivo Excel (`treino_com_sentimentos.xlsx`).

7. **Tratamento de Erros:**
   - Se a coluna "Resumo" não for encontrada, o script exibe uma mensagem de erro solicitando a verificação do nome da coluna no arquivo Excel.

## **Saída**
- O script gera um novo arquivo Excel (`treino_com_sentimentos.xlsx`) contendo os dados originais e a coluna adicional "Sentimento", que indica o sentimento associado a cada texto na coluna "Resumo".

## **Notas Adicionais**
- Certifique-se de que o arquivo Excel (`treino.xlsx`) possui uma coluna "Resumo" antes de executar o script.
- O modelo Mistral da Ollama pode ter restrições quanto ao número de requisições por minuto, então o script pode levar tempo para processar grandes volumes de dados.

---

Essa documentação deve ajudar a entender e utilizar o script de forma eficaz. Se precisar de mais detalhes ou ajustes, estou à disposição!
