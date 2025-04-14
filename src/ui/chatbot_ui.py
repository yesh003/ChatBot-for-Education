from tkinter import Tk, Label, Entry, Button, Text, END, Scrollbar, VERTICAL, RIGHT, Y

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

        self.scrollbar = Scrollbar(master, command=self.response_area.yview, orient=VERTICAL)
        self.response_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def send_query(self):
        user_query = self.entry.get()
        self.entry.delete(0, END)
        response = self.get_response(user_query)
        self.response_area.insert(END, f"You: {user_query}\n")
        self.response_area.insert(END, f"Chatbot: {response}\n")

    def get_response(self, query):
        # Simulate a response from ChatGPT
        return f"This is a simulated response to your query: '{query}'"

if __name__ == "__main__":
    root = Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()