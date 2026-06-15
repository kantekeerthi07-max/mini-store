import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

# ---------------- Product Data ----------------
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

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.chat-title {
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("""
<div class="chat-title">
    <h1>💬 MiniStore Support Chatbot</h1>
    <p>Ask about products, delivery, refunds, returns, payments, or order status.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Session State for Chat History ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# ---------------- Rule-Based Chatbot Function ----------------
def get_bot_response(user_input):
    user_input = user_input.lower()

    product_names = [product["name"].lower() for product in products]

    # Product questions
    if any(word in user_input for word in ["product", "items", "available", "sell", "price", "cost"]):
        response = "Here are some products available in MiniStore:\n\n"
        for product in products:
            response += f"• {product['name']} - ₹{product['price']} ({product['category']})\n"
        return response

    # Specific product questions
    for product in products:
        if product["name"].lower() in user_input:
            return (
                f"{product['name']} costs ₹{product['price']}.\n\n"
                f"Category: {product['category']}\n\n"
                f"Description: {product['description']}"
            )

    # Delivery questions
    if any(word in user_input for word in ["delivery", "shipping", "deliver", "arrival"]):
        return (
            "MiniStore offers standard delivery within 3 to 5 business days. "
            "Delivery charges may vary based on location and order value."
        )

    # Refund questions
    if any(word in user_input for word in ["refund", "money back", "cashback"]):
        return (
            "Refunds are processed after the returned product is checked. "
            "The refund usually takes 5 to 7 business days."
        )

    # Return questions
    if any(word in user_input for word in ["return", "replace", "exchange"]):
        return (
            "You can return or exchange eligible products within 7 days of delivery. "
            "The product should be unused and in original packaging."
        )

    # Payment questions
    if any(word in user_input for word in ["payment", "pay", "upi", "card", "cod", "cash"]):
        return (
            "MiniStore supports UPI, debit card, credit card, net banking, and cash on delivery."
        )

    # Order status questions
    if any(word in user_input for word in ["order", "status", "track", "tracking"]):
        return (
            "To check your order status, please enter your order ID on the orders page. "
            "For this demo app, order tracking is only shown as a sample feature."
        )

    # Greeting
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you with MiniStore today?"

    # Default response
    return (
        "I can help you with product details, delivery, refunds, returns, "
        "payment methods, and order status. Please ask about any of these topics."
    )

# ---------------- Display Chat History ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------- Chat Input ----------------
user_message = st.chat_input("Type your question here...")

if user_message:
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    with st.chat_message("user"):
        st.write(user_message)

    bot_response = get_bot_response(user_message)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    with st.chat_message("assistant"):
        st.write(bot_response)