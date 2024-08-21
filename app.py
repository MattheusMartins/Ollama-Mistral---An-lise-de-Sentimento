import pandas as pd
import ollama

# Ler o arquivo XLSX e verificar as colunas
arquivo = 'treino.xlsx'
df = pd.read_excel(arquivo)

# Exibir as colunas disponíveis para diagnóstico
print("Colunas disponíveis no DataFrame:", df.columns)

# Remover espaços no início e fim dos nomes das colunas para evitar erros
df.columns = df.columns.str.strip()

# Verifique se a coluna 'Resumo' está presente no DataFrame
if 'Resumo' in df.columns:
    # Garantir que a coluna 'Resumo' esteja no formato de texto
    df['Resumo'] = df['Resumo'].astype(str)
    
    # Função para analisar o sentimento usando o modelo Mistral do Ollama
    def analisar_sentimento(texto):
        # Enviar o texto para análise e retornar somente o sentimento ('Positivo', 'Neutro' ou 'Negativo')
        response = ollama.generate(model="mistral", prompt=f"Classifique o sentimento deste texto APENAS como 'Positivo', 'Neutro' ou 'Negativo'. Responda somente com uma dessas palavras, sem nenhuma explicação adicional: '{texto}'")
        sentiment = response["response"]  # Acessar diretamente a resposta do modelo
        return sentiment

    # Criar uma nova coluna no DataFrame para armazenar os sentimentos analisados
    df['Sentimento'] = df['Resumo'].apply(analisar_sentimento)

    # Exibir o DataFrame atualizado com a coluna de sentimentos
    print(df)

    # Salvar o DataFrame atualizado em um novo arquivo XLSX
    df.to_excel('treino_com_sentimentos.xlsx', index=False)
else:
    # Exibir uma mensagem de erro se a coluna 'Resumo' não for encontrada
    print("A coluna 'Resumo' não foi encontrada no arquivo. Verifique o nome da coluna no arquivo XLSX.")