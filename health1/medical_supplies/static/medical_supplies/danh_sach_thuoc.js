// Mở chat box
function openChat() {
    document.getElementById('chatPopup').style.display = 'flex';
}

// Đóng chat box
function closeChat() {
    document.getElementById('chatPopup').style.display = 'none';
}

// Gửi tin nhắn
function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const chatBody = document.getElementById('chatBody');

    if (chatInput.value.trim() === '') return;

    // Hiển thị tin nhắn của người dùng
    const userMessage = document.createElement('div');
    userMessage.textContent = `Bạn: ${chatInput.value}`;
    userMessage.style.marginBottom = '10px';
    chatBody.appendChild(userMessage);

    // Giả lập phản hồi từ AI
    const botMessage = document.createElement('div');
    botMessage.textContent = `AI: Tôi đã nhận được tin nhắn của bạn.`;
    botMessage.style.marginBottom = '10px';
    botMessage.style.color = '#007bff';
    chatBody.appendChild(botMessage);

    // Cuộn xuống cuối chat
    chatBody.scrollTop = chatBody.scrollHeight;

    // Xóa nội dung input
    chatInput.value = '';
}