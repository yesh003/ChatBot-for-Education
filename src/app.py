from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, VERTICAL, RIGHT, Y, END, Frame, PhotoImage
from tkinter.font import Font
from utils.response_handler import get_response

class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("Modern Chatbot UI")

        # Set window size and background color
        master.geometry("800x600")
        master.configure(bg="#1e1e2f")  # Dark background

        # Custom fonts
        self.title_font = Font(family="Helvetica", size=20, weight="bold")
        self.label_font = Font(family="Arial", size=12)
        self.button_font = Font(family="Arial", size=12, weight="bold")
        self.text_font = Font(family="Courier", size=10)

        # Header Section
        self.header_frame = Frame(master, bg="#2c2c3e", height=80)
        self.header_frame.pack(fill="x")

        # Add a logo to the header
        # self.logo_image = PhotoImage(file="logo.png")  # Replace with your logo file
        # self.logo_label = Label(self.header_frame, image=self.logo_image, bg="#2c2c3e")
        # self.logo_label.pack(side="left", padx=10, pady=10)

        self.title_label = Label(
            self.header_frame,
            text="Welcome to Chatbot",
            font=self.title_font,
            fg="white",
            bg="#2c2c3e"
        )
        self.title_label.pack(side="left", padx=10)

        # Main Content Section
        self.content_frame = Frame(master, bg="#1e1e2f")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Query Input Section
        self.query_frame = Frame(self.content_frame, bg="#1e1e2f")
        self.query_frame.pack(fill="x", pady=10)
        self.label = Label(
            self.query_frame,
            text="Enter your query:",
            font=self.label_font,
            fg="white",
            bg="#1e1e2f"
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
            bg="#4caf50",  # Green button
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            command=self.send_query
        )
        self.send_button.pack(side="left", padx=5)

        # Response Area Section
        self.response_frame = Frame(self.content_frame, bg="#1e1e2f")
        self.response_frame.pack(fill="both", expand=True, pady=10)
        self.response_area = Text(
            self.response_frame,
            height=20,
            width=70,
            font=self.text_font,
            bg="#f5f5f5",  # Light background for text area
            fg="#333333",  # Dark text
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
        self.footer_frame = Frame(master, bg="#2c2c3e", height=40)
        self.footer_frame.pack(fill="x")
        self.footer_label = Label(
            self.footer_frame,
            text="Chatbot UI - Powered by Python",
            font=self.label_font,
            fg="white",
            bg="#2c2c3e"
        )
        self.footer_label.pack(pady=10)

    def send_query(self):
        user_query = self.entry.get()
        self.response_area.insert(END, f"You: {user_query}\n")
        response = get_response(user_query)
        self.response_area.insert(END, f"Chatbot: {response}\n\n")
        self.entry.delete(0, END)

    def get_response(self, query):
        # Simulate a response from ChatGPT
        return f"This is a simulated response to your query: '{query}'"


if __name__ == "__main__":
    root = Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()