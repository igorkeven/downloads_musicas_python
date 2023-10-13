# Automação de Downloads de Músicas

Este é um script Python que automatiza o processo de download de músicas a partir de páginas web usando o Selenium, um framework para automação de navegação na web. O script foi projetado para funcionar com a plataforma "musio.net.br", mas pode ser adaptado para outras páginas da web, ajustando-se os seletores de elementos apropriados.

## Requisitos

- Python 3.x
- Selenium (você pode instalá-lo usando `pip install selenium`)
- Microsoft Edge (caso você deseje usar outro navegador, precisa adaptar o código para aquele navegador específico)
- Conexão à internet

## Configuração Inicial

O script começa importando as bibliotecas necessárias, definindo um mapeamento de gêneros musicais para suas respectivas páginas de download e configurando a pasta padrão de downloads. Certifique-se de ajustar a lista `generos_paginas` com as páginas específicas de onde deseja baixar músicas para cada gênero.

## Automatizando o Download

O script então inicia um navegador Edge, percorre a lista de gêneros e suas respectivas páginas e procura por botões de download nas páginas. O código usa Selenium para interagir com a página web, localizando os botões de download por seu título, clicando neles e aguardando um tempo entre os downloads.

## Organização dos Arquivos

Após o download, o script move os arquivos para pastas de destino correspondentes aos gêneros musicais. Certifique-se de ajustar a variável `pasta_destino` para o local desejado no seu sistema. O código também verifica se os arquivos já existem na pasta de destino e, se existirem, remove os duplicados.

## Finalização

O navegador é encerrado após o processamento de todas as páginas, e quaisquer erros são capturados e exibidos no terminal.

## Uso

1. Certifique-se de ter o Python 3.x instalado em seu sistema.

2. Instale a biblioteca Selenium, se ainda não estiver instalada, usando `pip install selenium`.

3. Configure o mapeamento de gêneros musicais e suas páginas na variável `generos_paginas`.

4. Execute o script.

```python
python nome_do_script.py
```

O script navegará pelas páginas configuradas, baixará as músicas e as organizará nas pastas de destino correspondentes. Certifique-se de ter uma conexão à internet durante a execução.

**Observação:** Este script é específico para a plataforma "musio.net.br" e pode não funcionar em outras páginas sem modificações substanciais. Certifique-se de observar as políticas de uso e direitos autorais ao baixar músicas da internet.
