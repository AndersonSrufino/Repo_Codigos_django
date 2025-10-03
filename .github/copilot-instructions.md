# Orientações para o Agente de IA - Projeto MedicSearch

Este documento fornece orientações para trabalhar no projeto Django `MedicSearch`.

## Arquitetura do Projeto

O projeto segue uma estrutura Django padrão com algumas especificidades:

-   **`medicSearchAdmin`**: Este é o diretório principal do projeto Django. Ele contém as configurações globais (`settings/`), URLs (`urls.py`) e o ponto de entrada WSGI.
-   **`medicSearch`**: Este é o principal aplicativo Django do projeto. Ele contém a lógica de negócios, modelos, views e templates.
-   **Modelos em um subdiretório**: Os modelos não estão em um único arquivo `models.py`. Em vez disso, eles estão organizados em arquivos individuais dentro do diretório `medicSearch/models/`. Cada arquivo representa um modelo (por exemplo, `perfil.py`, `endereco.py`). O arquivo `medicSearch/models/__init__.py` importa todos eles para que o Django possa descobri-los.
-   **Configurações por Ambiente**: As configurações são divididas por ambiente (desenvolvimento, produção, teste) e estão localizadas em `medicSearchAdmin/settings/`. O arquivo `settings.py` base contém as configurações comuns, enquanto os arquivos como `development.py` especificam as configurações do ambiente.

## Fluxos de Trabalho do Desenvolvedor

Os comandos essenciais para desenvolvimento estão documentados em `comandos.txt`.

-   **Executando o servidor de desenvolvimento**:
    Use o seguinte comando para especificar o ambiente de desenvolvimento. Isso é crucial porque o projeto está configurado para usar diferentes bancos de dados e configurações por ambiente.

    ```bash
    python manage.py runserver --settings=medicSearchAdmin.settings.development
    ```

-   **Aplicando Migrações**:
    Ao aplicar migrações, certifique-se de especificar o ambiente correto, pois isso pode afetar o banco de dados de destino.

    ```bash
    python manage.py migrate --settings=medicSearchAdmin.settings.testing
    ```

-   **Definindo o Módulo de Configurações (Alternativa)**:
    Você pode definir a variável de ambiente `DJANGO_SETTINGS_MODULE` para evitar ter que passar o parâmetro `--settings` a cada comando.

    ```powershell
    $env:DJANGO_SETTINGS_MODULE = "medicSearchAdmin.settings.production"
    ```

## Padrões e Convenções Específicas

-   **Upload de Imagens**: O modelo `Perfil` (`medicSearch/models/perfil.py`) usa um `ImageField` para uploads de imagens.
    -   As imagens são salvas no diretório definido por `MEDIA_ROOT` (geralmente `medicSearchAdmin/media/`).
    -   O subdiretório é especificado pelo parâmetro `upload_to` no campo do modelo (ex: `upload_to='perfil'`).
    -   Para que as imagens funcionem no desenvolvimento, o arquivo `medicSearchAdmin/urls.py` deve servir os arquivos de mídia estaticamente.

-   **Registro no Admin**: Os modelos são registrados para a interface de administração do Django no arquivo `medicSearch/admin.py`. Ao criar classes `ModelAdmin` personalizadas (como `ProfileAdmin`), certifique-se de registrar o modelo usando essa classe e evite registros duplicados do mesmo modelo.

    ```python
    # Exemplo em medicSearch/admin.py
    from django.contrib import admin
    from .models import Perfil

    class ProfileAdmin(admin.ModelAdmin):
        date_hierarchy = 'created_at'
        # ... outras customizações

    admin.site.register(Perfil, ProfileAdmin)
    ```
