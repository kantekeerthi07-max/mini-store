import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- Custom CSS Styling ----------------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        background: linear-gradient(135deg, #4f46e5, #06b6d4);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #111827;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        min-height: 260px;
        border: 1px solid #e5e7eb;
    }

    .product-card h3 {
        color: #111827;
        margin-bottom: 8px;
    }

    .category {
        color: #2563eb;
        font-size: 14px;
        font-weight: 600;
    }

    .price {
        font-size: 22px;
        font-weight: 700;
        color: #16a34a;
        margin-top: 10px;
    }

    .desc {
        color: #4b5563;
        font-size: 15px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Sample Product Data ----------------
products = [
    {
        "name": "Urban Classic T-Shirt",
        "price": 599,
        "description": "Soft cotton T-shirt perfect for casual everyday wear.",
        "category": "Fashion"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 2499,
        "description": "Track steps, heart rate, sleep, and daily activity easily.",
        "category": "Electronics"
    },
    {
        "name": "Wireless Bluetooth Earbuds",
        "price": 1799,
        "description": "Compact earbuds with clear sound and long battery life.",
        "category": "Electronics"
    },
    {
        "name": "Eco-Friendly Water Bottle",
        "price": 399,
        "description": "Reusable stainless steel bottle for school, office, or travel.",
        "category": "Lifestyle"
    },
    {
        "name": "Premium Notebook Set",
        "price": 299,
        "description": "A set of stylish notebooks for students and professionals.",
        "category": "Stationery"
    },
    {
        "name": "Comfort Running Shoes",
        "price": 1999,
        "description": "Lightweight shoes designed for walking, running, and fitness.",
        "category": "Fashion"
    }
]

# ---------------- Sidebar ----------------
st.sidebar.title("🛒 MiniStore Menu")

categories = ["All"] + sorted(list(set(product["category"] for product in products)))
selected_category = st.sidebar.selectbox("Select Product Category", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")

# Demo cart summary
cart_items = 0
cart_total = 0

st.sidebar.write(f"Items in Cart: **{cart_items}**")
st.sidebar.write(f"Total Amount: **₹{cart_total}**")
st.sidebar.info("Cart feature is for demo display only.")

# ---------------- Homepage Hero Section ----------------
st.markdown("""
<div class="hero">
    <h1>🛍️ Welcome to MiniStore</h1>
    <p>Your one-stop demo e-commerce website for fashion, electronics, lifestyle, and more.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Welcome Section ----------------
st.markdown('<div class="section-title">Why Shop With MiniStore?</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("✅ Quality Products")

with col2:
    st.info("🚚 Fast Delivery")

with col3:
    st.info("💳 Easy Payments")

# ---------------- Featured Products Section ----------------
st.markdown('<div class="section-title">Featured Products</div>', unsafe_allow_html=True)

# Filter products based on selected category
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# ---------------- Product Cards Layout ----------------
# Display products in rows of 3 columns
for i in range(0, len(filtered_products), 3):
    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):
        with col:
            st.markdown(f"""
            <div class="product-card">
                <p class="category">{product['category']}</p>
                <h3>{product['name']}</h3>
                <p class="desc">{product['description']}</p>
                <p class="price">₹{product['price']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("© 2026 MiniStore | Demo Streamlit E-commerce Website")
# ---------------- Floating Support Button ----------------
st.markdown("""
<style>
.support-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #4f46e5;
    color: white !important;
    padding: 14px 22px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 700;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    z-index: 9999;
}
.support-btn:hover {
    background-color: #3730a3;
}
</style>

<a href="/Support_Chatbot" target="_self" class="support-btn">
💬 Support
</a>
""", unsafe_allow_html=True)