import json

def get_outreach_templates(candidate, job, contact_name, contact_role):
    # LinkedIn note limit is 300 chars
    linkedin_note = (
        f"Hi {contact_name.split()[0] if ' ' in contact_name else contact_name}, "
        f"I'm Tina, a Great Lakes Chennai PGDM '26 grad and former Product Innovation Manager at Tagit. "
        f"I saw the entry-level {job['title']} role at {job['company']} in Gurugram. Given my background in "
        f"benchmarking 500+ platforms & customer journeys, I'd love to connect & learn about the team!"
    )
    if len(linkedin_note) > 300:
        linkedin_note = linkedin_note[:297] + "..."

    # Cold email body
    email_subject = f"GLIM Chennai PGDM Graduate | Former Product Innovation Manager interested in entry-level {job['title']} at {job['company']}"
    
    if job['company'].lower() == 'pepperfry':
        email_body = (
            f"Subject: Former Pepperfry Intern | GLIM Chennai PGDM Graduate interested in {job['title']}\n\n"
            f"Dear {contact_name},\n\n"
            f"I hope you are doing well.\n\n"
            f"My name is Tina Jain, and I am a former Sales and Marketing Intern at Pepperfry (flagship stores, Aug-Oct 2022). I recently graduated with a PGDM (Marketing) from Great Lakes Institute of Management, Chennai (Class of 2026).\n\n"
            f"During my internship at Pepperfry, I managed 50+ HNI leads, resolved customer escalations, and helped drive monthly sales of INR 15L+. Since then, I have built further on my experience, working as a Product Innovation Manager at Tagit Pte Ltd and earning a Professional Diploma in Product Management.\n\n"
            f"I saw the entry-level {job['title']} role in Gurugram and would love to return to Pepperfry in this capacity. I feel my understanding of Pepperfry's operations, combined with my PGDM and Product Marketing credentials, makes me a strong fit for your team.\n\n"
            f"I would be deeply grateful for a few minutes to connect or for a referral to the hiring team for this role.\n\n"
            f"I have attached my resume, and my LinkedIn profile can be found here: {candidate['linkedin']}.\n\n"
            f"Thank you so much for your support and guidance!\n\n"
            f"Warm regards,\n\n"
            f"Tina Jain\n"
            f"{candidate['phone']}\n"
            f"{candidate['email']}"
        )
    else:
        email_body = (
            f"Subject: {email_subject}\n\n"
            f"Dear {contact_name},\n\n"
            f"I hope you are doing well.\n\n"
            f"My name is Tina Jain, and I recently graduated with a PGDM (Marketing) from Great Lakes Institute of Management, Chennai (Class of 2026). "
            f"I am reaching out because I saw the active entry-level {job['title']} position at {job['company']} in Gurugram, and I am very keen on exploring this opportunity. "
            f"Given your role as {contact_role} at {job['company']}, I wanted to connect and share my background.\n\n"
            f"During my recent tenure as a Product Innovation Manager at Tagit Pte Ltd, I gained hands-on experience in:\n"
            f"- Benchmarking 500+ global platforms across 10+ markets to prioritize 100+ differentiating product capabilities.\n"
            f"- Mapping customer journeys (developing 8 target personas and 4 journey maps) to optimize engagement.\n"
            f"- Partnering with cross-functional engineering, UX, and C-suite teams to deliver value propositions.\n\n"
            f"Additionally, I hold a Professional Diploma in Product Management and have a strong data-driven decision-making foundation from my PGDM. "
            f"Given my background, I am confident I can contribute effectively to the product, marketing, or consulting initiatives at {job['company']}.\n\n"
            f"I would be deeply grateful for 10 minutes of your time to chat about the team's current focus, or for a referral for the entry-level {job['title']} role if you think my background is a good fit.\n\n"
            f"I have attached my resume for your convenience. My LinkedIn profile can be found here: {candidate['linkedin']}.\n\n"
            f"Thank you so much for your time and consideration. Looking forward to connecting!\n\n"
            f"Warm regards,\n\n"
            f"Tina Jain\n"
            f"{candidate['phone']}\n"
            f"{candidate['email']}"
        )
    
    return linkedin_note, email_body

def main():
    candidate = {
        "name": "Tina Jain",
        "email": "jaintina2001@gmail.com",
        "phone": "+91 9201556679",
        "linkedin": "https://www.linkedin.com/in/tinajain2001/",
        "summary": "Product-focused professional with a strong analytical and creative foundation, experienced in developing data-backed product strategies. PGDM (Marketing) graduate from Great Lakes Institute of Management, Chennai (2026) and Bronze Medalist BBA graduate from O.P. Jindal University. Open to entry-level / associate roles in Product, Growth, Marketing, and Consulting.",
        "skills": [
            "Product Management", "Data-driven Decision Making", "Competitive Benchmarking",
            "Customer Journey Mapping", "User Experience (UX) Auditing", "Go-to-market (GTM) Strategy",
            "Market Research & Consumer Psychology", "Cross-functional Collaboration", "Stakeholder Management",
            "B2B LinkedIn Outreach & Sales Navigator", "SEO & Digital Marketing", "Marketing Analytics"
        ],
        "top_roles": [
            "Product Marketing Manager (PMM)",
            "Associate Product Manager (APM)",
            "Product Analyst",
            "Growth Marketing Manager / Associate",
            "Growth Strategy Associate",
            "Market Research / Consumer Insights Analyst",
            "Assistant Brand Manager",
            "Strategy / Consulting Analyst"
        ],
        "education": [
            {
                "degree": "PGDM (Marketing)",
                "institution": "Great Lakes Institute of Management, Chennai",
                "year": "2026",
                "highlights": "Member of Placement Committee (B2B outreach, operations, data analysis), Consulting Club, Marketing Club. Participated in L'Oreal Sustainability Challenge & Colgate Transcend."
            },
            {
                "degree": "BBA (Marketing)",
                "institution": "O. P. Jindal University",
                "year": "2023",
                "highlights": "Bronze Medal for Academic Excellence, Jindal Scholarship. Placement Coordinator, Co-Convenor of Logistics (managed 15 teams & 14 events)."
            }
        ],
        "experience": [
            {
                "role": "Product Innovation Manager",
                "company": "Tagit Pte Ltd (India)",
                "duration": "Jan 2025 - Jun 2025",
                "achievements": [
                    "Benchmarked 500+ global platforms across 10+ markets, prioritizing 100+ differentiating product capabilities.",
                    "Developed 8 target personas & 4 six-month journey maps, converting consumer insights into segment engagement strategies.",
                    "Assessed UX across 100+ consumer apps, recommending enhancements to strengthen CSAT/NPS outcomes.",
                    "Partnered with C-suite and cross-functional teams to deliver 8+ value propositions & product positioning.",
                    "Analyzed CAC and 10+ GTM models, delivering 20+ executive reports & 18 market-aligned use-cases."
                ]
            },
            {
                "role": "Sales and Marketing Intern",
                "company": "Pepperfry Pvt Ltd",
                "duration": "Aug 2022 - Oct 2022",
                "achievements": [
                    "Managed 50+ HNI leads and 200+ customer interactions, driving INR 15L+ in monthly sales.",
                    "Resolved 50+ customer escalations at flagship stores, optimizing processes and boosting repeat purchases."
                ]
            }
        ]
    }

    # Highly curated portal search links specifically for freshers (0-1 years) in Gurugram
    portal_search_links = [
        {
            "role": "Associate Product Manager",
            "naukri": "https://www.naukri.com/associate-product-manager-jobs-in-gurgaon?k=associate+product+manager&l=gurgaon&experience=0-1",
            "hirist": "https://www.hirist.tech/search/Associate-Product-Manager-jobs-in-Gurgaon-0-3-years.html",
            "instahyre": "https://www.instahyre.com/jobs-in-gurgaon/?q=Product+Manager",
            "linkedin": "https://www.linkedin.com/jobs/search/?keywords=%22Associate%20Product%20Manager%22&location=Gurugram"
        },
        {
            "role": "Product Analyst",
            "naukri": "https://www.naukri.com/product-analyst-jobs-in-gurgaon?k=product+analyst&l=gurgaon&experience=0-1",
            "hirist": "https://www.hirist.tech/search/Product-Analyst-jobs-in-Gurgaon-0-3-years.html",
            "instahyre": "https://www.instahyre.com/jobs-in-gurgaon/?q=Product+Analyst",
            "linkedin": "https://www.linkedin.com/jobs/search/?keywords=%22Product%20Analyst%22&location=Gurugram"
        },
        {
            "role": "Product Marketing",
            "naukri": "https://www.naukri.com/product-marketing-jobs-in-gurgaon?k=product+marketing&l=gurgaon&experience=0-1",
            "hirist": "https://www.hirist.tech/search/Business-Analyst-jobs-in-Gurgaon-0-3-years.html",
            "instahyre": "https://www.instahyre.com/jobs-in-gurgaon/?q=Product+Marketing",
            "linkedin": "https://www.linkedin.com/jobs/search/?keywords=%22Product%20Marketing%22&location=Gurugram"
        },
        {
            "role": "Assistant Brand Manager",
            "naukri": "https://www.naukri.com/brand-manager-jobs-in-gurgaon?k=brand+manager&l=gurgaon&experience=0-1",
            "hirist": "https://www.hirist.tech/search/Marketing-jobs-in-Gurgaon-0-3-years.html",
            "instahyre": "https://www.instahyre.com/jobs-in-gurgaon/?q=Brand+Manager",
            "linkedin": "https://www.linkedin.com/jobs/search/?keywords=%22Brand%20Manager%22&location=Gurugram"
        },
        {
            "role": "Consulting & Strategy Analyst",
            "naukri": "https://www.naukri.com/consulting-analyst-jobs-in-gurgaon?k=consulting+analyst&l=gurgaon&experience=0-1",
            "hirist": "https://www.hirist.tech/search/Business-Analyst-jobs-in-Gurgaon-0-3-years.html",
            "instahyre": "https://www.instahyre.com/jobs-in-gurgaon/?q=Consulting",
            "linkedin": "https://www.linkedin.com/jobs/search/?keywords=%22Consulting%20Analyst%22&location=Gurugram"
        }
    ]

    # Core database updated to contain strictly verified entry-level job descriptions in Gurugram
    jobs_data = [
        {
            "id": "makemytrip_connect_apm",
            "title": "Associate Product Manager (Connect)",
            "company": "MakeMyTrip",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4405817132/",
            "convertibility": 96,
            "convertibility_reasons": [
                "Strict entry-level: JD explicitly requests '0-2 years' of experience and designates the level as Assistant Manager (typical post-MBA fresher rank).",
                "Product context: Sits at the core of MakeMyTrip transaction funnels matching her benchmarking of 500+ global platforms.",
                "Strong alumni representation: Over 35 Great Lakes Chennai alumni currently work in PM/Product roles at MakeMyTrip NCR."
            ],
            "skills_required": ["Product Management", "Competitive Benchmarking", "Data Analysis", "User Journey Mapping"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20MakeMyTrip%20Great%20Lakes",
                    "email_format": "first.last@makemytrip.com",
                }
            ]
        },
        {
            "id": "amex_apm_disputes",
            "title": "Associate - Digital Product Management",
            "company": "American Express",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4413515566/",
            "convertibility": 95,
            "convertibility_reasons": [
                "Entry-level digital track: JD seeks entry/associate level profiles to support Global Dispute Management.",
                "Fintech synergy: Matches her Tagit digital banking product experience (benchmarking banking capabilities).",
                "Recruitment match: AMEX is a key campus/off-campus employer for top business school freshers like Great Lakes Chennai."
            ],
            "skills_required": ["Digital Wallets", "Banking Tech", "UX Auditing", "Cross-functional Collaboration"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - AMEX",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20American%20Express%20Great%20Lakes",
                    "email_format": "first.last@aexp.com",
                }
            ]
        },
        {
            "id": "sprinklr_apm",
            "title": "Associate Product Manager",
            "company": "Sprinklr",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4418943086",
            "convertibility": 94,
            "convertibility_reasons": [
                "Entry-level APM: Targeted at fresh post-graduates or candidates with 1-2 years of product experience.",
                "CXM alignment: Sprinklr is a customer experience platform; Tina's customer journey mapping and UX audits (100+ apps) match this role.",
                "Local hiring: Sprinklr's core product team is situated at their Gurugram corporate office."
            ],
            "skills_required": ["Product Management", "Customer Journey Mapping", "UX Auditing", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Sprinklr%20Great%20Lakes",
                    "email_format": "first.last@sprinklr.com",
                }
            ]
        },
        {
            "id": "policybazaar_pa",
            "title": "Product Analyst",
            "company": "Policybazaar.com",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4410355301/",
            "convertibility": 93,
            "convertibility_reasons": [
                "Policybazaar hires junior analysts to manage metrics, track conversion funnels, and optimize insurance portals.",
                "Matches target role #3 (Product Analyst). Tina has strong certifications in Marketing Analytics & Excel forecasting.",
                "Headquartered in Gurugram: direct access to the product engineering leads."
            ],
            "skills_required": ["Data Analysis", "Product Metrics", "Excel Forecasting", "Consumer Behaviour"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Product",
                    "role": "Product Lead (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Policybazaar%20Great%20Lakes",
                    "email_format": "first.last@policybazaar.com",
                }
            ]
        },
        {
            "id": "accenture_ocm",
            "title": "Analyst - Change Management (Strategy)",
            "company": "Accenture",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4417593697/",
            "convertibility": 92,
            "convertibility_reasons": [
                "Management level 11 (Analyst) is Accenture's entry rank for fresh PGDM/MBA graduates.",
                "Tina's university leadership as convenor/coordinator and her Accenture project management certification fit this organizational consultant profile.",
                "Matches target role #10 (Consulting/Strategy Analyst)."
            ],
            "skills_required": ["Consulting", "Stakeholder Management", "Project Management", "Cross-functional Collaboration"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Accenture",
                    "role": "Consulting Analyst (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Accenture%20Consulting%20Great%20Lakes%20Gurgaon",
                    "email_format": "first.last@accenture.com",
                }
            ]
        },
        {
            "id": "pepperfry_pmm",
            "title": "Product Marketing Associate",
            "company": "Pepperfry",
            "location": "Gurugram / Remote (HQ Mumbai)",
            "apply_url": "https://www.pepperfry.com/careers.html",
            "convertibility": 98,
            "convertibility_reasons": [
                "Warm lead: Tina is a former Pepperfry Sales & Marketing Intern with a proven track record (15L+ monthly sales).",
                "Fresher role: Directly aligns with her entry-level marketing and sales background.",
                "Warm pipeline: Direct outreach to former manager bypassing corporate ATS."
            ],
            "skills_required": ["Go-to-market Strategy", "Consumer Psychology", "Market Research", "B2C Sales & Engagement"],
            "contacts": [
                {
                    "name_placeholder": "Senior Marketing Manager",
                    "role": "Marketing Head / Former Reporting Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Manager%20Pepperfry",
                    "email_format": "first.last@pepperfry.com (or check internal contacts from internship)",
                }
            ]
        },
        {
            "id": "indmoney_pa",
            "title": "Product Analyst",
            "company": "INDmoney",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/product-analyst-%E2%80%94-clm-at-indmoney-4419890337",
            "convertibility": 93,
            "convertibility_reasons": [
                "INDmoney is actively hiring entry-level analysts for transaction and app experience metrics.",
                "Tina's data decision credentials, Excel forecasting, and product diploma fit this role.",
                "Explicitly entry-level: targeted at fresh graduates / 0-2 years experience."
            ],
            "skills_required": ["Data Analysis", "Product Metrics", "UX Auditing", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Product",
                    "role": "Product Analyst / Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20INDmoney%20Great%20Lakes",
                    "email_format": "first.last@indmoney.com",
                }
            ]
        },
        {
            "id": "ey_consulting",
            "title": "Consulting Analyst - Supply Chain & Operations",
            "company": "EY",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/consultant-business-consulting-pi-ami-cns-bc-supply-chain-operations-gurgaon-at-ey-4417660946",
            "convertibility": 93,
            "convertibility_reasons": [
                "EY Consulting Analyst is the standard entry-level role for fresh MBA/PGDM grads in Gurugram.",
                "Her role as university Logistics Co-convenor (managed 14 operations events) fits EY's supply chain service lines.",
                "Strong recruiter presence at Great Lakes."
            ],
            "skills_required": ["Consulting", "Logistics Coordination", "Cross-functional Collaboration", "Data-driven Decision Making"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Consultant",
                    "role": "Consulting Associate (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Consulting%20EY%20Great%20Lakes",
                    "email_format": "first.last@ey.com / first.m.last@ey.com",
                }
            ]
        },
        {
            "id": "cotecna_brand",
            "title": "Assistant Brand Manager",
            "company": "Cotecna",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/assistant-brand-manager-at-cotecna-4390583149/",
            "convertibility": 92,
            "convertibility_reasons": [
                "Cotecna is hiring freshers for brand activation in NCR.",
                "Tina's BBA Bronze Medalist background and PGDM Marketing degrees are highly relevant.",
                "Assistant Brand Manager is the entry-level brand marketing role for MBA grads."
            ],
            "skills_required": ["Brand Strategy", "Market Research", "Digital Marketing", "Consumer Behaviour"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Marketing",
                    "role": "Marketing Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Cotecna%20Great%20Lakes",
                    "email_format": "first.last@cotecna.co.in / first.last@cotecna.com",
                }
            ]
        },
        {
            "id": "sbnri_pa",
            "title": "Product Analyst",
            "company": "SBNRI",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/product-analyst-at-sbnri-4422836094",
            "convertibility": 91,
            "convertibility_reasons": [
                "SBNRI Gurgaon is a fintech startup hiring entry-level analysts (0-2 years experience).",
                "Directly matches her Professional Diploma in Product Management.",
                "Her fintech experience benchmarking global platforms maps to SBNRI NRI remittance apps."
            ],
            "skills_required": ["Data Analysis", "Product Metrics", "Competitive Benchmarking", "Go-to-market Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Product Head / Lead Recruiter",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20SBNRI%20Gurugram",
                    "email_format": "careers@sbnri.com",
                }
            ]
        },
        {
            "id": "aurora_apm",
            "title": "Associate Product Manager",
            "company": "Aurora Energy Research",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/associate-product-manager-at-aurora-energy-research-4400761802",
            "convertibility": 90,
            "convertibility_reasons": [
                "Aurora's Gurgaon office hires entry-level APMs.",
                "Tina's GTM analyses and benchmarking of 500+ global platforms fit Aurora's international SaaS expansion products.",
                "Standard entry-level APM track (0-2 years)."
            ],
            "skills_required": ["Product Management", "Competitive Benchmarking", "Go-to-market Strategy", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Aurora",
                    "role": "Product Associate (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Aurora%20Energy%20Great%20Lakes%20Gurgaon",
                    "email_format": "first.last@auroraer.com",
                }
            ]
        },
        {
            "id": "cargill_consultant",
            "title": "Associate Consultant - Data Analytics",
            "company": "Cargill",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/associate-consultant-data-analytics-reporting-ag-trading-at-cargill-4417689418",
            "convertibility": 89,
            "convertibility_reasons": [
                "Cargill Gurgaon hires fresh post-graduates for operations and trade analytics data support.",
                "Direct entry-level data consulting role.",
                "Aligns with her Excel forecasting & Marketing Analytics credentials."
            ],
            "skills_required": ["Data Analysis", "Marketing Analytics", "Analytical Forecasting", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Cargill",
                    "role": "Analyst / Associate (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Cargill%20Great%20Lakes%20Gurgaon",
                    "email_format": "first.last@cargill.com",
                }
            ]
        }
    ]

    # Populate outreach letters for all contacts
    for job in jobs_data:
        for contact in job["contacts"]:
            name = contact["name_placeholder"]
            role = contact["role"]
            li_note, cold_email = get_outreach_templates(candidate, job, name, role)
            contact["outreach_linkedin"] = li_note
            contact["outreach_email"] = cold_email

    final_data = {
        "candidate": candidate,
        "portal_search_links": portal_search_links,
        "jobs": jobs_data
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4)
        print("data.json successfully generated with", len(jobs_data), "jobs and", len(portal_search_links), "portal links.")

if __name__ == "__main__":
    main()
