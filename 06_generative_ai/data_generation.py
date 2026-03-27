"""
╔══════════════════════════════════════════════════════════════╗
║   FILE 1 of 2 — RByte.ai                                   ║
║   generate_bajaj_data.py                                    ║
║                                                             ║
║   What this does:                                           ║
║   → Calls GPT-4o to generate 10 realistic Bajaj Finance     ║
║     policy documents                                        ║
║   → Saves each document as a real PDF file                  ║
║   → These PDFs are then used by bajaj_rag_strategies.py     ║
║                                                             ║
║   Run FIRST:                                                ║
║   pip install openai fpdf2                                  ║
║   export OPENAI_API_KEY=your-key-here                       ║
║   python generate_bajaj_data.py                             ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json
from openai import OpenAI
from fpdf import FPDF
from dotenv import load_dotenv
# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

OUTPUT_DIR   = "./bajaj_finance_pdfs"
MODEL        = "gpt-4o"
os.makedirs(OUTPUT_DIR, exist_ok=True)
load_dotenv()
client = None


def get_client() -> OpenAI:
    """Create the OpenAI client only when it is actually needed."""
    global client
    if client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set.")
        client = OpenAI(api_key=api_key)
    return client


def sanitize_pdf_text(text: str) -> str:
    """Replace characters unsupported by default FPDF core fonts."""
    replacements = {
        "₹": "Rs. ",
        "•": "-",
        "→": "->",
        "—": "-",
        "–": "-",
        "“": '"',
        "”": '"',
        "’": "'",
        "‘": "'",
        "…": "...",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# ─────────────────────────────────────────────
# 10 DOCUMENT TOPICS TO GENERATE
# Each has: filename, topic, metadata
# ─────────────────────────────────────────────

DOCUMENTS_TO_GENERATE = [
    {
        "filename":   "01_personal_loan_eligibility.pdf",
        "topic":      "Personal Loan Eligibility Criteria",
        "department": "sales",
        "loan_type":  "personal",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Personal Loan Eligibility Criteria.
Include:
- Minimum income requirements for salaried employees (exact ₹ amounts)
- Age limits (min/max)
- CIBIL score requirements
- FOIR (Fixed Obligation to Income Ratio) limits
- Eligibility for self-employed professionals (doctors, CAs, architects)
- Employment tenure requirements
- Special categories (government employees, defense personnel)
Write in formal policy document style. 300-400 words. Use real-sounding numbers.
"""
    },
    {
        "filename":   "02_personal_loan_interest_rates.pdf",
        "topic":      "Personal Loan Interest Rates and Charges",
        "department": "risk",
        "loan_type":  "personal",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Personal Loan Interest Rates and Charges.
Include:
- Interest rate slabs based on CIBIL score (e.g. 750+, 700-749, 650-699, below 650)
- Separate rates for salaried vs self-employed
- Processing fee structure
- Prepayment charges
- Late payment penalty
- Bounce charges for ECS/NACH
Write in formal policy document style. 300-400 words. Use real-sounding percentage values.
"""
    },
    {
        "filename":   "03_personal_loan_documents.pdf",
        "topic":      "Personal Loan Required Documents",
        "department": "operations",
        "loan_type":  "personal",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Required Documents for Personal Loan.
Include:
- Identity proof options (Aadhaar, PAN, Passport etc)
- Address proof options
- Income proof for salaried (salary slips, Form 16, bank statements)
- Income proof for self-employed (ITR, P&L, balance sheet, bank statements)
- Additional documents for high loan amounts (above ₹15 lakhs)
- Document validity requirements
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "04_home_loan_eligibility.pdf",
        "topic":      "Home Loan Eligibility and Terms",
        "department": "sales",
        "loan_type":  "home",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Home Loan Eligibility and Terms.
Include:
- Loan amount range (₹ values)
- Loan-to-value ratios for different loan amounts
- Minimum income requirements
- Age limits
- Tenure options (min/max years)
- Interest rate slabs based on CIBIL score
- Prepayment and foreclosure policy
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "05_loan_rejection_policy.pdf",
        "topic":      "Loan Rejection Reasons and Reapplication Policy",
        "department": "risk",
        "loan_type":  "personal",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Loan Rejection Reasons and Reapplication Policy.
Include:
- Primary reasons for loan rejection (CIBIL, FOIR, income, job stability)
- Multiple loan enquiries impact
- Default history impact
- Documentation issues
- Property issues for home loans
- Reapplication waiting period
- How to improve chances before reapplying
- Appeal process
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "06_emi_default_policy.pdf",
        "topic":      "EMI Payment and Default Policy",
        "department": "collections",
        "loan_type":  "personal",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about EMI Payment and Default Policy.
Include:
- NACH/ECS mandate process
- EMI date options
- Consequences of 1, 2, 3, 6+ missed EMIs
- NPA classification timeline
- Legal notice process
- Prepayment options (part and full)
- EMI holiday policy for financial hardship
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "07_business_loan_products.pdf",
        "topic":      "Business Loan Products for SME and MSME",
        "department": "sales",
        "loan_type":  "business",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Business Loan Products for SME and MSME.
Include:
- Loan amount range
- Tenure options
- Eligibility: business vintage, annual turnover, CIBIL score
- Business types eligible (proprietorship, partnership, Pvt Ltd)
- Interest rate range
- Collateral requirements
- Document requirements
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "08_grievance_policy.pdf",
        "topic":      "Customer Grievance Redressal Policy",
        "department": "operations",
        "loan_type":  "general",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Customer Grievance Redressal Policy.
Include:
- All complaint channels (helpline number, email, branch, online portal)
- Resolution timelines for each escalation level (L1, L2, L3, Ombudsman)
- Loan statement request process
- NOC (No Objection Certificate) issuance timeline
- Duplicate NOC process
- Loan account closure process
- Lien release timeline
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "09_gold_loan_products.pdf",
        "topic":      "Gold Loan Products and Process",
        "department": "sales",
        "loan_type":  "gold",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Gold Loan Products.
Include:
- Loan amount range
- Gold purity accepted (karat)
- Maximum LTV ratio (RBI limit)
- Interest rate slabs by tenure
- Step-by-step loan process (appraisal to disbursement timeline)
- Gold storage and insurance
- Auction policy if loan not repaid
Write in formal policy document style. 300-400 words.
"""
    },
    {
        "filename":   "10_cibil_impact_policy.pdf",
        "topic":      "Credit Score Impact and Reporting Policy",
        "department": "risk",
        "loan_type":  "general",
        "year":       2024,
        "prompt":     """
Write a realistic Bajaj Finance internal policy document about Credit Score Impact and Reporting.
Include:
- Which credit bureaus Bajaj Finance reports to (CIBIL, Experian, Equifax)
- Reporting frequency and date
- CIBIL score impact of on-time payments (+points per month)
- Impact of 30, 60, 90 day late payments (negative points)
- Impact of default/settlement
- Impact of loan closure
- Hard vs soft enquiry explanation
- Dispute resolution process and timeline
Write in formal policy document style. 300-400 words.
"""
    },
]


# ─────────────────────────────────────────────
# PDF GENERATOR CLASS
# ─────────────────────────────────────────────

class BajajPDF(FPDF):
    def __init__(self, title, department, loan_type, year):
        super().__init__()
        self.doc_title    = title
        self.doc_dept     = department
        self.doc_loan     = loan_type
        self.doc_year     = year

    def header(self):
        # Logo area
        self.set_fill_color(0, 82, 204)         # Bajaj blue
        self.rect(0, 0, 210, 18, "F")
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(255, 255, 255)
        self.set_y(5)
        self.cell(0, 8, "BAJAJ FINANCE LIMITED - INTERNAL POLICY DOCUMENT", align="C")
        self.set_text_color(0, 0, 0)
        self.ln(16)

        # Document title
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(0, 60, 150)
        self.cell(0, 8, sanitize_pdf_text(self.doc_title.upper()), ln=True, align="C")
        self.set_text_color(0, 0, 0)

        # Metadata line
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        meta = f"Department: {self.doc_dept.title()}  |  Category: {self.doc_loan.title()} Loan  |  Year: {self.doc_year}  |  CONFIDENTIAL"
        self.cell(0, 6, sanitize_pdf_text(meta), ln=True, align="C")
        self.set_text_color(0, 0, 0)

        # Divider
        self.set_draw_color(0, 82, 204)
        self.set_line_width(0.5)
        self.line(10, self.get_y() + 2, 200, self.get_y() + 2)
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10,
            sanitize_pdf_text(
                f"Bajaj Finance Limited | Page {self.page_no()} | {self.doc_year} | For Internal Use Only"
            ),
            align="C"
        )

    def add_body(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        left_margin = self.l_margin
        body_width = self.w - self.l_margin - self.r_margin
        bullet_indent = 15.0
        bullet_width = self.w - bullet_indent - self.r_margin

        for line in text.strip().split("\n"):
            line = sanitize_pdf_text(line.strip())
            if not line:
                self.ln(3)
                continue

            # Section headers (ALL CAPS lines)
            if line.isupper() and len(line) > 5:
                self.ln(3)
                self.set_font("Helvetica", "B", 10)
                self.set_text_color(0, 60, 150)
                self.set_x(left_margin)
                self.multi_cell(body_width, 6, line)
                self.set_font("Helvetica", "", 10)
                self.set_text_color(40, 40, 40)

            # Numbered / bullet points
            elif line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "-", "•", "→")):
                self.set_x(bullet_indent)
                self.multi_cell(bullet_width, 6, line)

            # Normal paragraph
            else:
                self.set_x(left_margin)
                self.multi_cell(body_width, 6, line)

        self.ln(4)


# ─────────────────────────────────────────────
# MAIN — GENERATE ALL 10 PDFS
# ─────────────────────────────────────────────

def generate_document_content(doc_config: dict) -> str:
    """Call GPT-4o to generate realistic policy document content."""
    print(f"   🤖 Calling GPT-4o for: {doc_config['topic']}...")

    response = get_client().chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior policy writer at Bajaj Finance Limited, India. "
                    "Write realistic, professional internal policy documents. "
                    "Use Indian financial terminology, rupee amounts (₹), and realistic numbers. "
                    "Write in clear formal English. Use ALL CAPS for section headers."
                )
            },
            {
                "role": "user",
                "content": doc_config["prompt"]
            }
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content


def save_as_pdf(content: str, doc_config: dict) -> str:
    """Save generated content as a PDF file."""
    filepath = os.path.join(OUTPUT_DIR, doc_config["filename"])

    pdf = BajajPDF(
        title=doc_config["topic"],
        department=doc_config["department"],
        loan_type=doc_config["loan_type"],
        year=doc_config["year"]
    )
    pdf.add_page()
    pdf.add_body(content)
    pdf.output(filepath)
    return filepath


def save_metadata(doc_configs: list):
    """Save metadata JSON — used by strategies script to load PDFs with metadata."""
    metadata = []
    for doc in doc_configs:
        metadata.append({
            "filename":   doc["filename"],
            "topic":      doc["topic"],
            "department": doc["department"],
            "loan_type":  doc["loan_type"],
            "year":       doc["year"],
        })

    meta_path = os.path.join(OUTPUT_DIR, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n   ✅ Metadata saved → {meta_path}")
    return meta_path


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":

    print("\n" + "="*60)
    print("  RByte.ai - Bajaj Finance PDF Generator")
    print("  Using: GPT-4o + fpdf2")
    print("="*60)

    if not os.environ.get("OPENAI_API_KEY"):
        print("\n❌ OPENAI_API_KEY not set!")
        print("   Run: export OPENAI_API_KEY=your-key-here")
        exit(1)

    print(f"\n📁 Output directory: {OUTPUT_DIR}")
    print(f"📄 Generating {len(DOCUMENTS_TO_GENERATE)} PDF documents...\n")

    generated = []

    for i, doc_config in enumerate(DOCUMENTS_TO_GENERATE, 1):
        print(f"[{i:02d}/{len(DOCUMENTS_TO_GENERATE)}] {doc_config['topic']}")

        # Step 1: GPT-4o generates content
        content = generate_document_content(doc_config)

        # Step 2: Save as PDF
        filepath = save_as_pdf(content, doc_config)
        file_size = os.path.getsize(filepath)

        print(f"   ✅ Saved → {filepath} ({file_size/1024:.1f} KB)")
        generated.append(filepath)

    # Save metadata for strategies script
    save_metadata(DOCUMENTS_TO_GENERATE)

    print(f"\n{'='*60}")
    print(f"  ✅ Done! {len(generated)} PDFs generated")
    print(f"  📁 Location: {OUTPUT_DIR}/")
    print(f"\n  Files created:")
    for f in generated:
        print(f"   → {os.path.basename(f)}")

    print(f"\n  Next step:")
    print(f"  python bajaj_rag_strategies.py")
    print(f"{'='*60}\n")
