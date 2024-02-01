import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import PyPDF2
import os

def extract_pages():
    pdf_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return
    
    pages_to_extract = simpledialog.askstring("Input", "Enter pages to extract (e.g., 1,3,5):")
    pages_to_extract = [int(page.strip()) - 1 for page in pages_to_extract.split(',')] if pages_to_extract else []
    
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not save_path:
        return
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page_num in pages_to_extract:
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        with open(save_path, 'wb') as output_file:
            pdf_writer.write(output_file)
    
    messagebox.showinfo("Success", f"Pages extracted and saved as: {os.path.basename(save_path)}")

root = tk.Tk()
root.title("PDF Page Extractor")

extract_button = tk.Button(root, text="Extract Pages", command=extract_pages)
extract_button.pack(pady=20)

root.mainloop()
