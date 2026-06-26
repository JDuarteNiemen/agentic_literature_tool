import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from summary import summarise

from IPython.terminal.shortcuts.auto_suggest import accept

# ==========================================================
# Dark Blue Theme Palette
# ==========================================================
_BG        = "#0B1020"   # deep navy background
_CARD_BG   = "#111A33"   # raised panel / card surface
_SURFACE_2 = "#162042"   # optional secondary panels

_ACCENT    = "#4DA3FF"   # primary blue accent
_ACCENT_HI = "#2F86E6"   # hover / active accent
_ACCENT_FG = "#FFFFFF"   # text on accent

_TEXT      = "#E6ECFF"   # main text (soft white-blue)
_TEXT_DIM  = "#9AA7C7"   # secondary text (muted blue-grey)

_BORDER    = "#263154"   # subtle borders
_HOVER     = "#1A274D"   # hover highlight
_TREE_SEL  = "#22335F"   # selected row highlight

_STREAM_BG = "#0A0F1F"   # terminal / console background
_STREAM_FG = "#CFE1FF"   # terminal text

_SUCCESS   = "#3DDC97"   # green (kept slightly cool)
_WARNING   = "#FFB454"   # amber
_DANGER    = "#FF5A6A"   # soft red
_DANGER_HI = "#E04455"



def _apply_glass_theme(root: tk.Tk):
    """Configure a ttk Style with the warm Robin palette."""
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure(".", background=_BG, foreground=_TEXT,
                    font=("Helvetica Neue", 12))
    style.configure("TFrame", background=_BG)
    style.configure("Card.TFrame", background=_CARD_BG, relief="flat")
    style.configure("TLabel", background=_BG, foreground=_TEXT)
    style.configure("Card.TLabel", background=_CARD_BG, foreground=_TEXT)
    style.configure("Dim.TLabel", background=_BG, foreground=_TEXT_DIM,
                    font=("Helvetica Neue", 11))
    style.configure("Heading.TLabel", background=_BG, foreground=_TEXT,
                    font=("Helvetica Neue", 22, "bold"))
    style.configure("SubHeading.TLabel", background=_BG, foreground=_TEXT_DIM,
                    font=("Helvetica Neue", 13))

    # Accent button (robin orange)
    style.configure("Accent.TButton", background=_ACCENT, foreground=_ACCENT_FG,
                    font=("Helvetica Neue", 12, "bold"), padding=(18, 10),
                    borderwidth=0)
    style.map("Accent.TButton",
              background=[("active", _ACCENT_HI), ("disabled", _BORDER)])

    # Default button
    style.configure("TButton", padding=(12, 6), borderwidth=1,
                    relief="flat", background=_CARD_BG, foreground=_TEXT)
    style.map("TButton", background=[("active", _HOVER)])

    # Danger button
    style.configure("Danger.TButton", background=_DANGER, foreground="#ffffff",
                    font=("Helvetica Neue", 11), padding=(14, 7),
                    borderwidth=0)
    style.map("Danger.TButton",
              background=[("active", _DANGER_HI), ("disabled", _BORDER)])

    # Small quiet button (refresh ↻ / toggle)
    style.configure("Small.TButton", padding=(6, 3), font=("Helvetica Neue", 13))

    # Entry
    style.configure("TEntry", fieldbackground=_CARD_BG, foreground=_TEXT,
                    borderwidth=1, relief="solid", padding=7)

    # Combobox
    style.configure("TCombobox", fieldbackground=_CARD_BG, foreground=_TEXT,
                    padding=5)

    # Treeview – alternating rows handled in code, taller rows for readability
    style.configure("Treeview", background=_CARD_BG, foreground=_TEXT,
                    fieldbackground=_CARD_BG, rowheight=32,
                    font=("Helvetica Neue", 11), borderwidth=0)
    style.configure("Treeview.Heading", background=_BG, foreground=_TEXT,
                    font=("Helvetica Neue", 11, "bold"), padding=(8, 4))
    style.map("Treeview", background=[("selected", _TREE_SEL)],
              foreground=[("selected", _TEXT)])

    # Notebook tabs – wider padding, accent underline on selected
    style.configure("TNotebook", background=_BG, borderwidth=0)
    style.configure("TNotebook.Tab", background=_BG, foreground=_TEXT_DIM,
                    padding=(22, 10), font=("Helvetica Neue", 12))
    style.map("TNotebook.Tab",
              background=[("selected", _CARD_BG)],
              foreground=[("selected", _ACCENT)])

    # LabelFrame
    style.configure("TLabelframe", background=_CARD_BG, borderwidth=1,
                    relief="solid")
    style.configure("TLabelframe.Label", background=_CARD_BG, foreground=_ACCENT,
                    font=("Helvetica Neue", 11, "bold"))

    # Separator
    style.configure("TSeparator", background=_BORDER)

    # Progressbar (used for indeterminate busy indicator)
    style.configure("Accent.Horizontal.TProgressbar",
                    troughcolor=_BORDER, background=_ACCENT)


# Create the main window
class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AGENTIC LITERATURE TOOL")
        self.geometry("700x550")
        self.minsize(700, 520)

        _apply_glass_theme(self)


        # IMPORTANT: force visible background layer
        self.container = tk.Frame(self, bg=_BG)
        self.container.pack(fill="both", expand=True)

        tk.Label(
            self.container,
            text="AGENTIC LITERATURE TOOL",
            bg=_BG,
            fg=_TEXT,
            font=("Calibri", 24, "bold")
        ).pack(pady=40)

        form_frame = tk.Frame(self.container, bg=_CARD_BG)
        form_frame.pack(padx=40, pady=20, fill="x")

        tk.Label(form_frame, text="Accession:", bg=_CARD_BG, fg=_TEXT).pack(anchor="w", padx=10, pady=(10, 0))
        self.accession_entry = tk.Entry(form_frame)
        self.accession_entry.pack(fill="x", padx=10, pady=(0, 10))

        tk.Label(form_frame, text="Topic:", bg=_CARD_BG, fg=_TEXT).pack(anchor="w", padx=10)
        self.topic_entry = tk.Entry(form_frame)
        self.topic_entry.pack(fill="x", padx=10, pady=(0, 10))

        # Submit button
        submit_btn = tk.Button(
            self.container,
            text="Submit",
            command=self.process_inputs
        )
        submit_btn.pack(pady=10)

    def process_inputs(self):
            accession = self.accession_entry.get()
            topic = self.topic_entry.get()
            # send them wherever you want
            print("Accession:", accession)
            print("Topic:", topic)
            # example: call another function
            self.handle_data(accession, topic)

    def handle_data(self, accession, topic):
            messagebox.showinfo(
                "Received",
                f"Accession: {accession}\nTopic: {topic}")


LibraryApp().mainloop()