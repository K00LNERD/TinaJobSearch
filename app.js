document.addEventListener('DOMContentLoaded', () => {
    let appData = null;
    let activeJob = null;

    // DOM Elements
    const candidateName = document.getElementById('candidateName');
    const candidateSkills = document.getElementById('candidateSkills');
    const candidateEducation = document.getElementById('candidateEducation');
    const statTotalJobs = document.getElementById('statTotalJobs');
    const statHighConvert = document.getElementById('statHighConvert');
    
    const searchInput = document.getElementById('searchInput');
    const companyFilter = document.getElementById('companyFilter');
    const scoreFilter = document.getElementById('scoreFilter');
    const salaryFilter = document.getElementById('salaryFilter');
    const resetFiltersBtn = document.getElementById('resetFiltersBtn');
    
    const jobsGrid = document.getElementById('jobsGrid');
    const resultsCount = document.getElementById('resultsCount');
    
    const detailPanel = document.getElementById('detailPanel');
    const detailPanelOverlay = document.getElementById('detailPanelOverlay');
    const detailPanelContent = document.getElementById('detailPanelContent');
    const closePanelBtn = document.getElementById('closePanelBtn');
    
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');

    // Fetch and Load Data
    fetch('data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch data.json');
            }
            return response.json();
        })
        .then(data => {
            appData = data;
            initializeDashboard();
        })
        .catch(error => {
            console.error('Error loading data:', error);
            jobsGrid.innerHTML = `
                <div class="error-state" style="grid-column: 1/-1; text-align: center; padding: 3rem; background: var(--bg-secondary); border-radius: 18px; border: 1px dashed var(--accent-rose);">
                    <i class="fa-solid fa-triangle-exclamation" style="font-size: 2.5rem; color: var(--accent-rose); margin-bottom: 1rem;"></i>
                    <h4>Failed to Load Database</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">Please check if data.json exists and is valid.</p>
                </div>
            `;
        });

    // Initialize Dashboard Elements
    function initializeDashboard() {
        if (!appData) return;

        // Render Profile
        const candidate = appData.candidate;
        candidateName.textContent = candidate.name;
        
        // Target Roles
        const candidateRoles = document.getElementById('candidateRoles');
        if (candidateRoles && candidate.top_roles) {
            candidateRoles.innerHTML = candidate.top_roles.map(role => 
                `<div style="padding: 0.35rem 0.6rem; background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 8px; font-weight: 500; font-size: 0.75rem; color: var(--text-secondary);">
                    <i class="fa-solid fa-angle-right" style="color: var(--accent-indigo); margin-right: 0.25rem;"></i>${role}
                </div>`
            ).join('');
        }
        
        // Live Portal Feeds
        const portalSearchLinks = document.getElementById('portalSearchLinks');
        if (portalSearchLinks && appData.portal_search_links) {
            portalSearchLinks.innerHTML = appData.portal_search_links.map(portal => `
                <div style="background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 10px; padding: 0.6rem; display: flex; flex-direction: column; gap: 0.4rem;">
                    <span style="font-size: 0.75rem; font-weight: 600; color: #fff; line-height: 1.2;">${portal.role}</span>
                    <div style="display: flex; gap: 0.3rem;">
                        <a href="${portal.naukri}" target="_blank" class="btn btn-secondary" style="padding: 0.25rem 0.5rem; font-size: 0.65rem; flex: 1; border-radius: 6px;" title="Search on Naukri">Naukri</a>
                        <a href="${portal.hirist}" target="_blank" class="btn btn-secondary" style="padding: 0.25rem 0.5rem; font-size: 0.65rem; flex: 1; border-radius: 6px;" title="Search on Hirist">Hirist</a>
                        <a href="${portal.instahyre}" target="_blank" class="btn btn-secondary" style="padding: 0.25rem 0.5rem; font-size: 0.65rem; flex: 1; border-radius: 6px;" title="Search on Instahyre">Instahyre</a>
                    </div>
                </div>
            `).join('');
        }
        
        // Skills
        candidateSkills.innerHTML = candidate.skills.map(skill => 
            `<span class="skill-tag">${skill}</span>`
        ).join('');

        // Education
        candidateEducation.innerHTML = candidate.education.map(edu => `
            <div class="edu-item">
                <div class="edu-degree">${edu.degree}</div>
                <div class="edu-institution">${edu.institution}</div>
                <div class="edu-year">${edu.year}</div>
            </div>
        `).join('');

        // Setup filter options (Companies)
        const companies = [...new Set(appData.jobs.map(job => job.company))].sort();
        companyFilter.innerHTML = '<option value="">All Companies</option>' + 
            companies.map(c => `<option value="${c}">${c}</option>`).join('');

        // Stats
        statTotalJobs.textContent = appData.jobs.length;
        const highMatchCount = appData.jobs.filter(job => job.convertibility >= 90).length;
        statHighConvert.textContent = highMatchCount;

        // Initial Render of Jobs
        renderJobs(appData.jobs);

        // Event Listeners
        searchInput.addEventListener('input', applyFilters);
        companyFilter.addEventListener('change', applyFilters);
        scoreFilter.addEventListener('change', applyFilters);
        salaryFilter.addEventListener('change', applyFilters);
        resetFiltersBtn.addEventListener('click', resetFilters);
        
        closePanelBtn.addEventListener('click', closeDetails);
        detailPanelOverlay.addEventListener('click', closeDetails);

        // Escape key to close details
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && detailPanel.classList.contains('active')) {
                closeDetails();
            }
        });
    }

    // Render Job Cards
    function renderJobs(jobsList) {
        jobsGrid.innerHTML = '';
        resultsCount.textContent = `Showing ${jobsList.length} opportunit${jobsList.length === 1 ? 'y' : 'ies'}`;

        if (jobsList.length === 0) {
            jobsGrid.innerHTML = `
                <div class="empty-state" style="grid-column: 1/-1; text-align: center; padding: 4rem 2rem; background: var(--bg-secondary); border-radius: 18px; border: 1px dashed var(--border-color);">
                    <i class="fa-solid fa-briefcase" style="font-size: 3rem; color: var(--text-muted); margin-bottom: 1rem;"></i>
                    <h4>No Matching Job Postings Found</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">Try adjusting your search criteria or resetting filters.</p>
                </div>
            `;
            return;
        }

        jobsList.forEach(job => {
            const card = document.createElement('article');
            card.className = 'job-card';
            card.id = `card-${job.id}`;
            
            const isHighScore = job.convertibility >= 90;
            const scoreClass = isHighScore ? 'high' : 'medium';
            const starIcon = isHighScore ? 'fa-star' : 'fa-star-half-stroke';
            
            card.innerHTML = `
                <div class="job-card-header">
                    <span class="job-company-badge">${job.company}</span>
                    <span class="score-badge ${scoreClass}">
                        <i class="fa-solid ${starIcon}"></i> ${job.convertibility}% Fit
                    </span>
                </div>
                <div class="job-card-body">
                    <h4 class="job-title">${job.title}</h4>
                    <div class="job-meta-row">
                        <span class="job-meta-item"><i class="fa-solid fa-location-dot"></i> ${job.location}</span>
                    </div>
                    <div class="job-skills">
                        ${job.skills_required.slice(0, 3).map(skill => `<span class="job-skill-tag">${skill}</span>`).join('')}
                        ${job.skills_required.length > 3 ? `<span class="job-skill-tag">+${job.skills_required.length - 3}</span>` : ''}
                    </div>
                </div>
                <div class="job-card-footer">
                    <div class="contact-preview">
                        <div class="contact-avatar-stack">${job.contacts.length}</div>
                        <span>Reference Paths</span>
                    </div>
                    <span class="explore-details">
                        View Details <i class="fa-solid fa-arrow-right"></i>
                    </span>
                </div>
            `;

            card.addEventListener('click', () => openDetails(job));
            jobsGrid.appendChild(card);
        });
    }

    // Apply Filters and Search
    function applyFilters() {
        if (!appData) return;

        const searchQuery = searchInput.value.toLowerCase().trim();
        const selectedCompany = companyFilter.value;
        const selectedMinScore = scoreFilter.value ? parseInt(scoreFilter.value) : 0;
        const selectedSalaryTier = salaryFilter.value;

        const filteredJobs = appData.jobs.filter(job => {
            // Text Search matching role, company, or skills
            const matchSearch = searchQuery === '' || 
                job.title.toLowerCase().includes(searchQuery) ||
                job.company.toLowerCase().includes(searchQuery) ||
                job.skills_required.some(skill => skill.toLowerCase().includes(searchQuery));
            
            // Company Filter
            const matchCompany = selectedCompany === '' || job.company === selectedCompany;
            
            // Score Filter
            const matchScore = job.convertibility >= selectedMinScore;

            // Salary Filter
            let matchSalary = true;
            if (selectedSalaryTier) {
                const firstReason = job.convertibility_reasons[0].toLowerCase();
                if (selectedSalaryTier === 'premium') {
                    matchSalary = firstReason.includes('premium');
                } else if (selectedSalaryTier === 'standard') {
                    matchSalary = firstReason.includes('standard');
                }
            }

            return matchSearch && matchCompany && matchScore && matchSalary;
        });

        renderJobs(filteredJobs);
    }

    // Reset Filters
    function resetFilters() {
        searchInput.value = '';
        companyFilter.value = '';
        scoreFilter.value = '';
        salaryFilter.value = '';
        applyFilters();
    }

    // Open Details Panel
    function openDetails(job) {
        activeJob = job;
        detailPanelContent.innerHTML = `
            <div class="detail-header">
                <div class="detail-header-row">
                    <h3 class="detail-title">${job.title}</h3>
                </div>
                <div class="detail-meta-list">
                    <span><i class="fa-solid fa-building"></i> ${job.company}</span>
                    <span><i class="fa-solid fa-location-dot"></i> ${job.location}</span>
                </div>
                <a href="${job.apply_url}" target="_blank" class="btn btn-primary" style="width: 100%;">
                    Apply Direct <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>

            <div class="convertibility-analysis">
                <div class="analysis-header">
                    <span>Hiring Convertibility Analysis</span>
                    <div class="analysis-score-container">
                        <span>${job.convertibility}% Likelihood</span>
                    </div>
                </div>
                <ul class="reasons-list">
                    ${job.convertibility_reasons.map(reason => `<li>${reason}</li>`).join('')}
                </ul>
            </div>

            <div class="contacts-section">
                <h4>Recommended Outreach Portals</h4>
                <div class="contact-cards-container">
                    ${job.contacts.map((contact, idx) => `
                        <div class="contact-outreach-card">
                            <div class="contact-card-header">
                                <div class="contact-meta">
                                    <h5>${contact.name_placeholder}</h5>
                                    <p>${contact.role}</p>
                                    <div class="contact-email-format">
                                        <i class="fa-solid fa-at"></i> Typical Email Format: <code>${contact.email_format}</code>
                                    </div>
                                </div>
                            </div>
                            <div class="contact-actions">
                                <div class="action-row">
                                    <a href="${contact.search_url}" target="_blank" class="btn btn-secondary">
                                        <i class="fa-brands fa-linkedin"></i> Find Connection
                                    </a>
                                </div>
                                
                                <div class="template-box">
                                    <div class="template-header">
                                        <span>LinkedIn Invite Note (300 Chars Limit)</span>
                                        <button class="btn-copy-mini" onclick="copyTextToClipboard('${job.id}-li-${idx}', 'LinkedIn Connection Note copied!')">
                                            <i class="fa-solid fa-copy"></i> Copy Note
                                        </button>
                                    </div>
                                    <div class="template-content" id="${job.id}-li-${idx}">${escapeHtml(contact.outreach_linkedin)}</div>
                                </div>

                                <div class="template-box">
                                    <div class="template-header">
                                        <span>Cold Email Outreach Template</span>
                                        <button class="btn-copy-mini" onclick="copyTextToClipboard('${job.id}-email-${idx}', 'Outreach Email copied!')">
                                            <i class="fa-solid fa-copy"></i> Copy Email
                                        </button>
                                    </div>
                                    <div class="template-content" id="${job.id}-email-${idx}">${escapeHtml(contact.outreach_email)}</div>
                                </div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;

        detailPanel.classList.add('active');
        detailPanelOverlay.classList.add('active');
        detailPanel.setAttribute('aria-hidden', 'false');
    }

    // Close Details Panel
    function closeDetails() {
        detailPanel.classList.remove('active');
        detailPanelOverlay.classList.remove('active');
        detailPanel.setAttribute('aria-hidden', 'true');
        activeJob = null;
    }

    // Helper: Escape HTML string
    function escapeHtml(unsafe) {
        return unsafe
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
    }

    // Clipboard copy mechanism with Toast
    window.copyTextToClipboard = function(elementId, successMessage) {
        const text = document.getElementById(elementId).innerText;
        navigator.clipboard.writeText(text)
            .then(() => {
                showToast(successMessage);
            })
            .catch(err => {
                console.error('Could not copy text: ', err);
                showToast('Failed to copy. Please manually select and copy.');
            });
    };

    function showToast(message) {
        toastMessage.textContent = message;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }
});
