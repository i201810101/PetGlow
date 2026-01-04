import tkinter as tk
from datetime import datetime, date
import re

def center_window(window):
    """Centrar ventana en la pantalla"""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def validate_email(email):
    """Validar formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validar formato de teléfono"""
    pattern = r'^[0-9\s\-\+\(\)]{7,15}$'
    return re.match(pattern, phone) is not None

def validate_dni(dni):
    """Validar formato de DNI"""
    pattern = r'^[0-9]{8}$'
    return re.match(pattern, dni) is not None

def format_currency(amount):
    """Formatear número como moneda"""
    return f"S/. {float(amount):,.2f}"

def format_date(date_obj):
    """Formatear fecha"""
    if isinstance(date_obj, date) or isinstance(date_obj, datetime):
        return date_obj.strftime("%d/%m/%Y")
    return date_obj

def format_datetime(datetime_obj):
    """Formatear fecha y hora"""
    if isinstance(datetime_obj, datetime):
        return datetime_obj.strftime("%d/%m/%Y %H:%M")
    return datetime_obj

def show_error(message, parent=None):
    """Mostrar mensaje de error"""
    tk.messagebox.showerror("Error", message, parent=parent)

def show_success(message, parent=None):
    """Mostrar mensaje de éxito"""
    tk.messagebox.showinfo("Éxito", message, parent=parent)

def show_warning(message, parent=None):
    """Mostrar mensaje de advertencia"""
    tk.messagebox.showwarning("Advertencia", message, parent=parent)

def confirm_action(message, parent=None):
    """Pedir confirmación al usuario"""
    return tk.messagebox.askyesno("Confirmar", message, parent=parent)