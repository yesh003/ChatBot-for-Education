from tkinter import Tk, Label, Entry, Button, Text, END
from utils.response_handler import get_response

class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot UI")

        self.label = Label(master, text="Enter your query:")
        self.label.pack()

        self.entry = Entry(master, width=50)
        self.entry.pack()

        self.send_button = Button(master, text="Send", command=self.send_query)
        self.send_button.pack()

        self.response_area = Text(master, height=15, width=50)
        self.response_area.pack()

    def send_query(self):
        user_query = self.entry.get()
        self.response_area.insert(END, f"You: {user_query}\n")
        response = get_response(user_query)
        self.response_area.insert(END, f"Chatbot: {response}\n")
        self.entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()