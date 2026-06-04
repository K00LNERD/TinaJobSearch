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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
            "status": "applied",
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
        },
        {
            "id": "eazydiner_apm",
            "title": "Associate Product Manager",
            "company": "EazyDiner",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.eazydiner.com/careers",
            "convertibility": 95,
            "status": "applied",
            "convertibility_reasons": [
                "Growth stage: Leading restaurant booking app expanding features in Delhi NCR.",
                "Fresher alignment: JD prioritizes candidates with SQL, user journey mapping, and wireframing skills.",
                "Alumni fit: Multiple Great Lakes Chennai grads work in growth/PM teams here."
            ],
            "skills_required": ["Product Management", "SQL", "UX Prototyping", "User Research"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20EazyDiner%20Great%20Lakes",
                    "email_format": "first.last@eazydiner.com",
                }
            ]
        },
        {
            "id": "collegedekho_apm",
            "title": "Associate Product Manager",
            "company": "CollegeDekho",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.collegedekho.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "EdTech growth: Commutable Gurgaon office, scaling lead ingestion and matching products.",
                "Marketing/Growth: Direct alignment with her BBA/PGDM marketing background for onboarding flow metrics.",
                "High fit: Values candidates with diplomas in product management."
            ],
            "skills_required": ["Product Management", "Onboarding Funnels", "Data Analytics", "GTM Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Growth PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20CollegeDekho%20Great%20Lakes",
                    "email_format": "first.last@collegedekho.com",
                }
            ]
        },
        {
            "id": "cypherock_apm",
            "title": "Product Associate",
            "company": "Cypherock",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.cypherock.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Web3/SaaS startup: Smaller founder-led hardware/crypto wallet startup offering immense PM experience.",
                "Tagit overlap: Matches her benchmarking (500+ apps) and platform auditing capabilities.",
                "Direct response: Highly active co-founders hiring directly via LinkedIn and Wellfound."
            ],
            "skills_required": ["Product Management", "Competitive Benchmarking", "UX Auditing", "Platform Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Founder / Chief of Staff",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Founder%20Cypherock",
                    "email_format": "info@cypherock.com",
                }
            ]
        },
        {
            "id": "hack2skill_da",
            "title": "Product Analyst (Data & Cohorts)",
            "company": "Hack2skill",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://hack2skill.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "Community/EdTech startup: Focuses on hackathons and cohort engagement platforms in Noida.",
                "Marketing analytics: Matches her diploma credentials and Excel forecasting tools.",
                "Hiring path: Actively posts and hires junior analysts from the Noida/Delhi region."
            ],
            "skills_required": ["Data Analysis", "Cohort Engagement", "Product Metrics", "Excel Forecasting"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Recruiter",
                    "role": "HR Talent Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Hack2skill",
                    "email_format": "hr@hack2skill.com",
                }
            ]
        },
        {
            "id": "syook_apm",
            "title": "Associate Product Manager",
            "company": "Syook",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://www.syook.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "Enterprise IoT: Noida software company specializing in asset tracking platforms.",
                "B2B Outreach: Direct alignment with her Tagit enterprise analysis and CAC/GTM modeling projects.",
                "SaaS structure: Commutable Noida office, agile junior product role."
            ],
            "skills_required": ["Product Management", "B2B SaaS", "GTM Strategy", "Logistics Coordination"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Co-founder / Product Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Lead%20Syook",
                    "email_format": "careers@syook.com",
                }
            ]
        },
        {
            "id": "cashify_pmm",
            "title": "Product Marketing Associate",
            "company": "Cashify",
            "location": "New Delhi",
            "apply_url": "https://www.cashify.in/careers",
            "convertibility": 95,
            "status": "applied",
            "convertibility_reasons": [
                "Re-commerce scale: Major D2C/re-commerce startup, HQ in Gurgaon/Delhi.",
                "D2C fit: Combines e-commerce merchandising, brand positioning, and pricing campaigns.",
                "Pepperfry synergy: Fits her prior Pepperfry flagship stores intern marketing background."
            ],
            "skills_required": ["Product Marketing", "D2C Strategy", "Brand Positioning", "Campaign Management"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Marketing",
                    "role": "Brand / Growth Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Cashify%20Great%20Lakes",
                    "email_format": "first.last@cashify.in",
                }
            ]
        },
        {
            "id": "indiagold_growth",
            "title": "Growth & Alliances Associate",
            "company": "Indiagold",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.indiagold.co/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "Fintech gold loan: High-growth fintech startup backed by top VCs.",
                "B2B/B2C: Matches her sales intern experience (HNI leads, monthly sales targets).",
                "Reference paths: Active hiring for fresher associates in Gurgaon office."
            ],
            "skills_required": ["Growth Hacking", "B2C Sales & Engagement", "Partnerships", "Lead Management"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Talent Acquisition Head",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20Indiagold",
                    "email_format": "careers@indiagold.co",
                }
            ]
        },
        {
            "id": "progcap_analyst",
            "title": "Strategy & Operations Analyst",
            "company": "Progcap",
            "location": "New Delhi",
            "apply_url": "https://www.progcap.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "Fintech GTM: Enterprise credit platform for retailers, backed by Tiger Global.",
                "Logistics fit: Perfectly fits her university Logistics Co-convenor background (managing 15 teams).",
                "MBA target: Actively recruits fresh B-school graduates in Delhi."
            ],
            "skills_required": ["Strategy Analysis", "Operations Management", "Fintech Domain", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Operations Director",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Operations%20Progcap",
                    "email_format": "hr@progcap.com",
                }
            ]
        },
        {
            "id": "planetspark_growth",
            "title": "Business Growth Associate",
            "company": "PlanetSpark",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.planetspark.in/careers",
            "convertibility": 95,
            "status": "applied",
            "convertibility_reasons": [
                "EdTech speed: Fast-paced sales and brand growth environment, large hiring pool.",
                "Consumer behaviour: Direct application of B2C sales and student user acquisition strategies.",
                "Gurgaon base: Massive modern corporate center located in Sector 44."
            ],
            "skills_required": ["Growth Hacking", "B2C Sales & Engagement", "Consumer Behaviour", "Campaign Management"],
            "contacts": [
                {
                    "name_placeholder": "Recruitment Executive",
                    "role": "HR Executive",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Recruiter%20PlanetSpark",
                    "email_format": "hr@planetspark.in",
                }
            ]
        },
        {
            "id": "leverageedu_pmm",
            "title": "Product Marketing Associate",
            "company": "Leverage Edu",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://leverageedu.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "Study abroad tech: EdTech startup expanding its digital and visa platforms in Noida.",
                "SEO & Growth: Direct alignment with her SEO and digital marketing credentials.",
                "Outreach: Founder-led environment with strong alumni presence."
            ],
            "skills_required": ["Product Marketing", "SEO & Digital Marketing", "GTM Strategy", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Marketing",
                    "role": "Marketing Lead (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Leverage%20Edu%20Great%20Lakes",
                    "email_format": "first.last@leverageedu.com",
                }
            ]
        },
        {
            "id": "shiprocket_pa",
            "title": "Product Analyst (E-commerce Operations)",
            "company": "Shiprocket",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.shiprocket.in/careers",
            "convertibility": 95,
            "status": "applied",
            "convertibility_reasons": [
                "Logistics tech unicorn: Leading SaaS platform for D2C logistics management.",
                "Logistics synergy: Matches her university Logistics Convenor background.",
                "Data skills: Heavy focus on analytics dashboard mapping, SQL, and cohort tracking."
            ],
            "skills_required": ["Product Analytics", "Logistics Coordination", "SQL", "Dashboard Mapping"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Shiprocket%20Great%20Lakes",
                    "email_format": "first.last@shiprocket.com",
                }
            ]
        },
        {
            "id": "ofbusiness_strategy",
            "title": "Strategy Associate",
            "company": "OfBusiness",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.ofbusiness.com/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "B2B giant: Industrial B2B procurement and credit platform, HQ in Gurgaon.",
                "Business GTM: Aligns with her corporate sales leads and internship operations management.",
                "Hiring: Fast-growth strategy team hiring MBA freshers."
            ],
            "skills_required": ["Strategy Analysis", "B2B Sales & Engagement", "Operations Management", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Strategy",
                    "role": "Strategy Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Strategy%20OfBusiness%20Great%20Lakes",
                    "email_format": "first.last@ofbusiness.com",
                }
            ]
        },
        {
            "id": "lenskart_apm",
            "title": "Associate Product Manager (Store Tech)",
            "company": "Lenskart",
            "location": "Gurugram / Delhi NCR",
            "apply_url": "https://www.lenskart.com/careers",
            "convertibility": 95,
            "status": "applied",
            "convertibility_reasons": [
                "Omnichannel scale: PM role for retail store dashboards and app experiences.",
                "Pepperfry match: Aligns with her Pepperfry retail store internship.",
                "Local hub: Headquarters in Gurgaon, strong team representation."
            ],
            "skills_required": ["Product Management", "UX Auditing", "Category Management", "Cross-functional Collaboration"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Lenskart%20Great%20Lakes",
                    "email_format": "first.last@lenskart.in",
                }
            ]
        },
        {
            "id": "honasa_brand",
            "title": "Brand Executive",
            "company": "Mamaearth",
            "location": "Gurugram, Haryana",
            "apply_url": "https://honasaconsumer.com/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "D2C FMCG: India's top beauty D2C group, recruiting Brand Executives in Gurgaon.",
                "Marketing fit: Strong alignment with her BBA/PGDM marketing core.",
                "GLIM Alumni: Multiple alumni work in brand team pipelines."
            ],
            "skills_required": ["Brand Strategy", "Campaign Management", "Consumer Psychology", "Market Research"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Brand PM",
                    "role": "Brand Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Brand%20Manager%20Honasa%20Great%20Lakes",
                    "email_format": "first.last@honasa.in",
                }
            ]
        },
        {
            "id": "dukaan_growth",
            "title": "Growth Hacker / Product Marketer",
            "company": "Dukaan",
            "location": "Noida / Gurugram",
            "apply_url": "https://mydukaan.io/careers",
            "convertibility": 93,
            "status": "applied",
            "convertibility_reasons": [
                "SaaS platform: Direct application of onboarding flows and conversion funnel optimizations.",
                "Benchmarking: Direct fit for her platform auditing and user persona mapping experience.",
                "Founder-led: Quick decisions, highly visible role for execution-driven graduates."
            ],
            "skills_required": ["Growth Hacking", "Product Marketing", "Onboarding Funnels", "UX Auditing"],
            "contacts": [
                {
                    "name_placeholder": "Growth Lead",
                    "role": "Marketing Head",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Dukaan",
                    "email_format": "careers@mydukaan.io",
                }
            ]
        },
        {
            "id": "sleephyowl_marketing",
            "title": "Digital Marketing Executive",
            "company": "Sleepy Owl Coffee",
            "location": "New Delhi",
            "apply_url": "https://sleepyowl.co/careers",
            "convertibility": 94,
            "status": "applied",
            "convertibility_reasons": [
                "D2C retail: High-growth artisanal coffee brand, Delhi based.",
                "Marketing execution: Aligns with her digital marketing and lead generation credentials.",
                "Consumer insights: Direct application of PGDM consumer psychology analytics."
            ],
            "skills_required": ["Digital Marketing", "SEO & Digital Marketing", "Consumer Behaviour", "Campaign Management"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Brand Lead / HR Recruiter",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Sleepy%20Owl",
                    "email_format": "hello@sleepyowl.co",
                }
            ]
        },
        {
            "id": "power2sme_ops",
            "title": "Management Trainee (Operations & Procurement)",
            "company": "Power2SME Pvt Ltd",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.power2sme.com/careers",
            "convertibility": 92,
            "status": "active",
            "convertibility_reasons": [
                "B2B procurement platform aligns with her B2B marketing project background.",
                "Excellent match for her logistics co-convenor and operations planning skills.",
                "NCR based: Headquartered in Udyog Vihar, Gurugram, offering direct face-to-face team opportunities."
            ],
            "skills_required": ["Operations Management", "B2B Marketing", "Procurement Strategy", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Operations & Recruitment Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Power2SME%20Operations%20Recruitment",
                    "email_format": "careers@power2sme.com",
                }
            ]
        },
        {
            "id": "onemetric_growth",
            "title": "Growth Marketing Analyst",
            "company": "Onemetric",
            "location": "Gurugram, Haryana",
            "apply_url": "https://growtomation.foundit.in/",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "RevOps & B2B growth agency. Directly leverages her high-volume LinkedIn outreach (Sales Navigator) experience.",
                "Matches her remote SEO Externship using 5 AI tools to generate high-performing content.",
                "Local hiring: Growing team based in Gurugram, values marketing analytics."
            ],
            "skills_required": ["Growth Hacking", "B2B LinkedIn Outreach", "SEO & Digital Marketing", "Marketing Analytics"],
            "contacts": [
                {
                    "name_placeholder": "Growth Recruiter",
                    "role": "Talent Acquisition Head",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Onemetric%20Recruiter",
                    "email_format": "careers@onemetric.co",
                }
            ]
        },
        {
            "id": "tentimes_floor",
            "title": "Business Development Executive (Virtual Events)",
            "company": "Floor (by 10Times)",
            "location": "Noida, Uttar Pradesh",
            "apply_url": "https://10times.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "10Times Floor is a global virtual event and networking community platform based in Noida.",
                "Direct alignment with her Co-Convenor Logistics role (led 15 teams and managed 14 events).",
                "Placement Coordinator background matches B2B engagement and corporate networking."
            ],
            "skills_required": ["Logistics Coordination", "Event Management", "B2B Sales & Engagement", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Manager",
                    "role": "Recruitment Executive",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=10Times%20Floor%20Recruiter",
                    "email_format": "hr@10times.com",
                }
            ]
        },
        {
            "id": "akasaair_training",
            "title": "Operations & Training Coordinator",
            "company": "Akasa Air Learning Academy",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.akasaair.com/careers",
            "convertibility": 91,
            "status": "active",
            "convertibility_reasons": [
                "Corporate operations track at Akasa Air Learning Academy in Gurgaon.",
                "Matches her logistics management, scheduling, and placement operations background.",
                "Fast-growing aviation brand valuing process-driven post-graduates."
            ],
            "skills_required": ["Operations Management", "Logistics Coordination", "Scheduling", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Training Recruiter",
                    "role": "Akasa Air Talent Acquisition",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Akasa%20Air%20Recruiter%20Gurgaon",
                    "email_format": "careers@akasaair.com",
                }
            ]
        },
        {
            "id": "tecnova_consultant",
            "title": "Research Analyst - Market Entry & Growth Strategy",
            "company": "Tecnova India",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.tecnovaglobal.com/careers",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "Premium consulting firm specializing in India entry and expansion strategies.",
                "Matches her consulting club membership, research dissertation, and competitive benchmarking.",
                "Headquartered in Gurgaon with high preference for MBA grads with marketing & consulting focus."
            ],
            "skills_required": ["Market Research", "Consulting", "Go-to-market Strategy", "Competitive Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Hiring Coordinator",
                    "role": "Consulting Recruitment Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Tecnova%20India%20Recruiter",
                    "email_format": "jobs@tecnovaglobal.com",
                }
            ]
        },
        {
            "id": "wizfair_ops",
            "title": "Travel Operations Associate",
            "company": "Wizfair Travels",
            "location": "Gurugram, Haryana",
            "apply_url": "https://wizfairtravels.com/",
            "convertibility": 90,
            "status": "active",
            "convertibility_reasons": [
                "Travel services startup in Gurgaon hiring operations associates.",
                "Synergizes with her customer support, client relations, and Pepperfry customer interaction (managed 200+ clients).",
                "Logistics coordination skills apply directly to travel bookings and vendor management."
            ],
            "skills_required": ["B2C Sales & Engagement", "Customer Support", "Operations Management", "Logistics Coordination"],
            "contacts": [
                {
                    "name_placeholder": "Operations Lead",
                    "role": "Operations Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Wizfair%20Travels%20Operations",
                    "email_format": "hr@wizfairtravels.com",
                }
            ]
        },
        {
            "id": "lcx_analyst",
            "title": "Crypto Research Analyst",
            "company": "LCX Tech",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.lcx.com/careers",
            "convertibility": 92,
            "status": "active",
            "convertibility_reasons": [
                "Crypto exchange and tokenization platform with major operations in Gurgaon.",
                "Directly leverages her benchmarking of 500+ global platforms and competitive intelligence.",
                "Ideal for her analytical skills and professional product management diploma."
            ],
            "skills_required": ["Competitive Benchmarking", "Market Research", "Data Analysis", "Fintech Domain"],
            "contacts": [
                {
                    "name_placeholder": "Research Lead",
                    "role": "Crypto Research Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=LCX%20Research%20Gurgaon",
                    "email_format": "careers@lcx.com",
                }
            ]
        },
        {
            "id": "jagsonpal_brand",
            "title": "Brand Executive",
            "company": "Jagsonpal Pharmaceuticals",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.jagsonpal.com/careers",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "Established pharma company hiring brand executives in Gurgaon.",
                "Matches her PGDM (Marketing), Colgate Transcend campus round qualification, and e-commerce certifications.",
                "Focus on market analysis, brand execution, and consumer insights."
            ],
            "skills_required": ["Brand Strategy", "Market Research", "Digital Marketing", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Product Manager",
                    "role": "Brand Marketing Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Jagsonpal%20Brand%20Manager",
                    "email_format": "careers@jagsonpal.com",
                }
            ]
        },
        {
            "id": "richi_scm",
            "title": "Supply Chain & Procurement Analyst",
            "company": "Richi Circuitronix",
            "location": "Gurugram, Haryana",
            "apply_url": "https://circuitronix.in/",
            "convertibility": 89,
            "status": "active",
            "convertibility_reasons": [
                "Electronics manufacturing firm hiring SCM analysts in Gurgaon.",
                "Direct match for her logistics co-convenor and operations planning background.",
                "Focuses on inventory data analytics and supplier coordination."
            ],
            "skills_required": ["Logistics Coordination", "Operations Management", "Excel Analytics", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "SCM Manager",
                    "role": "Supply Chain Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Richi%20Circuitronix%20SCM",
                    "email_format": "careers@circuitronix.com",
                }
            ]
        },
        {
            "id": "shadowfax_ops",
            "title": "Operations Analyst (Last Mile)",
            "company": "Shadowfax Technologies",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.shadowfax.in/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Logistics tech unicorn with major operations hubs in NCR.",
                "Direct fit for her logistics background and operations management.",
                "Analytical role focused on fleet metrics, driver onboarding, and quick commerce delivery speeds."
            ],
            "skills_required": ["Operations Management", "Logistics Coordination", "Data Analysis", "Cross-functional Collaboration"],
            "contacts": [
                {
                    "name_placeholder": "Operations Lead",
                    "role": "Operations Manager (NCR)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Shadowfax%20Operations%20NCR",
                    "email_format": "careers@shadowfax.in",
                }
            ]
        },
        {
            "id": "pcm_travel_ops",
            "title": "Travel Operations Coordinator",
            "company": "PCM Pvt Ltd (PCM Worldwide Flights)",
            "location": "New Delhi",
            "apply_url": "https://pcmtravels.com/",
            "convertibility": 90,
            "status": "active",
            "convertibility_reasons": [
                "Travel and tour operations company based in New Delhi.",
                "Applies her customer relationship (resolved 50+ escalations at Pepperfry) and logistics coordination skills.",
                "Focus on coordination, booking management, and customer satisfaction."
            ],
            "skills_required": ["Operations Management", "Customer Support", "Logistics Coordination", "Scheduling"],
            "contacts": [
                {
                    "name_placeholder": "Operations Manager",
                    "role": "Travel Operations Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=PCM%20Travels%20Operations",
                    "email_format": "careers@pcmtravels.com",
                }
            ]
        },
        {
            "id": "novus_insights_research",
            "title": "Research Associate (Market Research)",
            "company": "Novus Insights",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.novusinsights.com/careers.php",
            "convertibility": 96,
            "status": "active",
            "convertibility_reasons": [
                "Premium research and consulting agency in Gurgaon.",
                "Directly leverages her market research training and PGDM marketing analytics credentials.",
                "Strong match for her dissertation project on trust and digital consumer behaviour."
            ],
            "skills_required": ["Market Research", "Marketing Analytics", "Excel Forecasting", "Report Writing"],
            "contacts": [
                {
                    "name_placeholder": "Research Director",
                    "role": "Research Lead (GLIM Alumni / HR)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Novus%20Insights%20Research",
                    "email_format": "careers@novusinsights.com",
                }
            ]
        },
        {
            "id": "unimrkt_research_analyst",
            "title": "Market Research Analyst",
            "company": "Unimrkt Research",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.unimrkt.com/work-with-us.php",
            "convertibility": 96,
            "status": "active",
            "convertibility_reasons": [
                "Global B2B market research firm headquartered in Udyog Vihar, Gurgaon.",
                "Directly matches her B2B outreach background (YE Stack Venture Studios client conversions).",
                "Excellent alignment with Google Digital Marketing & E-commerce credentials."
            ],
            "skills_required": ["Market Research", "B2B Outreach", "Competitive Analysis", "Secondary Research"],
            "contacts": [
                {
                    "name_placeholder": "Research Manager",
                    "role": "B2B Research Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Unimrkt%20Research%20Manager",
                    "email_format": "hr@unimrkt.com",
                }
            ]
        },
        {
            "id": "unimrkt_healthcare_assoc",
            "title": "Healthcare Research Associate",
            "company": "Unimrkt Healthcare",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.unimrkthealth.com/careers.php",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "Specialized healthcare market research firm, hiring junior associates in Gurgaon.",
                "Leverages her consumer insights, journey mapping, and secondary research capabilities.",
                "Matches her professional customer relationship management diploma."
            ],
            "skills_required": ["Market Research", "Customer Journey Mapping", "Secondary Research", "Data Collection"],
            "contacts": [
                {
                    "name_placeholder": "Healthcare Research Lead",
                    "role": "Healthcare Insights Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Unimrkt%20Healthcare%20Insights",
                    "email_format": "hr@unimrkthealth.com",
                }
            ]
        },
        {
            "id": "mfcw_product",
            "title": "E-commerce Product Analyst",
            "company": "Mahindra First Choice Wheels",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.mahindrafirstchoice.com/careers",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "Used vehicle e-commerce leader, hiring analysts for store tech & online platform enhancements.",
                "Strong synergy with her Tagit experience in app audits, customer journey maps, and GTM modeling.",
                "Headquartered in Gurgaon, providing high visibility in product operations."
            ],
            "skills_required": ["Product Management", "UX Auditing", "Competitive Benchmarking", "Data Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Product Lead",
                    "role": "Digital Product Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Mahindra%20First%20Choice",
                    "email_format": "careers.mfcw@mahindra.com",
                }
            ]
        },
        {
            "id": "carandbike_growth",
            "title": "Digital Marketing Executive",
            "company": "carandbike",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.carandbike.com/",
            "convertibility": 93,
            "status": "active",
            "convertibility_reasons": [
                "Automotive portal under MFCW group, expanding digital acquisition channels.",
                "Direct match for her remote SEO Externship (AI blogs) and Google Digital Marketing certifications.",
                "Fits her retail client interaction and brand promotion background (Pepperfry)."
            ],
            "skills_required": ["SEO & Digital Marketing", "Brand Strategy", "Campaign Management", "Consumer Behaviour"],
            "contacts": [
                {
                    "name_placeholder": "Marketing Head",
                    "role": "Digital Marketing Manager",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Marketing%20Manager%20carandbike",
                    "email_format": "marketing@carandbike.com",
                }
            ]
        },
        {
            "id": "zoom_media_ops",
            "title": "Media Operations Coordinator",
            "company": "Zoom Communications",
            "location": "Gurugram, Haryana",
            "apply_url": "https://zoomcom.tv/",
            "convertibility": 90,
            "status": "active",
            "convertibility_reasons": [
                "Outside broadcast & media production firm based in Gurgaon.",
                "Matches her logistics management background (led logistics for major university festivals).",
                "Focuses on scheduling, crew coordination, and vendor relations."
            ],
            "skills_required": ["Operations Management", "Logistics Coordination", "Stakeholder Management", "Scheduling"],
            "contacts": [
                {
                    "name_placeholder": "Operations Coordinator",
                    "role": "Media Operations Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Zoom%20Communications%20Operations",
                    "email_format": "hr@zoomcom.tv",
                }
            ]
        },
        {
            "id": "paxcom_business_analyst",
            "title": "E-commerce Business Analyst",
            "company": "Paxcom (A Paymentus Company)",
            "location": "Gurugram, Haryana",
            "apply_url": "https://paxcom.ai/",
            "convertibility": 94,
            "status": "active",
            "convertibility_reasons": [
                "E-commerce analytics & software solutions provider, part of Paymentus group in Gurgaon.",
                "Excellent match with her Tagit CAC analytics and 10+ GTM models reporting.",
                "Aligns with her Excel forecasting & Marketing Analytics certifications."
            ],
            "skills_required": ["Data Analysis", "Excel Forecasting", "Competitive Analysis", "GTM Strategy"],
            "contacts": [
                {
                    "name_placeholder": "Business Analysis Lead",
                    "role": "E-commerce Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Paxcom%20E-commerce%20Manager",
                    "email_format": "hr@paxcom.net",
                }
            ]
        },
        {
            "id": "hike_edu_bde",
            "title": "Business Development Executive",
            "company": "Hike Education",
            "location": "Gurugram, Haryana",
            "apply_url": "https://www.hikeedu.in/",
            "convertibility": 95,
            "status": "active",
            "convertibility_reasons": [
                "EdTech counselor and MBA partner with corporate offices in Noida and Udyog Vihar, Gurugram.",
                "Directly leverages her placement committee member B2B outreach & customer sales background.",
                "Strong match for her BBA/PGDM marketing credentials and consumer behaviour studies."
            ],
            "skills_required": ["B2C Sales & Engagement", "B2B LinkedIn Outreach", "Lead Management", "Consumer Psychology"],
            "contacts": [
                {
                    "name_placeholder": "Admissions Lead",
                    "role": "Recruitment & Placement Lead",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Hike%20Education%20Recruiter",
                    "email_format": "careers@hikeedu.in",
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
