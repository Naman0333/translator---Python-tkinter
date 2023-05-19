#import rquired library
import tkinter as tk
from googletrans import Translator, LANGUAGES
from PIL import ImageTk, Image

class TranslatorApp:
    def __init__(self,root):
        self.root = root
        
        # Set the title of the root window to 'Translator'
        self.root.title('Translator')
        
        # Set the background color of the root window to a unique shade of blue
        self.root.config(bg='#7FDBFF')
        
        #Create an instane of the Translator class from googletrans
        self.translator = Translator()

        #Get a full list of all available languages from LANGUAGES dictionary
        self.languages = list(LANGUAGES.values())
    
        #Label for source language.
        self.source_label = tk.Label(self.root, text="Select source language:",font=('Arial',16,'bold'),bg='#7FDBFF',fg='black')
        self.source_label.grid(row=0, column=0, sticky=tk.W,pady=5)

        #Dropdown for select a translate language.
        self.source_var = tk.StringVar()
        self.source_var.set(self.languages[0])
        self.source_dropdown = tk.OptionMenu(self.root, self.source_var, *self.languages)
        self.source_dropdown.config(font=('Arial',12,'italic'),bg='#7FDBFF',fg='black')
        self.source_dropdown.grid(row=0,column=1,sticky=tk.NSEW,pady=5)

        #Label for target language.
        self.target_label = tk.Label(self.root, text="Select target language:",font=('Arial',16,'bold'),bg='#7FDBFF',fg='black')
        self.target_label.grid(row=1, column=0, sticky=tk.W,pady=5)

        #Dropdown for select a target language.
        self.target_var = tk.StringVar()
        self.target_var.set(list(LANGUAGES.values())[1])
        self.target_dropdown = tk.OptionMenu(self.root, self.target_var, *LANGUAGES.values())
        self.target_dropdown.config(font=('Arial',12,'italic'),bg='#7FDBFF',fg='black')
        self.target_dropdown.grid(row=1, column=1, sticky=tk.NSEW,pady=5)

        #Label for enter text to translate.
        self.input_label = tk.Label(self.root, text="Enter the text to translate:",font=('Arial',16,'bold'),bg='#7FDBFF',fg='black')
        self.input_label.grid(row=2, column=0, sticky=tk.W,pady=5)

        #Entry for enter text to translate.
        self.input_entry =tk.Entry(self.root, width=50)
        self.input_entry.grid(row=2, column=1, sticky=tk.NSEW,pady=5)

        #Label for translation text.
        self.output_label =tk.Label(self.root, text="Translation:",font=('Arial',16,'bold'),bg='#7FDBFF',fg='black')
        self.output_label.grid(row=3, column=0, sticky=tk.W,pady=5)

        #Textbox for after translation text.
        self.output_text = tk.Text(self.root, width=50, height=10)
        self.output_text.grid(row=3, column=1, sticky=tk.NSEW,pady=5)

        #Button for Translate.
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate,font=('Arial',16,'bold'),bg='black',fg='white')
        self.translate_button.grid(row=4, column=0, columnspan=2,pady=5)



    #Translate function translate the text.    
    def translate(self):
        
        # Get the input text from the input entry widget.
        text = self.input_entry.get()
        
        # Get the selected source and target languages from the dropdown menus.
        source_lang = self.source_var.get()
        target_lang = self.target_var.get()

        # Perform the translation using the translator object.
        translation = self.translator.translate(text, src=source_lang, dest=target_lang)

        # Clear the output text widget.
        self.output_text.delete(1.0,'end')

        # Insert the translation result into the output text widget.
        self.output_text.insert('end',translation.text)

    
# Check if the script is being run directly
if __name__ == '__main__':
    # Create the root window
    root = tk.Tk()

    # Set the size of the window
    root.geometry("900x500")
    
    # Set the icon for the window
    root.wm_iconbitmap('icon.ico')
    
    # Create an instance of the TranslatorApp and pass the root window
    translator_app = TranslatorApp(root)

    # Start the Tkinter event loop
    root.mainloop()