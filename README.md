# Anima AI

Animações virais a partir de uma ideia (spec 44, parte 5.1, ecossistema Rangel Tech): a pessoa escreve uma frase e recebe a animação pronta para Reels, TikTok e Shorts, com roteiro do diretor (GPT), cenas nos 10 estilos, narração, legenda e o @ dela.

- `app/`: FastAPI (login com senha ou código no e-mail, fila, webhook da Cakto) e o pipeline de animação (`animacao.py`, `ganchos.py`).
- `app/rt_midia.py`: regra de imagem comum a todos os produtos (GPT de imagem; recusa ou NSFW vai ao Runware pelo Estúdio do llm-access).
- Nasceu do Cortaí (os cortes ficam lá); o código de cortes ainda existe aqui mas a API só aceita `tipo=animacao`.
- Deploy só pelo `vps_rt_infra` (stack `animaai`, domínio `anima-ai.rangeltech.net`).

Testes: `python -m pytest -q`.
