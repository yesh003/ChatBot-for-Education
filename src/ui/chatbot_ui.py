from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, VERTICAL, RIGHT, Y, END, Frame
from tkinter.font import Font
from response_handler import handle_user_query

class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("Gemini AI Chatbot")
        master.geometry("800x600")
        master.configure(bg="#2c3e50")

        # Fonts
        self.title_font = Font(family="Helvetica", size=20, weight="bold")
        self.label_font = Font(family="Arial", size=12)
        self.button_font = Font(family="Arial", size=12, weight="bold")
        self.text_font = Font(family="Courier", size=10)

        # Header Section
        self.header_frame = Frame(master, bg="#34495e", height=80)
        self.header_frame.pack(fill="x")
        self.title_label = Label(
            self.header_frame,
            text="Welcome to Gemini AI Chatbot",
            font=self.title_font,
            fg="white",
            bg="#34495e"
        )
        self.title_label.pack(pady=20)

        # Content Section
        self.content_frame = Frame(master, bg="#2c3e50")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Input Section
        self.query_frame = Frame(self.content_frame, bg="#2c3e50")
        self.query_frame.pack(fill="x", pady=10)
        self.label = Label(
            self.query_frame,
            text="Enter your query:",
            font=self.label_font,
            fg="white",
            bg="#2c3e50"
        )
        self.label.pack(side="left", padx=5)
        self.entry = Entry(
            self.query_frame,
            width=50,
            font=self.label_font,
            bd=2,
            relief="solid"
        )
        self.entry.pack(side="left", padx=5)
        self.send_button = Button(
            self.query_frame,
            text="Send",
            font=self.button_font,
            bg="#1abc9c",
            fg="white",
            activebackground="#16a085",
            activeforeground="white",
            command=self.send_query
        )
        self.send_button.pack(side="left", padx=5)

        # Response Section
        self.response_frame = Frame(self.content_frame, bg="#2c3e50")
        self.response_frame.pack(fill="both", expand=True, pady=10)
        self.response_area = Text(
            self.response_frame,
            height=20,
            width=70,
            font=self.text_font,
            bg="#ecf0f1",
            fg="#2c3e50",
            bd=2,
            relief="solid",
            wrap="word"
        )
        self.response_area.pack(side="left", fill="both", expand=True, padx=5)
        self.scrollbar = Scrollbar(
            self.response_frame,
            command=self.response_area.yview,
            orient=VERTICAL
        )
        self.response_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Footer Section
        self.footer_frame = Frame(master, bg="#34495e", height=40)
        self.footer_frame.pack(fill="x")
        self.footer_label = Label(
            self.footer_frame,
            text="Gemini AI Chatbot • Powered by Google AI",
            font=self.label_font,
            fg="white",
            bg="#34495e"
        )
        self.footer_label.pack(pady=10)

    def send_query(self):
        user_query = self.entry.get().strip()
        if user_query:
            self.response_area.insert(END, f"You: {user_query}\n")
            self.entry.delete(0, END)

            try:
                response = handle_user_query(user_query)
            except Exception as e:
                response = f"[Error] {str(e)}"

            self.response_area.insert(END, f"Chatbot: {response}\n\n")
            self.response_area.see(END)

if __name__ == "__main__":
    root = Tk()
    app = ChatbotUI(root)
    root.mainloop()
