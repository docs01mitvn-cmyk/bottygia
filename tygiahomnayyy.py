import requests

BOT_TOKEN = '8726945212:AAFpP1JaclIAAPhGAYebJycJpIGCytVB6Z0'
CHAT_ID = '-5360917001' 

def get_exchange_rate():
    """Lấy dữ liệu tỷ giá USD sang VND"""
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    try:
        response = requests.get(url)
        data = response.json()
        vnd_rate = data['rates']['VND']
        message = f"💵 Tỷ giá USD hôm nay:\n1 USD = {vnd_rate:,.0f} VNĐ"
        return message
    except Exception as e:
        return f"⚠️ Lỗi lấy tỷ giá: {e}"

def send_telegram_message(text):
    """Gửi tin nhắn qua Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, json=payload)

# Lấy tỷ giá và gửi ngay lập tức khi file được chạy
if __name__ == "__main__":
    msg = get_exchange_rate()
    send_telegram_message(msg)