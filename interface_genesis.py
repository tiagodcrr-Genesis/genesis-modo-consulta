# -*- coding: utf-8 -*-
"""
interface_genesis.py — Gênesis | Interface Web v1
Modo Consultoria com design moderno
Rodar: streamlit run interface_genesis.py
"""

import streamlit as st
import json, shutil, sys
from pathlib import Path
from datetime import datetime, date

# ── Configuração da página ────────────────────────────────────────────────────
st.set_page_config(
    page_title="GENESIS | Consultoria Juridica",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS customizado — Dark Mode Moderno ───────────────────────────────────────
st.markdown("""
<style>
/* ── VARIÁVEIS ── */
:root {
    --bg:       #080E1A;
    --surface:  #0F1829;
    --card:     #141F35;
    --elevated: #1A2744;
    --border:   #1E3354;
    --blue:     #3A82FF;
    --cyan:     #22D3EE;
    --green:    #34D399;
    --amber:    #FBBF24;
    --red:      #F87171;
    --text:     #F1F5F9;
    --text2:    #8895A7;
    --text3:    #3D4F6B;
}

/* ── GLOBAL ── */
.stApp, .stApp * { font-family: 'Inter','Segoe UI',sans-serif; }
.stApp { background: var(--bg); color: var(--text); }
.block-container {
    background: var(--surface);
    border-radius: 20px;
    padding: 2rem 2.5rem !important;
    margin-top: 0.5rem;
    border: 1px solid var(--border);
    box-shadow: 0 0 60px rgba(58,130,255,0.06);
}

/* ── HEADER ── */
.genesis-header {
    background: linear-gradient(135deg, #0F2350 0%, #1A3A7A 50%, #0E2060 100%);
    border: 1px solid #1E3A7A;
    border-radius: 20px; padding: 40px;
    margin-bottom: 28px; text-align: center;
    box-shadow: 0 8px 48px rgba(58,130,255,0.25);
    position: relative; overflow: hidden;
}
.genesis-header::before {
    content: ''; position: absolute; top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle at 30% 40%, rgba(58,130,255,0.15) 0%, transparent 60%),
                radial-gradient(circle at 70% 60%, rgba(34,211,238,0.1) 0%, transparent 50%);
    pointer-events: none;
}

/* ── SECTION TITLE ── */
.section-title {
    font-size: 0.67rem; font-weight: 800; letter-spacing: 4px;
    text-transform: uppercase; color: var(--blue);
    margin-bottom: 16px; padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}

/* ── TEMA BADGE ── */
.tema-badge {
    background: var(--card); border: 1px solid var(--blue);
    border-radius: 10px; padding: 12px 20px;
    font-size: 0.95rem; font-weight: 600; color: #93C5FD; margin: 12px 0;
}

/* ── BOTÕES ── */
.stButton > button {
    background: linear-gradient(135deg,#1D4ED8,#3A82FF) !important;
    color: #FFF !important; border: none !important;
    border-radius: 10px !important; padding: 12px 28px !important;
    font-size: 0.95rem !important; font-weight: 700 !important;
    width: 100% !important; transition: all 0.2s !important;
    box-shadow: 0 4px 20px rgba(58,130,255,0.4) !important;
    letter-spacing: 0.3px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg,#1E40AF,#2563EB) !important;
    box-shadow: 0 8px 28px rgba(58,130,255,0.55) !important;
    transform: translateY(-2px) !important;
}

/* ── INPUTS ── */
.stTextInput input, .stTextArea textarea {
    background: var(--card) !important; border: 1px solid var(--border) !important;
    color: var(--text) !important; border-radius: 8px !important; font-size: 0.9rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--blue) !important;
    box-shadow: 0 0 0 3px rgba(58,130,255,0.2) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder { color: var(--text3) !important; }

/* ── SELECTBOX ── */
.stSelectbox > div > div {
    background: var(--card) !important; border: 1px solid var(--border) !important;
    color: var(--text) !important; border-radius: 8px !important;
}

/* ── LABELS ── */
label { color: var(--text2) !important; font-size: 0.82rem !important; font-weight: 500 !important; }

/* ── CHECKBOX ── */
.stCheckbox label,
.stCheckbox label p,
.stCheckbox span,
[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] span {
    color: #FFFFFF !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    opacity: 1 !important;
}
.stCheckbox input[type="checkbox"] { accent-color: var(--blue); }

/* ── PROGRESS BAR ── */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--blue), var(--cyan)) !important;
    border-radius: 99px !important;
}
.stProgress > div { background: var(--card) !important; border-radius: 99px !important; }

/* ── ALERTS ── */
.stSuccess { background:#022C22 !important; color:var(--green) !important; border-radius:8px !important; border:1px solid #065F46 !important; }
.stError   { background:#1A0A0A !important; color:var(--red) !important;   border-radius:8px !important; border:1px solid #7F1D1D !important; }
.stWarning { background:#1A1200 !important; color:var(--amber) !important; border-radius:8px !important; border:1px solid #78350F !important; }

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; margin: 20px 0 !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] { background: var(--bg) !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--elevated); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--blue); }
</style>
""", unsafe_allow_html=True)

# ── Autenticação (acesso restrito) ────────────────────────────────────────────
def _verificar_login():
    if st.session_state.get("autenticado"):
        return True

    st.markdown("<div style='max-width:380px;margin:100px auto 0;text-align:center'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:3rem;font-weight:900;letter-spacing:2px;margin:0'>⚖️ GÊNESIS</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8895A7;margin-bottom:24px'>Acesso restrito — Consultoria Jurídica</p>", unsafe_allow_html=True)

    with st.form("login_form"):
        senha = st.text_input("Senha de acesso", type="password")
        entrar = st.form_submit_button("Entrar", use_container_width=True)

    if entrar:
        senha_correta = st.secrets.get("app_password", "genesis2026")
        if senha == senha_correta:
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta.")

    st.markdown("</div>", unsafe_allow_html=True)
    return False

if not _verificar_login():
    st.stop()

# ── Carrega dados ─────────────────────────────────────────────────────────────
PASTA = Path(__file__).parent
TEMAS_JSON = PASTA / "consulta_temas_v2.json"
CLIENTES_DIR = PASTA / "clientes"
CLIENTES_DIR.mkdir(exist_ok=True)

def carregar_temas():
    with open(TEMAS_JSON, encoding="utf-8") as f:
        return json.load(f)["temas"]

def _normalizar(texto):
    """Remove acentos para comparacao robusta."""
    import unicodedata
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

def detectar_tema(descricao, temas):
    desc_norm = _normalizar(descricao)
    melhor, melhor_pts = None, 0
    for t in temas:
        pts = sum(1 for kw in t["keywords"] if _normalizar(kw) in desc_norm)
        if pts > melhor_pts:
            melhor_pts, melhor = pts, t
    return melhor if melhor_pts >= 1 else None

def calcular_situacao_caso(provas_tem):
    """Retorna a situação do caso baseada nos 3 status das provas."""
    nao_tem = sum(1 for v in provas_tem.values() if "Não tenho" in str(v) or "Não sei" in str(v))
    buscar  = sum(1 for v in provas_tem.values() if "Vou buscar" in str(v))
    if nao_tem == 0 and buscar == 0:
        return "CASO BEM DOCUMENTADO", "#34D399", "#022C22"
    elif nao_tem == 0:
        return "AGUARDANDO DOCUMENTOS", "#FCD34D", "#1C1007"
    else:
        return "PROVAS INCOMPLETAS", "#F87171", "#1F0A0A"

# ── Header ────────────────────────────────────────────────────────────────────
_nome = "G" + chr(202) + "NESIS"
st.markdown(f"""
<div class="genesis-header">
    <p style="font-size:4rem;font-weight:900;letter-spacing:2px;color:#FFFFFF;margin:0;text-align:center;text-shadow:0 2px 20px rgba(0,0,0,0.3)">{_nome}</p>
    <p style="font-size:0.95rem;letter-spacing:2px;color:rgba(255,255,255,0.6);margin:6px 0 0 0;text-align:center;font-weight:300">
        Consultoria Jur&iacute;dica Inteligente
    </p>
</div>
""", unsafe_allow_html=True)

# ── Progress steps ────────────────────────────────────────────────────────────
temas = carregar_temas()

if "step" not in st.session_state:
    st.session_state.step = 0          # 0 = tela inicial de seleção
if "dados" not in st.session_state:
    st.session_state.dados = {}

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 0 — TELA INICIAL: NOVO CLIENTE ou CLIENTE EXISTENTE
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.step == 0:
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 1. HEADLINE ───────────────────────────────────────────────────────────
    st.markdown("""
<div style="text-align:center;max-width:850px;margin:0 auto 0 auto;padding:0 0 24px 0">
  <p style="font-size:2rem;font-weight:900;color:#F8FAFC;line-height:1.3;margin:0">
    Transforme cada consulta em uma<br>oportunidade real de contratação.
  </p>
</div>
""", unsafe_allow_html=True)

    # ── 2. BLOCO DE DOR ───────────────────────────────────────────────────────
    st.markdown("""
<div style="text-align:center;max-width:850px;margin:0 auto 32px auto">
  <p style="font-size:1.05rem;color:rgba(255,255,255,0.88);line-height:1.75;margin:0 0 12px 0">
    Já terminou uma consulta e depois percebeu que esqueceu perguntas importantes,
    provas relevantes ou documentos essenciais para o caso?
  </p>
  <p style="font-size:1.05rem;color:#00D4FF;font-weight:600;margin:0">
    O Gênesis foi criado para evitar exatamente isso.
  </p>
</div>
""", unsafe_allow_html=True)

    # ── 3. LISTA DE BENEFÍCIOS ────────────────────────────────────────────────
    st.markdown("""
<div style="max-width:900px;margin:0 auto 36px auto;text-align:center">
  <div style="display:inline-flex;flex-direction:column;align-items:flex-start;gap:10px">
    <div style="color:#F8FAFC;font-size:0.95rem;line-height:1.5">
      <span style="color:#00D4FF;font-weight:700;margin-right:10px">&#10003;</span>Descubra informações relevantes durante a consulta
    </div>
    <div style="color:#F8FAFC;font-size:0.95rem;line-height:1.5">
      <span style="color:#00D4FF;font-weight:700;margin-right:10px">&#10003;</span>Saiba exatamente quais provas solicitar
    </div>
    <div style="color:#F8FAFC;font-size:0.95rem;line-height:1.5">
      <span style="color:#00D4FF;font-weight:700;margin-right:10px">&#10003;</span>Conduza casos inéditos com mais segurança
    </div>
    <div style="color:#F8FAFC;font-size:0.95rem;line-height:1.5">
      <span style="color:#00D4FF;font-weight:700;margin-right:10px">&#10003;</span>Reduza retrabalho e contatos posteriores
    </div>
    <div style="color:#F8FAFC;font-size:0.95rem;line-height:1.5">
      <span style="color:#00D4FF;font-weight:700;margin-right:10px">&#10003;</span>Aumente a confiança do cliente desde o primeiro atendimento
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── 4. BLOCO DE IMPACTO ───────────────────────────────────────────────────
    st.markdown("""
<div style="max-width:900px;margin:0 auto 40px auto;
            background:#0E1E36;border:1px solid #00D4FF;
            border-radius:16px;padding:28px 36px;text-align:center">
  <p style="color:#F8FAFC;font-size:1.05rem;font-weight:600;margin:0 0 6px 0">
    Ao final da consulta, o cliente sai com clareza.
  </p>
  <p style="color:#F8FAFC;font-size:1.05rem;font-weight:600;margin:0 0 16px 0">
    O advogado sai com o caso estruturado.
  </p>
  <p style="color:#00D4FF;font-size:0.9rem;font-style:italic;margin:0">
    Porque grandes causas começam com grandes atendimentos.
  </p>
</div>
""", unsafe_allow_html=True)

    # ── 5. O QUE VOCÊ RECEBE ──────────────────────────────────────────────────
    st.markdown("""
<div style="max-width:900px;margin:0 auto 32px auto;text-align:center">
  <p style="color:#F8FAFC;font-weight:700;font-size:1rem;margin:0 0 16px 0">
    O que você recebe ao final da consulta?
  </p>
  <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px">
    <span style="background:#101D33;border:1px solid rgba(0,212,255,0.35);
                 border-radius:8px;padding:8px 16px;color:#B7C3D0;font-size:0.82rem">
      &#10003; Guia probatório personalizado
    </span>
    <span style="background:#101D33;border:1px solid rgba(0,212,255,0.35);
                 border-radius:8px;padding:8px 16px;color:#B7C3D0;font-size:0.82rem">
      &#10003; Linha do tempo do caso
    </span>
    <span style="background:#101D33;border:1px solid rgba(0,212,255,0.35);
                 border-radius:8px;padding:8px 16px;color:#B7C3D0;font-size:0.82rem">
      &#10003; Contrato e procuração
    </span>
    <span style="background:#101D33;border:1px solid rgba(0,212,255,0.35);
                 border-radius:8px;padding:8px 16px;color:#B7C3D0;font-size:0.82rem">
      &#10003; Orientações ao cliente
    </span>
    <span style="background:#101D33;border:1px solid rgba(0,212,255,0.35);
                 border-radius:8px;padding:8px 16px;color:#B7C3D0;font-size:0.82rem">
      &#10003; Pasta organizada do atendimento
    </span>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── 6. TRÊS CARDS ─────────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
<div style="background:#101D33;border:1px solid rgba(0,212,255,0.25);border-top:3px solid #123D8D;
            border-radius:12px;padding:24px 20px;text-align:center;height:100%">
  <div style="font-size:1.4rem;margin-bottom:12px">💬</div>
  <div style="color:#00D4FF;font-weight:700;font-size:0.9rem;margin-bottom:10px">
    Perguntas Inteligentes
  </div>
  <div style="color:#B7C3D0;font-size:0.82rem;line-height:1.6">
    Conduza o atendimento com mais segurança e descubra informações que normalmente
    surgiriam apenas depois da consulta.
  </div>
</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div style="background:#101D33;border:1px solid rgba(0,212,255,0.25);border-top:3px solid #00D4FF;
            border-radius:12px;padding:24px 20px;text-align:center;height:100%">
  <div style="font-size:1.4rem;margin-bottom:12px">&#128269;</div>
  <div style="color:#00D4FF;font-weight:700;font-size:0.9rem;margin-bottom:10px">
    Guia Probatório
  </div>
  <div style="color:#B7C3D0;font-size:0.82rem;line-height:1.6">
    Saiba exatamente quais provas e documentos solicitar
    para cada tipo de caso.
  </div>
</div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
<div style="background:#101D33;border:1px solid rgba(0,212,255,0.25);border-top:3px solid #123D8D;
            border-radius:12px;padding:24px 20px;text-align:center;height:100%">
  <div style="font-size:1.4rem;margin-bottom:12px">&#128203;</div>
  <div style="color:#00D4FF;font-weight:700;font-size:0.9rem;margin-bottom:10px">
    Documentos Prontos
  </div>
  <div style="color:#B7C3D0;font-size:0.82rem;line-height:1.6">
    Organize contratos, procurações e orientações iniciais sem retrabalho.
  </div>
</div>""", unsafe_allow_html=True)

    # ── 7. POR QUE O GÊNESIS EXISTE ──────────────────────────────────────────
    st.markdown("""
<div style="max-width:900px;margin:40px auto 36px auto;
            background:#0A1628;border:1px solid #1A2E50;
            border-radius:16px;padding:40px 48px;text-align:center">
  <p style="color:#00D4FF;font-weight:700;font-size:1rem;
            letter-spacing:2px;text-transform:uppercase;margin:0 0 20px 0">
    Por que o Gênesis existe?
  </p>
  <p style="color:#B7C3D0;font-size:0.95rem;line-height:1.8;margin:0 0 16px 0">
    Já terminou uma consulta e, dias depois, percebeu que deveria ter feito outras perguntas,
    solicitado outras provas ou aprofundado melhor determinados pontos do caso?
  </p>
  <p style="color:#B7C3D0;font-size:0.95rem;line-height:1.8;margin:0 0 16px 0">
    Isso acontece porque, muitas vezes, o advogado precisa estudar o problema primeiro
    para só depois descobrir quais informações realmente importam.
  </p>
  <p style="color:#F8FAFC;font-size:1rem;font-weight:600;line-height:1.8;margin:0 0 16px 0">
    O Gênesis foi criado para encurtar esse caminho.
  </p>
  <p style="color:#B7C3D0;font-size:0.95rem;line-height:1.8;margin:0 0 16px 0">
    Ele identifica o tema do caso, conduz uma entrevista inteligente, orienta a coleta
    das provas mais relevantes e ajuda você a estruturar o atendimento desde o primeiro contato.
  </p>
  <p style="color:#B7C3D0;font-size:0.95rem;line-height:1.8;margin:0">
    Assim, mesmo diante de situações inéditas, você conduz a consulta com mais segurança,
    transmite mais confiança ao cliente e aumenta suas chances de transformar
    um atendimento em contratação.
  </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── BOTÕES ────────────────────────────────────────────────────────────────
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Iniciar Novo Atendimento", use_container_width=True, type="primary"):
            st.session_state.step = 1
            st.session_state.dados = {}
            st.rerun()

    with col_b:

        busca = st.text_input("🔍 Digite o nome do cliente",
                              placeholder="Ex: Vaneuza...",
                              key="busca_cliente")

        if busca and len(busca) >= 2:
            # Busca pastas de clientes que contenham o nome
            pastas = sorted(CLIENTES_DIR.glob(f"*"), key=lambda p: p.stat().st_mtime, reverse=True)
            encontrados = [p for p in pastas if busca.lower() in p.name.lower() and p.is_dir()]

            if encontrados:
                import platform as _plat, subprocess as _sub
                import io as _io, zipfile as _zf2
                from datetime import datetime as _dt

                for pasta in encontrados[:5]:
                    nome_pasta = pasta.name
                    data_fmt   = _dt.fromtimestamp(pasta.stat().st_mtime).strftime("%d/%m/%Y %H:%M")

                    # Lê tema do card
                    tema_txt = ""
                    card = pasta / "03_card_do_caso.txt"
                    if card.exists():
                        try:
                            for linha in card.read_text(encoding="utf-8").split("\n"):
                                if "Tema" in linha:
                                    tema_txt = linha.split(":", 1)[-1].strip()
                                    break
                        except: pass

                    # Lê nome e telefone do cadastro
                    nome_cli, tel_cli = "", ""
                    cad_file = pasta / "01_cadastro_cliente.txt"
                    if cad_file.exists():
                        try:
                            for ln in cad_file.read_text(encoding="utf-8").split("\n"):
                                if "Nome" in ln and ":" in ln and not nome_cli:
                                    nome_cli = ln.split(":", 1)[-1].strip()
                                if "Telefone" in ln and ":" in ln and not tel_cli:
                                    tel_cli = ln.split(":", 1)[-1].strip()
                        except: pass

                    nome_display = nome_cli or nome_pasta.split("_")[0].capitalize()

                    # Card do cliente
                    st.markdown(f"""
<div style="background:#0F1829;border:1px solid #1E3354;border-radius:10px;
            padding:14px 18px;margin-bottom:10px;">
  <div style="color:#E2E8F0;font-weight:700;font-size:0.95rem">{nome_display}</div>
  <div style="color:#475569;font-size:0.78rem;margin-top:2px">
    {data_fmt} &nbsp;·&nbsp; {tema_txt if tema_txt else 'sem tema registrado'}
  </div>
</div>""", unsafe_allow_html=True)

                    col_b1, col_b2 = st.columns(2)

                    # Botão: novo caso
                    with col_b1:
                        if st.button("+ Novo caso", key=f"novo_{nome_pasta}",
                                     use_container_width=True, type="primary"):
                            for _k in ["pasta_cliente", "obs_advogado", "prazo_provas", "proximo_contato"]:
                                st.session_state.pop(_k, None)
                            st.session_state.step    = 1
                            st.session_state.dados   = {}
                            st.session_state["prefill_nome"] = nome_cli
                            st.session_state["prefill_tel"]  = tel_cli
                            st.rerun()

                    # Botão: baixar documentos
                    with col_b2:
                        try:
                            _buf = _io.BytesIO()
                            _arquivos = [
                                "01_cadastro_cliente.txt","02_linha_do_tempo.txt",
                                "03_card_do_caso.txt","04_guia_probatorio.txt",
                                "05_orientacao_cliente.docx","06_proposta_honorarios.docx",
                                "07_procuracao.docx","08_contrato_honorarios.docx",
                                "09_plano_de_acao.txt",
                            ]
                            with _zf2.ZipFile(_buf, 'w', _zf2.ZIP_DEFLATED) as _zfile:
                                for _f in _arquivos:
                                    _fp = pasta / _f
                                    if _fp.exists():
                                        _zfile.write(_fp, _f)
                            _buf.seek(0)
                            st.download_button(
                                label="Baixar documentos",
                                data=_buf.read(),
                                file_name=f"genesis_{nome_pasta}.zip",
                                mime="application/zip",
                                key=f"zip_{nome_pasta}",
                                use_container_width=True,
                            )
                        except Exception as _e:
                            st.caption(f"Erro ao gerar ZIP: {_e}")

            else:
                st.caption("Nenhum atendimento encontrado para este nome.")

    st.stop()   # não renderiza o resto enquanto step == 0

steps = ["Cliente", "Caso", "Análise", "Entrevista", "Provas", "Resultado"]
cols_step = st.columns(len(steps))
for i, (col, step) in enumerate(zip(cols_step, steps), 1):
    with col:
        if i < st.session_state.step:
            st.markdown(f"<div style='text-align:center;color:#34D399;font-size:0.75rem;font-weight:700'>✓ {step}</div>", unsafe_allow_html=True)
        elif i == st.session_state.step:
            st.markdown(f"<div style='text-align:center;color:#818CF8;font-size:0.75rem;font-weight:700'>● {step}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:center;color:#475569;font-size:0.75rem'>○ {step}</div>", unsafe_allow_html=True)

st.progress(min((st.session_state.step - 1) / (len(steps) - 1), 1.0))
st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 — CADASTRO DO CLIENTE
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.step == 1:
    # Botão voltar para home
    if st.button("← Voltar"):
        st.session_state.step = 0
        st.session_state.pop("prefill_nome", None)
        st.session_state.pop("prefill_tel", None)
        st.rerun()

    st.markdown('<div class="section-title">01 — DADOS DO CLIENTE</div>', unsafe_allow_html=True)

    # Pré-preenchimento se vier de cliente existente
    _pnome = st.session_state.pop("prefill_nome", "")
    _ptel  = st.session_state.pop("prefill_tel", "")

    col1, col2 = st.columns(2)
    with col1:
        nome      = st.text_input("Nome completo *", value=_pnome)
        cpf       = st.text_input("CPF", placeholder="000.000.000-00")
        rg        = st.text_input("RG")
        nascimento = st.text_input("Data de nascimento", placeholder="01/01/1980")
    with col2:
        profissao = st.text_input("Profissão")
        telefone  = st.text_input("Telefone / WhatsApp *", value=_ptel,
                                   placeholder="(61) 9-8235-2676")
        email     = st.text_input("E-mail")
        endereco  = st.text_input("Endereço completo")

    cep = st.text_input("CEP")

    st.markdown("<br>", unsafe_allow_html=True)

    def formatar_data(d):
        """Converte 01011980 ou 01/01/1980 para 01/01/1980."""
        d = d.strip().replace("-", "/").replace(".", "/")
        if len(d) == 8 and "/" not in d:
            return f"{d[:2]}/{d[2:4]}/{d[4:]}"
        return d

    def formatar_fone(f):
        """Converte 61982352676 para (61) 9-8235-2676."""
        f = f.strip().replace(" ","").replace("-","").replace("(","").replace(")","")
        if len(f) == 11:
            return f"({f[:2]}) {f[2]}-{f[3:7]}-{f[7:]}"
        elif len(f) == 10:
            return f"({f[:2]}) {f[2:6]}-{f[6:]}"
        return f

    if st.button("Avançar →"):
        if not nome or not telefone:
            st.error("Nome e telefone são obrigatórios.")
        else:
            st.session_state.dados["cliente"] = {
                "nome": nome, "cpf": cpf, "rg": rg,
                "nascimento": formatar_data(nascimento),
                "profissao": profissao,
                "telefone": formatar_fone(telefone), "email": email,
                "endereco": endereco, "cep": cep,
                "polo_passivo": [],
                "data_atendimento": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            st.session_state.step = 2
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2 — DESCRIÇÃO DO CASO (limpo e intuitivo)
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 2:
    nome = st.session_state.dados["cliente"]["nome"]

    st.markdown(f'<div class="section-title">02 — CASO DE {nome.upper()}</div>',
                unsafe_allow_html=True)

    # ── Instrução clara ───────────────────────────────────────────────────────
    st.markdown("""
<div style="background:#0F1829;border:1px solid #1E3354;border-left:4px solid #00D4FF;
            border-radius:10px;padding:16px 20px;margin-bottom:20px">
  <div style="color:#F8FAFC;font-size:1rem;font-weight:600;margin-bottom:6px">
    Me conta o que aconteceu com seu cliente.
  </div>
  <div style="color:#94A3B8;font-size:0.85rem;line-height:1.6">
    Descreva com suas próprias palavras — quanto mais detalhes, mais preciso
    será o roteiro de perguntas que vou gerar.<br>
    <span style="color:#00D4FF">O Gênesis identifica o tema automaticamente.</span>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Campo de texto principal ──────────────────────────────────────────────
    descricao = st.text_area(
        "Descrição do caso",
        placeholder="Ex: Minha cliente descobriu que seu pai biológico faleceu. Ela nunca foi reconhecida. Quer incluir o nome no registro e participar da herança...",
        height=180,
        label_visibility="collapsed"
    )

    # ── Detecção em tempo real ────────────────────────────────────────────────
    tema_detectado = None
    if descricao and len(descricao) > 20:
        tema_detectado = detectar_tema(descricao, temas)
        if tema_detectado:
            st.markdown(f"""
<div style="background:#0A1E0A;border:1px solid #065F46;border-radius:10px;
            padding:14px 18px;margin-top:12px;display:flex;align-items:center;gap:10px">
  <span style="font-size:1.2rem">⚡</span>
  <div>
    <div style="color:#34D399;font-size:0.75rem;font-weight:700;letter-spacing:1px">
      TEMA IDENTIFICADO
    </div>
    <div style="color:#F8FAFC;font-size:0.95rem;font-weight:600">
      {tema_detectado['subtema']}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
        else:
            st.markdown("""
<div style="background:#1A0A0A;border:1px solid #7F1D1D;border-radius:10px;
            padding:12px 18px;margin-top:12px;color:#FCA5A5;font-size:0.85rem">
  ⚠️ Não consegui identificar o tema ainda. Adicione mais detalhes ou selecione abaixo.
</div>
""", unsafe_allow_html=True)

    # ── Seleção manual (só aparece se não detectou ou usuário quer corrigir) ──
    st.markdown("<br>", unsafe_allow_html=True)
    nomes_temas = [t["subtema"] for t in temas]
    idx_tema = 0
    if tema_detectado:
        idx_tema = next((i for i, t in enumerate(temas) if t["id"] == tema_detectado["id"]), 0)

    if tema_detectado:
        st.markdown("""
<div style="color:#475569;font-size:0.8rem;margin-bottom:4px">
  ✏️ <strong>O Gênesis identificou o tema acima automaticamente.</strong>
  Se estiver errado, marque a caixa abaixo para corrigir.
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div style="background:#1A0A0A;border:1px solid #7F1D1D;border-radius:8px;
            padding:10px 14px;color:#FCA5A5;font-size:0.82rem;margin-bottom:8px">
  ⚠️ Não identifiquei o tema ainda. Selecione o tipo de caso manualmente.
</div>
""", unsafe_allow_html=True)

    mostrar_selecao = st.checkbox("✏️ Corrigir tema" if tema_detectado else "Selecionar o tipo de caso")
    if mostrar_selecao or not tema_detectado:
        tema_escolhido_nome = st.selectbox("Tipo de caso", nomes_temas, index=idx_tema,
                                            label_visibility="collapsed")
    else:
        tema_escolhido_nome = tema_detectado["subtema"]
    tema_final = next(t for t in temas if t["subtema"] == tema_escolhido_nome)

    # ── Navegação ─────────────────────────────────────────────────────────────
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 1
            st.rerun()
    with col_nav[1]:
        if st.button("Avançar →", type="primary"):
            if not descricao or len(descricao) < 10:
                st.error("Descreva o caso antes de avançar.")
            else:
                st.session_state.dados["descricao"] = descricao
                st.session_state.dados["datas"] = {}   # preenchido no step 3
                st.session_state.dados["tema"] = tema_final
                st.session_state.step = 3
                st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — ANÁLISE DE INTELIGÊNCIA
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 3:
    import unicodedata

    tema      = st.session_state.dados["tema"]
    descricao = st.session_state.dados["descricao"]
    cliente   = st.session_state.dados.get("cliente", {})
    intel     = tema.get("inteligencia", {})

    def _norm(t):
        return unicodedata.normalize('NFKD', t).encode('ASCII', 'ignore').decode('ASCII').lower()

    desc_norm = _norm(descricao)

    # ── Detecta subtema (best-score, não first-match) ────────────────────────
    subtemas_kw = intel.get("subtemas", {})
    subtema_detectado = intel.get("subtema_default", tema.get("subtema", ""))
    melhor_pts = 0
    for nome_sub, kws in subtemas_kw.items():
        pts = sum(1 for kw in kws if _norm(kw) in desc_norm)
        if pts > melhor_pts:
            melhor_pts, subtema_detectado = pts, nome_sub

    # ── Extrai fatos do relato ───────────────────────────────────────────────
    import re
    fatos = []
    nome_cliente = cliente.get("nome", "")
    if nome_cliente:
        fatos.append(f"Cliente: {nome_cliente}")

    # Idade
    m = re.search(r'(\d{1,2})\s*anos', descricao)
    if m:
        fatos.append(f"Idade informada: {m.group(1)} anos")

    # Falecimento
    if any(p in desc_norm for p in ["faleceu", "falecido", "falecimento", "morreu", "obito"]):
        # Tenta capturar mês/ano
        m2 = re.search(r'(janeiro|fevereiro|março|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+de\s+(\d{4})', descricao, re.IGNORECASE)
        if m2:
            fatos.append(f"Falecimento mencionado: {m2.group(1)} de {m2.group(2)}")
        else:
            fatos.append("Falecimento mencionado no relato")

    # DNA / exame
    if "dna" in desc_norm or "exame" in desc_norm:
        fatos.append("Possibilidade de exame de DNA mencionada")

    # Herança / inventário
    if any(p in desc_norm for p in ["heranca", "inventario", "quinhao", "bens"]):
        fatos.append("Interesse patrimonial/sucessório mencionado")

    # Registro civil
    if any(p in desc_norm for p in ["registro", "certidao", "certidão"]):
        fatos.append("Questão de registro civil mencionada")

    # Guarda / visitas
    if any(p in desc_norm for p in ["guarda", "visita", "visitacao"]):
        fatos.append("Questão de guarda/visitas mencionada")

    # Pensão alimentícia
    if any(p in desc_norm for p in ["pensao", "alimentos", "alimenticio"]):
        fatos.append("Questão alimentar mencionada")

    # Casamento / divórcio
    if any(p in desc_norm for p in ["casamento", "casados", "divorc", "separac"]):
        fatos.append("Vínculo matrimonial mencionado")

    # União estável
    if any(p in desc_norm for p in ["uniao estavel", "companheiro", "companheira"]):
        fatos.append("União estável mencionada")

    # Imóvel
    if any(p in desc_norm for p in ["apartamento", "imovel", "casa", "imovel", "lote"]):
        fatos.append("Bem imóvel mencionado")

    # ── Fatos TRABALHISTA ────────────────────────────────────────────────────
    tema_id = tema.get("id", "")
    if "TRABALHISTA" in tema_id or any(p in desc_norm for p in ["trabalhista","vinculo","clt","trt"]):
        if any(p in desc_norm for p in ["carteira", "ctps", "anotacao"]):
            fatos.append("Registro em carteira mencionado")
        if any(p in desc_norm for p in ["informal", "sem carteira", "autonomo", "autonoma"]):
            fatos.append("Vínculo informal mencionado")
        if any(p in desc_norm for p in ["pejotizacao", "pj", "pessoa juridica"]):
            fatos.append("Possível pejotização (PJ forçada) mencionada")
        if any(p in desc_norm for p in ["prescrit", "prescricao", "prazo"]):
            fatos.append("Questão de prescrição mencionada")
        if any(p in desc_norm for p in ["demissao", "demitido", "dispensado", "rescisao"]):
            fatos.append("Rescisão/demissão mencionada")
        if any(p in desc_norm for p in ["subordinacao", "horario", "jornada"]):
            fatos.append("Indício de subordinação mencionado")

    # ── Fatos SOCIETÁRIO ─────────────────────────────────────────────────────
    if "SOCIETARIO" in tema_id or any(p in desc_norm for p in ["socio", "quadro", "contrato social", "empresa"]):
        if any(p in desc_norm for p in ["inclusao indevida", "incluido sem", "sem saber", "sem autorizar"]):
            fatos.append("Possível inclusão indevida no quadro societário")
        if any(p in desc_norm for p in ["assinatura", "falsificada", "forjada", "nao assinou"]):
            fatos.append("Questão de assinatura/falsificação mencionada")
        if any(p in desc_norm for p in ["desconsideracao", "penhora", "bloqueio", "execucao"]):
            fatos.append("Execução/desconsideração da personalidade mencionada")
        if any(p in desc_norm for p in ["nulidade", "nulo", "invalido", "fraudulento"]):
            fatos.append("Nulidade do ato societário mencionada")
        if any(p in desc_norm for p in ["jucdf", "junta comercial"]):
            fatos.append("Via administrativa JUCDF mencionada")
        if any(p in desc_norm for p in ["trabalhista", "trt", "reclamacao trabalhista"]):
            fatos.append("Conexão com processo trabalhista mencionada")

    # Label do subtema — usa o detectado diretamente (sem override hardcoded)
    if subtema_detectado and subtema_detectado != intel.get("subtema_default", ""):
        subtema_label = f"{tema['subtema']} › {subtema_detectado.title()}"
    else:
        subtema_label = tema["subtema"]

    # ── Hipóteses e Lacunas para subtema detectado ───────────────────────────
    hipoteses_mapa = intel.get("hipoteses", {})
    lacunas_mapa   = intel.get("lacunas", {})

    hipoteses = hipoteses_mapa.get(subtema_detectado, [])
    lacunas   = lacunas_mapa.get(subtema_detectado, [])

    # Filtra lacunas que o relato já respondeu
    lacunas_reais = []
    for lac in lacunas:
        lac_norm = _norm(lac)
        # Heurística: se mais de 3 palavras-chave da lacuna aparecem no relato, pula
        palavras = [w for w in lac_norm.split() if len(w) > 4]
        hits = sum(1 for w in palavras if w in desc_norm)
        if hits < 2:
            lacunas_reais.append(lac)

    # ── RENDER ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">03 — O QUE O GÊNESIS ENTENDEU</div>',
                unsafe_allow_html=True)
    st.markdown(
        "<div style='color:#94A3B8;font-size:0.85rem;margin-bottom:1.5rem'>"
        "Com base no relato inicial, o Gênesis identificou os pontos abaixo. "
        "As perguntas seguintes servem para confirmar, ajustar ou detalhar."
        "</div>",
        unsafe_allow_html=True
    )

    # Subtema
    st.markdown(f"""
    <div style="background:#141F35;border:1px solid #1E3354;border-left:4px solid #818CF8;
                border-radius:10px;padding:14px 18px;margin-bottom:1rem">
        <div style="color:#818CF8;font-size:0.7rem;font-weight:700;letter-spacing:2px;
                    text-transform:uppercase;margin-bottom:4px">Tema identificado</div>
        <div style="color:#E2E8F0;font-size:1rem;font-weight:700">{subtema_label}</div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    # Bloco Fatos Confirmados
    with col_a:
        if fatos:
            fatos_html = "".join(
                f"<div style='display:flex;align-items:flex-start;gap:8px;margin-bottom:6px'>"
                f"<span style='color:#34D399;font-weight:700;flex-shrink:0'>✓</span>"
                f"<span style='color:#CBD5E1;font-size:0.88rem'>{f}</span></div>"
                for f in fatos
            )
            st.markdown(f"""
            <div style="background:#0F1829;border:1px solid #1E3354;border-radius:10px;
                        padding:16px 18px;height:100%">
                <div style="color:#34D399;font-size:0.7rem;font-weight:700;letter-spacing:2px;
                            text-transform:uppercase;margin-bottom:10px">✓ Fatos identificados</div>
                {fatos_html}
            </div>
            """, unsafe_allow_html=True)

    # Bloco Hipóteses Jurídicas
    with col_b:
        if hipoteses:
            hip_html = "".join(
                f"<div style='display:flex;align-items:flex-start;gap:8px;margin-bottom:6px'>"
                f"<span style='color:#FBBF24;font-weight:700;flex-shrink:0'>◈</span>"
                f"<span style='color:#CBD5E1;font-size:0.88rem'>{h}</span></div>"
                for h in hipoteses
            )
            st.markdown(f"""
            <div style="background:#0F1829;border:1px solid #1E3354;border-radius:10px;
                        padding:16px 18px;height:100%">
                <div style="color:#FBBF24;font-size:0.7rem;font-weight:700;letter-spacing:2px;
                            text-transform:uppercase;margin-bottom:10px">◈ Hipóteses jurídicas prováveis</div>
                <div style="color:#64748B;font-size:0.74rem;margin-bottom:8px;font-style:italic">
                    hipóteses iniciais — sujeitas à confirmação
                </div>
                {hip_html}
            </div>
            """, unsafe_allow_html=True)

    # Bloco Lacunas
    if lacunas_reais:
        st.markdown("<br>", unsafe_allow_html=True)
        lac_html = "".join(
            f"<div style='display:flex;align-items:flex-start;gap:8px;margin-bottom:6px'>"
            f"<span style='color:#F59E0B;font-weight:700;flex-shrink:0'>🟡</span>"
            f"<span style='color:#CBD5E1;font-size:0.88rem'>{l}</span></div>"
            for l in lacunas_reais
        )
        st.markdown(f"""
        <div style="background:#0F1829;border:1px solid #1E3354;border-radius:10px;
                    padding:16px 18px">
            <div style="color:#F59E0B;font-size:0.7rem;font-weight:700;letter-spacing:2px;
                        text-transform:uppercase;margin-bottom:10px">🟡 O que ainda precisamos confirmar</div>
            <div style="color:#64748B;font-size:0.74rem;margin-bottom:8px;font-style:italic">
                As perguntas seguintes foram geradas a partir dessas lacunas
            </div>
            {lac_html}
        </div>
        """, unsafe_allow_html=True)

    # ── ALERTAS ESTRATÉGICOS por tema/subtema ────────────────────────────────
    tema_id_s3 = tema.get("id", "")

    # Alerta: STF Tema 1.389 — pejotização suspensa
    if subtema_detectado == "vinculo_societario" or "pejotizacao" in desc_norm or "pejotiz" in desc_norm:
        st.markdown("""
<div style="background:#1A0F00;border:1px solid #F59E0B;border-left:5px solid #F59E0B;
            border-radius:10px;padding:16px 20px;margin-top:16px">
  <div style="color:#F59E0B;font-size:0.72rem;font-weight:800;letter-spacing:2px;
              text-transform:uppercase;margin-bottom:6px">⚠️ Alerta — STF Tema 1.389</div>
  <div style="color:#FDE68A;font-size:0.9rem;font-weight:600;margin-bottom:4px">
    Processos de pejotização com verbas trabalhistas estão SUSPENSOS nacionalmente desde abril/2025
  </div>
  <div style="color:#B45309;font-size:0.82rem;line-height:1.5">
    Estratégia recomendada: ajuizar ação <strong>declaratória de vínculo</strong> no TRT-10 (imprescritível).
    A sentença declaratória serve de base para <strong>nulidade do quadro societário no TJDFT</strong> (CC art. 169 — nulidade absoluta = imprescritível).
    Consulte TST Tema 30 antes de prosseguir com pedidos de verbas.
  </div>
</div>
""", unsafe_allow_html=True)

    # Alerta: Via administrativa JUCDF — mais rápida e gratuita
    if subtema_detectado == "nulidade_inclusao" or "SOCIETARIO" in tema_id_s3:
        st.markdown("""
<div style="background:#001A0F;border:1px solid #34D399;border-left:5px solid #34D399;
            border-radius:10px;padding:16px 20px;margin-top:12px">
  <div style="color:#34D399;font-size:0.72rem;font-weight:800;letter-spacing:2px;
              text-transform:uppercase;margin-bottom:6px">💡 Via Administrativa — JUCDF</div>
  <div style="color:#6EE7B7;font-size:0.9rem;font-weight:600;margin-bottom:4px">
    Exclusão do quadro societário pode ser feita sem processo judicial
  </div>
  <div style="color:#065F46;font-size:0.82rem;line-height:1.5">
    Se houver assinatura falsificada comprovada (perícia grafotécnica ou declaração), o JUCDF
    aceita pedido administrativo de <strong>anulação de alteração contratual</strong>.
    É gratuito, mais rápido e não exclui a via judicial posterior.
    <strong>Avaliar sempre antes de ajuizar.</strong>
  </div>
</div>
""", unsafe_allow_html=True)

    # Alerta: Desconsideração — requisitos da teoria maior
    if subtema_detectado == "desconsideracao":
        st.markdown("""
<div style="background:#0A0A1A;border:1px solid #818CF8;border-left:5px solid #818CF8;
            border-radius:10px;padding:16px 20px;margin-top:12px">
  <div style="color:#818CF8;font-size:0.72rem;font-weight:800;letter-spacing:2px;
              text-transform:uppercase;margin-bottom:6px">⚖️ Atenção — Teoria Maior (CC art. 50)</div>
  <div style="color:#C7D2FE;font-size:0.9rem;font-weight:600;margin-bottom:4px">
    TJDFT exige desvio de finalidade OU confusão patrimonial
  </div>
  <div style="color:#4338CA;font-size:0.82rem;line-height:1.5">
    Encerramento irregular da empresa <strong>sozinho não basta</strong> (TJDFT 2127976/2026).
    É necessário provar: (a) desvio de finalidade — uso da PJ para fins ilícitos;
    ou (b) confusão patrimonial — mistura de bens pessoais e da empresa.
    <strong>Competência: Vara Cível comum</strong>, não Vara Empresarial.
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 2
            st.rerun()
    with col_nav[1]:
        if st.button("Avançar — Responder perguntas →", type="primary"):
            st.session_state.dados["subtema_detectado"] = subtema_detectado
            st.session_state.step = 4
            st.rerun()

# STEP 4 — ENTREVISTA GUIADA
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 4:
    tema = st.session_state.dados["tema"]
    subtema_label_4 = st.session_state.dados.get("subtema_detectado", tema.get("subtema","")).upper()
    st.markdown(f'<div class="section-title">04 — ENTREVISTA · {subtema_label_4}</div>',
                unsafe_allow_html=True)

    # ── Seleciona marcos e perguntas baseado no subtema detectado ────────────
    subtema_det = st.session_state.dados.get("subtema_detectado", "")
    marcos_sub  = tema.get("marcos_por_subtema", {}).get(subtema_det, {})
    if marcos_sub:
        marcos      = marcos_sub.get("marcos", [])
        marcos_desc = marcos_sub.get("descricao", {})
    else:
        marcos      = tema.get("marcos_temporais", [])
        marcos_desc = tema.get("marcos_descricao", {})

    perguntas_sub = tema.get("perguntas_por_subtema", {}).get(subtema_det, [])
    perguntas_ativas = perguntas_sub if perguntas_sub else tema.get("perguntas_consulta", [])

    datas = st.session_state.dados.get("datas", {})

    if marcos:
        st.markdown('<div class="section-title">LINHA DO TEMPO DOS EVENTOS</div>',
                    unsafe_allow_html=True)
        st.caption("Preencha o que souber. Deixe em branco ou escreva 'Não sei' se não tiver a informação.")
        st.markdown("<br>", unsafe_allow_html=True)

        col_dt1, col_dt2 = st.columns(2)
        for i, marco in enumerate(marcos):
            descricao_campo = marcos_desc.get(marco, "")
            with (col_dt1 if i % 2 == 0 else col_dt2):
                val = st.text_input(
                    marco,
                    value=datas.get(marco, ""),
                    placeholder="DD/MM/AAAA ou 'Não se aplica'",
                    key=f"dt3_{tema['id']}_{i}"
                )
                if descricao_campo:
                    st.caption(f"ℹ️ {descricao_campo}")
                if val:
                    datas[marco] = val
        st.session_state.dados["datas"] = datas
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<br>", unsafe_allow_html=True)

    # ── MOTOR DE PERGUNTAS CONDICIONAIS ──────────────────────────────────────
    st.markdown('<div class="section-title">PERGUNTAS DO CASO</div>', unsafe_allow_html=True)
    st.caption("Responda o que souber. Novas perguntas aparecerão conforme o caso se desenvolve.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Todas as perguntas do subtema, indexadas por id
    todas_pqs = perguntas_ativas  # lista com campo 'condicao' opcional
    todas_por_id = {p["id"]: p for p in todas_pqs if "id" in p}

    # Recupera respostas já dadas nesta sessão
    respostas = st.session_state.dados.get("respostas_motor", {})

    def _condicao_ok(pq, resps):
        """Retorna True se a pergunta deve ser exibida."""
        cond = pq.get("condicao")
        if not cond:
            return True
        # formato: "ID=Valor"
        partes = cond.split("=", 1)
        if len(partes) != 2:
            return False
        ref_id, val_esperado = partes
        return resps.get(ref_id, "") == val_esperado

    # Calcula quais perguntas estão ativas agora (com base nas respostas atuais)
    pqs_visiveis = [p for p in todas_pqs if _condicao_ok(p, respostas)]

    # Renderiza cada pergunta visível
    num_visivel = 0
    for pq in pqs_visiveis:
        pq_id   = pq.get("id", "")
        tipo    = pq.get("tipo", "texto")
        opcoes  = pq.get("opcoes", [])
        cond    = pq.get("condicao")

        # Badge condicional (sinaliza visualmente que surgiu por uma resposta)
        badge = ""
        if cond:
            badge = "<span style='background:#1E3354;color:#22D3EE;font-size:0.65rem;padding:2px 8px;border-radius:99px;margin-left:8px'>↳ pergunta adicional</span>"

        num_visivel += 1
        st.markdown(f"""
        <div style="background:#141F35;border:1px solid #1E3354;border-left:4px solid {'#22D3EE' if cond else '#3A82FF'};
                    border-radius:10px;padding:14px 18px;margin-bottom:8px">
            <div style="font-weight:700;color:#E2E8F0;font-size:0.92rem;margin-bottom:4px">
                {num_visivel}. {pq['pergunta']}{badge}
            </div>
            <div style="color:#64748B;font-size:0.76rem">
                &#9654;&nbsp; {pq.get('motivo','')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        resp_atual = respostas.get(pq_id, "")

        if tipo == "sim_nao":
            opcoes_sn = ["— selecione —", "Sim", "Não"]
            idx_sn = opcoes_sn.index(resp_atual) if resp_atual in opcoes_sn else 0
            resp = st.selectbox("", opcoes_sn, index=idx_sn,
                                key=f"motor_{pq_id}", label_visibility="collapsed")
            if resp != "— selecione —":
                respostas[pq_id] = resp
            elif pq_id in respostas:
                del respostas[pq_id]

        elif tipo == "escolha" and opcoes:
            opcoes_c = ["— selecione —"] + opcoes
            idx_c = opcoes_c.index(resp_atual) if resp_atual in opcoes_c else 0
            resp = st.selectbox("", opcoes_c, index=idx_c,
                                key=f"motor_{pq_id}", label_visibility="collapsed")
            if resp != "— selecione —":
                respostas[pq_id] = resp
            elif pq_id in respostas:
                del respostas[pq_id]

        else:  # texto
            resp = st.text_area("", value=resp_atual, height=68,
                                key=f"motor_{pq_id}", label_visibility="collapsed",
                                placeholder="Digite aqui...")
            if resp.strip():
                respostas[pq_id] = resp.strip()
            elif pq_id in respostas:
                del respostas[pq_id]

        st.markdown("<div style='margin-bottom:4px'></div>", unsafe_allow_html=True)

    # Salva respostas no session_state a cada rerun
    st.session_state.dados["respostas_motor"] = respostas

    # Contador dinâmico
    total_possiveis = len(todas_pqs)
    total_visiveis  = len(pqs_visiveis)
    st.markdown(f"""
    <div style="color:#475569;font-size:0.75rem;text-align:right;margin-top:8px">
        {total_visiveis} pergunta(s) ativas · máximo possível: {total_possiveis}
    </div>
    """, unsafe_allow_html=True)

    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 3
            st.rerun()
    with col_nav[1]:
        if st.button("Avançar →"):
            # Salva respostas consolidadas (motor condicional)
            st.session_state.dados["respostas"] = st.session_state.dados.get("respostas_motor", {})
            st.session_state.step = 5
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5 — GUIA PROBATÓRIO
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 5:
    tema = st.session_state.dados["tema"]
    st.markdown(f'<div class="section-title">05 — PROVAS DO CASO</div>', unsafe_allow_html=True)

    st.markdown("**Para cada prova, informe a situação atual:**")
    st.caption("Selecione o que melhor descreve a situação de cada documento.")
    st.markdown("<br>", unsafe_allow_html=True)

    provas_tem = {}
    opcoes = [
        "✅ Já tenho",
        "🔄 Vou buscar",
        "⚠️ Não tenho e não vou conseguir",
        "❓ Não sei se existe",
        "➖ Não se aplica"
    ]

    subtema_det = st.session_state.dados.get("subtema_detectado", "")
    provas_sub_data = tema.get("provas_por_subtema", {}).get(subtema_det, {})
    provas_ativas = provas_sub_data.get("provas", []) if provas_sub_data else tema.get("provas_essenciais", [])
    provas_como_obter = provas_sub_data.get("como_obter", {}) if provas_sub_data else tema.get("provas_como_obter", {})

    for prova in provas_ativas:
        col_p1, col_p2 = st.columns([2, 1])
        with col_p1:
            st.markdown(f"<div style='color:#E2E8F0;font-size:0.9rem;padding-top:8px;font-weight:600'>{prova}</div>",
                        unsafe_allow_html=True)
            como = provas_como_obter.get(prova, "")
            if como:
                st.markdown(f"<div style='color:#94A3B8;font-size:0.78rem;margin-top:2px'>→ {como}</div>",
                            unsafe_allow_html=True)
        with col_p2:
            status = st.selectbox(
                label=prova,
                options=opcoes,
                key=f"prova_{prova[:30]}",
                label_visibility="collapsed"
            )
        provas_tem[prova] = status
        st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

    # Como obter — só mostra para quem vai buscar ou não tem
    st.markdown("<br>", unsafe_allow_html=True)
    pendentes = {p: s for p, s in provas_tem.items() if "Vou buscar" in s or "Não tenho" in s}
    if pendentes:
        st.markdown("**Como obter as provas pendentes:**")
        for prova, status in pendentes.items():
            como = provas_como_obter.get(prova, "")
            emoji = "🔄" if "Vou buscar" in status else "⚠️"
            if como:
                st.markdown(f"{emoji} **{prova}**  \n→ {como}")

    # ── POLO PASSIVO GUIADO ───────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">POLO PASSIVO — Contra quem vamos ajuizar</div>',
                unsafe_allow_html=True)

    polo_info = tema.get("polo_passivo", {})
    if polo_info:
        st.markdown(f"""
        <div style="background:#141F35;border-left:4px solid #22D3EE;border-radius:8px;
                    padding:14px 18px;margin-bottom:10px">
            <div style="color:#22D3EE;font-size:0.72rem;font-weight:700;letter-spacing:2px;
                        text-transform:uppercase;margin-bottom:4px">Gênesis sugere</div>
            <div style="color:#E2E8F0;font-size:0.92rem;font-weight:600">{polo_info.get('sugestao','')}</div>
        </div>
        """, unsafe_allow_html=True)
        if polo_info.get("alerta"):
            st.warning(f"⚠️ {polo_info['alerta']}")

    # Campos dinâmicos baseados no tipo (PF ou PJ)
    tipo_polo = polo_info.get("tipo", "PJ")
    is_pf = tipo_polo == "PF"
    is_variavel = "/" in tipo_polo  # PF/PJ

    if is_variavel:
        reu_tipo = st.radio("Tipo do réu", ["Pessoa Jurídica", "Pessoa Física"],
                            horizontal=True, key="reu_tipo")
        is_pf = reu_tipo == "Pessoa Física"
    else:
        reu_tipo = "Pessoa Física" if is_pf else "Pessoa Jurídica"

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        label_nome = "Nome completo" if is_pf else "Razão Social"
        reu_nome = st.text_input(label_nome, key="reu_nome")
    with col_r2:
        label_doc = "CPF" if is_pf else "CNPJ"
        reu_doc = st.text_input(label_doc, key="reu_doc")

    segundo_reu = st.checkbox("Adicionar segundo réu")
    reu2_nome, reu2_doc, reu2_tipo = "", "", reu_tipo
    if segundo_reu:
        col_r3, col_r4 = st.columns(2)
        with col_r3:
            reu2_nome = st.text_input(f"{label_nome} (2º réu)", key="reu2_nome")
        with col_r4:
            reu2_doc = st.text_input(f"{label_doc} (2º réu)", key="reu2_doc")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Honorários:**")
    col_h = st.columns(3)
    with col_h[0]:
        fixo = st.text_input("Valor fixo (R$)", value="***")
    with col_h[1]:
        exito = st.text_input("% Êxito", value="20")
    with col_h[2]:
        parcelas = st.selectbox("Pagamento", ["À vista", "2x", "3x", "4x", "A combinar"])

    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 4
            st.rerun()
    with col_nav[1]:
        if st.button("⚡ Gerar Análise e Documentos"):
            polo = [{"nome": reu_nome, "doc": reu_doc, "tipo": reu_tipo}] if reu_nome else []
            if segundo_reu and reu2_nome:
                polo.append({"nome": reu2_nome, "doc": reu2_doc, "tipo": reu2_tipo})
            st.session_state.dados["cliente"]["polo_passivo"] = polo
            st.session_state.dados["provas_tem"] = provas_tem
            st.session_state.dados["honor"] = {
                "fixo": fixo, "exito": exito,
                "parcelas": parcelas,
                "referencia": tema.get("valor_referencia", "A calcular")
            }
            st.session_state.step = 6
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 6 — RESULTADO FINAL
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 6:
    import sys
    sys.path.insert(0, str(PASTA))
    from modo_consultoria_v2 import gerar_todos_documentos

    d = st.session_state.dados
    # Proteção: se dados incompletos, volta ao início
    chaves_necessarias = ["cliente", "tema", "descricao", "datas", "respostas", "provas_tem", "honor"]
    if not all(k in d for k in chaves_necessarias):
        st.error("Sessão incompleta. Reiniciando atendimento...")
        st.session_state.step = 0
        st.session_state.dados = {}
        for _k in ["pasta_cliente", "obs_advogado", "prazo_provas", "proximo_contato"]:
            st.session_state.pop(_k, None)
        st.rerun()
    cliente   = d["cliente"]
    tema      = d["tema"]
    descricao = d["descricao"]
    datas     = d["datas"]
    respostas = d["respostas"]
    provas    = d["provas_tem"]
    honor     = d["honor"]

    # Classifica provas pelos estados
    provas_ja_tem  = [p for p, v in provas.items() if "Já tenho" in str(v)]
    provas_buscar  = [p for p, v in provas.items() if "Vou buscar" in str(v)]
    provas_nao_tem = [p for p, v in provas.items() if "Não tenho" in str(v) or "Não sei" in str(v)]
    total = len(provas)
    tem_count = len(provas_ja_tem)

    # Define situação geral do caso
    if not provas_nao_tem and not provas_buscar:
        cor_caso, bg_caso, txt_caso = "#34D399", "#022C22", "CASO BEM DOCUMENTADO"
    elif not provas_nao_tem:
        cor_caso, bg_caso, txt_caso = "#FCD34D", "#1C1007", "AGUARDANDO DOCUMENTOS"
    else:
        cor_caso, bg_caso, txt_caso = "#F87171", "#1F0A0A", "PROVAS INCOMPLETAS"

    # Gera documentos apenas uma vez — salva pasta no session_state
    if "pasta_cliente" not in st.session_state:
        with st.spinner("Analisando caso e gerando documentos..."):
            slug = cliente["nome"].split()[0].lower()
            ts_pasta = datetime.now().strftime("%Y%m%d_%H%M")
            pasta_cliente = CLIENTES_DIR / f"{slug}_{ts_pasta}"
            pasta_cliente.mkdir(exist_ok=True)
            prob_dict = {"nivel": txt_caso, "tem": tem_count, "total": total,
                         "ja_tem": provas_ja_tem, "buscar": provas_buscar, "nao_tem": provas_nao_tem}
            try:
                gerar_todos_documentos(pasta_cliente, cliente, tema, descricao,
                                       datas, respostas, provas, prob_dict, honor)
                st.session_state.pasta_cliente = str(pasta_cliente)
                sucesso = True
            except Exception as e:
                sucesso = False
                st.error(f"Erro: {e}")
    else:
        pasta_cliente = Path(st.session_state.pasta_cliente)
        sucesso = True

    if sucesso:
        # ── HERO RESULTADO ────────────────────────────────────────────────────
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0F2350,#1A3A7A);border:1px solid #1E3A7A;border-radius:20px;
                    padding:32px 40px;margin-bottom:24px;color:white;text-align:center;
                    box-shadow:0 12px 40px rgba(79,70,229,0.35)">
            <div style="font-size:0.75rem;letter-spacing:4px;opacity:0.8;text-transform:uppercase;margin-bottom:8px">
                ANÁLISE CONCLUÍDA
            </div>
            <div style="font-size:1.6rem;font-weight:800;margin-bottom:4px">
                {cliente['nome']}
            </div>
            <div style="font-size:1rem;opacity:0.85">{tema['subtema']}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── MÉTRICAS PRINCIPAIS ───────────────────────────────────────────────
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div style="background:{bg_caso};border:2px solid {cor_caso};border-radius:16px;
                        padding:24px;text-align:center">
                <div style="font-size:0.7rem;letter-spacing:3px;color:#94A3B8;text-transform:uppercase;margin-bottom:8px">
                    Como o caso está
                </div>
                <div style="font-size:1.3rem;font-weight:900;color:{cor_caso};line-height:1.3;margin:8px 0">
                    {txt_caso}
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div style="background:#141F35;border:2px solid #1E3354;border-radius:16px;
                        padding:24px;text-align:center">
                <div style="font-size:0.7rem;letter-spacing:3px;color:#94A3B8;text-transform:uppercase;margin-bottom:8px">
                    Provas em Mãos
                </div>
                <div style="font-size:3.5rem;font-weight:900;color:#3A82FF;line-height:1">
                    {tem_count}<span style="font-size:1.5rem;color:#3D4F6B">/{total}</span>
                </div>
                <div style="font-size:0.9rem;color:#22D3EE;margin-top:6px">essenciais coletadas</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div style="background:#141F35;border:2px solid #1E3354;border-radius:16px;
                        padding:24px;text-align:center">
                <div style="font-size:0.7rem;letter-spacing:3px;color:#64748B;text-transform:uppercase;margin-bottom:8px">
                    Documentos Gerados
                </div>
                <div style="font-size:3.5rem;font-weight:900;color:#34D399;line-height:1">8</div>
                <div style="font-size:0.9rem;color:#34D399;margin-top:6px">prontos para usar</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── DOCUMENTOS ────────────────────────────────────────────────────────
        st.markdown('<div class="section-title">DOCUMENTOS PRONTOS</div>', unsafe_allow_html=True)

        docs_info = [
            ("01_cadastro_cliente.txt",    "📋", "Cadastro do Cliente",      "#EEF2FF", "#6366F1"),
            ("02_linha_do_tempo.txt",       "📅", "Linha do Tempo",           "#EEF2FF", "#6366F1"),
            ("03_card_do_caso.txt",         "🃏", "Card do Caso",             "#EEF2FF", "#6366F1"),
            ("04_guia_probatorio.txt",      "🔍", "Guia Probatório",          "#FFFBEB", "#D97706"),
            ("05_orientacao_cliente.docx",  "📝", "Orientação ao Cliente",    "#FFFBEB", "#D97706"),
            ("06_proposta_honorarios.docx", "💰", "Proposta de Honorários",   "#F0FDF4", "#16A34A"),
            ("07_procuracao.docx",          "✍️", "Procuração",               "#F0FDF4", "#16A34A"),
            ("08_contrato_honorarios.docx", "📄", "Contrato de Honorários",   "#F0FDF4", "#16A34A"),
        ]

        # Lista os documentos gerados
        col_d1, col_d2 = st.columns(2)
        for i, (fname, icon, label, bg, cor) in enumerate(docs_info):
            fpath = pasta_cliente / fname
            col = col_d1 if i % 2 == 0 else col_d2
            with col:
                if fpath.exists():
                    st.markdown(f"""
                    <div style="background:{bg};border:1px solid {cor}30;border-left:4px solid {cor};
                                border-radius:10px;padding:12px 16px;margin-bottom:6px;
                                display:flex;align-items:center;gap:10px;">
                        <span style="font-size:1.2rem">{icon}</span>
                        <div>
                            <div style="font-weight:700;color:#1a1a2e;font-size:0.85rem">{label}</div>
                            <div style="color:#16A34A;font-size:0.72rem;font-weight:600">✓ Gerado</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # ── BOTÃO ÚNICO: BAIXAR TUDO EM ZIP ──────────────────────────────────
        import io, zipfile as _zip
        zip_buf = io.BytesIO()
        slug_nome = cliente['nome'].split()[0].lower()
        with _zip.ZipFile(zip_buf, 'w', _zip.ZIP_DEFLATED) as zf:
            for fname, _, label, _, _ in docs_info:
                fpath = pasta_cliente / fname
                if fpath.exists():
                    zf.write(fpath, fname)
        zip_buf.seek(0)

        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label=f"📁 Baixar pasta completa — {cliente['nome']}",
            data=zip_buf.read(),
            file_name=f"genesis_{slug_nome}_{datetime.now().strftime('%Y%m%d')}.zip",
            mime="application/zip",
            use_container_width=True,
            type="primary",
        )

        # ── PASTA DO CLIENTE ──────────────────────────────────────────────────
        import platform, subprocess
        if platform.system() == "Windows":
            # Na máquina local: mostra caminho clicável e abre o Explorer
            st.markdown(f"""
            <div style="background:#141F35;border:1px solid #1E3354;border-radius:12px;
                        padding:16px 20px;margin:16px 0;display:flex;align-items:center;gap:12px">
                <span style="font-size:1.5rem">📁</span>
                <div>
                    <div style="font-weight:700;color:#E2E8F0;font-size:0.85rem">Pasta do cliente criada</div>
                    <div style="color:#94A3B8;font-size:0.78rem;font-family:monospace">{pasta_cliente}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📂 Abrir pasta no Windows Explorer", use_container_width=True):
                subprocess.Popen(f'explorer "{pasta_cliente}"')
        else:
            # Na versão online: só mostra o nome do cliente, sem caminho de servidor
            st.markdown(f"""
            <div style="background:#022C22;border:1px solid #065F46;border-radius:12px;
                        padding:16px 20px;margin:16px 0;display:flex;align-items:center;gap:12px">
                <span style="font-size:1.5rem">✅</span>
                <div>
                    <div style="font-weight:700;color:#34D399;font-size:0.9rem">
                        Documentos gerados — use os botões ⬇️ para baixar
                    </div>
                    <div style="color:#6EE7B7;font-size:0.78rem">
                        {cliente['nome']} · {datetime.now().strftime('%d/%m/%Y %H:%M')}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── ORIENTAÇÕES AO CLIENTE (filtradas por subtema) ───────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">ORIENTAÇÕES AO CLIENTE</div>', unsafe_allow_html=True)
        subtema_det6 = d.get("subtema_detectado", "")
        oris = (tema.get("orientacao_por_subtema", {}).get(subtema_det6)
                or tema.get("orientacao_cliente", []))
        for i, ori in enumerate(oris, 1):
            st.markdown(f"""
            <div style="background:#1E293B;border:1px solid #334155;border-radius:8px;
                        padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;
                        box-shadow:0 1px 3px rgba(0,0,0,0.04)">
                <div style="background:#1D4ED8;color:white;border-radius:50%;width:24px;height:24px;
                            display:flex;align-items:center;justify-content:center;
                            font-size:0.75rem;font-weight:800;flex-shrink:0;margin-top:1px">{i}</div>
                <div style="color:#CBD5E1;font-size:0.9rem;line-height:1.5">{ori}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── PLANO DE AÇÃO ─────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">PLANO DE AÇÃO</div>', unsafe_allow_html=True)

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            prazo_provas = st.date_input("📁 Cliente traz as provas até",
                                         value=None, format="DD/MM/YYYY",
                                         key="prazo_provas")
        with col_p2:
            proximo_contato = st.date_input("📆 Próximo contato agendado",
                                             value=None, format="DD/MM/YYYY",
                                             key="proximo_contato")

        obs = st.text_area("📝 Observação do advogado",
                           placeholder="Ex: Elaborar declaração de anuência para o filho Vinícius. Conferir percentual na sentença original.",
                           height=90, key="obs_advogado")

        # Gera mensagem de WhatsApp automaticamente
        provas_faltam = [p for p, v in provas.items() if "Vou buscar" in str(v) or "Não tenho" in str(v) or "Não sei" in str(v)]
        prazo_str     = prazo_provas.strftime("%d/%m/%Y") if prazo_provas else "___/___/______"
        contato_str   = proximo_contato.strftime("%d/%m/%Y") if proximo_contato else "___/___/______"

        msg_wp = f"Olá {cliente['nome'].split()[0]}, tudo bem?\n\n"
        msg_wp += f"Conforme combinamos hoje, precisamos que você nos envie:\n"
        if provas_faltam:
            for pf in provas_faltam:
                msg_wp += f"• {pf}\n"
        else:
            msg_wp += "• Documentos conforme orientação enviada\n"
        msg_wp += f"\nPrazo: *{prazo_str}*\n"
        msg_wp += f"Próximo contato: *{contato_str}*\n\n"
        msg_wp += f"Qualquer dúvida, estou à disposição!\n\n"
        msg_wp += f"Fernando Rosa — OAB/DF 46.284\n(61) 99170-7225"

        with st.expander("📱 Mensagem pronta para WhatsApp — clique para copiar"):
            st.code(msg_wp, language=None)

        # Botão que abre WhatsApp Web com número e mensagem preenchidos
        import urllib.parse
        tel_raw = cliente.get("telefone", "").replace(" ","").replace("-","").replace("(","").replace(")","")
        if not tel_raw.startswith("55"):
            tel_raw = "55" + tel_raw
        msg_encoded = urllib.parse.quote(msg_wp)
        wp_link = f"whatsapp://send?phone={tel_raw}&text={msg_encoded}"
        st.markdown(f"""
        <a href="{wp_link}" target="_blank" style="
            display:block; text-align:center; background:linear-gradient(135deg,#128C7E,#25D366);
            color:white; font-weight:700; font-size:1rem; padding:14px;
            border-radius:10px; text-decoration:none; margin-top:8px;
            box-shadow:0 4px 16px rgba(37,211,102,0.4); letter-spacing:0.3px;">
            📲 Abrir WhatsApp e enviar mensagem para {cliente['nome'].split()[0]}
        </a>
        """, unsafe_allow_html=True)

        # Salva plano na pasta do cliente
        if st.button("💾 Salvar plano de ação na pasta", use_container_width=True):
            plano_txt  = f"PLANO DE AÇÃO — {cliente['nome']}\n"
            plano_txt += f"{'='*50}\n"
            plano_txt += f"Prazo para provas : {prazo_str}\n"
            plano_txt += f"Próximo contato   : {contato_str}\n\n"
            plano_txt += f"OBSERVAÇÃO DO ADVOGADO:\n{obs or '(sem observações)'}\n\n"
            plano_txt += f"PROVAS QUE FALTAM:\n"
            for pf in provas_faltam:
                plano_txt += f"  [ ] {pf}\n"
            plano_txt += f"\nMENSAGEM WHATSAPP:\n{msg_wp}\n"
            (pasta_cliente / "09_plano_de_acao.txt").write_text(plano_txt, encoding="utf-8")
            st.success("✅ Plano salvo como 09_plano_de_acao.txt na pasta do cliente.")

        # ── BOTÃO NOVO ATENDIMENTO ────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("+ Novo Atendimento"):
            for key in ["pasta_cliente", "obs_advogado", "prazo_provas", "proximo_contato"]:
                st.session_state.pop(key, None)
            st.session_state.step = 0
            st.session_state.dados = {}
            st.rerun()
