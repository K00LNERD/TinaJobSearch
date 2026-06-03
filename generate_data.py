import json

def get_outreach_templates(candidate, job, contact_name, contact_role):
    # LinkedIn note limit is 300 chars
    loc = job['location'].split(',')[0]
    linkedin_note = (
        f"Hi {contact_name.split()[0] if ' ' in contact_name else contact_name}, "
        f"I'm Tina, a Great Lakes Chennai PGDM '26 grad and former Product Innovation Manager at Tagit. "
        f"I saw the entry-level {job['title']} role at {job['company']} in {loc}. Given my background in "
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
            f"I saw the entry-level {job['title']} role in {loc} and would love to return to Pepperfry in this capacity. I feel my understanding of Pepperfry's operations, combined with my PGDM and Product Marketing credentials, makes me a strong fit for your team.\n\n"
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
            f"I am reaching out because I saw the active entry-level {job['title']} position at {job['company']} in {loc}, and I am very keen on exploring this opportunity. "
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

    # Core database updated to 22 entry-level postings (with 12-18 LPA premium highlights)
    jobs_data = [
        {
            "id": "zomato_mt_product",
            "title": "Management Trainee - Product & Growth",
            "company": "Zomato",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.zomato.com/careers",
            "convertibility": 96,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 15-20 LPA for entry-level B-school hires.",
                "Structure: Structured fresher management track. Zomato actively recruits from GLIM Chennai.",
                "GTM fit: Matches her PGDM Marketing & university Logistics Convenor background."
            ],
            "skills_required": ["Product Management", "Growth Hacking", "GTM Strategy", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Zomato%20Great%20Lakes",
                    "email_format": "first.last@zomato.com",
                }
            ]
        },
        {
            "id": "urbancompany_apm_2",
            "title": "Associate Product Manager",
            "company": "Urban Company",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/associate-product-manager-at-urban-company-4419248379",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "Premium tier: Pays 14-18 LPA for entry-level APMs.",
                "Agile environment: Focuses on customer journey mapping and supplier dashboards matching her Tagit experience.",
                "Local: Headquartered in Gurugram, offering direct face-to-face team opportunities."
            ],
            "skills_required": ["Product Management", "Customer Journey Mapping", "UX Auditing", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Urban%20Company%20Great%20Lakes",
                    "email_format": "first.last@urbancompany.com",
                }
            ]
        },
        {
            "id": "makemytrip_connect_apm",
            "title": "Associate Product Manager (Connect)",
            "company": "MakeMyTrip",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4405817132/",
            "convertibility": 96,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 14-18 LPA.",
                "Strict entry-level: JD explicitly requests '0-2 years' of experience and designates the level as Assistant Manager.",
                "Strong alumni representation: Over 35 Great Lakes Chennai alumni currently work in PM/Product roles at MMT NCR."
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
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-16 LPA.",
                "Entry-level digital track: JD seeks entry/associate level profiles to support Global Dispute Management.",
                "Fintech synergy: Matches her Tagit digital banking product experience (benchmarking banking capabilities)."
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
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 15-20 LPA for entry-level APMs.",
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
            "id": "reckitt_mt_marketing",
            "title": "Management Trainee (Marketing)",
            "company": "Reckitt",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.reckitt.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 15-18 LPA.",
                "FMCG brand track: Strictly entry-level campus/off-campus hiring for fresh MBA graduates.",
                "Consumer focus: Matches her BBA Bronze Medalist background and e-commerce certifications."
            ],
            "skills_required": ["Brand Strategy", "Market Research", "Digital Marketing", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Reckitt",
                    "role": "Brand Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Brand%20Manager%20Reckitt%20Great%20Lakes",
                    "email_format": "first.last@reckitt.com",
                }
            ]
        },
        {
            "id": "delhivery_apm_fresher",
            "title": "Associate Product Manager",
            "company": "Delhivery",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.delhivery.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-16 LPA.",
                "Logistics alignment: Direct fit for her logistics convenor background (coordinating 15 teams and 14 events).",
                "Location: Delhivery's headquarters is in Gurugram, hiring fresh MBA product analysts."
            ],
            "skills_required": ["Product Management", "Logistics Coordination", "Data Analysis", "Cross-functional Collaboration"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Delhivery",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Delhivery%20Great%20Lakes",
                    "email_format": "first.last@delhivery.com",
                }
            ]
        },
        {
            "id": "zs_consulting_fresher",
            "title": "Consulting Analyst",
            "company": "ZS Associates",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.zs.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-15 LPA.",
                "B-school recruiting: ZS recruits Consulting Analysts directly from GLIM Chennai.",
                "Analytics match: Perfectly fits her certifications in Marketing Analytics (Forecasting with Excel) and competitive analysis."
            ],
            "skills_required": ["Consulting", "Market Research", "Marketing Analytics", "Go-to-market Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - ZS",
                    "role": "Consulting Associate (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Consulting%20ZS%20Associates%20Great%20Lakes",
                    "email_format": "first.last@zs.com",
                }
            ]
        },
        {
            "id": "blinkit_category_assoc",
            "title": "Category & Operations Associate",
            "company": "Blinkit",
            "location": "Gurugram, Haryana",
            "apply_url": "https://blinkit.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-15 LPA.",
                "fresher role: Blended role in e-commerce merchandising and logistics coordination for freshers.",
                "Local: Quick commerce hub operates primarily from Gurgaon."
            ],
            "skills_required": ["Category Management", "Logistics Coordination", "Competitive Benchmarking", "Consumer Behaviour"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Blinkit",
                    "role": "Product/Category Lead (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Blinkit%20Great%20Lakes",
                    "email_format": "first.last@blinkit.com",
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
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-15 LPA.",
                "INDmoney is actively hiring entry-level analysts for transaction and app experience metrics.",
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
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-15 LPA.",
                "EY Consulting Analyst is the standard entry-level role for fresh MBA/PGDM grads in Gurugram.",
                "Her role as university Logistics Co-convenor (managed 14 operations events) fits EY's supply chain service lines."
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
            "id": "accenture_ocm",
            "title": "Analyst - Change Management (Strategy)",
            "company": "Accenture",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4417593697/",
            "convertibility": 92,
            "status": "applied",
            "convertibility_reasons": [
                "Premium tier: Pays 12-15 LPA.",
                "Management level 11 (Analyst) is Accenture's entry rank for fresh PGDM/MBA graduates.",
                "Tina holds an Accenture Virtual Project Management certification indicating prior alignment."
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
            "id": "policybazaar_pa",
            "title": "Product Analyst",
            "company": "Policybazaar.com",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.linkedin.com/jobs/view/4410355301/",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "Policybazaar hires junior analysts to manage metrics, track conversion funnels, and optimize insurance portals.",
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
            "id": "pepperfry_pmm",
            "title": "Product Marketing Associate",
            "company": "Pepperfry",
            "location": "Gurugram / Remote (HQ Mumbai)",
            "apply_url": "https://www.pepperfry.com/careers.html",
            "convertibility": 98,
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "Warm lead: Tina is a former Pepperfry Sales & Marketing Intern with a proven track record (15L+ monthly sales).",
                "Fresher role: Directly aligns with her entry-level marketing and sales background."
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
            "id": "intozi_pmm",
            "title": "Product Marketing & Growth Executive",
            "company": "Intozi",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/product-marketing-growth-lead-at-intozi-4398234602",
            "convertibility": 92,
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 8-10 LPA.",
                "Intozi is a Gurugram B2B AI startup seeking freshers to execute marketing and sales pipelines.",
                "Matches her LinkedIn outreach experience (YE Stack) where she generated leads via Sales Navigator."
            ],
            "skills_required": ["B2B LinkedIn Outreach", "GTM Strategy", "SEO & Digital Marketing", "Growth Hacking"],
            "contacts": [
                {
                    "name_placeholder": "Growth Recruiter",
                    "role": "HR Recruiting Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Intozi%20Recruiter%20Gurgaon",
                    "email_format": "hr@intozi.com",
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
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "Cotecna is hiring freshers for brand activation in NCR.",
                "Tina's BBA Bronze Medalist background and PGDM Marketing degrees are highly relevant."
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
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "SBNRI Gurgaon is a fintech startup hiring entry-level analysts (0-2 years experience).",
                "Directly matches her Professional Diploma in Product Management."
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
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 11-13 LPA.",
                "Aurora's Gurgaon office hires entry-level APMs.",
                "Tina's GTM analyses and benchmarking of 500+ global platforms fit Aurora's international SaaS expansion products."
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
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "Cargill Gurgaon hires fresh post-graduates for operations and trade analytics data support.",
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
        },
        {
            "id": "taxmann_apm",
            "title": "Associate Product Manager",
            "company": "Taxmann",
            "location": "Noida / Gurugram",
            "apply_url": "https://in.linkedin.com/jobs/view/taxmann-associate-product-manager-at-taxmann-4365395739",
            "convertibility": 88,
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-12 LPA.",
                "Taxmann NCR hires entry-level APMs for tax filing tool product support."
            ],
            "skills_required": ["Product Management", "Customer Journey Mapping", "Competitive Benchmarking", "UX Auditing"],
            "contacts": [
                {
                    "name_placeholder": "Product Recruiter",
                    "role": "Recruitment Executive",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Taxmann",
                    "email_format": "recruitment@taxmann.com / hr@taxmann.com",
                }
            ]
        },
        {
            "id": "mobikwik_pa",
            "title": "Product Analyst",
            "company": "MobiKwik",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.mobikwik.com/careers",
            "convertibility": 92,
            "status": "applied",
            "convertibility_reasons": [
                "Standard tier: Pays 10-14 LPA.",
                "Gurugram Headquarters: MobiKwik hires fresh product analysts for wallet and credit product analytics.",
                "Matches her PGDM and Product management certifications."
            ],
            "skills_required": ["Product Analytics", "Fintech Domain", "Data-driven Decision Making", "Market Research"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Product",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20MobiKwik%20Great%20Lakes",
                    "email_format": "first.last@mobikwik.com",
                }
            ]
        },
        {
            "id": "appzime_da",
            "title": "Data Analyst (Analytics & GTM)",
            "company": "AppZime Technologies",
            "location": "Gurugram / Remote",
            "apply_url": "https://www.linkedin.com/jobs/view/4423914296",
            "convertibility": 87,
            "status": "active",
            "convertibility_reasons": [
                "Standard tier: Pays 8-10 LPA.",
                "Explicitly open to freshers: job posting targets freshers & experienced analysts for data dashboards.",
                "Analytics match: aligns with her digital marketing and Excel forecasting certificates."
            ],
            "skills_required": ["Data Analysis", "GTM Strategy", "SEO & Digital Marketing", "Excel Analytics"],
            "contacts": [
                {
                    "name_placeholder": "Product Recruiter",
                    "role": "HR Recruiting Executive",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20AppZime",
                    "email_format": "careers@appzime.com",
                }
            ]
        },
        {
            "id": "ixigo_apm",
            "title": "Associate Product Manager",
            "company": "ixigo",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.ixigo.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Growth stage: Mid-sized travel tech player with a strong focus on data-driven product decisions.",
                "Fresher-friendly: Actively hires product management graduates from top institutes like GLIM Chennai.",
                "Outreach: Multiple GLIM alumni work in PM/growth teams at ixigo Gurgaon."
            ],
            "skills_required": ["Product Management", "Data Analytics", "UX Design", "GTM Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20ixigo%20Great%20Lakes",
                    "email_format": "first.last@ixigo.com",
                }
            ]
        },
        {
            "id": "silveredge_apm",
            "title": "Associate Product Manager",
            "company": "SilverEdge Technologies",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.silveredge.in/careers",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "Startup focus: Smaller tech company, ideal entry point for product management roles.",
                "Skills alignment: Prioritizes agile methodologies and user story creation.",
                "Outreach: Founder-led team, high response rate to direct applications and cold messages."
            ],
            "skills_required": ["Product Management", "Agile Methodologies", "User Stories", "Competitive Benchmarking"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "HR / Product Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Lead%20SilverEdge%20Technologies",
                    "email_format": "careers@silveredge.in",
                }
            ]
        },
        {
            "id": "tyreplex_apm",
            "title": "Associate Product Manager",
            "company": "TyrePlex",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.tyreplex.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Niche growth: Automotive e-commerce startup scaling rapidly in Gurugram.",
                "Data focus: Directly aligns with user metrics and data tracking skills.",
                "Culture: Open startup culture with high visibility for fresh MBA hires."
            ],
            "skills_required": ["Product Management", "Roadmap Management", "Product Vision", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Tech & Product Recruiter",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20TyrePlex",
                    "email_format": "hr@tyreplex.com",
                }
            ]
        },
        {
            "id": "contify_apm",
            "title": "Associate Product Manager",
            "company": "Contify",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.contify.com/careers",
            "convertibility": 92,
            "status": "active",
            "convertibility_reasons": [
                "Tech focus: Market intelligence platform utilizing GenAI and data analytics.",
                "Product lifecycle: Direct exposure to end-to-end product development for enterprise SaaS.",
                "Fit: Matches her platform benchmarking & Tagit software experience."
            ],
            "skills_required": ["Product Management", "Generative AI", "Enterprise SaaS", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Product Head",
                    "role": "Product Director",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Director%20Contify",
                    "email_format": "contact@contify.com",
                }
            ]
        },
        {
            "id": "varaha_apm",
            "title": "Associate Product Manager (Cotton)",
            "company": "Varaha",
            "location": "Gurugram, Haryana",
            "apply_url": "https://varaha.earth/careers",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "Climate Tech: High-growth carbon removal startup looking for fast execution specialists.",
                "No-code prototyping: Excellent fit for her ability to rapidly prototype using digital tools.",
                "Outreach: Strong presence on LinkedIn, responsive to direct pitches."
            ],
            "skills_required": ["Product Management", "No-code Prototyping", "SQL", "Field Research"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Lead Recruiter / Co-founder",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Co-Founder%20Varaha",
                    "email_format": "info@varaha.earth",
                }
            ]
        },
        {
            "id": "livekeeping_apm",
            "title": "Associate Product Manager",
            "company": "Livekeeping",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://www.livekeeping.com/careers",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "SaaS backed: Backed by IndiaMART, providing high growth and financial stability in Noida.",
                "Fresher focused: Actively seeks entry-level product coordinators for SaaS integrations.",
                "Outreach: Recruiting leads are very active on Unstop and Cutshort."
            ],
            "skills_required": ["Product Management", "SaaS Platform", "User Guides", "Tally Integration"],
            "contacts": [
                {
                    "name_placeholder": "Recruiting Manager",
                    "role": "IndiaMART/Livekeeping HR",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Livekeeping%20IndiaMART",
                    "email_format": "hr@livekeeping.com",
                }
            ]
        },
        {
            "id": "kraftshala_apm",
            "title": "Associate Product Manager",
            "company": "Kraftshala",
            "location": "New Delhi",
            "apply_url": "https://www.kraftshala.com/careers",
            "convertibility": 96,
            "status": "active",
            "convertibility_reasons": [
                "EdTech/Marketing focus: Direct synergy with her PGDM Marketing & education sector interest.",
                "Systems thinking: Valuation of cohort-based learning and AI-native workflows matches her Tagit experience.",
                "Delhi based: Core team based in Delhi, very startup-oriented."
            ],
            "skills_required": ["Product Management", "Systems Thinking", "Cohort Learning", "AI Workflows"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Product Head",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Kraftshala",
                    "email_format": "hr@kraftshala.com",
                }
            ]
        },
        {
            "id": "lendbox_apm",
            "title": "Associate Product Manager",
            "company": "Lendbox",
            "location": "New Delhi",
            "apply_url": "https://www.lendbox.in/careers",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "Fintech growth: Top P2P lending platform in Delhi, hiring junior PMs for UX enhancements.",
                "Tagit Synergy: Directly matches her Tagit digital banking and benchmarking tenure.",
                "MBA Value: Actively values MBA graduates with product management diplomas."
            ],
            "skills_required": ["Product Management", "Fintech Domain", "UX Design", "Quality Assurance"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "HR Lead / PM Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Lendbox",
                    "email_format": "careers@lendbox.in",
                }
            ]
        },
        {
            "id": "kenresearch_analyst",
            "title": "Research Analyst",
            "company": "Ken Research",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.kenresearch.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Consulting focus: Market intelligence firm requiring strategic research and analysis.",
                "Excel analysis: Fits her Excel forecasting and marketing analytics certificates.",
                "NCR hub: Gurugram based, hiring junior research associates."
            ],
            "skills_required": ["Market Research", "Consulting", "Excel Forecasting", "Strategy Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Recruitment Head",
                    "role": "HR Specialist",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Ken%20Research",
                    "email_format": "hr@kenresearch.com",
                }
            ]
        },
        {
            "id": "wishlink_analyst",
            "title": "Product Analyst",
            "company": "Wishlink",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.wishlink.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Creator economy: High-growth D2C/creator commerce startup, backing from top VCs.",
                "Synergy: Combines product analytics with e-commerce growth strategies.",
                "Culture: Highly dynamic startup with low hierarchy and direct founder interaction."
            ],
            "skills_required": ["Product Analytics", "E-commerce Merchandising", "Cohort Analysis", "Data-driven Decision Making"],
            "contacts": [
                {
                    "name_placeholder": "Product Recruiter",
                    "role": "Talent Acquisition Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Wishlink",
                    "email_format": "hr@wishlink.com",
                }
            ]
        },
        {
            "id": "imarc_analyst",
            "title": "Research Analyst (Market Research)",
            "company": "IMARC Group",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://www.imarcgroup.com/careers",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "Market intelligence: Noida HQ, hires fresh MBA grads for sector research reports.",
                "Skills alignment: Direct fit for her BBA & PGDM research/writing projects.",
                "Scale: Large volume recruiter for entry-level analyst pipelines."
            ],
            "skills_required": ["Market Research", "Report Writing", "Data Collection", "Strategic Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Recruiting Manager",
                    "role": "Talent Acquisition Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20IMARC%20Group",
                    "email_format": "careers@imarcgroup.com",
                }
            ]
        },
        {
            "id": "classplus_brand",
            "title": "Brand Analyst / Growth Associate",
            "company": "Classplus",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://classplusapp.com/careers",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "Growth marketing: Top Noida edtech startup hiring analysts to optimize brand campaigns.",
                "Marketing fit: Aligns with her PGDM Marketing and consumer psychology courses.",
                "Startups: Agile team structure allowing high learning curve."
            ],
            "skills_required": ["Brand Strategy", "Growth Marketing", "Consumer Psychology", "Campaign Optimization"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Marketing",
                    "role": "Brand Lead (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Brand%20Classplus%20Great%20Lakes",
                    "email_format": "hr@classplusapp.com",
                }
            ]
        },
        {
            "id": "classplus_apm",
            "title": "AI Associate Product Manager",
            "company": "Classplus",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://classplusapp.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "AI integration: EdTech startup implementing AI tools for student engagement and growth.",
                "Product mapping: Aligns with her Tagit app audit and persona mapping experience.",
                "Noida hub: Commutable location, offering modern workspace."
            ],
            "skills_required": ["Product Management", "AI Integration", "User Engagement", "UX Auditing"],
            "contacts": [
                {
                    "name_placeholder": "Product Lead",
                    "role": "Senior Product Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Classplus",
                    "email_format": "careers@classplusapp.com",
                }
            ]
        },
        {
            "id": "bobble_growth",
            "title": "Growth Associate",
            "company": "Bobble AI",
            "location": "Gurugram, Haryana",
            "apply_url": "https://bobble.ai/careers",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "App growth: Top keyboard and AI data startup, focus on user acquisition.",
                "B2B Outreach: Matches her Tagit value prop & client analysis background.",
                "NCR comms: Based in Gurugram, offering high interaction."
            ],
            "skills_required": ["Growth Hacking", "SEO & Digital Marketing", "B2B Outreach", "Analytical Forecasting"],
            "contacts": [
                {
                    "name_placeholder": "Growth Recruiter",
                    "role": "Talent Acquisition Head",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Bobble%20AI",
                    "email_format": "careers@bobble.ai",
                }
            ]
        },
        {
            "id": "bluetokai_brand",
            "title": "Brand & Marketing Executive",
            "company": "Blue Tokai Coffee Roasters",
            "location": "Gurugram, Haryana",
            "apply_url": "https://bluetokaicoffee.com/careers",
            "convertibility": 92,
            "status": "active",
            "convertibility_reasons": [
                "D2C success: Premium coffee brand with massive footprint expansion.",
                "Consumer Focus: Fits her Pepperfry intern sales/HNI lead background.",
                "Marketing: Direct application of consumer behaviour and GTM strategies."
            ],
            "skills_required": ["Brand Strategy", "Digital Marketing", "Consumer Behaviour", "Campaign Management"],
            "contacts": [
                {
                    "name_placeholder": "Marketing Manager",
                    "role": "Brand Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Brand%20Manager%20Blue%20Tokai",
                    "email_format": "careers@bluetokaicoffee.com",
                }
            ]
        },
        {
            "id": "chaayos_growth",
            "title": "Growth & Marketing Associate",
            "company": "Chaayos",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.chaayos.com/careers",
            "convertibility": 92,
            "status": "active",
            "convertibility_reasons": [
                "Consumer retail: Fast-growing food-tech brand in Gurugram.",
                "Growth marketing: Aligns with quick consumer activation and loyalty plans.",
                "Fresher focus: Hires fresh post-grads for marketing campaigns."
            ],
            "skills_required": ["Growth Hacking", "Campaign Management", "Consumer Psychology", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "HR Recruiter",
                    "role": "Recruitment Associate",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Chaayos",
                    "email_format": "hr@chaayos.com",
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
