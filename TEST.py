# Assuming other parts of the code remain unchanged

class GridWindow:
    def __init__(self):
        # other initialization code...
        self.left_canvas = ...  # existing code to create left_canvas
        
        # Change font selection for root labels
        try:
            self.root_label_font = tkFont.Font(file=resource_path('assets/fonts/DejaVuSans.ttf'))
        except Exception:
            self.root_label_font = "Arial"  # fallback to Arial

    def export_pdf(self):
        # Always register and use DejaVuSans font
        try:
            pdfmetrics.registerFont(TTFont('DejaVuSans', resource_path('assets/fonts/DejaVuSans.ttf')))
        except Exception:
            pdfmetrics.registerFont(TTFont('Helvetica', resource_path('assets/fonts/Helvetica.ttf')))  # fallback to Helvetica