from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]


class PdfPrinter:
    def __init__(self, canvas, current_height, contact_height):
        self.current_height = current_height
        self.contact_height = contact_height
        self.canvas = canvas
        self.normal_width = 50

    def create_header(self, text):
        self.canvas.setFont("Helvetica", 24)
        self.canvas.drawString((PAGE_WIDTH - stringWidth(text, "Helvetica", 24)) / 2, PAGE_HEIGHT - 50, text)

    def create_text_line(self, s_text, text):
        self.current_height += 20
        self.canvas.setFont("Helvetica-Bold", 14)
        self.canvas.drawString(self.normal_width, PAGE_HEIGHT - self.current_height, s_text + ": ")
        self.canvas.setFont("Helvetica", 14)
        width = self.normal_width + stringWidth(s_text + ": ", "Helvetica-Bold", 14)
        self.canvas.drawString(width, PAGE_HEIGHT - self.current_height, str(text))

    def create_contact_line(self, s_text, text):
        self.contact_height += 20
        self.canvas.setFont("Helvetica-Bold", 14)
        self.canvas.drawString(self.normal_width+280, PAGE_HEIGHT - self.contact_height, s_text + ": ")
        self.canvas.setFont("Helvetica", 14)
        width = self.normal_width + 280 + stringWidth(s_text + ": ", "Helvetica-Bold", 14)
        self.canvas.drawString(width, PAGE_HEIGHT - self.contact_height, str(text))

    def horizontal_line(self):
        self.current_height += 20
        self.canvas.line(50, PAGE_HEIGHT - self.current_height, PAGE_WIDTH - 50, PAGE_HEIGHT - self.current_height)
        self.current_height += 20

    def create_half_title(self, text):
        self.current_height += 10
        self.canvas.setFont("Helvetica-Bold", 18)
        self.canvas.drawString(self.normal_width, PAGE_HEIGHT - self.current_height, text)
        self.canvas.line(
            self.normal_width,
            PAGE_HEIGHT - (self.current_height + 3),
            self.normal_width + stringWidth(text, "Helvetica-Bold", 18),
            PAGE_HEIGHT - (self.current_height + 3)
        )
        self.current_height += 13

    def create_hospitalization(self, hospitalization):
        self.create_text_line("Symptoms start date", hospitalization.fecha_inicio_sintomas)
        self.create_text_line("Hospitalizaiton date", hospitalization.fecha_inicio_sintomas)
        self.create_text_line("Diagnostic date", hospitalization.fecha_inicio_sintomas)
        self.create_text_line("Current illness", hospitalization.enfermedad_actual)
        self.create_text_line("Description", hospitalization.descripcion)
        if hospitalization.fecha_egreso:
            self.create_text_line("Discharge date", hospitalization.fecha_egreso)
        self.current_height += 40
