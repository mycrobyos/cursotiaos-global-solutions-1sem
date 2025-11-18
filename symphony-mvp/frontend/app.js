// =========================
// Configuração da API
// =========================
const API_URL = 'http://localhost:5001';

// =========================
// Navegação entre tabs
// =========================
function showTab(tabName, event) {
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(btn => btn.classList.remove('active'));

    document.getElementById(`${tabName}-tab`).classList.add('active');
    if (event) event.currentTarget.classList.add('active');
}

// =========================
// Chat
// =========================
async function sendMessage() {
    const input = document.getElementById('question');
    const question = input.value.trim();
    if (!question) return;

    const messagesDiv = document.getElementById('chat-messages');
    messagesDiv.innerHTML += `
        <div class="message user">
            <strong>Você:</strong> ${question}
        </div>
    `;
    input.value = '';
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    // Loading
    messagesDiv.innerHTML += `
        <div class="message bot" id="loading">
            <strong>Iza:</strong> Pensando... 💭
        </div>
    `;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ question })
        });
        const data = await response.json();
        document.getElementById('loading').remove();

        messagesDiv.innerHTML += `
            <div class="message bot">
                <strong>Iza:</strong> ${data.answer}
            </div>
        `;
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (error) {
        document.getElementById('loading').remove();
        messagesDiv.innerHTML += `
            <div class="message bot">
                <strong>Iza:</strong> ⚠️ Erro ao conectar com o servidor.
            </div>
        `;
    }
}

// =========================
// Recomendação de Mentores
// =========================
async function findMentors() {
    const skills = document.getElementById('skills').value.trim();
    const interests = document.getElementById('interests').value.trim();
    if (!skills && !interests) {
        alert('Preencha pelo menos um campo!');
        return;
    }

    const recDiv = document.getElementById('recommendations');
    recDiv.innerHTML = '<div class="loading">🔍 Analisando perfis...</div>';

    try {
        const response = await fetch(`${API_URL}/recommend`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ skills, interests })
        });
        const data = await response.json();

        if (data.recommendations && data.recommendations.length) {
            recDiv.innerHTML = '<h3>Top 3 Mentores Recomendados:</h3>';
            data.recommendations.forEach((mentor, index) => {
                recDiv.innerHTML += `
                    <div class="mentor-card">
                        <h3>#${index+1} ${mentor.nome}</h3>
                        <span class="score">${mentor.score}% de match</span>
                        <div class="detail">🏢 ${mentor.departamento} - ${mentor.cargo}</div>
                        <div class="detail">💡 <strong>Habilidades:</strong> ${mentor.habilidades}</div>
                        <div class="detail">⭐ <strong>Interesses:</strong> ${mentor.interesses}</div>
                        <div class="detail">🎯 <strong>Por quê?</strong> ${mentor.explicacao}</div>
                    </div>
                `;
            });
        } else {
            recDiv.innerHTML = '<p>Nenhum mentor encontrado. Tente outras habilidades ou interesses.</p>';
        }
    } catch (error) {
        recDiv.innerHTML = '<p>⚠️ Erro ao buscar mentores. Verifique se o backend está rodando.</p>';
    }
}

// =========================
// Missões & Progresso
// =========================
async function saveMission(missionKey, completed) {
    try {
        await fetch(`${API_URL}/missions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mission: missionKey, completed })
        });
    } catch (error) {
        console.error('Erro ao salvar missão:', error);
    }
}

function initMissionListeners() {
    const checkboxes = document.querySelectorAll('.mission input[type="checkbox"]');
    checkboxes.forEach(cb => {
        cb.addEventListener('change', () => {
            saveMission(cb.dataset.key, cb.checked);
            updateProgress();
        });
    });
}

function updateProgress() {
    const checkboxes = document.querySelectorAll('.mission input[type="checkbox"]');
    const completed = Array.from(checkboxes).filter(cb => cb.checked).length;
    const total = checkboxes.length;
    const percentage = (completed / total) * 100;

    document.getElementById('progress-fill').style.width = `${percentage}%`;
    document.getElementById('progress-text').textContent = `${completed}/${total} missões`;

    // Atualizar badge
    const badgeStatus = document.getElementById('badge-status');
    const points = completed * 17;
    if (completed === 0) {
        badgeStatus.textContent = 'Complete missões para ganhar badges!';
    } else if (points >= 50 && points < 100) {
        badgeStatus.textContent = '🥉 Badge Bronze desbloqueado! Continue para Prata.';
    } else if (points >= 100 && points < 150) {
        badgeStatus.textContent = '🥈 Badge Prata desbloqueado! Falta pouco para Ouro!';
    } else if (points >= 150) {
        badgeStatus.textContent = '🥇 Parabéns! Badge Ouro conquistado!';
    }
}

// =========================
// Inicialização
// =========================
document.addEventListener('DOMContentLoaded', () => {
    initMissionListeners(); // adicione listeners de missões uma única vez
    updateProgress();       // atualiza barra e badges
});
