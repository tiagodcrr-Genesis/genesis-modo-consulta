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

# ── Carrega dados ─────────────────────────────────────────────────────────────
PASTA = Path(__file__).parent
TEMAS_JSON = PASTA / "consulta_temas_v2.json"
CLIENTES_DIR = PASTA / "clientes"
CLIENTES_DIR.mkdir(exist_ok=True)

def carregar_temas():
    with open(TEMAS_JSON, encoding="utf-8") as f:
        return json.load(f)["temas"]

def detectar_tema(descricao, temas):
    desc = descricao.lower()
    melhor, melhor_pts = None, 0
    for t in temas:
        pts = sum(1 for kw in t["keywords"] if kw.lower() in desc)
        if pts > melhor_pts:
            melhor_pts, melhor = pts, t
    return melhor if melhor_pts >= 1 else None

def calcular_prob(tema, provas_tem):
    base = tema.get("probabilidade_base", 60)
    essenciais = tema.get("provas_essenciais", [])
    if not essenciais:
        return base
    tem = sum(1 for v in provas_tem.values() if v)
    faltando = len(essenciais) - tem
    prob = max(20, base - faltando * 8)
    return prob

# ── Header ────────────────────────────────────────────────────────────────────
_nome = "G" + chr(202) + "NESIS"
st.markdown(f"""
<div class="genesis-header">
    <p style="font-size:4rem;font-weight:900;letter-spacing:2px;color:#FFFFFF;margin:0;text-align:center;text-shadow:0 2px 20px rgba(0,0,0,0.3)">{_nome}</p>
    <p style="font-size:0.85rem;letter-spacing:3px;color:rgba(255,255,255,0.75);margin:8px 0 0 0;text-align:center">
        MODO CONSULTORIA &nbsp;&middot;&nbsp; FERNANDO ROSA ADVOCACIA
    </p>
</div>
""", unsafe_allow_html=True)

# ── Progress steps ────────────────────────────────────────────────────────────
temas = carregar_temas()

if "step" not in st.session_state:
    st.session_state.step = 1
if "dados" not in st.session_state:
    st.session_state.dados = {}

steps = ["Cliente", "Caso", "Entrevista", "Provas", "Resultado"]
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
    st.markdown('<div class="section-title">01 — DADOS DO CLIENTE</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        nome      = st.text_input("Nome completo *")
        cpf       = st.text_input("CPF")
        rg        = st.text_input("RG")
        nascimento= st.text_input("Data de nascimento (DD/MM/AAAA)")
    with col2:
        profissao = st.text_input("Profissão")
        telefone  = st.text_input("Telefone / WhatsApp *")
        email     = st.text_input("E-mail")
        endereco  = st.text_input("Endereço completo")

    cep = st.text_input("CEP")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Avançar →"):
        if not nome or not telefone:
            st.error("Nome e telefone são obrigatórios.")
        else:
            st.session_state.dados["cliente"] = {
                "nome": nome, "cpf": cpf, "rg": rg,
                "nascimento": nascimento, "profissao": profissao,
                "telefone": telefone, "email": email,
                "endereco": endereco, "cep": cep,
                "data_atendimento": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            st.session_state.step = 2
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2 — DESCRIÇÃO DO CASO
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 2:
    nome = st.session_state.dados["cliente"]["nome"]
    st.markdown(f'<div class="section-title">02 — CASO DE {nome.upper()}</div>', unsafe_allow_html=True)

    descricao = st.text_area(
        "Descreva o que aconteceu",
        placeholder="Ex: Meu cliente foi demitido sem justa causa após 5 anos de empresa. Não recebeu FGTS...",
        height=150
    )

    # Detecta tema em tempo real
    tema_detectado = None
    if descricao and len(descricao) > 20:
        tema_detectado = detectar_tema(descricao, temas)
        if tema_detectado:
            st.markdown(f"""
            <div class="tema-badge">
                ⚡ Tema identificado: <strong>{tema_detectado['subtema']}</strong>
            </div>
            """, unsafe_allow_html=True)

    # Linha do tempo
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">LINHA DO TEMPO DOS EVENTOS</div>', unsafe_allow_html=True)

    tema_para_datas = tema_detectado or temas[0]
    marcos = tema_para_datas.get("marcos_temporais", [])

    datas = {}
    col_dt = st.columns(min(len(marcos), 2)) if marcos else st.columns(1)
    for i, marco in enumerate(marcos):
        with col_dt[i % 2]:
            val = st.text_input(marco, placeholder="DD/MM/AAAA ou descrição",
                                key=f"data_{tema_para_datas['id']}_{i}")
            if val:
                datas[marco] = val

    # Seleção manual de tema
    if not tema_detectado and descricao:
        st.warning("Tema não detectado automaticamente. Selecione abaixo:")

    nomes_temas = [t["subtema"] for t in temas]
    idx_tema = 0
    if tema_detectado:
        idx_tema = next((i for i, t in enumerate(temas) if t["id"] == tema_detectado["id"]), 0)

    tema_escolhido_nome = st.selectbox("Tipo de caso", nomes_temas, index=idx_tema)
    tema_final = next(t for t in temas if t["subtema"] == tema_escolhido_nome)

    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 1
            st.rerun()
    with col_nav[1]:
        if st.button("Avançar →"):
            if not descricao:
                st.error("Descreva o caso antes de avançar.")
            else:
                st.session_state.dados["descricao"] = descricao
                st.session_state.dados["datas"] = datas
                st.session_state.dados["tema"] = tema_final
                st.session_state.step = 3
                st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — ENTREVISTA GUIADA
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 3:
    tema = st.session_state.dados["tema"]
    st.markdown(f'<div class="section-title">03 — ENTREVISTA · {tema["subtema"].upper()}</div>', unsafe_allow_html=True)

    respostas = {}
    for pq in tema.get("perguntas_consulta", []):
        st.markdown(f"""
        <div style="background:#141F35;border:1px solid #1E3354;border-left:4px solid #3A82FF;
                    border-radius:10px;padding:16px 20px;margin-bottom:12px;
                    box-shadow:0 1px 4px rgba(0,0,0,0.06)">
            <div style="font-weight:700;color:#E2E8F0;font-size:0.95rem;margin-bottom:6px">
                {pq['id']}. {pq['pergunta']}
            </div>
            <div style="color:#22D3EE;font-size:0.78rem">
                &#9654;&nbsp; {pq['motivo']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        resp = st.text_area("Resposta", key=f"resp_{pq['id']}", height=70,
                            label_visibility="collapsed",
                            placeholder="Digite a resposta aqui...")
        respostas[pq["id"]] = resp or "(não informado)"
        st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("← Voltar"):
            st.session_state.step = 2
            st.rerun()
    with col_nav[1]:
        if st.button("Avançar →"):
            st.session_state.dados["respostas"] = respostas
            st.session_state.step = 4
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4 — GUIA PROBATÓRIO
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 4:
    tema = st.session_state.dados["tema"]
    st.markdown(f'<div class="section-title">04 — GUIA PROBATÓRIO</div>', unsafe_allow_html=True)

    st.markdown("**Provas essenciais — marque o que o cliente já tem:**")
    provas_tem = {}
    for prova in tema.get("provas_essenciais", []):
        provas_tem[prova] = st.checkbox(prova, key=f"prova_{prova}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Como obter as provas que faltam:**")
    for prova, como in tema.get("provas_como_obter", {}).items():
        tem = provas_tem.get(prova, False)
        if not tem:
            st.markdown(f"📋 **{prova}**  \n→ {como}")

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
            st.session_state.step = 3
            st.rerun()
    with col_nav[1]:
        if st.button("⚡ Gerar Análise e Documentos"):
            st.session_state.dados["provas_tem"] = provas_tem
            st.session_state.dados["honor"] = {
                "fixo": fixo, "exito": exito,
                "parcelas": parcelas,
                "referencia": tema.get("valor_referencia", "A calcular")
            }
            st.session_state.step = 5
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5 — RESULTADO FINAL
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == 5:
    import sys
    sys.path.insert(0, str(PASTA))
    from modo_consultoria_v2 import gerar_todos_documentos

    d = st.session_state.dados
    cliente   = d["cliente"]
    tema      = d["tema"]
    descricao = d["descricao"]
    datas     = d["datas"]
    respostas = d["respostas"]
    provas    = d["provas_tem"]
    honor     = d["honor"]

    prob = calcular_prob(tema, provas)
    tem_count = sum(1 for v in provas.values() if v)
    total = len(provas)

    if prob >= 75:   cor_prob, bg_prob, txt_prob, emoji_prob = "#34D399", "#022C22", "PRONTO", "✅"
    elif prob >= 55: cor_prob, bg_prob, txt_prob, emoji_prob = "#FCD34D", "#1C1007", "PARCIAL", "⚠️"
    else:            cor_prob, bg_prob, txt_prob, emoji_prob = "#F87171", "#1F0A0A", "PREMATURO", "❌"

    # Gera documentos apenas uma vez — salva pasta no session_state
    if "pasta_cliente" not in st.session_state:
        with st.spinner("Analisando caso e gerando documentos..."):
            slug = cliente["nome"].split()[0].lower()
            ts_pasta = datetime.now().strftime("%Y%m%d_%H%M")
            pasta_cliente = CLIENTES_DIR / f"{slug}_{ts_pasta}"
            pasta_cliente.mkdir(exist_ok=True)
            prob_dict = {"percentual": prob, "nivel": txt_prob, "tem": tem_count, "total": total}
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
            <div style="background:{bg_prob};border:2px solid {cor_prob};border-radius:16px;
                        padding:24px;text-align:center">
                <div style="font-size:0.7rem;letter-spacing:3px;color:#94A3B8;text-transform:uppercase;margin-bottom:8px">
                    Prontidão para Protocolar
                </div>
                <div style="font-size:3.5rem;font-weight:900;color:{cor_prob};line-height:1">{prob}%</div>
                <div style="font-size:1rem;font-weight:700;color:{cor_prob};margin-top:6px">
                    {emoji_prob} {txt_prob}
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

        col_d1, col_d2 = st.columns(2)
        for i, (fname, icon, label, bg, cor) in enumerate(docs_info):
            fpath = pasta_cliente / fname
            col = col_d1 if i % 2 == 0 else col_d2
            with col:
                if fpath.exists():
                    st.markdown(f"""
                    <div style="background:{bg};border:1px solid {cor}30;border-left:4px solid {cor};
                                border-radius:10px;padding:14px 18px;margin-bottom:4px;
                                display:flex;align-items:center;gap:12px;">
                        <span style="font-size:1.4rem">{icon}</span>
                        <div>
                            <div style="font-weight:700;color:#E2E8F0;font-size:0.9rem">{label}</div>
                            <div style="color:#16A34A;font-size:0.75rem;font-weight:600">✓ Gerado</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    mime = ("application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            if fname.endswith(".docx") else "text/plain")
                    st.download_button(
                        label="⬇️ Baixar",
                        data=fpath.read_bytes(),
                        file_name=fname,
                        mime=mime,
                        key=f"dl_{fname}",
                        use_container_width=True,
                    )
                    st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

        # ── PASTA DO CLIENTE ──────────────────────────────────────────────────
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

        import platform, subprocess
        if platform.system() == "Windows":
            if st.button("📂 Abrir pasta no Windows Explorer"):
                subprocess.Popen(f'explorer "{pasta_cliente}"')

        # ── ORIENTAÇÕES AO CLIENTE ────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">ORIENTAÇÕES AO CLIENTE</div>', unsafe_allow_html=True)
        oris = tema.get("orientacao_cliente", [])
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
        provas_faltam = [p for p, tem in provas.items() if not tem]
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
            st.session_state.step = 1
            st.session_state.dados = {}
            st.rerun()
