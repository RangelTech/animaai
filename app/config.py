"""Configuração por variável de ambiente (segredos em /opt/platform/secrets/animaai.env na VPS)."""
from __future__ import annotations

import os
import json
from dataclasses import dataclass, field


@dataclass
class Config:
    dados: str = "/data"
    base_url: str = "https://anima-ai.rangeltech.net"
    llm_base: str = "https://qwen.rangeltech.net/v1"
    llm_key: str = ""
    llm_modelo: str = "qwen-abliterated"
    llm_planejador: str = "rt-planejar"   # escolhe os trechos (Claude/ChatGPT), com llm_modelo de reserva
    llm_visao: str = "visao"              # valida olhando os quadros (ChatGPT)
    validar: bool = True
    segredo_sessao: str = "dev"
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_senha: str = ""
    smtp_from: str = "Anima AI <contato@rangeltech.net>"
    cakto_segredo: str = ""
    checkout_mensal: str = ""
    trabalhos_teste: int = 0          # sem plano grátis (decisão do Lucas, 14/11)
    trabalhos_mes: int = 60           # limite do plano mensal
    max_duracao_s: int = 6 * 3600     # vídeo de entrada: lives de até 6 h
    max_cortes: int = 5
    workers: int = 1
    guardar_dias: int = 7
    proxy: str = ""                    # proxy para o yt-dlp (opcional)
    yt_cookies: str = "/data/yt_cookies.txt"  # cookies de uma conta do YouTube (o IP de datacenter cai no "não sou robô" sem eles)
    dev: bool = False
    checkouts: dict = field(default_factory=dict)          # {"start": url, "pro": url, "turbo": url}
    planos_por_produto: dict = field(default_factory=dict)  # {"<id do produto Cakto>": plano}
    lancamento_ate: str = "2026-11-30"
    admin_key: str = ""
    demo_email: str = ""
    demo_senha: str = ""


def carregar() -> Config:
    e = os.environ.get
    return Config(
        dados=e("ANIMAAI_DADOS", "/data"),
        base_url=e("ANIMAAI_BASE_URL", "https://anima-ai.rangeltech.net").rstrip("/"),
        llm_base=e("ANIMAAI_LLM_BASE", "https://qwen.rangeltech.net/v1").rstrip("/"),
        llm_key=e("ANIMAAI_LLM_KEY", ""),
        llm_modelo=e("ANIMAAI_LLM_MODELO", "qwen-abliterated"),
        llm_planejador=e("ANIMAAI_LLM_PLANEJADOR", "rt-planejar"),
        llm_visao=e("ANIMAAI_LLM_VISAO", "visao"),
        validar=e("ANIMAAI_VALIDAR", "1") == "1",
        segredo_sessao=e("ANIMAAI_SEGREDO_SESSAO", "dev"),
        smtp_host=e("SMTP_HOST", ""),
        smtp_port=int(e("SMTP_PORT", "587") or 587),
        smtp_user=e("SMTP_USER", ""),
        smtp_senha=e("SMTP_PASSWORD", ""),
        smtp_from=e("ANIMAAI_SMTP_FROM", "Anima AI <contato@rangeltech.net>"),
        cakto_segredo=e("ANIMAAI_CAKTO_SEGREDO", ""),
        checkout_mensal=e("ANIMAAI_CHECKOUT_MENSAL", ""),
        trabalhos_teste=int(e("ANIMAAI_TRABALHOS_TESTE", "0")),
        trabalhos_mes=int(e("ANIMAAI_TRABALHOS_MES", "60")),
        max_duracao_s=int(e("ANIMAAI_MAX_DURACAO_S", str(6 * 3600))),
        max_cortes=int(e("ANIMAAI_MAX_CORTES", "5")),
        workers=int(e("ANIMAAI_WORKERS", "1")),
        guardar_dias=int(e("ANIMAAI_GUARDAR_DIAS", "7")),
        proxy=e("ANIMAAI_PROXY", ""),
        yt_cookies=e("ANIMAAI_YT_COOKIES", "/data/yt_cookies.txt"),
        dev=e("ANIMAAI_DEV", "") == "1",
        checkouts=json.loads(e("ANIMAAI_CHECKOUTS", "") or "{}"),
        planos_por_produto=json.loads(e("ANIMAAI_PLANOS_CAKTO", "") or "{}"),
        lancamento_ate=e("ANIMAAI_LANCAMENTO_ATE", "2026-11-30"),
        admin_key=e("ANIMAAI_ADMIN_KEY", ""),
        demo_email=e("ANIMAAI_DEMO_EMAIL", ""),
        demo_senha=e("ANIMAAI_DEMO_SENHA", ""),
    )
