import os
from datetime import datetime
from fpdf import FPDF

# ------------------------------
# Settings
# ------------------------------
PLOT_DIR = "plots"
REPORT_FILE = f"COVID19_Summary_Report_{datetime.now().strftime('%Y-%m-%d')}.pdf"

# Έλεγξε αν υπάρχουν plots
plot_files = sorted([f for f in os.listdir(PLOT_DIR) if f.endswith(".png")])
if not plot_files:
    print(f"No plot images found in the '{PLOT_DIR}' folder.")
    exit()

# ------------------------------
# PDF setup
# ------------------------------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 18)
pdf.multi_cell(0, 10, "COVID-19 Summary Report", align="C")
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C")
pdf.ln(10)

# ------------------------------
# Sections
# ------------------------------
sections = {
    "Daily Cases": ["Daily_cases", "Daily_deaths"],
    "Total Cases & Deaths": ["Total_cases", "Total_deaths"],
    "Vaccinations": ["Total_vaccinations", "Vaccination_Trend"],
    "Comparisons": ["vs"]
}

for section, keywords in sections.items():
    pdf.set_font("Arial", "B", 14)
    pdf.multi_cell(0, 10, section, align="L")
    pdf.ln(2)
    
    # Add relevant plots
    for plot_file in plot_files:
        if any(kw.lower() in plot_file.lower() for kw in keywords):
            title = plot_file.replace("_", " ").replace(".png", "")
            pdf.set_font("Arial", "B", 12)
            pdf.multi_cell(0, 8, title, align="C")
            
            plot_path = os.path.join(PLOT_DIR, plot_file)
            pdf.image(plot_path, x=15, w=180)
            pdf.ln(8)

# ------------------------------
# Save PDF
# ------------------------------
pdf.output(REPORT_FILE)
print(f"\n✅ Summary report generated: {REPORT_FILE}")
