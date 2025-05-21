# 💬 RAG-LGPD-Chatbot

Um sistema modularizado de Pergunta-Resposta sobre a LGPD utilizando LangChain, ChromaDB, OpenAI e Gradio.  
Ideal para aplicações em atendimento jurídico automatizado, análise de compliance e suporte baseado em documentos.

---

## 📌 Visão Geral

Este projeto implementa um pipeline completo de RAG (*Retrieval-Augmented Generation*) com as seguintes etapas:

1. **Ingestão de PDFs** contendo conteúdos jurídicos (ex: LGPD)
2. **Divisão dos documentos em chunks** para granularidade semântica
3. **Geração de embeddings** com modelo da OpenAI
4. **Armazenamento vetorial** persistente via ChromaDB
5. **Criação de uma chain conversacional** com memória usando LangChain
6. **Interface de Chat com Gradio** para perguntas em linguagem natural

---

## 🧱 Estrutura do Projeto

```
.
├── main.py                    # Script principal
├── data/                     # Pasta com documentos PDF (LGPD, etc.)
├── .env                      # Chave da API OpenAI
├── src/
│   ├── config.py             # Parâmetros e variáveis de ambiente
│   ├── utils.py              # Funções auxiliares (hash, etc.)
│   ├── loader.py             # Carregamento de documentos PDF
│   ├── splitter.py           # Divisão em chunks
│   ├── embedding.py          # Embeddings via OpenAI
│   ├── vectorstore.py        # Armazenamento no Chroma
│   ├── retriever.py          # Configuração do retriever
│   └── langchain_layer.py    # Construção da chain conversacional
```

---

## 🚀 Como Executar

1. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

2. **Crie o arquivo `.env`:**

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. **Adicione arquivos PDF à pasta `data/`**

4. **Execute o projeto:**

```bash
python main.py
```

5. **Acesse a interface interativa do chat via navegador.**

---

## 🧠 Tecnologias Utilizadas

- [LangChain](https://python.langchain.com/)
- [OpenAI Embeddings](https://platform.openai.com/)
- [Chroma Vector DB](https://www.trychroma.com/)
- [Gradio](https://www.gradio.app/)
- [Python 3.10+](https://www.python.org/)

---

## ✅ Funcionalidades Finais

- Suporte a múltiplos documentos PDF
- Histórico de conversa preservado com memória
- Pipeline desacoplado e testável
- Pode ser expandido para múltiplas leis ou domínios (ex: compliance, RH, medicina)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuição

Pull requests são bem-vindos. Para sugestões, dúvidas ou bugs, abra uma issue.

---

## Autor

Desenvolvido por **André Rizzo** — [LinkedIn](https://www.linkedin.com/in/andrerizzo1)
