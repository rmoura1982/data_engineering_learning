# 12. Databricks

Plataforma unificada que reúne em um só lugar tudo o que é necessário para trabalhar com análise de dados, combinando engenharia de dados, ciência de dados e machine learning. Utiliza o Apache Spark para processar grandes volumes de dados de forma distribuída. Possui suporte a notebooks, facilitando a colaboração e a organização do trabalho. Também conta com integração ao Delta Lake, que cuida do armazenamento dos dados de forma organizada, confiável e com controle de versões.

---

- **12.1. Apache Spark**

O Apache Spark é um motor de processamento que permite analisar grandes volumes de dados de forma distribuída. Ele divide o trabalho entre vários computadores ao mesmo tempo, tornando o processamento mais rápido e eficiente. O Spark suporta diversas linguagens, como Python e SQL, para que possa transformar e analisar os dados facilmente.

- **12.2. Delta Lake**

O Delta Lake é uma camada de armazenamento que pode ser usada para salvar os dados processados com Spark. Ele armazena os dados fisicamente em arquivos `.parquet` dentro do data lake e mantém um histórico das mudanças, permitindo versionamento e atualizações eficientes. O Delta Lake oferece controle, confiabilidade e facilita operações como atualização, exclusão e recuperação de versões anteriores dos dados.

![Databricks](image/databricks.png)

**✅ Prós:**
- Escalável para Big Data e processamento em lote ou streaming.
- Suporte a notebooks colaborativos (Python, SQL, etc.).
- Time travel e controle transacional com Delta Lake.

**❌ Contras:**
- Custo mais alto em uso contínuo.
- Requer conhecimento técnico (Spark, PySpark).
- Exige configuração de clusters.

---

- **12.2.** Governança com Unity Catalog

O Unity Catalog é responsável pela governança dos dados, organizando e controlando os metadados — que são informações sobre os dados, como nome, formato, localização e permissões — definindo quem pode acessar e manipular tabelas, views e funções, garantindo segurança e controle centralizado.

Os dados em si são sempre armazenados fisicamente em um data lake.

# Prós e Contras

**✅ Prós:**  
- Plataforma unificada.  
- Processamento distribuído rápido com Apache Spark.  
- Governança centralizada e controle de acesso com Unity Catalog.

**❌ Contras:**  
- Curva de aprendizado para dominar todas as funcionalidades.  
- Dependência de configuração correta do ambiente e metastore.  
- Custo pode ser elevado para grandes clusters e volumes.


---

[🔗 Link – Databricks](https://www.databricks.com/product/databricks-platform)

---





---



