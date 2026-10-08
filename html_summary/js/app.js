/**
 * AI COURSE PORTAL INTERACTIVE JAVASCRIPT ENGINE
 * Handles Theme Toggling, Chapter Tabs, Quiz Grading & Progress Analytics
 */

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('ai_portal_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('ai_portal_theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }
}

function updateThemeIcon(theme) {
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) {
    themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
    themeToggleBtn.setAttribute('title', theme === 'dark' ? 'เปลี่ยนเป็นธีมสว่าง' : 'เปลี่ยนเป็นธีมมืด');
  }
}

// Chapter Detail Tab Switching (Summary vs Quiz)
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const summaryView = document.getElementById('tab-summary-content');
  const quizView = document.getElementById('tab-quiz-content');

  if (!tabBtns.length) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const targetTab = btn.getAttribute('data-tab');
      if (targetTab === 'summary') {
        if (summaryView) summaryView.style.display = 'grid';
        if (quizView) quizView.style.display = 'none';
      } else if (targetTab === 'quiz') {
        if (summaryView) summaryView.style.display = 'none';
        if (quizView) quizView.style.display = 'block';
        // Scroll smoothly to quiz wrapper if clicking from top
        if (quizView) quizView.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

// Quiz Engine Class
class QuizEngine {
  constructor(containerId, questions, options = {}) {
    this.container = document.getElementById(containerId);
    this.questions = questions || [];
    this.options = options;
    this.userAnswers = {};
    this.score = 0;
    this.answeredCount = 0;
    
    if (this.container && this.questions.length > 0) {
      this.render();
    }
  }

  render() {
    this.container.innerHTML = `
      <div class="quiz-wrapper">
        <div class="quiz-header-bar">
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.25rem;">
              🎯 แบบทดสอบประเมินความรู้ (${this.questions.length} ข้อ)
            </h2>
            <p style="font-size: 0.9rem; color: var(--text-secondary);">
              คลิกเลือกคำตอบเพื่อดูผลตรวจทันที พร้อมเฉลยละเอียดและวิเคราะห์เหตุผล
            </p>
          </div>
          <div class="quiz-stats">
            <div class="stat-pill">
              <span>ทำแล้ว:</span>
              <strong id="quiz-answered-count">0</strong> / <span>${this.questions.length}</span>
            </div>
            <div class="stat-pill">
              <span>คะแนน:</span>
              <strong id="quiz-current-score" style="color: var(--success);">0</strong>
            </div>
          </div>
        </div>

        <div class="quiz-progress-bar-container">
          <div id="quiz-progress-fill" class="quiz-progress-bar-fill"></div>
        </div>

        <div class="quiz-questions-list" id="questions-list-root"></div>

        <div id="quiz-result-card" class="quiz-result-card">
          <div class="result-badge-icon" id="result-icon">🏆</div>
          <div class="result-score-number" id="result-score-display">0 / 0</div>
          <p class="result-message" id="result-message-text">ทำแบบทดสอบครบทุกข้อแล้ว!</p>
          <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <button class="btn btn-primary" onclick="location.reload()">
              🔄 ทำแบบทดสอบใหม่อีกครั้ง
            </button>
            <a href="index.html" class="btn btn-secondary">
              🏠 กลับหน้าหลัก
            </a>
          </div>
        </div>
      </div>
    `;

    const listRoot = this.container.querySelector('#questions-list-root');
    this.questions.forEach((q, qIndex) => {
      const qCard = document.createElement('div');
      qCard.className = 'question-card';
      qCard.id = `qcard-${qIndex}`;

      const alphabet = ['ก', 'ข', 'ค', 'ง'];

      qCard.innerHTML = `
        <div class="question-meta">
          <span class="question-badge">ข้อที่ ${qIndex + 1} ${q.chapterTitle ? `• ${q.chapterTitle}` : ''}</span>
          <span class="question-status-badge" id="status-badge-${qIndex}"></span>
        </div>
        <div class="question-text">${q.question}</div>
        ${q.hasCustomDiagram ? `
          <div class="convolution-diagram-container">
            <div class="matrix-block">
              <div class="matrix-grid-5x5">
                <div class="m-cell cell-active">1</div><div class="m-cell cell-active">2</div><div class="m-cell cell-active">3</div><div class="m-cell cell-dim">0</div><div class="m-cell cell-dim">1</div>
                <div class="m-cell cell-active">4</div><div class="m-cell cell-active">0</div><div class="m-cell cell-active">1</div><div class="m-cell cell-dim">1</div><div class="m-cell cell-dim">2</div>
                <div class="m-cell cell-active">7</div><div class="m-cell cell-active">1</div><div class="m-cell cell-active">9</div><div class="m-cell cell-dim">2</div><div class="m-cell cell-dim">3</div>
                <div class="m-cell cell-dim">2</div><div class="m-cell cell-dim">3</div><div class="m-cell cell-dim">4</div><div class="m-cell cell-dim">3</div><div class="m-cell cell-dim">4</div>
                <div class="m-cell cell-dim">1</div><div class="m-cell cell-dim">2</div><div class="m-cell cell-dim">3</div><div class="m-cell cell-dim">4</div><div class="m-cell cell-dim">5</div>
              </div>
              <div class="matrix-label">Input (5&times;5)</div>
            </div>
            <div class="diagram-symbol">&times;</div>
            <div class="matrix-block">
              <div class="matrix-grid-3x3">
                <div class="m-cell cell-filter-orange">1</div><div class="m-cell cell-filter-white">0</div><div class="m-cell cell-filter-blue">-1</div>
                <div class="m-cell cell-filter-orange">1</div><div class="m-cell cell-filter-white">0</div><div class="m-cell cell-filter-blue">-1</div>
                <div class="m-cell cell-filter-orange">1</div><div class="m-cell cell-filter-white">0</div><div class="m-cell cell-filter-blue">-1</div>
              </div>
              <div class="matrix-label">Filter (3&times;3)</div>
            </div>
          </div>
        ` : ''}
        <div class="options-group">
          ${q.options.map((opt, optIndex) => `
            <button class="option-btn" data-qindex="${qIndex}" data-optindex="${optIndex}">
              <span class="option-letter">${alphabet[optIndex] || optIndex + 1}</span>
              <span class="option-content">${opt}</span>
            </button>
          `).join('')}
        </div>
        <div class="explanation-box" id="explanation-${qIndex}">
          <div class="explanation-title" id="explanation-title-${qIndex}">💡 คำอธิบายเฉลย:</div>
          <div class="explanation-desc">${q.explanation}</div>
        </div>
      `;

      listRoot.appendChild(qCard);
    });

    // Attach Event Handlers
    this.container.querySelectorAll('.option-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const qIndex = parseInt(btn.getAttribute('data-qindex'), 10);
        const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
        this.handleAnswer(qIndex, optIndex);
      });
    });
  }

  handleAnswer(qIndex, selectedOptIndex) {
    if (this.userAnswers[qIndex] !== undefined) return; // Already answered

    const question = this.questions[qIndex];
    const isCorrect = selectedOptIndex === question.correctIndex;
    this.userAnswers[qIndex] = selectedOptIndex;
    this.answeredCount++;

    if (isCorrect) {
      this.score++;
    }

    // Update UI for this question card
    const qCard = document.getElementById(`qcard-${qIndex}`);
    const optionBtns = qCard.querySelectorAll('.option-btn');
    const explanationBox = document.getElementById(`explanation-${qIndex}`);
    const statusBadge = document.getElementById(`status-badge-${qIndex}`);

    if (isCorrect) {
      qCard.classList.add('answered-correct');
      if (statusBadge) {
        statusBadge.textContent = '✓ ถูกต้อง';
        statusBadge.style.display = 'inline-block';
        statusBadge.style.color = 'var(--success)';
      }
    } else {
      qCard.classList.add('answered-wrong');
      if (statusBadge) {
        statusBadge.textContent = '✗ ไม่ถูกต้อง';
        statusBadge.style.display = 'inline-block';
        statusBadge.style.color = 'var(--danger)';
      }
    }

    // Disable all options and highlight
    optionBtns.forEach((btn, idx) => {
      btn.disabled = true;
      if (idx === question.correctIndex) {
        btn.classList.add(isCorrect ? 'selected-correct' : 'correct-dimmed');
      } else if (idx === selectedOptIndex && !isCorrect) {
        btn.classList.add('selected-wrong');
      }
    });

    // Reveal explanation
    if (explanationBox) {
      explanationBox.style.display = 'block';
      explanationBox.className = `explanation-box ${isCorrect ? 'correct' : 'wrong'}`;
      const title = document.getElementById(`explanation-title-${qIndex}`);
      if (title) {
        title.innerHTML = isCorrect ? '🎉 ถูกต้อง! เฉลยละเอียด:' : '⚠️ ยังไม่ถูกต้อง! ดูเฉลยและเหตุผล:';
      }
    }

    // Update Overall Stats
    this.updateStats();
  }

  updateStats() {
    const answeredCountEl = document.getElementById('quiz-answered-count');
    const currentScoreEl = document.getElementById('quiz-current-score');
    const progressFillEl = document.getElementById('quiz-progress-fill');

    if (answeredCountEl) answeredCountEl.textContent = this.answeredCount;
    if (currentScoreEl) currentScoreEl.textContent = this.score;

    const progressPercent = (this.answeredCount / this.questions.length) * 100;
    if (progressFillEl) progressFillEl.style.width = `${progressPercent}%`;

    // Check completion
    if (this.answeredCount === this.questions.length) {
      this.showFinalResult();
    }
  }

  showFinalResult() {
    const resultCard = document.getElementById('quiz-result-card');
    if (!resultCard) return;

    resultCard.style.display = 'block';
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });

    const scoreDisplay = document.getElementById('result-score-display');
    const iconDisplay = document.getElementById('result-icon');
    const messageDisplay = document.getElementById('result-message-text');

    const total = this.questions.length;
    const percent = Math.round((this.score / total) * 100);

    if (scoreDisplay) scoreDisplay.textContent = `${this.score} / ${total} (${percent}%)`;

    if (percent >= 85) {
      if (iconDisplay) iconDisplay.textContent = '🏆';
      if (messageDisplay) messageDisplay.textContent = 'ยอดเยี่ยมระดับสูงสุด! คุณมีความเข้าใจเนื้อหาอย่างลึกซึ้งและพร้อมสำหรับข้อสอบจริง!';
    } else if (percent >= 65) {
      if (iconDisplay) iconDisplay.textContent = '🌟';
      if (messageDisplay) messageDisplay.textContent = 'ผ่านเกณฑ์ดีเยี่ยม! สามารถทบทวนจุดที่ผิดเพื่อเพิ่มความมั่นใจให้เต็ม 100%';
    } else {
      if (iconDisplay) iconDisplay.textContent = '💪';
      if (messageDisplay) messageDisplay.textContent = 'ได้คะแนนทบทวนในระดับเริ่มต้น แนะนำให้อ่านส่วนสรุปเนื้อหาด้านบนและลองทำใหม่อีกครั้ง!';
    }
  }
}

// Global Search Filter for Home Portal
function initSearch() {
  const searchInput = document.getElementById('portal-search-input');
  if (!searchInput) return;

  const cards = document.querySelectorAll('.chapter-card');
  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      if (text.includes(query)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

// Global initialization on DOM load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initTabs();
  initSearch();
});
