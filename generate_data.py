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
    email_subject = f"GLIM Chennai PGDM Graduate | Former Product Innovation Manager interested in {job['title']} at {job['company']}"
    
    if job['company'].lower() == 'pepperfry':
        email_body = (
            f"Subject: Former Pepperfry Intern | GLIM Chennai PGDM Graduate interested in {job['title']}\n\n"
            f"Dear {contact_name},\n\n"
            f"I hope you are doing well.\n\n"
            f"My name is Tina Jain, and I am a former Sales and Marketing Intern at Pepperfry (flagship stores, Aug-Oct 2022). I recently graduated with a PGDM (Marketing) from Great Lakes Institute of Management, Chennai (Class of 2026).\n\n"
            f"During my internship at Pepperfry, I managed 50+ HNI leads, resolved customer escalations, and helped drive monthly sales of INR 15L+. Since then, I have built further on my experience, working as a Product Innovation Manager at Tagit Pte Ltd and earning a Professional Diploma in Product Management.\n\n"
            f"I saw the opening for the {job['title']} role in Gurugram and would love to return to Pepperfry in this capacity. I feel my understanding of Pepperfry's operations, combined with my PGDM and Product Marketing credentials, makes me a strong fit for your team.\n\n"
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
            f"I would be deeply grateful for 10 minutes of your time to chat about the team's current focus, or for a referral for the {job['title']} role if you think my background is a good fit.\n\n"
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

    # Dynamic company data and exact entry-level job view links in Gurugram
    jobs_data = [
        {
            "id": "pepperfry_pmm",
            "title": "Product Marketing Associate",
            "company": "Pepperfry",
            "location": "Gurugram / Remote (HQ Mumbai)",
            "apply_url": "https://www.pepperfry.com/careers.html",
            "convertibility": 98,
            "convertibility_reasons": [
                "Warm lead: Tina is an alum Sales & Marketing Intern with a proven track record (15L+ monthly sales) at Pepperfry.",
                "High relevance: Combines her Marketing PGDM with her tagit product innovation credentials.",
                "Direct pipeline: Allows bypassing standard portals to reach former managers."
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
            "id": "airtel_pmm",
            "title": "Product Marketing Manager",
            "company": "Airtel",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/product-marketing-manager-at-airtel-4409288390?position=20&pageNum=0",
            "convertibility": 95,
            "convertibility_reasons": [
                "Airtel is headquartered in Gurugram, offering robust entry-level programs for PGDM Marketing grads.",
                "Her competitive benchmarking experience at Tagit maps perfectly to Airtel's high-velocity consumer feature releases.",
                "Matches top target role #1 (Product Marketing)."
            ],
            "skills_required": ["Product Marketing", "GTM Strategy", "Consumer Behaviour", "Competitive Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Marketing",
                    "role": "Product Marketing Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Marketing%20Airtel%20Great%20Lakes",
                    "email_format": "first.last@airtel.com",
                }
            ]
        },
        {
            "id": "airtel_apm",
            "title": "Associate Product Manager",
            "company": "Airtel Digital",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/associate-product-manager-at-airtel-digital-4373443164?position=1&pageNum=0",
            "convertibility": 94,
            "convertibility_reasons": [
                "Airtel Digital is situated in Gurugram.",
                "Her 6-month Product Innovation internship at Tagit maps directly to digital product roles.",
                "Great Lakes Chennai has a very active, senior alumni network at Airtel."
            ],
            "skills_required": ["Product Management", "Competitive Benchmarking", "UX Auditing", "Stakeholder Management"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - PM",
                    "role": "Product Manager (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Product%20Manager%20Airtel%20Great%20Lakes",
                    "email_format": "first.last@airtel.com",
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
                "INDmoney is headquartered in Gurugram and actively hires entry-level Product Analysts.",
                "Tina's data forecasting skills and UX analysis of 100+ consumer apps fits INDmoney's transaction-heavy fintech app audits.",
                "Matches top target role #3 (Product Analyst)."
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
                "EY Gurugram recruits heavily from Great Lakes Chennai (Class of 26 target).",
                "Tina was the Co-Convenor of Logistics at university, managing 15 teams and 14 operations events, showing direct domain alignment.",
                "Matches top target role #10 (Consulting Analyst)."
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
            "id": "intozi_pmm",
            "title": "Product Marketing & Growth Lead",
            "company": "Intozi",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/product-marketing-growth-lead-at-intozi-4398234602",
            "convertibility": 92,
            "convertibility_reasons": [
                "Intozi is a Gurugram-based AI startup hiring entry-level professionals to spearhead lead generation and GTM.",
                "Her B2B project (YE Stack) achieved rapid conversion using LinkedIn outreach, matching Intozi's B2B target market.",
                "Matches top target role #4 (Growth Marketing Manager)."
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
            "convertibility_reasons": [
                "Cotecna is expanding operations in NCR and hires fresh Brand Assistants.",
                "Tina's PGDM Marketing background, certifications in forecasting, and BBA Bronze Medalist status are highly valued.",
                "Matches top target role #8 (Brand Manager / Assistant Brand Manager)."
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
                "SBNRI is a Gurgaon fintech startup hiring entry-level analysts.",
                "Matches her Professional Diploma in Product Management and data-driven decision-making skillset.",
                "SBNRI focuses on NRI banking products, matching her benchmarking of international platforms at Tagit."
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
            "id": "accenture_consultant",
            "title": "Custom Analytics Strategy Consultant",
            "company": "Accenture",
            "location": "Gurugram, Haryana",
            "apply_url": "https://in.linkedin.com/jobs/view/s-c-gn-t-o-i-i-%E2%80%93-custom-analytics-consultant-at-accenture-services-pvt-ltd-4418503644",
            "convertibility": 91,
            "convertibility_reasons": [
                "Accenture is a massive recruiter of Consulting Analysts at GLIM.",
                "Tina holds an Accenture Virtual Project Management certification (2022) indicating prior domain alignment.",
                "Perfect fit for target role #10 (Consulting Analyst) & #9 (Strategy Analyst)."
            ],
            "skills_required": ["Consulting", "Marketing Analytics", "Data-driven Decision Making", "Competitive Analysis"],
            "contacts": [
                {
                    "name_placeholder": "Great Lakes Alum - Accenture",
                    "role": "Consulting Associate (GLIM Alumni)",
                    "search_url": "https://www.linkedin.com/search/results/people/?keywords=Accenture%20Consulting%20Great%20Lakes%20Gurgaon",
                    "email_format": "first.last@accenture.com",
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
                "Aurora Energy has a strong office in Gurgaon and hires fresh MBA/PGDM analysts for product teams.",
                "Tina's GTM analyses and benchmarking of 500+ global platforms fit Aurora's international SaaS expansion products.",
                "Matches target role #2 (Associate Product Manager)."
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
                "Cargill's trade analytics headquarters is in Gurgaon.",
                "Entry-level role seeking fresh post-graduates with forecasting and data management qualifications.",
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
            "convertibility_reasons": [
                "Taxmann hires entry-level APMs in NCR to manage their tax filing digital tools.",
                "Tina's CRM diploma and customer mapping fits Taxmann's core audience segment optimization needs."
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
        "jobs": jobs_data
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4)
        print("data.json successfully generated with", len(jobs_data), "jobs.")

if __name__ == "__main__":
    main()
