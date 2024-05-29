from fpdf import FPDF
from flask import Flask, request, send_file
from io import BytesIO

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, 'Currículo', 0, 1, 'C')
            self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

@app.route('/api/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.form
    pdf = PDF()
    pdf.add_page()

    try:
        # Adicionar dados ao PDF
        pdf.chapter_title('Nome Completo')
        pdf.chapter_body(data.get('name', ''))
        pdf.chapter_title('Email')
        pdf.chapter_body(data.get('email', ''))

        # Criar arquivo PDF em memória
        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        return send_file(pdf_output, as_attachment=True, download_name='curriculo.pdf', mimetype='application/pdf')

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
