# AI Real Estate Pipeline (Arquitetura Enterprise)

> **[ 🇺🇸 Read in English ](README.md)**

## Sumário Executivo
O **AI Real Estate Pipeline** é um agente autônomo robusto de ponta a ponta projetado para revolucionar a análise e subscrição imobiliária (property underwriting). Orquestrando um fluxo contínuo desde a ingestão de dados brutos até a visualização geoespacial avançada, o sistema vai além da análise simples. A solução utiliza **GPT-4** para avaliação sofisticada de riscos, **Geopy** para inteligência de localização precisa e **Monday.com Enterprise** para visualização de alta fidelidade, eliminando trabalho manual e fornecendo inteligência instantânea e acionável para investimentos imobiliários de alto volume.

## Principais Recursos

### 1. Geocodificação Automatizada & Inteligência de Localização
*   **Mapeamento de Precisão**: Utiliza `geopy` para converter automaticamente endereços em coordenadas precisas de Latitude/Longitude.
*   **Enriquecimento Geoespacial**: Permite que sistemas a montante plotem propriedades com precisão em camadas de mapa, essencial para análise de vizinhança e planejamento logístico.

### 2. Modelagem Financeira Avançada
*   **Lógica de Investimento**: Calcula automaticamente métricas financeiras críticas, incluindo **ARV (After Repair Value / Valor Pós-Reforma)** e **Custos Estimados de Reforma** com base nas características do imóvel e relatórios de vistoria.
*   **Suporte à Tomada de Decisão**: Sintetiza dados financeiros com análises qualitativas geradas por IA para emitir recomendações definitivas de "Comprar" ou "Passar".

### 3. Visualização Enterprise
*   **Integração com Monday.com**: Envia dados estruturados para um Quadro Enterprise no Monday.com.
*   **Visualização em Mapa**: Aproveita as coordenadas geocodificadas para preencher as **Visualizações de Mapa** interativas do Monday.com, permitindo que os stakeholders visualizem a distribuição do portfólio e agrupamentos geográficos instantaneamente.

## Tecnologias Utilizadas (Tech Stack)
*   **Core**: Python 3.12
*   **IA/LLM**: OpenAI GPT-4 (via LangChain)
*   **Geoespacial**: `geopy` (Nominatim)
*   **Integração**: Monday.com API v2 (GraphQL)
*   **Arquitetura**: Enterprise Board Architecture
*   **Validação**: Pydantic Strict Schemas

## Instalação

1.  **Clonar o Repositório**
    ```bash
    git clone https://github.com/jraphaelbarbosa/AI_Real_Estate_Pipeline.git
    cd AI_Real_Estate_Pipeline
    ```

2.  **Configurar o Ambiente Virtual**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Instalar Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Variáveis**
    Crie um arquivo `.env` na raiz do projeto:
    ```env
    OPENAI_API_KEY=sua_chave_openai
    MONDAY_API_KEY=sua_chave_monday
    ```

## Como Executar

Execute o pipeline completo de dados:

```bash
python -m src.main
```

**Fluxo de Trabalho:**
1.  **Ingestão**: Carrega dados brutos das propriedades.
2.  **Enriquecimento**: Geocodifica endereços para (Lat, Lon).
3.  **Análise**: A IA avalia a condição do imóvel e os dados financeiros.
4.  **Implantação**: Sincroniza os resultados no Dashboard e Mapa interativo do Monday.com.
