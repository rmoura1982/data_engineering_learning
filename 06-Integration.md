# 6. Integration

Integração de dados é o processo de conectar diferentes fontes e sistemas, permitindo a ingestão e unificação dos dados, para que possam ser usados de forma centralizada e consistente.

---

- **6.1.** APIs 

APIs (Application Programming Interfaces) são interfaces que permitem a comunicação entre sistemas diferentes, facilitando a troca e o consumo de dados de forma padronizada e segura.

#### Objetivos

- Conectar sistemas e serviços de forma eficiente  
- Permitir acesso controlado a dados e funcionalidades  
- Facilitar automação e orquestração de processos  
- Suportar integração entre aplicações internas e externas

#### Práticas Comuns

- Uso de APIs RESTful para comunicação entre serviços  
- Autenticação e autorização via tokens (ex: OAuth, JWT)  
- Documentação clara e atualizada das APIs  
- Monitoramento e logging das chamadas de API  

---

- **6.2.** Connectors  

Conectores são componentes que permitem a comunicação e transferência de dados entre diferentes sistemas, bancos de dados ou serviços, facilitando a integração e automação de pipelines.

#### Objetivos

- Facilitar a integração entre diferentes sistemas e fontes de dados  
- Simplificar a extração e carregamento de dados de múltiplas plataformas  
- Garantir conexões seguras e estáveis entre ferramentas e serviços  
- Automatizar o fluxo de dados

#### Práticas Comuns

- Uso de conectores pré-construídos para bancos de dados, APIs e serviços na nuvem  
- Configuração de drivers e adaptadores para diferentes tecnologias (JDBC, ODBC)  
- Monitoramento contínuo das conexões para evitar falhas  
- Implementação de autenticação segura para acesso aos sistemas  

---

- **6.3.** Batch Ingestion & Streaming Ingestion

### Batch

A ingestão batch consiste na coleta e processamento de grandes volumes de dados em intervalos definidos, geralmente em horários agendados.

**✅ Prós:**

- Processamento eficiente de grandes volumes de dados  
- Simplicidade na implementação e manutenção  
- Menor custo computacional em comparação com streaming contínuo

**❌ Contras:**

- Latência alta — dados não disponíveis em tempo real  
- Menos adequado para cenários que demandam respostas imediatas  

---

### Streaming

A ingestão streaming é o processo de captura e processamento contínuo de dados em tempo real ou quase real.

**✅ Prós:**

- Baixa latência, dados quase em tempo real  
- Ideal para aplicações que exigem agilidade (monitoramento, alertas, etc.)  
- Permite análise contínua e imediata

**❌ Contras:**

- Maior complexidade de implementação  
- Maior custo computacional e recursos contínuos  
- Requer gestão cuidadosa da ordem e consistência dos dados

---

[🔗 Links - Integration](https://www.google.com/search?q=integra%C3%A7%C3%A3o+de+dados&sca_esv=449df59cb87f206b&biw=1280&bih=598&sxsrf=AE3TifMiaRuJvEK8sfpmBjirIp1u003w4A%3A1748530781796&ei=XXY4aOmQMNeh5NoPgbvKuAs&ved=0ahUKEwips4Lh-MiNAxXXEFkFHYGdErcQ4dUDCBA&uact=5&oq=integra%C3%A7%C3%A3o+de+dados&gs_lp=Egxnd3Mtd2l6LXNlcnAiFWludGVncmHDp8OjbyBkZSBkYWRvczIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBRAAGIAEMgQQABgeSKIWUABYgBNwAHgBkAEAmAFLoAGEBaoBAjEwuAEDyAEA-AEBmAIKoALOBcICCBAAGBMYBxgemAMAkgcCMTCgB71SsgcCMTC4B84FwgcFMi04LjLIB0Q&sclient=gws-wiz-serp)
