import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import io

st.set_page_config(
    page_title="DieselDeck – Truck Dashboard",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── TOP BAR ── */
.fiq-topbar {
    background: #1A1A2E;
    padding: 14px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
}
.fiq-logo {
    color: #E65C00;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.04em;
}
.fiq-fleet-sub {
    color: #9E9E9E;
    font-size: 12px;
    margin-top: 2px;
}
.fiq-score-bubble {
    background: #E65C00;
    color: white;
    border-radius: 10px;
    padding: 8px 18px;
    text-align: center;
}
.fiq-score-num {
    font-size: 24px;
    font-weight: 800;
    line-height: 1;
}
.fiq-score-lbl {
    font-size: 10px;
    opacity: 0.85;
    margin-top: 2px;
}

/* ── UPLOAD ZONE ── */
.fiq-upload-zone {
    background: #FFF5EF;
    border: 2px dashed #E65C00;
    border-radius: 14px;
    padding: 32px 24px;
    text-align: center;
    margin: 24px 28px;
}
.fiq-upload-title {
    font-size: 18px;
    font-weight: 700;
    color: #1A1A2E;
    margin-bottom: 6px;
}
.fiq-upload-sub {
    font-size: 13px;
    color: #888;
    margin-bottom: 16px;
}

/* ── STAT CARDS ── */
.fiq-stat-card {
    background: white;
    border: 1.5px solid #F0EDE8;
    border-radius: 12px;
    padding: 14px 16px;
}
.fiq-stat-label {
    font-size: 11px;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}
.fiq-stat-value {
    font-size: 26px;
    font-weight: 800;
    color: #1A1A2E;
    line-height: 1.1;
}
.fiq-stat-meaning {
    font-size: 11px;
    color: #999;
    margin-top: 4px;
}

/* ── TRUCK CARDS ── */
.fiq-truck-card {
    background: white;
    border: 1.5px solid #F0EDE8;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 10px;
    border-left: 5px solid #ccc;
}
.fiq-truck-card.on-route   { border-left-color: #00875A; }
.fiq-truck-card.alert      { border-left-color: #E65C00; }
.fiq-truck-card.at-depot   { border-left-color: #378ADD; }
.fiq-truck-card.loss       { border-left-color: #CC0000; }
.fiq-truck-card.delivered  { border-left-color: #7F77DD; }
.fiq-truck-num  { font-size: 15px; font-weight: 700; color: #1A1A2E; }
.fiq-truck-info { font-size: 12px; color: #666; margin-top: 3px; }

/* ── BADGES ── */
.fiq-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
}
.badge-green    { background: #EAF3DE; color: #27500A; }
.badge-orange   { background: #FAEEDA; color: #633806; }
.badge-red      { background: #FCEBEB; color: #791F1F; }
.badge-blue     { background: #E6F1FB; color: #0C447C; }
.badge-purple   { background: #EEEDFE; color: #3C3489; }
.badge-gray     { background: #F1EFE8; color: #444441; }

/* ── GOODS PILLS ── */
.fiq-goods-pill {
    display: inline-block;
    background: #E6F1FB;
    color: #0C447C;
    border-radius: 14px;
    padding: 2px 10px;
    font-size: 11px;
    margin: 2px 3px 2px 0;
}

/* ── ACTION CARDS ── */
.fiq-action-crit {
    background: #FFF0F0;
    border-left: 4px solid #CC0000;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 7px;
    font-size: 13px;
}
.fiq-action-warn {
    background: #FFF5EF;
    border-left: 4px solid #E65C00;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 7px;
    font-size: 13px;
}
.fiq-action-good {
    background: #F0FFF5;
    border-left: 4px solid #00875A;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 7px;
    font-size: 13px;
}

/* ── SECTION HEADING ── */
.fiq-section-head {
    font-size: 12px;
    font-weight: 700;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin: 20px 0 10px;
    padding-bottom: 6px;
    border-bottom: 1.5px solid #F0EDE8;
}

/* ── EDIT PANEL ── */
.fiq-edit-panel {
    background: #FAFAFA;
    border: 1.5px solid #E65C00;
    border-radius: 12px;
    padding: 16px 18px;
    margin-top: 10px;
    margin-bottom: 14px;
}

/* ── BUTTONS ── */
.stButton > button {
    background: #E65C00 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    width: 100%;
}
.stButton > button:hover {
    background: #CC5200 !important;
}
[data-testid="stDownloadButton"] > button {
    background: #00875A !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    width: 100%;
}
div[data-testid="stRadio"] > label:first-child {
    display: none;
}
</style>
""", unsafe_allow_html=True)

BENCHMARK_CPK = 28.5
DIESEL_DEFAULT = 93.52
TYRE_PER_KM = 3.20
MAINTENANCE_PKM = 1.80
DRIVER_MONTHLY = 18000
KM_PER_DAY = 400
APP_NAME = "DieselDeck"
SERVICE_INTERVAL_KM = 10000

VALID_STATUSES = [
    'On route', 'At depot', 'Fuel alert',
    'Delivered', 'Loss-making', 'Maintenance',
]

GOODS_OPTIONS = [
    'Marble', 'Onions', 'Cement', 'Cotton', 'Textiles',
    'Steel', 'Salt', 'Tiles', 'Fruits', 'Chemicals',
    'Electronics', 'Food grains', 'Furniture', 'Auto parts',
    'Medicine', 'Sand & gravel', 'Fertilizers', 'Other',
]

INDIAN_CITIES = [
    'Jodhpur', 'Jaipur', 'Delhi', 'Mumbai', 'Ahmedabad',
    'Surat', 'Pune', 'Indore', 'Agra', 'Nagpur', 'Bhopal',
    'Vadodara', 'Rajkot', 'Udaipur', 'Kota', 'Ajmer',
    'Bikaner', 'Alwar', 'Sikar', 'Hyderabad', 'Bengaluru',
    'Chennai', 'Kolkata', 'Lucknow', 'Kanpur', 'Srinagar',
    'Amritsar', 'Ludhiana', 'Varanasi', 'Patna',
]


def clean_html(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def compute_cost(km, fuel_litres, toll, diesel_price):
    km = float(km or 0)
    fuel_litres = float(fuel_litres or 0)
    toll = float(toll or 0)
    fuel_cost = fuel_litres * diesel_price
    driver_cost = DRIVER_MONTHLY / 26 * max(1, km // KM_PER_DAY)
    tyre_cost = km * TYRE_PER_KM
    maint_cost = km * MAINTENANCE_PKM
    total = fuel_cost + driver_cost + tyre_cost + maint_cost + toll
    return round(total, 0), round(total / km, 1) if km > 0 else 0


def fleet_health(df):
    if df.empty:
        return 50
    score = 100
    avg_cpk = df['cost_per_km'].mean() if 'cost_per_km' in df.columns else 30
    if avg_cpk > 35:
        score -= 20
    elif avg_cpk > 31:
        score -= 10
    if 'fuel_efficiency' in df.columns:
        avg_eff = df['fuel_efficiency'].replace([np.inf, -np.inf], np.nan).mean()
        if avg_eff < 3.5:
            score -= 15
        elif avg_eff < 4.0:
            score -= 7
    if 'profit_status' in df.columns:
        loss_pct = (df['profit_status'] == 'Loss-making').mean()
        score -= int(loss_pct * 30)
    return max(0, min(100, int(score)))


def status_class(s):
    return {
        'On route': 'on-route',
        'At depot': 'at-depot',
        'Fuel alert': 'alert',
        'Loss-making': 'loss',
        'Delivered': 'delivered',
        'Maintenance': 'alert',
    }.get(s, 'at-depot')


def status_badge(s):
    mapping = {
        'On route': ('badge-green', '● On route'),
        'At depot': ('badge-blue', '🅿 At depot'),
        'Fuel alert': ('badge-orange', '⛽ Fuel alert'),
        'Loss-making': ('badge-red', '📉 Loss-making'),
        'Delivered': ('badge-purple', '✔ Delivered'),
        'Maintenance': ('badge-orange', '🔧 Maintenance'),
    }
    cls, txt = mapping.get(s, ('badge-gray', s))
    return f'<span class="fiq-badge {cls}">{txt}</span>'


def status_text(s):
    return {
        'On route': 'On route',
        'At depot': 'At depot',
        'Fuel alert': 'Fuel alert',
        'Loss-making': 'Loss-making',
        'Delivered': 'Delivered',
        'Maintenance': 'Maintenance',
    }.get(s, str(s))


def status_callout(status, label):
    if status == 'On route':
        st.success(label)
    elif status in ['Fuel alert', 'Loss-making', 'Maintenance']:
        st.warning(label)
    elif status == 'Delivered':
        st.info(label)
    else:
        st.info(label)


def cpk_color(v):
    if v <= 28.5:
        return '#00875A'
    if v <= 35:
        return '#E65C00'
    return '#CC0000'


def build_support_tables(trips, live):
    trucks = live['truck_no'].dropna().unique().tolist() if not live.empty else trips['truck_no'].dropna().unique().tolist()
    today = datetime.now().date()
    doc_rows = []
    service_rows = []
    payment_rows = []
    settlement_rows = []
    for i, truck in enumerate(trucks):
        tdf = trips[trips['truck_no'] == truck]
        total_km = int(tdf['km_driven'].sum()) if not tdf.empty else 0
        doc_rows.append({
            'truck_no': truck,
            'insurance_expiry': today + timedelta(days=[12, 28, 46, 75, 110, 8, 65, 140][i % 8]),
            'permit_expiry': today + timedelta(days=[55, 18, 96, 21, 180, 36, 12, 70][i % 8]),
            'pollution_expiry': today + timedelta(days=[7, 33, 58, 90, 15, 120, 26, 44][i % 8]),
            'fitness_expiry': today + timedelta(days=[82, 17, 155, 43, 22, 68, 98, 9][i % 8]),
        })
        last_service = max(0, total_km - [3200, 7600, 9800, 11200, 4500, 8900, 6100, 10100][i % 8])
        km_since = max(0, total_km - last_service)
        service_rows.append({
            'truck_no': truck,
            'current_km': total_km,
            'last_service_km': last_service,
            'km_since_service': km_since,
            'km_to_service': SERVICE_INTERVAL_KM - km_since,
            'priority': 'Overdue' if km_since >= SERVICE_INTERVAL_KM else 'Due soon' if km_since >= 8500 else 'OK',
        })
        trip = tdf.iloc[-1] if not tdf.empty else {}
        revenue = float(trip.get('revenue', 0) or 0)
        paid = i % 4 == 0
        payment_rows.append({
            'customer': f"{str(trip.get('destination', 'Jaipur'))} Freight Co.",
            'truck_no': truck,
            'invoice_amount': round(revenue, 0),
            'paid_status': 'Paid' if paid else 'Pending',
            'days_pending': 0 if paid else [6, 14, 22, 39, 9, 31, 4, 18][i % 8],
        })
        advance = [3000, 5000, 2500, 6000, 4500, 3500, 7000, 4000][i % 8]
        toll = float(trip.get('toll_charges', 0) or 0)
        fuel_cash = float(trip.get('fuel_litres', 0) or 0) * DIESEL_DEFAULT
        unloading = [700, 950, 500, 1200, 650, 850, 1100, 750][i % 8]
        settlement_rows.append({
            'truck_no': truck,
            'driver': str(trip.get('driver_name', 'Unknown')),
            'advance_paid': advance,
            'diesel_cash': round(fuel_cash, 0),
            'toll_paid': round(toll, 0),
            'unloading': unloading,
            'balance_due': round(advance - toll - unloading, 0),
        })
    return pd.DataFrame(doc_rows), pd.DataFrame(service_rows), pd.DataFrame(payment_rows), pd.DataFrame(settlement_rows)


def enrich_trip_analysis(df):
    enriched = df.copy()
    for col in ['km_driven', 'fuel_litres', 'toll_charges', 'freight_rate', 'load_tonnes']:
        if col in enriched.columns:
            enriched[col] = pd.to_numeric(enriched[col], errors='coerce').fillna(0)
    costs = enriched.apply(
        lambda r: compute_cost(
            r.get('km_driven', 0),
            r.get('fuel_litres', 0),
            r.get('toll_charges', 0),
            st.session_state.get('diesel_price', DIESEL_DEFAULT),
        ),
        axis=1,
    )
    enriched['total_cost'] = costs.apply(lambda x: x[0])
    enriched['cost_per_km'] = costs.apply(lambda x: x[1])
    enriched['revenue'] = (enriched['freight_rate'] * enriched['load_tonnes']).round(0)
    enriched['profit_status'] = enriched.apply(
        lambda r: 'Profitable'
        if r['revenue'] > r['total_cost'] * 1.15
        else 'Break-even'
        if r['revenue'] > r['total_cost']
        else 'Loss-making',
        axis=1,
    )
    enriched['fuel_efficiency'] = (
        enriched['km_driven'] / enriched['fuel_litres'].replace(0, np.nan)
    ).round(2).fillna(0)
    expected_fuel = enriched['km_driven'] / 4.2
    enriched['expected_fuel_litres'] = expected_fuel.round(1)
    enriched['fuel_variance_litres'] = (enriched['fuel_litres'] - expected_fuel).round(1)
    enriched['fuel_variance_pct'] = np.where(expected_fuel > 0, enriched['fuel_variance_litres'] / expected_fuel * 100, 0).round(1)
    enriched['fuel_risk'] = np.select(
        [enriched['fuel_variance_pct'] > 25, enriched['fuel_variance_pct'] > 12],
        ['High risk', 'Watch'],
        default='Normal'
    )
    return enriched


def make_report_html(df, live_df, docs_df, payments_df, service_df, fleet_name, health, diesel):
    avg_cpk = df['cost_per_km'].mean() if not df.empty else 0
    revenue = df['revenue'].sum() if not df.empty else 0
    cost = df['total_cost'].sum() if 'total_cost' in df.columns else 0
    pending = payments_df.loc[payments_df['paid_status'] == 'Pending', 'invoice_amount'].sum() if not payments_df.empty else 0
    overdue_docs = 0
    if not docs_df.empty:
        today = pd.Timestamp(datetime.now().date())
        date_cols = [c for c in docs_df.columns if c.endswith('_expiry')]
        overdue_docs = int((docs_df[date_cols].apply(pd.to_datetime) <= today + pd.Timedelta(days=30)).sum().sum())
    urgent_service = int(service_df['priority'].isin(['Overdue', 'Due soon']).sum()) if not service_df.empty else 0
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{fleet_name} Fleet Report</title>
<style>body{{font-family:Arial,sans-serif;margin:32px;color:#1A1A2E}}h1{{color:#E65C00}}.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}}.card{{border:1px solid #ddd;border-left:5px solid #E65C00;border-radius:8px;padding:14px}}table{{border-collapse:collapse;width:100%;margin-top:18px}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}th{{background:#FFF5EF}}</style>
</head><body>
<h1>{APP_NAME} Owner Report</h1>
<p><b>Fleet:</b> {fleet_name} &nbsp; <b>Date:</b> {datetime.now().strftime('%d %b %Y')} &nbsp; <b>Diesel:</b> ₹{diesel}/L</p>
<div class="grid">
<div class="card"><b>Fleet Health</b><br><span style="font-size:28px">{health}/100</span></div>
<div class="card"><b>Average Cost/KM</b><br><span style="font-size:28px">₹{avg_cpk:.1f}</span></div>
<div class="card"><b>Monthly Revenue</b><br><span style="font-size:28px">₹{revenue:,.0f}</span></div>
<div class="card"><b>Estimated Profit</b><br><span style="font-size:28px">₹{revenue - cost:,.0f}</span></div>
<div class="card"><b>Payment Pending</b><br><span style="font-size:28px">₹{pending:,.0f}</span></div>
<div class="card"><b>Action Alerts</b><br>{overdue_docs} document alerts · {urgent_service} service alerts</div>
</div>
<h2>Top Trucks</h2>
{df.groupby('truck_no')[['km_driven','revenue']].sum().sort_values('revenue', ascending=False).head(8).to_html()}
<p style="margin-top:28px;color:#666">Use browser Print → Save as PDF for a clean PDF copy.</p>
</body></html>"""


def wa_summary(df, live_df, fleet_name, health, diesel):
    avg_cpk = df['cost_per_km'].mean() if 'cost_per_km' in df.columns else 0
    total_km = df['km_driven'].sum() if 'km_driven' in df.columns else 0
    active = (live_df['status'] == 'On route').sum() if not live_df.empty else 0
    alerts = live_df['status'].isin(['Fuel alert', 'Loss-making']).sum() if not live_df.empty else 0
    loss_ct = (df['profit_status'] == 'Loss-making').sum() if 'profit_status' in df.columns else 0
    today = datetime.now().strftime('%d %b %Y')
    return f"""🚛 *{APP_NAME} Report — {today}*
Fleet: *{fleet_name}*
Health Score: *{health}/100*
━━━━━━━━━━━━━
🟢 Active trucks: {active}/{len(live_df)}
⛽ Diesel: ₹{diesel}/L
💰 Avg cost/km: ₹{avg_cpk:.1f} (target ₹{BENCHMARK_CPK})
📏 Total KM: {total_km:,.0f}
{"⚠️ Alerts: " + str(alerts) + " truck(s)" if alerts > 0 else "✅ No fuel alerts"}
{"📉 Loss trips: " + str(loss_ct) if loss_ct > 0 else "✅ All trips profitable or break-even"}
━━━━━━━━━━━━━
_Powered by {APP_NAME}_"""


def split_goods(df):
    goods = df[['goods', 'load_tonnes']].copy()
    goods['goods'] = goods['goods'].fillna('Unknown').astype(str).str.split(',')
    goods = goods.explode('goods')
    goods['goods'] = goods['goods'].str.strip().replace('', 'Unknown')
    return goods


def make_sample_data():
    import random
    random.seed(42)

    trucks = [
        'RJ14 GA 4421', 'RJ14 CH 8832', 'RJ14 AB 1104',
        'RJ14 KP 7743', 'RJ14 ZX 2291', 'RJ14 MN 5512',
        'RJ14 DL 9901', 'RJ14 SS 3367',
    ]
    drivers = [
        'Ramesh Kumar', 'Suresh Singh', 'Mohan Lal', 'Raju Yadav',
        'Bharat Sharma', 'Dinesh Patel', 'Vikram Rathore', 'Ajay Meena',
    ]
    route_pool = [
        ('Jodhpur', 'Mumbai', 1200), ('Jodhpur', 'Ahmedabad', 320),
        ('Jaipur', 'Delhi', 280), ('Jodhpur', 'Indore', 520),
        ('Agra', 'Pune', 980), ('Jodhpur', 'Surat', 680),
        ('Jaipur', 'Mumbai', 1150), ('Jodhpur', 'Nagpur', 820),
    ]
    statuses = [
        'On route', 'On route', 'At depot',
        'On route', 'Fuel alert', 'Delivered',
        'Loss-making', 'Maintenance',
    ]
    goods_pool = GOODS_OPTIONS[:12]
    today = datetime.now()

    rows = []
    for _ in range(60):
        r = random.choice(route_pool)
        g1 = random.choice(goods_pool)
        g2 = random.choice(goods_pool) if random.random() > 0.55 else ''
        truck = random.choice(trucks)
        driver = random.choice(drivers)
        km = r[2] + random.randint(-60, 90)
        load = round(random.uniform(8, 22), 1)
        fuel = km / random.uniform(3.2, 5.1)
        toll = km * random.uniform(1.8, 2.5)
        total, cpk = compute_cost(km, fuel, toll, DIESEL_DEFAULT)
        trip_dt = today - timedelta(days=random.randint(0, 30))
        freight = random.uniform(1800, 2800)
        revenue = freight * load
        rpk = revenue / km
        if rpk > cpk * 1.15:
            ps = 'Profitable'
        elif rpk > cpk:
            ps = 'Break-even'
        else:
            ps = 'Loss-making'
        goods_str = g1
        if g2 and g2 != g1:
            goods_str += ', ' + g2
        rows.append({
            'trip_date': trip_dt.strftime('%Y-%m-%d'),
            'truck_no': truck,
            'driver_name': driver,
            'origin': r[0],
            'destination': r[1],
            'km_driven': km,
            'load_tonnes': load,
            'goods': goods_str,
            'fuel_litres': round(fuel, 1),
            'toll_charges': round(toll, 0),
            'freight_rate': round(freight, 0),
            'total_cost': total,
            'cost_per_km': cpk,
            'revenue': round(revenue, 0),
            'profit_status': ps,
            'fuel_efficiency': round(km / fuel, 2),
            'notes': '',
        })
    trips = pd.DataFrame(rows)

    live_rows = []
    for i, truck in enumerate(trucks):
        r = route_pool[i % len(route_pool)]
        km_done = random.randint(80, r[2] - 40)
        fuel_l = km_done / random.uniform(3.5, 4.8)
        _, cpk_l = compute_cost(km_done, fuel_l, km_done * 2.1, DIESEL_DEFAULT)
        live_rows.append({
            'truck_no': truck,
            'driver': drivers[i],
            'status': statuses[i],
            'origin': r[0],
            'destination': r[1],
            'km_done': km_done,
            'km_total': r[2],
            'cost_per_km': cpk_l,
            'goods': random.choice(goods_pool),
            'load_tonnes': round(random.uniform(12, 22), 1),
            'notes': '',
        })
    live = pd.DataFrame(live_rows)
    return trips, live


def load_uploaded_file(uploaded_file, diesel_price):
    import difflib

    if uploaded_file.name.endswith('.csv'):
        raw = pd.read_csv(uploaded_file)
    else:
        raw = pd.read_excel(uploaded_file)

    raw.dropna(how='all', inplace=True)
    raw.dropna(axis=1, how='all', inplace=True)
    raw.columns = raw.columns.str.strip()

    canonical = {
        'trip_date': ['date', 'trip date', 'tripdate', 'journey date', 'travel date'],
        'truck_no': ['truck', 'truck no', 'vehicle', 'vehicle no', 'truck number', 'lorry'],
        'driver_name': ['driver', 'driver name', 'driver_name'],
        'origin': ['from', 'origin', 'source', 'from city', 'departure'],
        'destination': ['to', 'destination', 'dest', 'to city', 'arrival'],
        'km_driven': ['km', 'distance', 'kms', 'kilometers', 'km driven', 'total km'],
        'load_tonnes': ['load', 'weight', 'tonnes', 'ton', 'goods weight', 'cargo weight'],
        'goods': ['goods', 'cargo', 'material', 'item', 'product', 'commodity'],
        'fuel_litres': ['fuel', 'fuel litres', 'diesel', 'fuel consumed', 'litres'],
        'toll_charges': ['toll', 'tolls', 'toll charges', 'toll tax'],
        'freight_rate': ['freight', 'rate', 'freight rate', 'price per tonne'],
        'notes': ['notes', 'remarks', 'comment', 'description'],
    }

    col_map = {}
    raw_lower = {c.lower().strip(): c for c in raw.columns}
    used_cols = set()

    for canon, aliases in canonical.items():
        matched = None
        for alias in aliases:
            close = difflib.get_close_matches(alias, raw_lower.keys(), n=1, cutoff=0.7)
            if close and raw_lower[close[0]] not in used_cols:
                matched = raw_lower[close[0]]
                break
        if matched:
            col_map[matched] = canon
            used_cols.add(matched)

    required = ['trip_date', 'truck_no', 'driver_name', 'origin', 'destination', 'km_driven', 'load_tonnes']
    mapped_canons = set(col_map.values())
    for canon in required:
        if canon not in mapped_canons:
            st.warning(f"Could not auto-detect required column: {canon}")
            choice = st.selectbox(
                f"Map '{canon}' manually",
                ["-- Missing / use default --"] + list(raw.columns),
                key=f"map_{canon}_{uploaded_file.name}",
            )
            if choice != "-- Missing / use default --":
                col_map[choice] = canon

    df = raw.rename(columns=col_map)
    defaults = {
        'trip_date': datetime.now().strftime('%Y-%m-%d'),
        'truck_no': 'Unknown Truck',
        'driver_name': 'Unknown',
        'origin': 'Jodhpur',
        'destination': 'Jaipur',
        'km_driven': 0,
        'load_tonnes': 0,
        'notes': '',
        'toll_charges': 0,
        'freight_rate': 2000,
        'goods': 'Unknown',
        'fuel_litres': None,
    }
    for col, default in defaults.items():
        if col not in df.columns:
            df[col] = default

    for col in ['km_driven', 'load_tonnes', 'fuel_litres', 'toll_charges', 'freight_rate']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    df['trip_date'] = pd.to_datetime(df['trip_date'], errors='coerce', dayfirst=True)
    df['trip_date'] = df['trip_date'].fillna(pd.Timestamp.today()).dt.strftime('%Y-%m-%d')
    df['fuel_litres'] = df.apply(
        lambda r: r['km_driven'] / 4.2 if r['fuel_litres'] <= 0 and r['km_driven'] > 0 else r['fuel_litres'],
        axis=1,
    )
    df['fuel_efficiency'] = (df['km_driven'] / df['fuel_litres'].replace(0, np.nan)).round(2).fillna(0)

    if 'total_cost' not in df.columns or 'cost_per_km' not in df.columns:
        costs = df.apply(
            lambda r: compute_cost(
                r.get('km_driven', 0),
                r.get('fuel_litres', r.get('km_driven', 0) / 4.2),
                r.get('toll_charges', 0),
                diesel_price,
            ),
            axis=1,
        )
        df['total_cost'] = costs.apply(lambda x: x[0])
        df['cost_per_km'] = costs.apply(lambda x: x[1])

    if 'revenue' not in df.columns:
        df['revenue'] = (df['freight_rate'] * df['load_tonnes']).round(0)

    if 'profit_status' not in df.columns:
        df['profit_status'] = df.apply(
            lambda r: 'Profitable'
            if r['revenue'] > r['total_cost'] * 1.15
            else 'Break-even'
            if r['revenue'] > r['total_cost']
            else 'Loss-making',
            axis=1,
        )

    live_rows = []
    for truck in df['truck_no'].dropna().unique():
        sub = df[df['truck_no'] == truck].sort_values('trip_date', ascending=False)
        latest = sub.iloc[0]
        live_rows.append({
            'truck_no': truck,
            'driver': latest.get('driver_name', 'Unknown'),
            'status': 'On route',
            'origin': latest.get('origin', ''),
            'destination': latest.get('destination', ''),
            'km_done': int(latest.get('km_driven', 0) * 0.6),
            'km_total': int(latest.get('km_driven', 0)),
            'cost_per_km': latest.get('cost_per_km', 30),
            'goods': latest.get('goods', ''),
            'load_tonnes': latest.get('load_tonnes', 0),
            'notes': '',
        })
    live = pd.DataFrame(live_rows)
    return df, live


for key, value in {
    'trips_df': pd.DataFrame(),
    'live_df': pd.DataFrame(),
    'docs_df': pd.DataFrame(),
    'payments_df': pd.DataFrame(),
    'service_df': pd.DataFrame(),
    'settlement_df': pd.DataFrame(),
    'fleet_name': 'My Fleet',
    'diesel_price': DIESEL_DEFAULT,
    'show_add': False,
    'edit_truck': None,
    'data_loaded': False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

df = st.session_state['trips_df']
live_df = st.session_state['live_df']

if not st.session_state['data_loaded']:
    st.markdown("""
    <div class="fiq-topbar">
      <div>
        <div class="fiq-logo">⛽ DieselDeck</div>
        <div class="fiq-fleet-sub">
          Fleet Cost Intelligence · India
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fiq-upload-zone">
      <div class="fiq-upload-title">Upload your trip sheet</div>
      <div class="fiq-upload-sub">
        CSV or Excel · Any column names · Auto-detected
      </div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        uploaded_file = st.file_uploader("Choose your trip log file", type=["csv", "xlsx", "xls"])
        if uploaded_file is not None:
            df_loaded, live_loaded = load_uploaded_file(uploaded_file, st.session_state['diesel_price'])
            df_loaded = enrich_trip_analysis(df_loaded)
            docs_df, service_df, payments_df, settlement_df = build_support_tables(df_loaded, live_loaded)
            st.session_state['trips_df'] = df_loaded
            st.session_state['live_df'] = live_loaded
            st.session_state['docs_df'] = docs_df
            st.session_state['service_df'] = service_df
            st.session_state['payments_df'] = payments_df
            st.session_state['settlement_df'] = settlement_df
            st.session_state['data_loaded'] = True
            st.rerun()

        st.markdown("**— or —**")
        if st.button("🚛 Try with sample data", use_container_width=True):
            trips, live = make_sample_data()
            trips = enrich_trip_analysis(trips)
            docs_df, service_df, payments_df, settlement_df = build_support_tables(trips, live)
            st.session_state['trips_df'] = trips
            st.session_state['live_df'] = live
            st.session_state['docs_df'] = docs_df
            st.session_state['service_df'] = service_df
            st.session_state['payments_df'] = payments_df
            st.session_state['settlement_df'] = settlement_df
            st.session_state['data_loaded'] = True
            st.rerun()

        with st.expander("What columns does my sheet need?"):
            st.dataframe(pd.DataFrame({
                "Column Name": [
                    "trip_date", "truck_no", "driver_name", "origin", "destination",
                    "km_driven", "load_tonnes", "goods", "fuel_litres",
                    "toll_charges", "freight_rate", "notes",
                ],
                "Examples": [
                    "01-05-2025, 1 May 2025", "RJ14 GA 4421, MH 12 AB 1234",
                    "Ramesh Kumar", "Jodhpur, Jaipur, Delhi", "Mumbai, Pune, Ahmedabad",
                    "450, 1200", "15.5, 22", "Marble, Onions, Cement",
                    "180, 320", "850, 2400", "2000, 1800 (₹ per tonne)", "Any remarks",
                ],
            }), use_container_width=True, hide_index=True)
            st.caption("Any column name close to these will be auto-matched.")
    st.stop()

df = st.session_state['trips_df']
live_df = st.session_state['live_df']
docs_df = st.session_state['docs_df']
payments_df = st.session_state['payments_df']
service_df = st.session_state['service_df']
settlement_df = st.session_state['settlement_df']
diesel = st.session_state['diesel_price']
fname = st.session_state['fleet_name']
if not df.empty and 'fuel_risk' not in df.columns:
    df = enrich_trip_analysis(df)
    st.session_state['trips_df'] = df
if not df.empty and (docs_df.empty or payments_df.empty or service_df.empty or settlement_df.empty):
    docs_df, service_df, payments_df, settlement_df = build_support_tables(df, live_df)
    st.session_state['docs_df'] = docs_df
    st.session_state['service_df'] = service_df
    st.session_state['payments_df'] = payments_df
    st.session_state['settlement_df'] = settlement_df
health = fleet_health(df)

st.markdown(f"""
<div class="fiq-topbar">
  <div>
    <div class="fiq-logo">⛽ DieselDeck</div>
    <div class="fiq-fleet-sub">
      {clean_html(fname)} ·
      {live_df['truck_no'].nunique() if not live_df.empty else 0}
      trucks · {datetime.now().strftime('%d %b %Y')}
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:14px">
    <div style="color:#9E9E9E;font-size:12px;text-align:right">
      Diesel today<br>
      <span style="color:#E65C00;font-weight:700;font-size:15px">
        ₹{diesel}/L
      </span>
    </div>
    <div class="fiq-score-bubble">
      <div class="fiq-score-num">{health}</div>
      <div class="fiq-score-lbl">Fleet score</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1.65, 1])

with left_col:
    st.markdown('<div style="padding:20px 10px 24px 28px">', unsafe_allow_html=True)

    stat_cols = st.columns(4)
    active = int((live_df['status'] == 'On route').sum()) if not live_df.empty else 0
    stopped = max(0, len(live_df) - active)
    avg_cpk = float(df['cost_per_km'].mean()) if not df.empty else 0.0
    cpk_delta = avg_cpk - BENCHMARK_CPK
    df_dates = pd.to_datetime(df['trip_date'], errors='coerce')
    now = datetime.now()
    month_df = df[(df_dates.dt.month == now.month) & (df_dates.dt.year == now.year)]
    km_month = month_df['km_driven'].sum() if not month_df.empty else df['km_driven'].sum()
    alert_count = int(live_df['status'].isin(['Fuel alert', 'Loss-making', 'Maintenance']).sum()) if not live_df.empty else 0
    stats = [
        ("Active trucks", active, "#00875A", f"{stopped} at depot or stopped"),
        ("Avg cost/km", f"₹{avg_cpk:.1f}", cpk_color(avg_cpk), f"₹{abs(cpk_delta):.1f} {'above' if cpk_delta >= 0 else 'below'} ₹28.5 benchmark"),
        ("KM this month", f"{km_month:,.0f}", "#1A1A2E", f"Across {df['truck_no'].nunique()} trucks"),
        ("Alerts", alert_count, "#CC0000" if alert_count > 0 else "#00875A", "trucks need attention" if alert_count > 0 else "All clear"),
    ]
    for col, (label, value, color, meaning) in zip(stat_cols, stats):
        col.markdown(f"""
        <div class="fiq-stat-card">
          <div class="fiq-stat-label">{label}</div>
          <div class="fiq-stat-value" style="color:{color}">
            {value}
          </div>
          <div class="fiq-stat-meaning">{meaning}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="fiq-section-head">📊 Dashboard Overview</div>', unsafe_allow_html=True)
    overview_a, overview_b = st.columns(2)
    with overview_a:
        route_df = df.copy()
        route_df['route'] = route_df['origin'].astype(str) + ' → ' + route_df['destination'].astype(str)
        route_cost = route_df.groupby('route', as_index=False)['cost_per_km'].mean().sort_values('cost_per_km').tail(8)
        fig_route = go.Figure(go.Bar(
            x=route_cost['cost_per_km'],
            y=route_cost['route'],
            orientation='h',
            marker_color=[cpk_color(v) for v in route_cost['cost_per_km']],
            text=[f"₹{v:.1f}" for v in route_cost['cost_per_km']],
            textposition='auto',
        ))
        fig_route.add_vline(x=BENCHMARK_CPK, line_dash="dash", line_color="#E65C00")
        fig_route.update_layout(
            title="Cost/km by route",
            height=280,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=0, r=20, t=40, b=0),
            xaxis=dict(title="", showgrid=False),
            yaxis=dict(title=""),
        )
        st.plotly_chart(fig_route, use_container_width=True, config={"displayModeBar": False})
    with overview_b:
        km_by_truck = df.groupby('truck_no', as_index=False)['km_driven'].sum().sort_values('km_driven', ascending=False)
        fig_km = go.Figure(go.Bar(
            x=km_by_truck['truck_no'],
            y=km_by_truck['km_driven'],
            marker_color="#378ADD",
            text=[f"{v:,.0f}" for v in km_by_truck['km_driven']],
            textposition='auto',
        ))
        fig_km.update_layout(
            title="KM run by truck",
            height=280,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=0, r=20, t=40, b=0),
            xaxis=dict(title=""),
            yaxis=dict(title="KM", showgrid=False),
        )
        st.plotly_chart(fig_km, use_container_width=True, config={"displayModeBar": False})

    st.markdown('<div class="fiq-section-head">📌 Business Dashboards</div>', unsafe_allow_html=True)
    dash1, dash2 = st.columns(2)
    with dash1:
        profit_df = df.copy()
        profit_df['profit'] = profit_df['revenue'] - profit_df['total_cost']
        profit_by_truck = profit_df.groupby('truck_no', as_index=False)['profit'].sum().sort_values('profit', ascending=False)
        fig_profit = go.Figure(go.Bar(
            x=profit_by_truck['truck_no'],
            y=profit_by_truck['profit'],
            marker_color=['#00875A' if v >= 0 else '#CC0000' for v in profit_by_truck['profit']],
            text=[f"₹{v/1000:.0f}K" for v in profit_by_truck['profit']],
            textposition='auto',
        ))
        fig_profit.update_layout(
            title="Profit by truck",
            height=260,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=0, r=20, t=40, b=0),
            xaxis=dict(title=""),
            yaxis=dict(title="Profit ₹", showgrid=False),
        )
        st.plotly_chart(fig_profit, use_container_width=True, config={"displayModeBar": False})
    with dash2:
        trend_df = df.copy()
        trend_df['trip_date_dt'] = pd.to_datetime(trend_df['trip_date'], errors='coerce')
        daily = trend_df.groupby('trip_date_dt', as_index=False).agg(revenue=('revenue', 'sum'), total_cost=('total_cost', 'sum')).sort_values('trip_date_dt')
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(x=daily['trip_date_dt'], y=daily['revenue'], mode='lines+markers', name='Revenue', line=dict(color='#00875A')))
        fig_trend.add_trace(go.Scatter(x=daily['trip_date_dt'], y=daily['total_cost'], mode='lines+markers', name='Cost', line=dict(color='#E65C00')))
        fig_trend.update_layout(
            title="Daily revenue vs cost",
            height=260,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=0, r=20, t=40, b=0),
            xaxis=dict(title=""),
            yaxis=dict(title="₹", showgrid=False),
        )
        st.plotly_chart(fig_trend, use_container_width=True, config={"displayModeBar": False})

    dash3, dash4 = st.columns(2)
    with dash3:
        pay = payments_df.copy()
        pay['aging_bucket'] = pd.cut(
            pay['days_pending'],
            bins=[-1, 7, 21, 45, 10000],
            labels=['0-7 days', '8-21 days', '22-45 days', '45+ days'],
        )
        aging = pay[pay['paid_status'] == 'Pending'].groupby('aging_bucket', observed=False)['invoice_amount'].sum().reset_index()
        fig_aging = go.Figure(go.Bar(
            x=aging['aging_bucket'].astype(str),
            y=aging['invoice_amount'],
            marker_color=['#00875A', '#E65C00', '#CC0000', '#791F1F'],
            text=[f"₹{v/1000:.0f}K" for v in aging['invoice_amount']],
            textposition='auto',
        ))
        fig_aging.update_layout(title="Pending payment aging", height=240, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=0, r=20, t=40, b=0), xaxis=dict(title=""), yaxis=dict(title="Pending ₹", showgrid=False))
        st.plotly_chart(fig_aging, use_container_width=True, config={"displayModeBar": False})
    with dash4:
        doc_dates = docs_df[[c for c in docs_df.columns if c.endswith('_expiry')]].apply(pd.to_datetime) if not docs_df.empty else pd.DataFrame()
        if not doc_dates.empty:
            days_left = doc_dates.sub(pd.Timestamp(datetime.now().date())).min(axis=1).dt.days
            doc_status = pd.Series(np.select([days_left < 0, days_left <= 30], ['Expired', 'Due soon'], default='OK')).value_counts().reset_index()
            doc_status.columns = ['status', 'count']
            fig_docs = go.Figure(go.Bar(
                x=doc_status['status'],
                y=doc_status['count'],
                marker_color=['#CC0000' if s == 'Expired' else '#E65C00' if s == 'Due soon' else '#00875A' for s in doc_status['status']],
                text=doc_status['count'],
                textposition='auto',
            ))
            fig_docs.update_layout(title="Document health", height=240, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=0, r=20, t=40, b=0), xaxis=dict(title=""), yaxis=dict(title="Trucks", showgrid=False))
            st.plotly_chart(fig_docs, use_container_width=True, config={"displayModeBar": False})

    st.markdown('<div class="fiq-section-head">🚛 Live Truck Status</div>', unsafe_allow_html=True)
    status_rank = {'Fuel alert': 0, 'Loss-making': 1, 'On route': 2}
    live_sorted = live_df.copy()
    live_sorted['_rank'] = live_sorted['status'].map(status_rank).fillna(3)
    live_sorted = live_sorted.sort_values(['_rank', 'truck_no'])

    for _, row in live_sorted.iterrows():
        truck_no = str(row['truck_no'])
        status = str(row.get('status', 'At depot'))
        origin = clean_html(row.get('origin', ''))
        destination = clean_html(row.get('destination', ''))
        driver = clean_html(row.get('driver', ''))
        goods = clean_html(row.get('goods', ''))
        notes = clean_html(row.get('notes', ''))
        km_done = int(row.get('km_done', 0) or 0)
        km_total = int(row.get('km_total', 0) or 0)
        cpk = float(row.get('cost_per_km', 0) or 0)
        prog_pct = int(km_done / km_total * 100) if km_total > 0 else 0
        prog_pct = max(0, min(100, prog_pct))

        with st.container(border=True):
            top_l, top_r = st.columns([3, 1])
            with top_l:
                st.markdown(f"**🚛 {truck_no}**")
                st.caption(f"{origin} → {destination} · {driver}")
                st.write(f"Goods: **{goods}**")
                if notes:
                    st.caption(f"Note: {notes}")
            with top_r:
                status_callout(status, status_text(status))
                st.metric("Cost/km", f"₹{cpk:.1f}")
                st.caption(f"{km_done} / {km_total} km")
            if status == 'On route':
                st.progress(prog_pct / 100, text=f"{prog_pct}% trip completed")

        if st.button(f"✏️ Edit {truck_no}", key=f"edit_{truck_no}"):
            st.session_state['edit_truck'] = truck_no

        if st.session_state['edit_truck'] == truck_no:
            st.info("Edit live truck details")
            new_status = st.selectbox(
                "Status", VALID_STATUSES,
                index=VALID_STATUSES.index(status) if status in VALID_STATUSES else 0,
                key=f"status_{truck_no}",
            )
            new_driver = st.text_input("Driver name", value=str(row.get('driver', '')), key=f"driver_{truck_no}")
            new_goods = st.text_input("Goods on truck", value=str(row.get('goods', '')), key=f"goods_{truck_no}", help="e.g. Marble 18T, Onions 4T")
            c1, c2 = st.columns(2)
            with c1:
                new_origin = st.selectbox("Current from", INDIAN_CITIES, index=INDIAN_CITIES.index(row['origin']) if row['origin'] in INDIAN_CITIES else 0, key=f"origin_{truck_no}")
            with c2:
                new_dest = st.selectbox("Going to", INDIAN_CITIES, index=INDIAN_CITIES.index(row['destination']) if row['destination'] in INDIAN_CITIES else 0, key=f"dest_{truck_no}")
            new_km_done = st.slider("KM completed so far", min_value=0, max_value=km_total if km_total > 0 else 2000, value=min(km_done, km_total if km_total > 0 else 2000), key=f"km_{truck_no}")
            new_notes = st.text_area("Notes / remarks", value=str(row.get('notes', '')), height=68, key=f"notes_{truck_no}", placeholder="e.g. Tyre puncture at Surat, delayed by 1 day")
            save_col, cancel_col = st.columns(2)
            with save_col:
                if st.button("💾 Save changes", key=f"save_{truck_no}"):
                    idx = st.session_state['live_df'][st.session_state['live_df']['truck_no'] == truck_no].index[0]
                    st.session_state['live_df'].at[idx, 'status'] = new_status
                    st.session_state['live_df'].at[idx, 'driver'] = new_driver
                    st.session_state['live_df'].at[idx, 'goods'] = new_goods
                    st.session_state['live_df'].at[idx, 'origin'] = new_origin
                    st.session_state['live_df'].at[idx, 'destination'] = new_dest
                    st.session_state['live_df'].at[idx, 'km_done'] = new_km_done
                    st.session_state['live_df'].at[idx, 'notes'] = new_notes
                    st.session_state['edit_truck'] = None
                    st.success(f"✅ {truck_no} updated!")
                    st.rerun()
            with cancel_col:
                if st.button("✖ Cancel", key=f"cancel_{truck_no}"):
                    st.session_state['edit_truck'] = None
                    st.rerun()

    if st.button("➕ Add New Trip"):
        st.session_state['show_add'] = True

    if st.session_state['show_add']:
        st.info("Add a new trip and see live cost/profit preview")
        a, b = st.columns(2)
        with a:
            truck_options = live_df['truck_no'].dropna().unique().tolist()
            truck_no = st.selectbox("Truck", truck_options if truck_options else ["RJ14 NEW 0001"], key="add_truck")
            default_driver = live_df.loc[live_df['truck_no'] == truck_no, 'driver'].iloc[0] if truck_no in live_df['truck_no'].values else ""
            driver = st.text_input("Driver", value=default_driver, key="add_driver")
            origin = st.selectbox("Origin", INDIAN_CITIES, key="add_origin")
            destination = st.selectbox("Destination", INDIAN_CITIES, index=3, key="add_destination")
            km = st.number_input("KM", min_value=50, max_value=3000, value=500, key="add_km")
        with b:
            goods_type = st.multiselect("Goods type", GOODS_OPTIONS, default=["Marble"], key="add_goods")
            load_tonnes = st.number_input("Load tonnes", min_value=1.0, max_value=35.0, value=15.0, key="add_load")
            fuel_litres = st.number_input("Fuel litres", min_value=0.0, value=round(km / 4.2, 1), key="add_fuel")
            toll_charges = st.number_input("Toll charges", min_value=0.0, value=round(km * 2.1, 0), key="add_toll")
            freight_rate = st.number_input("Freight rate (₹/tonne)", min_value=500, max_value=10000, value=2000, key="add_freight")
            trip_date = st.date_input("Trip date", value=datetime.now(), key="add_date")
            notes = st.text_area("Notes", height=60, key="add_notes")

        total_cost, cpk = compute_cost(km, fuel_litres, toll_charges, diesel)
        revenue = freight_rate * load_tonnes
        profit = revenue - total_cost
        preview_cols = st.columns(4)
        preview = [
            ("Cost/km", f"₹{cpk}", cpk_color(cpk)),
            ("Total cost", f"₹{total_cost:,.0f}", "#1A1A2E"),
            ("Revenue", f"₹{revenue:,.0f}", "#1A1A2E"),
            ("Profit" if profit >= 0 else "Loss", f"₹{abs(profit):,.0f}", "#00875A" if profit >= 0 else "#CC0000"),
        ]
        for col, (label, value, color) in zip(preview_cols, preview):
            col.markdown(f'<div class="fiq-stat-card"><div class="fiq-stat-label">{label}</div><div class="fiq-stat-value" style="color:{color}">{value}</div></div>', unsafe_allow_html=True)
        if profit > 0:
            st.success(f"✅ This trip earns ₹{profit:,.0f} profit (₹{profit/km:.1f}/km margin)")
        else:
            required_rate = (total_cost / load_tonnes * 1.15) if load_tonnes > 0 else 0
            st.error(f"❌ This trip LOSES ₹{abs(profit):,.0f} — raise freight to ₹{required_rate:.0f}/tonne to be profitable")

        sc, cc = st.columns(2)
        with sc:
            if st.button("💾 Save trip"):
                expected_fuel = km / 4.2
                fuel_variance_litres = fuel_litres - expected_fuel
                fuel_variance_pct = (fuel_variance_litres / expected_fuel * 100) if expected_fuel > 0 else 0
                new_row = {
                    'trip_date': trip_date.strftime('%Y-%m-%d'),
                    'truck_no': truck_no,
                    'driver_name': driver,
                    'origin': origin,
                    'destination': destination,
                    'km_driven': km,
                    'load_tonnes': load_tonnes,
                    'goods': ', '.join(goods_type) if goods_type else 'Other',
                    'fuel_litres': fuel_litres,
                    'toll_charges': toll_charges,
                    'freight_rate': freight_rate,
                    'total_cost': total_cost,
                    'cost_per_km': cpk,
                    'revenue': round(revenue, 0),
                    'profit_status': 'Profitable' if revenue > total_cost * 1.15 else 'Break-even' if revenue > total_cost else 'Loss-making',
                    'fuel_efficiency': round(km / fuel_litres, 2) if fuel_litres > 0 else 0,
                    'expected_fuel_litres': round(expected_fuel, 1),
                    'fuel_variance_litres': round(fuel_variance_litres, 1),
                    'fuel_variance_pct': round(fuel_variance_pct, 1),
                    'fuel_risk': 'High risk' if fuel_variance_pct > 25 else 'Watch' if fuel_variance_pct > 12 else 'Normal',
                    'notes': notes,
                }
                st.session_state['trips_df'] = pd.concat([st.session_state['trips_df'], pd.DataFrame([new_row])], ignore_index=True)
                st.session_state['show_add'] = False
                st.rerun()
        with cc:
            if st.button("✖ Cancel add"):
                st.session_state['show_add'] = False
                st.rerun()

    st.markdown('<div class="fiq-section-head">📊 Quick Analytics</div>', unsafe_allow_html=True)
    chart_a, chart_b = st.columns(2)
    with chart_a:
        route_df = df.copy()
        route_df['route'] = route_df['origin'].astype(str) + ' → ' + route_df['destination'].astype(str)
        route_cost = route_df.groupby('route', as_index=False)['cost_per_km'].mean().sort_values('cost_per_km', ascending=True).tail(10)
        colors = [cpk_color(v) for v in route_cost['cost_per_km']]
        fig = go.Figure(go.Bar(x=route_cost['cost_per_km'], y=route_cost['route'], orientation='h', marker_color=colors))
        fig.add_vline(x=BENCHMARK_CPK, line_dash="dash", line_color="#1A1A2E", annotation_text="Target ₹28.5")
        fig.update_layout(height=240, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=0, r=40, t=36, b=0), xaxis=dict(showgrid=False, title=""), yaxis=dict(title=""))
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    with chart_b:
        goods_load = split_goods(df).groupby('goods', as_index=False)['load_tonnes'].sum().sort_values('load_tonnes', ascending=False).head(10)
        fig2 = go.Figure(go.Bar(x=goods_load['goods'], y=goods_load['load_tonnes'], marker_color="#378ADD"))
        fig2.update_layout(height=240, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=0, r=40, t=36, b=0), xaxis=dict(title="", showgrid=False), yaxis=dict(title="", showgrid=False))
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    st.markdown('<div class="fiq-section-head">📈 Route Profitability Ranking</div>', unsafe_allow_html=True)
    route_perf = df.copy()
    route_perf['route'] = route_perf['origin'].astype(str) + ' → ' + route_perf['destination'].astype(str)
    route_perf['profit'] = route_perf['revenue'] - route_perf['total_cost']
    route_summary = route_perf.groupby('route').agg(
        trips=('truck_no', 'count'),
        km=('km_driven', 'sum'),
        revenue=('revenue', 'sum'),
        total_cost=('total_cost', 'sum'),
        avg_cpk=('cost_per_km', 'mean'),
        profit=('profit', 'sum'),
    ).reset_index().sort_values('profit', ascending=False)
    best_col, worst_col = st.columns(2)
    with best_col:
        st.markdown("**Best routes**")
        st.dataframe(route_summary.head(5), use_container_width=True, hide_index=True)
    with worst_col:
        st.markdown("**Routes to renegotiate**")
        st.dataframe(route_summary.tail(5).sort_values('profit'), use_container_width=True, hide_index=True)

    st.markdown('<div class="fiq-section-head">⛽ Fuel Theft Suspicion</div>', unsafe_allow_html=True)
    fuel_watch = df.sort_values('fuel_variance_pct', ascending=False)[[
        'trip_date', 'truck_no', 'driver_name', 'origin', 'destination',
        'km_driven', 'fuel_litres', 'expected_fuel_litres',
        'fuel_variance_litres', 'fuel_variance_pct', 'fuel_risk'
    ]].head(12)
    risk_counts = df['fuel_risk'].value_counts().to_dict()
    fc1, fc2, fc3 = st.columns(3)
    fc1.metric("High-risk trips", risk_counts.get('High risk', 0))
    fc2.metric("Watch trips", risk_counts.get('Watch', 0))
    fc3.metric("Estimated excess litres", f"{max(0, df['fuel_variance_litres'].sum()):,.0f} L")
    st.dataframe(fuel_watch, use_container_width=True, hide_index=True)

    st.markdown('<div class="fiq-section-head">🧾 Driver Advance & Settlement</div>', unsafe_allow_html=True)
    edited_settlement = st.data_editor(
        settlement_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            'advance_paid': st.column_config.NumberColumn('Advance paid (₹)'),
            'diesel_cash': st.column_config.NumberColumn('Diesel cash (₹)'),
            'toll_paid': st.column_config.NumberColumn('Toll paid (₹)'),
            'unloading': st.column_config.NumberColumn('Unloading (₹)'),
            'balance_due': st.column_config.NumberColumn('Balance due (₹)'),
        },
        key="settlement_editor",
    )
    if not edited_settlement.equals(st.session_state['settlement_df']):
        st.session_state['settlement_df'] = edited_settlement

    st.markdown('<div class="fiq-section-head">📄 Documents & Service Tracker</div>', unsafe_allow_html=True)
    doc_view = docs_df.copy()
    today_ts = pd.Timestamp(datetime.now().date())
    for col in [c for c in doc_view.columns if c.endswith('_expiry')]:
        doc_view[col] = pd.to_datetime(doc_view[col])
    doc_view['next_expiry_days'] = doc_view[[c for c in doc_view.columns if c.endswith('_expiry')]].sub(today_ts).min(axis=1).dt.days
    doc_view['document_status'] = np.select(
        [doc_view['next_expiry_days'] < 0, doc_view['next_expiry_days'] <= 30],
        ['Expired', 'Due in 30 days'],
        default='OK'
    )
    doc_col, service_col = st.columns(2)
    with doc_col:
        st.markdown("**Document expiry alerts**")
        st.dataframe(doc_view.sort_values('next_expiry_days'), use_container_width=True, hide_index=True)
    with service_col:
        st.markdown("**Service reminder**")
        st.dataframe(service_df.sort_values('km_to_service'), use_container_width=True, hide_index=True)

    st.markdown('<div class="fiq-section-head">💳 Payment Pending Tracker</div>', unsafe_allow_html=True)
    edited_payments = st.data_editor(
        payments_df.sort_values(['paid_status', 'days_pending'], ascending=[False, False]),
        use_container_width=True,
        hide_index=True,
        column_config={
            'paid_status': st.column_config.SelectboxColumn('Paid status', options=['Paid', 'Pending']),
            'invoice_amount': st.column_config.NumberColumn('Invoice amount (₹)'),
            'days_pending': st.column_config.NumberColumn('Days pending'),
        },
        key="payment_editor",
    )
    if not edited_payments.equals(st.session_state['payments_df']):
        st.session_state['payments_df'] = edited_payments

    st.markdown('<div class="fiq-section-head">📆 Truck Utilization</div>', unsafe_allow_html=True)
    util = df.copy()
    util['trip_date_dt'] = pd.to_datetime(util['trip_date'], errors='coerce')
    active_days = util.groupby('truck_no')['trip_date_dt'].nunique().reset_index(name='running_days')
    active_days['idle_days'] = (30 - active_days['running_days']).clip(lower=0)
    active_days['utilization_pct'] = (active_days['running_days'] / 30 * 100).round(0)
    fig_util = go.Figure()
    fig_util.add_trace(go.Bar(x=active_days['truck_no'], y=active_days['running_days'], name='Running days', marker_color='#00875A'))
    fig_util.add_trace(go.Bar(x=active_days['truck_no'], y=active_days['idle_days'], name='Idle days', marker_color='#E6D5C8'))
    fig_util.update_layout(barmode='stack', height=250, plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=0, r=20, t=30, b=0), yaxis_title='Days')
    st.plotly_chart(fig_util, use_container_width=True, config={"displayModeBar": False})

    st.markdown('<div class="fiq-section-head">🧮 Data Entry Desk - Edit Without Excel</div>', unsafe_allow_html=True)
    st.caption("Use these sheets like Excel. Edit cells, add rows, and DieselDeck recalculates cost, profit, fuel risk, and dashboards.")
    sheet_tabs = st.tabs(["Trip sheet", "Truck status", "Documents", "Payments", "Service", "Driver settlement"])

    with sheet_tabs[0]:
        add_trip_row_col, _ = st.columns([1, 3])
        with add_trip_row_col:
            if st.button("➕ Add blank trip row", key="add_blank_trip_row"):
                blank = {
                    'trip_date': datetime.now().strftime('%Y-%m-%d'),
                    'truck_no': live_df['truck_no'].iloc[0] if not live_df.empty else 'RJ14 NEW 0001',
                    'driver_name': '',
                    'origin': 'Jodhpur',
                    'destination': 'Jaipur',
                    'km_driven': 0,
                    'load_tonnes': 0.0,
                    'goods': '',
                    'fuel_litres': 0.0,
                    'toll_charges': 0.0,
                    'freight_rate': 2000,
                    'total_cost': 0.0,
                    'cost_per_km': 0.0,
                    'revenue': 0.0,
                    'profit_status': 'Break-even',
                    'fuel_efficiency': 0.0,
                    'expected_fuel_litres': 0.0,
                    'fuel_variance_litres': 0.0,
                    'fuel_variance_pct': 0.0,
                    'fuel_risk': 'Normal',
                    'notes': '',
                }
                st.session_state['trips_df'] = pd.concat([st.session_state['trips_df'], pd.DataFrame([blank])], ignore_index=True)
                st.rerun()
        trip_edit_cols = ['trip_date', 'truck_no', 'driver_name', 'origin', 'destination', 'goods', 'km_driven', 'load_tonnes', 'fuel_litres', 'toll_charges', 'freight_rate', 'notes']
        edited_full_trips = st.data_editor(
            st.session_state['trips_df'][trip_edit_cols],
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                'origin': st.column_config.SelectboxColumn('Origin', options=INDIAN_CITIES),
                'destination': st.column_config.SelectboxColumn('Destination', options=INDIAN_CITIES),
                'goods': st.column_config.TextColumn('Goods'),
                'notes': st.column_config.TextColumn('Notes'),
            },
            key="full_trip_sheet_editor",
        )
        if not edited_full_trips.equals(st.session_state['trips_df'][trip_edit_cols]):
            updated = st.session_state['trips_df'].copy()
            for col in trip_edit_cols:
                updated[col] = edited_full_trips[col]
            st.session_state['trips_df'] = enrich_trip_analysis(updated)
            st.success("Trip sheet updated and calculations refreshed.")

    with sheet_tabs[1]:
        edited_live = st.data_editor(
            st.session_state['live_df'],
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                'status': st.column_config.SelectboxColumn('Status', options=VALID_STATUSES),
                'origin': st.column_config.SelectboxColumn('Origin', options=INDIAN_CITIES),
                'destination': st.column_config.SelectboxColumn('Destination', options=INDIAN_CITIES),
                'notes': st.column_config.TextColumn('Notes'),
            },
            key="live_sheet_editor",
        )
        if not edited_live.equals(st.session_state['live_df']):
            st.session_state['live_df'] = edited_live
            st.success("Truck status sheet updated.")

    with sheet_tabs[2]:
        edited_docs = st.data_editor(st.session_state['docs_df'], use_container_width=True, num_rows="dynamic", key="docs_sheet_editor")
        if not edited_docs.equals(st.session_state['docs_df']):
            st.session_state['docs_df'] = edited_docs
            st.success("Document sheet updated.")

    with sheet_tabs[3]:
        edited_pay = st.data_editor(
            st.session_state['payments_df'],
            use_container_width=True,
            num_rows="dynamic",
            column_config={'paid_status': st.column_config.SelectboxColumn('Paid status', options=['Paid', 'Pending'])},
            key="payments_sheet_editor",
        )
        if not edited_pay.equals(st.session_state['payments_df']):
            st.session_state['payments_df'] = edited_pay
            st.success("Payment sheet updated.")

    with sheet_tabs[4]:
        edited_service = st.data_editor(st.session_state['service_df'], use_container_width=True, num_rows="dynamic", key="service_sheet_editor")
        if not edited_service.equals(st.session_state['service_df']):
            st.session_state['service_df'] = edited_service
            st.success("Service sheet updated.")

    with sheet_tabs[5]:
        edited_settle_full = st.data_editor(st.session_state['settlement_df'], use_container_width=True, num_rows="dynamic", key="settlement_sheet_editor")
        if not edited_settle_full.equals(st.session_state['settlement_df']):
            st.session_state['settlement_df'] = edited_settle_full
            st.success("Driver settlement sheet updated.")

    all_sheets = {
        'trips': st.session_state['trips_df'],
        'truck_status': st.session_state['live_df'],
        'documents': st.session_state['docs_df'],
        'payments': st.session_state['payments_df'],
        'service': st.session_state['service_df'],
        'driver_settlement': st.session_state['settlement_df'],
    }
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        for sheet_name, sheet_df in all_sheets.items():
            sheet_df.to_excel(writer, sheet_name=sheet_name[:31], index=False)
    st.download_button(
        "⬇️ Download complete Excel workbook",
        data=excel_buffer.getvalue(),
        file_name="DieselDeck_owner_workbook.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    st.markdown('<div class="fiq-section-head">📋 Trip History</div>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    goods_first = df['goods'].fillna('Unknown').astype(str).str.split(',').str[0].str.strip()
    with f1:
        truck_filter = st.selectbox("Truck", ["All trucks"] + sorted(df['truck_no'].dropna().unique().tolist()))
    with f2:
        status_filter = st.selectbox("Status", ["All"] + sorted(df['profit_status'].dropna().unique().tolist()))
    with f3:
        goods_filter = st.selectbox("Goods", ["All goods"] + sorted(goods_first.dropna().unique().tolist()))

    filtered = df.copy()
    if truck_filter != "All trucks":
        filtered = filtered[filtered['truck_no'] == truck_filter]
    if status_filter != "All":
        filtered = filtered[filtered['profit_status'] == status_filter]
    if goods_filter != "All goods":
        filtered = filtered[filtered['goods'].fillna('').astype(str).str.split(',').str[0].str.strip() == goods_filter]

    table_cols = ['trip_date', 'truck_no', 'driver_name', 'origin', 'destination', 'goods', 'km_driven', 'cost_per_km', 'revenue', 'profit_status', 'notes']
    edited = st.data_editor(
        filtered[table_cols],
        use_container_width=True,
        column_config={
            "profit_status": st.column_config.SelectboxColumn("Profit status", options=['Profitable', 'Break-even', 'Loss-making']),
            "notes": st.column_config.TextColumn("Notes"),
            "cost_per_km": st.column_config.NumberColumn("Cost/km (₹)"),
            "revenue": st.column_config.NumberColumn("Revenue (₹)"),
        },
        disabled=["trip_date", "truck_no", "km_driven"],
        key="trip_history_editor",
    )
    if not edited.equals(filtered[table_cols]):
        for idx in edited.index:
            for col in table_cols:
                st.session_state['trips_df'].at[idx, col] = edited.at[idx, col]

    csv_buf = io.StringIO()
    filtered.to_csv(csv_buf, index=False)
    st.download_button("⬇️ Download filtered data", csv_buf.getvalue(), "fleetiq_filtered_trips.csv", "text/csv")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div style="padding:20px 28px 24px 10px">', unsafe_allow_html=True)
    st.markdown('<div class="fiq-section-head">⚡ Today\'s Actions</div>', unsafe_allow_html=True)
    actions = 0
    avg = df['cost_per_km'].mean() if not df.empty else 0
    total_km = df['km_driven'].sum() if not df.empty else 0
    if avg > 35:
        saving = (avg - BENCHMARK_CPK) * total_km
        st.markdown(f'<div class="fiq-action-crit">🚨 Cost too high — ₹{avg:.1f}/km vs target ₹28.5<br>Fix this to save ₹{saving:,.0f} this month</div>', unsafe_allow_html=True)
        actions += 1
    for _, r in live_df[live_df['status'] == 'Fuel alert'].iterrows():
        st.markdown(f'<div class="fiq-action-crit">⛽ Fuel alert — {clean_html(r["truck_no"])}<br>Cross-check fuel receipts with driver today</div>', unsafe_allow_html=True)
        actions += 1
    for _, r in live_df[live_df['status'] == 'Maintenance'].iterrows():
        st.markdown(f'<div class="fiq-action-warn">🔧 {clean_html(r["truck_no"])} needs maintenance<br>Take off route until serviced</div>', unsafe_allow_html=True)
        actions += 1
    loss_ct = int((live_df['status'] == 'Loss-making').sum())
    if loss_ct:
        st.markdown(f'<div class="fiq-action-warn">📉 {loss_ct} truck(s) loss-making<br>Freight rate may need renegotiation</div>', unsafe_allow_html=True)
        actions += 1
    if not docs_df.empty:
        doc_dates = docs_df[[c for c in docs_df.columns if c.endswith('_expiry')]].apply(pd.to_datetime)
        doc_due = int((doc_dates <= pd.Timestamp(datetime.now().date()) + pd.Timedelta(days=30)).sum().sum())
        if doc_due:
            st.markdown(f'<div class="fiq-action-warn">📄 {doc_due} document(s) expire within 30 days<br>Renew insurance, permit, pollution or fitness certificates</div>', unsafe_allow_html=True)
            actions += 1
    if not service_df.empty:
        service_due = int(service_df['priority'].isin(['Overdue', 'Due soon']).sum())
        if service_due:
            st.markdown(f'<div class="fiq-action-warn">🔧 {service_due} truck(s) due for service<br>Plan workshop slots before dispatch</div>', unsafe_allow_html=True)
            actions += 1
    if not payments_df.empty:
        pending_amt = payments_df.loc[payments_df['paid_status'] == 'Pending', 'invoice_amount'].sum()
        old_pending = int(((payments_df['paid_status'] == 'Pending') & (payments_df['days_pending'] > 21)).sum())
        if pending_amt > 0:
            st.markdown(f'<div class="fiq-action-crit">💳 ₹{pending_amt:,.0f} payment pending<br>{old_pending} invoice(s) older than 21 days</div>', unsafe_allow_html=True)
            actions += 1
    for _, r in live_df[live_df['status'] == 'At depot'].iterrows():
        st.markdown(f'<div class="fiq-action-good">🅿 {clean_html(r["truck_no"])} is at depot — ready to dispatch</div>', unsafe_allow_html=True)
        actions += 1
    if actions == 0:
        st.markdown('<div class="fiq-action-good">✅ All clear — fleet running healthy today</div>', unsafe_allow_html=True)

    st.markdown('<div class="fiq-section-head">👨‍✈️ Driver Scores</div>', unsafe_allow_html=True)
    driver_df = df.copy()
    driver_df['loss_flag'] = (driver_df['profit_status'] == 'Loss-making').astype(int)
    scores = driver_df.groupby('driver_name').agg(
        trips=('truck_no', 'count'),
        avg_cpk=('cost_per_km', 'mean'),
        avg_eff=('fuel_efficiency', 'mean'),
        loss_trips=('loss_flag', 'sum'),
    ).reset_index()
    if not scores.empty:
        eff_score = ((scores['avg_eff'] - 3.0) / 2.5 * 40).clip(0, 40)
        cost_score = ((40 - scores['avg_cpk'].clip(20, 40) + 20) / 20 * 40).clip(0, 40)
        vol_score = (scores['trips'].clip(1, 15) / 15 * 20)
        penalty = scores['loss_trips'] * 5
        scores['score'] = (eff_score + cost_score + vol_score - penalty).clip(0, 100).round(0)
        scores = scores.sort_values('score', ascending=False).head(6)
        medals = ["🥇", "🥈", "🥉", "#4", "#5", "#6"]
        for i, r in scores.reset_index(drop=True).iterrows():
            color = "#00875A" if r['score'] >= 70 else "#E65C00" if r['score'] >= 50 else "#CC0000"
            first = clean_html(str(r['driver_name']).split()[0])
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;border:1px solid #F0EDE8;border-radius:10px;padding:9px 11px;margin-bottom:7px;background:white">
              <div><b>{medals[i]} {first}</b><br><span style="font-size:11px;color:#888">{int(r['trips'])} trips · ₹{r['avg_cpk']:.1f}/km · {r['avg_eff']:.1f}km/L</span></div>
              <div style="font-size:20px;font-weight:800;color:{color}">{int(r['score'])}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="fiq-section-head">📦 Revenue by Goods</div>', unsafe_allow_html=True)
    rev_goods = df[['goods', 'revenue']].copy()
    rev_goods['goods_count'] = rev_goods['goods'].fillna('Unknown').astype(str).str.split(',').str.len().clip(lower=1)
    rev_goods['goods'] = rev_goods['goods'].fillna('Unknown').astype(str).str.split(',')
    rev_goods = rev_goods.explode('goods')
    rev_goods['goods'] = rev_goods['goods'].str.strip().replace('', 'Unknown')
    rev_goods['revenue_share'] = rev_goods['revenue'] / rev_goods['goods_count']
    goods_rev = rev_goods.groupby('goods', as_index=False)['revenue_share'].sum().sort_values('revenue_share', ascending=False).head(8)
    total_rev = goods_rev['revenue_share'].sum()
    for _, r in goods_rev.iterrows():
        pct = (r['revenue_share'] / total_rev * 100) if total_rev > 0 else 0
        st.markdown(f"""
        <div style="margin-bottom:7px">
          <div style="display:flex;justify-content:space-between;
          font-size:12px;margin-bottom:3px">
            <span>{clean_html(r['goods'])}</span>
            <span style="color:#666">
              ₹{r['revenue_share']/1000:.0f}K
              <span style="color:#999">({pct:.0f}%)</span>
            </span>
          </div>
          <div style="background:#F0EDE8;border-radius:4px;
          height:6px;overflow:hidden">
            <div style="width:{pct}%;height:100%;
            background:#378ADD;border-radius:4px"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="fiq-section-head">📱 WhatsApp Summary</div>', unsafe_allow_html=True)
    wa_text = wa_summary(df, live_df, fname, health, diesel)
    st.text_area("Weekly fleet message", value=wa_text, height=210, label_visibility="collapsed")
    st.caption("Copy → paste in your fleet WhatsApp group every Monday")

    st.markdown('<div class="fiq-section-head">🧾 Owner Report Export</div>', unsafe_allow_html=True)
    report_html = make_report_html(df, live_df, docs_df, payments_df, service_df, fname, health, diesel)
    st.download_button(
        "⬇️ Download print-ready report",
        data=report_html,
        file_name=f"{APP_NAME.replace(' ', '_')}_owner_report.html",
        mime="text/html",
    )
    st.caption("Open the report and use Print → Save as PDF for a clean owner PDF.")

    st.markdown('<div style="margin-top:16px"></div>', unsafe_allow_html=True)
    if st.button("📂 Upload a different file"):
        st.session_state['data_loaded'] = False
        st.session_state['trips_df'] = pd.DataFrame()
        st.session_state['live_df'] = pd.DataFrame()
        st.session_state['docs_df'] = pd.DataFrame()
        st.session_state['payments_df'] = pd.DataFrame()
        st.session_state['service_df'] = pd.DataFrame()
        st.session_state['settlement_df'] = pd.DataFrame()
        st.session_state['edit_truck'] = None
        st.session_state['show_add'] = False
        st.rerun()

    with st.expander("⚙️ Settings"):
        new_name = st.text_input("Fleet name", value=st.session_state['fleet_name'])
        new_diesel = st.number_input("Diesel price (₹/litre)", min_value=80.0, max_value=115.0, value=st.session_state['diesel_price'], step=0.01)
        if st.button("💾 Save settings"):
            st.session_state['fleet_name'] = new_name
            st.session_state['diesel_price'] = new_diesel
            st.success("Saved!")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
