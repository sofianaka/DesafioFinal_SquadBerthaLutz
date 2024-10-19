# DesafioFinal_SquadBerthaLutz

**estrutura de arquivos:**
- `/base`: corresponde ao aplicativo que gerencia as publicações do blog
- `/base/templates/base/`: contém os templates referentes ao blog.
    - `base.html`: é o template base, estendido para `post_list.html`, lista das postagens que fica na raiz do site, e `post_detail.html`.
- `base/templates/registration`: template para a página de cadastro de usuários

**views implementadas:**
- `post_list`: implementada na raiz do site, lista todos os posts publicados, ou seja que a data de publicação não está vazia.
- `post_detail`: mostra os detalhes da publicação numa url separada (`/post/{id}`)

**views implementadas que requerem login**
> funções de gerenciamento e edição das postagens, implementadas no front-end.
- `post_new`: cria novas publicações 
- `post_edit`: edita publicações 
- `draft_post_list`: lista as postagens que não foram publicadas
- `post_publish`: botão para publicação das postagens
- `delete_post`: botão para deletar publicação

**login de usuários**
rotas: 
- `/accounts/login/`:
- `s`:

**Adições no front-end:**
- Adicionada barra de pesquisa
- Implementação de "dark mode"
- Design responsivo implementado
- Adicionado diretório de templates em settings.py

