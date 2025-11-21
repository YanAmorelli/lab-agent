import logging
import time
from typing import Optional
from gitingest import ingest_async

logger = logging.getLogger(__name__)

async def read_context(token: str, repo_url: Optional[str], branch: Optional[str]) -> str:
    """Lê um repositório git e retorna um resumo, árvore de arquivos e conteúdo.

    Essa função usa a função `ingest` do pacote `gitingest` para ler um repositório git e retornar um resumo, árvore de arquivos e conteúdo.
    Para isso recebe os seguintes parâmetros:
    Args:
        token (str): Token de acesso ao repositório.
        repo_url (str): URL do repositório git.
        branch (str): Nome do branch a ser lido.
    Returns:
        tuple[str, str, str]: Resumo, árvore de arquivos e conteúdo do reposit    
            Uma tupla contendo:
            - A summary string of the analyzed repository or directory.
            - A tree-like string representation of the file structure.
            - The content of the files in the repository or directory.
    """
    source_repo_url = repo_url
    if branch: 
        source_repo_url = f"{repo_url}/tree/{branch}" 
        
    summary, tree, content = await ingest_async(source=source_repo_url, token=token, branch=branch)
    context = f"Repository summary:\n{summary}\n\nFile tree:\n{tree}\n\nContent:\n{content}"
    return context