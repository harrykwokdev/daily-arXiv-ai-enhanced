let reportDates = [];
let currentDate = '';
let currentCategory = '';
let currentIndex = null;

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
}

async function fetchReportDates() {
  const fileListUrl = DATA_CONFIG.getDataUrl('assets/file-list.txt');
  const response = await fetch(fileListUrl);
  if (!response.ok) {
    throw new Error(`Cannot fetch file list: ${response.status}`);
  }

  const text = await response.text();
  const files = text.trim().split('\n').filter(Boolean);
  const dateRegex = /^reports\/(\d{4}-\d{2}-\d{2})\/index\.json$/;
  const set = new Set();

  files.forEach(file => {
    const m = file.match(dateRegex);
    if (m && m[1]) {
      set.add(m[1]);
    }
  });

  reportDates = Array.from(set).sort((a, b) => new Date(b) - new Date(a));
  return reportDates;
}

async function loadIndexForDate(date) {
  const url = DATA_CONFIG.getDataUrl(`data/reports/${date}/index.json`);
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Cannot fetch report index for ${date}: ${response.status}`);
  }
  return response.json();
}

function renderDateSelect() {
  const select = document.getElementById('reportDateSelect');
  select.innerHTML = reportDates
    .map(date => `<option value="${date}">${date}</option>`)
    .join('');

  select.value = currentDate;
  select.addEventListener('change', async (e) => {
    currentDate = e.target.value;
    await loadAndRenderDate(currentDate);
  });
}

function renderCategoryTabs(indexData) {
  const container = document.getElementById('categoryTabs');
  const categories = Array.isArray(indexData.categories) ? indexData.categories : [];

  if (!categories.length) {
    container.innerHTML = '<div class="empty-state">No category reports on this day.</div>';
    return;
  }

  if (!currentCategory || !categories.some(c => c.category === currentCategory)) {
    currentCategory = categories[0].category;
  }

  container.innerHTML = categories
    .map(item => {
      const active = item.category === currentCategory ? 'active' : '';
      return `<button class="category-tab ${active}" data-category="${item.category}">${item.category} (${item.paper_count})</button>`;
    })
    .join('');

  container.querySelectorAll('.category-tab').forEach(button => {
    button.addEventListener('click', async () => {
      currentCategory = button.dataset.category;
      renderCategoryTabs(indexData);
      await renderCurrentCategoryReport();
    });
  });
}

async function renderCurrentCategoryReport() {
  const content = document.getElementById('reportContent');
  if (!currentIndex || !Array.isArray(currentIndex.categories)) {
    content.innerHTML = '<p class="empty-state">No report data.</p>';
    return;
  }

  const selected = currentIndex.categories.find(c => c.category === currentCategory);
  if (!selected) {
    content.innerHTML = '<p class="empty-state">Category report not found.</p>';
    return;
  }

  const rawPath = selected.report_file.replace(/^data\//, '');
  const url = DATA_CONFIG.getDataUrl(`data/${rawPath}`);

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Cannot fetch report markdown: ${response.status}`);
    }
    const markdown = await response.text();
    content.innerHTML = marked.parse(markdown);
  } catch (error) {
    console.error(error);
    content.innerHTML = `<p class="empty-state">Failed to load report: ${error.message}</p>`;
  }
}

async function loadAndRenderDate(date) {
  const dateText = document.getElementById('reportDateText');
  const content = document.getElementById('reportContent');
  content.innerHTML = '<div class="loading-container"><div class="loading-spinner"></div><p>Loading report...</p></div>';

  currentIndex = await loadIndexForDate(date);
  dateText.textContent = `Reports for ${formatDate(date)}`;

  renderCategoryTabs(currentIndex);
  await renderCurrentCategoryReport();
}

async function init() {
  try {
    await fetchReportDates();

    if (!reportDates.length) {
      document.getElementById('reportDateText').textContent = 'No reports available yet';
      document.getElementById('reportContent').innerHTML = '<p class="empty-state">No reports generated yet.</p>';
      return;
    }

    currentDate = reportDates[0];
    renderDateSelect();
    await loadAndRenderDate(currentDate);
  } catch (error) {
    console.error(error);
    document.getElementById('reportDateText').textContent = 'Load failed';
    document.getElementById('reportContent').innerHTML = `<p class="empty-state">${error.message}</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
