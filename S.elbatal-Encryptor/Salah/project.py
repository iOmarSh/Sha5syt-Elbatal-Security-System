import tkinter
from tkinter import filedialog, messagebox
import re
import numpy as np
import customtkinter
import os
from PIL import Image
import random
import math


class App(customtkinter.CTk):
    customtkinter.set_appearance_mode("Dark")

    def __init__(self):
        super().__init__()

        self.title("Home")
        self.geometry("900x500")
        Font = customtkinter.CTkFont(family="Georgia", size=40, weight="bold")
        customtkinter.set_default_color_theme("green")
        self.thirdFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.create_gui_elements(self.thirdFrame, "thirdFrame way")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        # self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
        #                                          dark_image=Image.open(os.path.join(image_path, "home_light.png")),
        #                                          size=(20, 20))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ICON (9).png")),
                                                 size=(26, 26))

        # --> Begin of navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)

        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Home page",
                                                             image=self.logo_image, compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.firstButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Ceaser",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.ceaser_button_event)
        self.firstButton.grid(row=1, column=0, sticky="ew", pady=5)
        self.secondButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Play Fair",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.playFair_button_event)

        self.secondButton.grid(row=1, column=1, sticky="ew", pady=5)
        self.RailFenceButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=10,
                                                       text="Rail Fence",
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),

                                                       image=self.logo_image, anchor="w",
                                                       command=self.RailFence_button_event)

        self.RailFenceButton.grid(row=2, column=0, sticky="ew", pady=5)
        self.fourthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Affine",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.Affine_button_event)

        self.fourthButton.grid(row=2, column=1, sticky="ew", pady=5)
        self.fifthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Transposition",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.Transposition_button_event)

        self.fifthButton.grid(row=3, column=0, sticky="ew", pady=5)
        self.Rot13Button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Rot 13",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.Rot13_button_event)
        self.Rot13Button.grid(row=3, column=1, sticky="ew", pady=5)
        self.HillcipherButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=10,
                                                        text="Hill Cipher",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),

                                                        image=self.logo_image, anchor="w",
                                                        command=self.Hillcipher_button_event)
        self.HillcipherButton.grid(row=4, column=0, sticky="ew", pady=5)
        self.eightButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Substitution",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.Substitution_button_event)
        self.eightButton.grid(row=4, column=1, sticky="ew", pady=5)
        self.VigenereButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10,
                                                      text="Vigenere",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.logo_image, anchor="w",
                                                      command=self.Vigenere_button_event)
        self.VigenereButton.grid(row=5, column=0, sticky="ns", pady=5, columnspan=2)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=0, pady=10, sticky="n", columnspan=2)
        self.playFairButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10,
                                                      text="Play Fair",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.logo_image, anchor="w")
        self.playFairButton.configure(command=self.playFairFunction)
        # ================> end of navigation <=================
        # ================> Frames Creation <===================
        self.ceaser = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.playFair = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.RailFence = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Affine = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Transposition = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Rot13 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Hillcipher = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Substitution = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Vigenere = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.tenthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eleventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.twelvethFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.create_gui_elements(self.ceaser, "Ceaser")
        self.create_gui_elements(self.playFair, "Play Fair")
        self.create_gui_elements(self.RailFence, "Rail Fence")
        self.create_gui_elements(self.Affine, "Affine")
        self.create_gui_elements(self.Rot13, "Rot13")
        self.create_gui_elements(self.Transposition, "Transposition")
        self.create_gui_elements(self.Hillcipher, "Hill Cipher")
        self.create_gui_elements(self.Substitution, "Substitution")
        self.create_gui_elements(self.Vigenere, "Vigenere")

        self.Rot13.keyTextBox.configure(state="readonly")
        # ==============> Edit process button name

        self.bind_update_process_button_text(self.ceaser)
        self.bind_update_process_button_text(self.playFair)
        self.bind_update_process_button_text(self.Affine)
        self.bind_update_process_button_text(self.Rot13)
        self.bind_update_process_button_text(self.Transposition)
        self.bind_update_process_button_text(self.RailFence)
        self.bind_update_process_button_text(self.Hillcipher)
        self.bind_update_process_button_text(self.Substitution)
        self.bind_update_process_button_text(self.Vigenere)

        # ================================================================>>
        self.ceaser.processButton.configure(command=self.ceaserprocess_button_click)
        self.playFair.processButton.configure(command=self.playFairFunction)
        self.playFairButton.configure(command=self.playFairFunction)
        self.Affine.processButton.configure(command=self.AffineFunction)
        self.Rot13.processButton.configure(command=self.Rot13Function)
        self.Transposition.processButton.configure(command=self.TranspositionFunction)
        self.RailFence.processButton.configure(command=self.RailFenceButtonClicked)
        self.Substitution.processButton.configure(command=self.SubstitutionFunction)
        self.Hillcipher.processButton.configure(command=self.HillcipherFunction)
        self.Vigenere.processButton.configure(command=self.VigenereFunction)
        # Select first frame as a default ============================================
        self.select_frame_by_name("ceaser")
        # ============================================================================
        self.ceaser.selectFileButton.configure(command=lambda: self.add_content(
            self.ceaser))  # self.playFair.selectFileButton.configure(command=self.download(self.playFair))
        self.Affine.selectFileButton.configure(command=lambda: self.add_content(self.Affine))
        self.Rot13.selectFileButton.configure(command=lambda: self.add_content(self.Rot13))
        self.Transposition.selectFileButton.configure(command=lambda: self.add_content(self.Transposition))
        self.RailFence.selectFileButton.configure(command=lambda: self.add_content(self.RailFence))
        self.Substitution.selectFileButton.configure(command=lambda: self.add_content(self.Substitution))
        self.Hillcipher.selectFileButton.configure(command=lambda: self.add_content(self.Hillcipher))
        self.Vigenere.selectFileButton.configure(command=lambda: self.add_content(self.Vigenere))
        self.playFair.selectFileButton.configure(command=lambda: self.add_content(self.playFair))
        # ============================================================================
        self.ceaser.downloadButton.configure(command=lambda: self.download(self.ceaser))
        self.Affine.downloadButton.configure(command=lambda: self.download(self.Affine))
        self.Rot13.downloadButton.configure(command=lambda: self.download(self.Rot13))
        self.Transposition.downloadButton.configure(command=lambda: self.download(self.Transposition))
        self.RailFence.downloadButton.configure(command=lambda: self.download(self.RailFence))
        self.Substitution.downloadButton.configure(command=lambda: self.download(self.Substitution))
        self.Hillcipher.downloadButton.configure(command=lambda: self.download(self.Hillcipher))
        self.Vigenere.downloadButton.configure(command=lambda: self.download(self.Vigenere))
        self.playFair.downloadButton.configure(command=lambda: self.download(self.playFair))

    # ===============================================================
    # ==> Functions
    def download(self, frameName):

        message = frameName.decryptTextBox.get()

        if message is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                                     title=f"Save {type} Message As")

            if file_path:
                # Write the encrypted message to the chosen file
                with open(file_path, "w") as file:
                    file.write(message)

                messagebox.showinfo("Download", "Your Encrypted Message is Downloaded Successfully.")
            else:
                messagebox.showinfo("Download", "Download Cancelled.")

    def VigenereFunction(self):
        # Get the ciphertext and key from the input fields
        self.Vigenere.decryptTextBox.delete(0, "end")
        PlainText = self.Vigenere.encryptTextBox.get()
        key = self.Vigenere.keyTextBox.get()

        # Store the indices of spaces in the plaintext and key
        space_indices_plain = [i for i, char in enumerate(PlainText) if char == ' ']
        space_indices_key = [i for i, char in enumerate(key) if char == ' ']

        # Remove spaces from the plaintext and key
        PlainText = PlainText.replace(' ', '')
        key = key.replace(' ', '')

        # Validate plaintext, ciphertext and key
        if not all(char.isalpha() for char in PlainText) or not all(char.isalpha() for char in key):
            messagebox.showerror("Error",
                                 "Invalid input. Please ensure the plaintext, ciphertext and key are alphabetic.")
            return

        # Validate key length
        if len(key) > len(PlainText):
            messagebox.showerror("Error",
                                 "Invalid key. The key length should be less than or equal to the plaintext or ciphertext length.")
            return

        rVar = self.Vigenere.radioVar.get()

        if rVar == 0:
            decryptedText = self.encryptionVigenereCipher(PlainText, key)
        else:
            try:
                decryptedText = self.decryptionVigenereCipher(PlainText, key)
            except ValueError:
                messagebox.showerror("Error", "Invalid ciphertext. It contains characters not present in the key.")
                return

        # Handle uppercase letters in the plaintext/ciphertext
        decryptedText = ''.join(
            [decryptedText[i].upper() if PlainText[i].isupper() else decryptedText[i] for i in range(len(PlainText))])

        # Insert the spaces back into the decrypted text and key
        for index in space_indices_plain:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]
        for index in space_indices_key:
            key = key[:index] + ' ' + key[index:]

        self.Vigenere.decryptTextBox.insert("end", decryptedText)

    def encryptionVigenereCipher(self, plainText, key):
        allLetters = "abcdefghijklmnopqrstuvwxyz"
        encryption = ""
        plainText = plainText.lower()
        key = key.lower()

        oldKey1 = len(plainText) // len(key)
        oldKey2 = len(plainText) / len(key)
        if oldKey2 > oldKey1:
            oldKey1 += 1

        key *= oldKey1

        j = 0
        for i in range(len(plainText)):
            if plainText[i] != ' ':
                numberOfLetterInMessage = allLetters.find(plainText[i])
                numberOfLetterInKey = allLetters.find(key[j])
                numberOfLetterInEncryption = (numberOfLetterInMessage + numberOfLetterInKey) % 26
                encryption += allLetters[numberOfLetterInEncryption]
                j += 1
            else:
                encryption += ' '
        return encryption

    def decryptionVigenereCipher(self, cipherText, key):
        allLetters = "abcdefghijklmnopqrstuvwxyz"
        decryption = ""
        cipherText = cipherText.lower()
        key = key.lower()

        oldKey1 = len(cipherText) // len(key)
        oldKey2 = len(cipherText) / len(key)
        if oldKey2 > oldKey1:
            oldKey1 += 1

        key *= oldKey1
        j = 0
        for i in range(len(cipherText)):
            if cipherText[i] != ' ':
                numberOfLetterInMessage = allLetters.find(cipherText[i])
                numberOfLetterInKey = allLetters.find(key[j])
                if (numberOfLetterInMessage - numberOfLetterInKey) < 0:
                    numberOfLetterInDecryption = (numberOfLetterInMessage - numberOfLetterInKey) + 26
                    decryption += allLetters[numberOfLetterInDecryption]
                else:
                    numberOfLetterInDecryption = (numberOfLetterInMessage - numberOfLetterInKey) % 26
                    decryption += allLetters[numberOfLetterInDecryption]
                j += 1
            else:
                decryption += ' '
        return decryption

    def HillcipherFunction(self):
        # Get the ciphertext and key from the input fields
        self.Hillcipher.decryptTextBox.delete(0, "end")
        PlainText = self.Hillcipher.encryptTextBox.get()
        key = self.Hillcipher.keyTextBox.get()

        # Store the indices of spaces
        space_indices = [i for i, char in enumerate(PlainText) if char == ' ']

        # Remove spaces from the plaintext
        PlainText = PlainText.replace(' ', '')

        # Validate plaintext and ciphertext
        if not all(char.isalpha() for char in PlainText):
            messagebox.showerror("Error",
                                 "Invalid plaintext. Please ensure the plaintext is alphabetic.")
            return

        # Validate plaintext length
        if len(PlainText) % 2 != 0:
            messagebox.showerror("Error",
                                 "Invalid plaintext. The length of the plaintext should be even.")
            return

        # Validate key
        if not ((len(key.split()) == 4 and all(i.isdigit() for i in key.split())) or (len(key) == 4 and key.isalpha())):
            messagebox.showerror("Error",
                                 "Invalid key. The key should be either four numbers separated by spaces or a string of length 4.")
            return

        rVar = self.Hillcipher.radioVar.get()

        if rVar == 0:
            decryptedText = self.encryptHill2x2(PlainText, key)
        else:
            decryptedText = self.decryptHill2x2(PlainText, key)

        # Insert the spaces back into the decrypted text
        for index in space_indices:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]

        self.Hillcipher.decryptTextBox.insert("end", decryptedText)

    def charToNum(self, char):
        return ord(char.lower()) - ord('a')

    def numToChar(self, num, is_upper):
        char = chr(num % 26 + ord('a'))
        if is_upper:
            return char.upper()
        else:
            return char

    def multiplyAndConvert(self, pair, keyMatrix):
        pairNums = np.array([[self.charToNum(char)] for char in pair])
        resultNums = np.dot(keyMatrix, pairNums).ravel() % 26
        return ''.join(self.numToChar(num, char.isupper()) for num, char in zip(resultNums, pair))

    def encryptHill2x2(self, text, keyMatrix):
        if keyMatrix.replace(' ', '').isdigit():
            # Split the string into a list of numbers
            numbers = list(map(int, keyMatrix.split()))
            # Arrange the numbers into a 2D numpy array
            keyMatrix = np.array(numbers).reshape(-1, 2)
        elif keyMatrix.isalpha():
            keyMatrix = self.key_matrix(keyMatrix)

        space_indices = [i for i, char in enumerate(text) if char == ' ']
        text = text.replace(' ', '')
        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        cipher = ''.join(self.multiplyAndConvert(pair, keyMatrix) for pair in pairs)
        for index in space_indices:
            cipher = cipher[:index] + ' ' + cipher[index:]
        return cipher

    # ----------------------------------------------------------------

    def key_matrix(self, key):
        key_values = [ord(char) - ord('a') for char in key]
        matrix = np.array([[key_values[0], key_values[1]], [key_values[2], key_values[3]]])
        if np.linalg.det(matrix) == 0:
            print("Invalid Key")
            exit()

        return matrix

    def inverse_matrix(self, matrix):
        det = int(round(np.linalg.det(matrix)))
        inv_det = pow(det, -1, 26)
        adjoint_matrix = np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])
        inverse = (inv_det * adjoint_matrix) % 26
        return inverse

    def decryptHill2x2(self, ciphertext, keyMatrix):
        if isinstance(keyMatrix, str):
            if keyMatrix.replace(' ', '').isdigit():
                # Split the string into a list of numbers
                numbers = list(map(int, keyMatrix.split()))
                # Arrange the numbers into a 2D numpy array
                keyMatrix = np.array(numbers).reshape(-1, 2)
            elif keyMatrix.isalpha():
                keyMatrix = self.key_matrix(keyMatrix)

        space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']
        ciphertext = ciphertext.replace(' ', '')
        inv_key = self.inverse_matrix(keyMatrix)
        ciphertext_values = [ord(char.lower()) - ord('a') for char in ciphertext]
        plaintext = ""
        for i in range(0, len(ciphertext_values), 2):
            block = np.array([[ciphertext_values[i]], [ciphertext_values[i + 1]]])
            decrypted_block = np.dot(inv_key, block) % 26
            for value, original_char in zip(decrypted_block, ciphertext[i:i + 2]):
                plaintext += self.numToChar(value[0], original_char.isupper())
        for index in space_indices:
            plaintext = plaintext[:index] + ' ' + plaintext[index:]
        return plaintext

    def add_content(self, frameName):
        # Ask the user to choose the file

        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], title="Choose File")

        if file_path:
            # Open the selected file and read its content
            with open(file_path, "r") as file:
                file_content = file.read()

                # Insert the file content into the entry widget
                frameName.encryptTextBox.delete(0, "end")
                frameName.encryptTextBox.insert(0, file_content)

            messagebox.showinfo("File Loaded", "Content from the selected file has been loaded.")
        else:
            messagebox.showinfo("No File Selected", "No file selected. Operation cancelled.")

    def Substitutionencrypt(self, plaintext, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
        keyIndices = [alphabet.index(k.lower()) for k in plaintext]
        return ''.join(key[keyIndex] for keyIndex in keyIndices)

    def Substitutiondecrypt(self, cipher, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
        decryptedText = ''
        for char in cipher:
            if char.isupper():
                try:
                    keyIndex = key.upper().index(char)
                except ValueError:
                    messagebox.showerror("Error", "Invalid cipher. It contains characters not present in the key.")
                    return
                decryptedText += alphabet[keyIndex].upper()
            else:
                try:
                    keyIndex = key.lower().index(char)
                except ValueError:
                    messagebox.showerror("Error", "Invalid cipher. It contains characters not present in the key.")
                    return
                decryptedText += alphabet[keyIndex].lower()
        return decryptedText

    def Rot13Function(self):
        # Get the ciphertext and key from the input fields
        self.Rot13.keyTextBox.configure(state="readonly")
        self.Rot13.decryptTextBox.delete(0, "end")
        PlainText = self.Rot13.encryptTextBox.get()
        rVar = self.Rot13.radioVar.get()

        if rVar == 0:
            decryptedText = self.Rot13encrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", decryptedText)
        else:
            encryptedText = self.Rot13decrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", encryptedText)

    def SubstitutionFunction(self):
        # Get the ciphertext and key from the input fields
        self.Substitution.decryptTextBox.delete(0, "end")
        PlainText = self.Substitution.encryptTextBox.get()
        key = self.Substitution.keyTextBox.get()

        # Store the indices of spaces
        space_indices = [i for i, char in enumerate(PlainText) if char == ' ']

        # Remove spaces from the plaintext
        PlainText = PlainText.replace(' ', '')

        # Validate plaintext and key
        if not all(char.isalpha() for char in PlainText):
            messagebox.showerror("Error", "Invalid plaintext. Please ensure the plaintext is alphabetic.")
            return

        # Validate key
        if len(key) != 26 or len(set(key.lower())) != 26 or not all(char.isalpha() for char in key):
            messagebox.showerror("Error", "Invalid key. The key should be 26 distinct alphabetic characters.")
            return

        # Convert key to match case of plaintext
        if PlainText.isupper():
            key = key.upper()
        else:
            key = key.lower()

        rVar = self.Substitution.radioVar.get()

        if rVar == 0:
            decryptedText = self.Substitutionencrypt(PlainText, key)
        else:
            try:
                decryptedText = self.Substitutiondecrypt(PlainText, key)
            except ValueError:
                messagebox.showerror("Error", "Invalid ciphertext. It contains characters not present in the key.")
                return

        # Convert the corresponding letter in the decrypted text to uppercase if the letter in the original text is uppercase
        decryptedText = ''.join(
            [decryptedText[i].upper() if PlainText[i].isupper() else decryptedText[i] for i in range(len(PlainText))])

        # Insert the spaces back into the decrypted text
        for index in space_indices:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]

        self.Substitution.decryptTextBox.insert("end", decryptedText)

    def Rot13encrypt(self, Plaintext):
        translated = ''
        for char in Plaintext:
            if char.isalpha():
                if char.isupper():
                    translated += chr(((ord(char) - 65 + 13) % 26) + 65)
                elif char.islower():
                    translated += chr(((ord(char) - 97 + 13) % 26) + 97)
            else:
                translated += char
        return translated

    def Rot13decrypt(self, cipher_text):
        decrypted = ''
        for char in cipher_text:
            if char.isalpha():
                if char.isupper():
                    decrypted += chr(((ord(char) - 65 - 13) % 26) + 65)
                elif char.islower():
                    decrypted += chr(((ord(char) - 97 - 13) % 26) + 97)
            else:
                decrypted += char
        return decrypted

    def ceaserprocess_button_click(self):
        # Get the ciphertext and key from the input fields
        PTxt = self.ceaser.encryptTextBox.get()
        K = self.ceaser.keyTextBox.get()
        CTxt = self.ceaser.decryptTextBox.get()
        rVar = self.ceaser.radioVar.get()

        # Validate inputs

        # Perform decryption
        if rVar == 0:
            if not all(char.isalpha() or char.isspace() for char in PTxt) or not K.isdigit():
                messagebox.showerror("Error",
                                     "Invalid input. Please ensure the plaintext and ciphertext are alphabetic (spaces allowed) and the key is numeric.")
                return
            decryptedText = self.CeaserEncryption(PTxt, int(K))
            self.ceaser.decryptTextBox.insert("end", decryptedText)
        else:
            if not all(
                    char.isalpha() or char.isspace() for char in CTxt) or not K.isdigit():
                messagebox.showerror("Error",
                                     "Invalid input. Please ensure the plaintext and ciphertext are alphabetic (spaces allowed) and the key is numeric.")
                return
            encryptedText = self.CeaserDecryption(CTxt, int(K))
            self.ceaser.encryptTextBox.insert("end", encryptedText)

    def columnar_transposition_encrypt(self, msg, key):
        cipher = ""
        k_indx = 0

        # Add spaces after every key size - 1 characters
        msg = ' '.join(msg[i:i + int(key) - 1] for i in range(0, len(msg), int(key) - 1))

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))
        col = len(key)
        row = int(math.ceil(msg_len / col))
        fill_null = int((row * col) - msg_len)
        msg_lst.extend(' ' * fill_null)
        matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] for row in matrix])
            k_indx += 1

        return cipher

    def columnar_transposition_decrypt(self, cipher, key):
        k_indx = 0
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)
        col = len(key)
        row = int(math.ceil(msg_len / col))
        key_lst = sorted(list(key))
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            for j in range(row):
                if msg_indx < len(msg_lst) and curr_idx < len(dec_cipher[j]):
                    dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                    msg_indx += 1
            k_indx += 1

        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot handle repeating words.")

        null_count = msg.count(' ')

        if null_count > 0:
            msg = msg[: -null_count]

        # Remove the spaces added during encryption
        msg = msg.replace(' ', '')

        return msg

    def AffineFunction(self):  # function

        def ceaserprocess_button_click(self):
            # Get the ciphertext and key from the input fields
            PTxt = self.ceaser.encryptTextBox.get()
            K = self.ceaser.keyTextBox.get()
            CTxt = self.ceaser.decryptTextBox.get()
            rVar = self.ceaser.radioVar.get()
            # Perform decryption
            if rVar == 0:
                decryptedText = self.CeaserEncryption(PTxt, iznt(K))
                self.ceaser.decryptTextBox.insert("end", decryptedText)
            else:
                encryptedText = self.CeaserDecryption(CTxt, int(K))
                self.ceaser.encryptTextBox.insert("end", encryptedText)

    def AffineFunction(self):
        # Get the ciphertext and key from the input fields
        self.Affine.decryptTextBox.delete(0, "end")
        PTxt = self.Affine.encryptTextBox.get()
        k = self.Affine.keyTextBox.get()

        # Validate key
        if not re.match(r'^\d+,\d+$', k) or any(int(i) <= 0 for i in k.split(',')):
            messagebox.showerror("Error",
                                 "Invalid key. Please ensure the key is two numbers separated by a comma and both are greater than 0.")
            return

        k = [int(i) for i in k.split(',')]

        rVar = self.Affine.radioVar.get()

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return

            Text = self.encryptAffine(PTxt, k)
            self.Affine.decryptTextBox.insert("end", Text)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return

            Text = self.decryptAffine(PTxt, k)
            self.Affine.decryptTextBox.insert("end", Text)

    def TranspositionFunction(self):
        # Get the ciphertext and key from the input fields
        self.Transposition.decryptTextBox.delete(0, "end")
        PTxt = self.Transposition.encryptTextBox.get()
        k = self.Transposition.keyTextBox.get()

        # Validate key
        if not k.isdigit() or len(k) <= 1 or len(set(k)) != len(k) or any(int(i) < 1 for i in k):
            messagebox.showerror("Error",
                                 "Invalid key. Please ensure the key is a string of numbers with length greater than 1, each digit is greater than or equal to 1, and all digits are distinct.")
            return

        rVar = self.Transposition.radioVar.get()

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return

            Text = self.columnar_transposition_encrypt(PTxt, k)
            self.Transposition.decryptTextBox.insert("end", Text)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return

            Text = self.columnar_transposition_decrypt(PTxt, k)
            self.Transposition.decryptTextBox.insert("end", Text)

        # # Perform decryption
        # if rVar == 0:
        #     Text = self.encryptAffine(PTxt,k)
        #     self.Affine.decryptTextBox.insert("end", Text)
        # else:
        #     Text = self.decryptAffine(PTxt, k)
        #     self.Affine.decryptTextBox.insert("end", Text)

    def inverse(self, b):
        # T = T1 - (T2 * Q)
        # Q , A, B, r, T1, T2, T
        t1, t2 = 0, 1
        ans = 0
        a = 26
        while b != 0:
            q = int(a / b);
            r = a % b;
            t = t1 - (t2 * q)
            if r == 0:
                ans = t2
                break
            a, b = b, r
            t1, t2 = t2, t

        if ans < 0:
            return ans + 26
        else:
            return ans

    def decryptAffine(self, cipher, key):
        inv = self.inverse(key[0])
        decryptedText = ''
        for i in range(len(cipher)):
            if cipher[i] >= 'A' and cipher[i] <= 'Z':
                decryptedText += chr(((inv * ((ord(cipher[i]) - ord('A')) - key[1])) % 26) + ord('A'))
            elif cipher[i] >= 'a' and cipher[i] <= 'z':
                decryptedText += chr(((inv * ((ord(cipher[i]) - ord('a')) - key[1])) % 26) + ord('a'))
            else:
                decryptedText += ' '
        return decryptedText

    def encryptAffine(self, text, key):
        # c = (ax + b) mod 26
        encryptedText = ""
        for i in range(len(text)):
            if text[i] >= 'A' and text[i] <= 'Z':
                encryptedText += chr((((key[0] * (ord(text[i]) - ord('A'))) + key[1]) % 26) + ord('A'))
            elif text[i] >= 'a' and text[i] <= 'z':
                encryptedText += chr((((key[0] * (ord(text[i]) - ord('a'))) + key[1]) % 26) + ord('a'))
            else:
                encryptedText += ' '
        return encryptedText

    def bind_update_process_button_text(self, frame):
        frame.radioVar.trace("w", lambda *args, f=frame: self.update_process_button_text(f))

    def CeaserEncryption(self, plaintext, n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) + n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) + n - 97) % 26 + 97)
        self.ceaser.decryptTextBox.delete(0, "end")
        return ans

    def CeaserDecryption(self, plaintext, n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) - n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) - n - 97) % 26 + 97)
        self.ceaser.encryptTextBox.delete(0, "end")
        return ans

    # ==========================================================>
    def generateKeyMatrix(self, key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        keyMatrix = [[None] * 5 for _ in range(5)]
        keySet = set()
        for char in key + alphabet:
            if char not in keySet:
                row, col = divmod(len(keySet), 5)
                keyMatrix[row][col] = char
                keySet.add(char)
        return keyMatrix

    def prepareMessage(self, message):
        message = message.upper().replace(" ", "")
        preparedMessage = ""
        i = 0
        while i < len(message):
            if i == len(message) - 1:
                preparedMessage += message[i] + "X"
            elif message[i] == message[i + 1]:
                preparedMessage += message[i] + "X"
                i -= 1
            else:
                preparedMessage += message[i:i + 2]
            i += 2

        return preparedMessage

    def encryptMessage(self, keyMatrix, message):
        encryptedMessage = ""

        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)
            if rowA == rowB:
                encryptedMessage += keyMatrix[rowA][(colA + 1) % 5] + keyMatrix[rowB][(colB + 1) % 5]
            elif colA == colB:
                encryptedMessage += keyMatrix[(rowA + 1) % 5][colA] + keyMatrix[(rowB + 1) % 5][colB]
            else:
                encryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return encryptedMessage

    def findPosition(self, keyMatrix, char):
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j] == char:
                    return i, j

    def decryptMessage(self, keyMatrix, message):
        decryptedMessage = ""
        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)

            if rowA == rowB:
                decryptedMessage += keyMatrix[rowA][(colA - 1) % 5] + keyMatrix[rowB][(colB - 1) % 5]
            elif colA == colB:
                decryptedMessage += keyMatrix[(rowA - 1) % 5][colA] + keyMatrix[(rowB - 1) % 5][colB]
            else:
                decryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return decryptedMessage

    def playFairFunction(self):
        msg = self.playFair.encryptTextBox.get()
        ky = self.playFair.keyTextBox.get()
        rVar = self.playFair.radioVar.get()

        # Replace 'j' with 'i'
        msg = msg.replace("j", "i")
        cipher = msg  # Assign msg to cipher before replacing 'j' with 'i'
        cipher = cipher.replace("j", "i")
        ky = ky.replace("j", "i")

        # Perform operation
        if rVar == 0:
            if not msg.isalpha() or not ky.isalpha():
                messagebox.showerror("Error", "Invalid input or key. Please ensure the key and message are alphabetic.")
                return
            key = ky.upper().replace(" ", "")
            keyMatrix = self.generateKeyMatrix(key)

            # Prepare message
            msg = self.prepareMessage(msg)
            result = self.encryptMessage(keyMatrix, msg)

            # Convert result to the case of the original message
            result = result.upper() if msg.isupper() else result.lower()

            self.playFair.decryptTextBox.delete(0, tkinter.END)
            self.playFair.decryptTextBox.insert("end", result)
        elif rVar == 1:
            if not cipher.isalpha() or not ky.isalpha():
                messagebox.showerror("Error",
                                     "Invalid input or key. Please ensure the key and cipher text are alphabetic.")
                return
            key = ky.upper().replace(" ", "")
            keyMatrix = self.generateKeyMatrix(key)

            # Prepare message
            msg = self.prepareMessage(msg)
            result = self.decryptMessage(keyMatrix, cipher)

            # Convert result to the case of the original cipher
            result = result.upper() if cipher.isupper() else result.lower()

            self.playFair.encryptTextBox.delete(0, tkinter.END)
            self.playFair.encryptTextBox.insert("end", result)

        # return result

    # ==============================================================>
    def update_process_button_text(self, frame):
        # Get the value of the variable to determine which radio button is selected
        selected_value = frame.radioVar.get()

        if selected_value == 0:  # Encryption
            frame.processButton.configure(text="Encrypt")


        else:  # Decryption
            frame.processButton.configure(text="Decrypt")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # ________________________________________

    def RailFenceButtonClicked(self):
        # Get the ciphertext and key from the input fields
        self.RailFence.decryptTextBox.delete(0, "end")
        PlainText = self.RailFence.encryptTextBox.get()
        Key = self.RailFence.keyTextBox.get()
        rVar = self.RailFence.radioVar.get()

        # Validate key
        if not Key.isdigit() or int(Key) <= 1:
            messagebox.showerror("Error", "Invalid key. Please ensure the key is a positive number greater than 1.")
            return

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PlainText):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return
            if int(Key) >= len(PlainText):
                decryptedText = PlainText
            else:
                decryptedText = self.rail_fence_encrypt(PlainText, int(Key))
            self.RailFence.decryptTextBox.insert("end", decryptedText)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PlainText):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return
            if int(Key) >= len(PlainText):
                encryptedText = PlainText
            else:
                encryptedText = self.rail_fence_decrypt(PlainText, int(Key))
            # encryptedText = self.rail_fence_decrypt(PlainText, int(Key))
            self.RailFence.decryptTextBox.insert("end", encryptedText)

    def rail_fence_encrypt(self, plaintext, rails):
        rails = int(rails)
        fence = [[] for _ in range(rails)]  # Create a list of empty lists to represent the fence
        rail = 0
        direction = 1  # Direction of movement along the rails (down or up)
        space_indices = [i for i, char in enumerate(plaintext) if char == ' ']  # Store the indices of spaces

        # Fill the fence with characters from the plaintext
        for char in plaintext:
            if char == ' ':
                continue
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1  # Change direction when reaching the top or bottom rail

        # Flatten the fence and concatenate the characters
        encrypted_text = ''.join(char for rail in fence for char in rail)

        # Add the spaces back into the encrypted text
        for index in space_indices:
            encrypted_text = encrypted_text[:index] + ' ' + encrypted_text[index:]

        return encrypted_text

    def rail_fence_decrypt(self, ciphertext, rails):
        rails = int(rails)
        fence = [['' for _ in ciphertext] for _ in range(rails)]  # Create an empty fence matrix
        rail = 0
        direction = 1
        space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']  # Store the indices of spaces

        # Remove spaces from ciphertext
        ciphertext = ciphertext.replace(' ', '')

        # Fill the fence matrix with placeholders for characters
        for i in range(len(ciphertext)):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Fill the fence matrix with ciphertext characters
        index = 0
        for i in range(rails):
            for j in range(len(ciphertext)):
                if fence[i][j] == '*':
                    fence[i][j] = ciphertext[index]
                    index += 1

        # Read the characters from the fence matrix to retrieve the plaintext
        rail = 0
        direction = 1
        decrypted_text = ''
        for i in range(len(ciphertext)):
            decrypted_text += fence[rail][i]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Add the spaces back into the decrypted text
        for index in space_indices:
            decrypted_text = decrypted_text[:index] + ' ' + decrypted_text[index:]

        return decrypted_text

    # ---------------------------------------------
    def Rot13Function(self):
        # Set the key to a static number
        self.Rot13.keyTextBox.delete(0, "end")
        self.Rot13.keyTextBox.insert("end", "13")
        self.Rot13.keyTextBox.configure(state="readonly")

        self.Rot13.decryptTextBox.delete(0, "end")
        PlainText = self.Rot13.encryptTextBox.get()
        rVar = self.Rot13.radioVar.get()

        if not all(char.isalpha() or char.isspace() for char in PlainText):
            messagebox.showerror("Error",
                                 "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
            return
        # Divide the function based on the value of rVar
        if rVar == 0:
            decryptedText = self.Rot13encrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", decryptedText)
        else:
            encryptedText = self.Rot13decrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", encryptedText)

    def select_frame_by_name(self, name):
        # set button color for selected button

        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "ceaser" else "transparent")
        self.secondButton.configure(fg_color=("gray75", "gray25") if name == "playFair" else "transparent")

        self.fourthButton.configure(fg_color=("gray75", "gray25") if name == "Affine" else "transparent")
        self.fifthButton.configure(fg_color=("gray75", "gray25") if name == "Transposition" else "transparent")
        self.RailFenceButton.configure(fg_color=("gray75", "gray25") if name == "RailFence" else "transparent")

        self.Rot13Button.configure(fg_color=("gray75", "gray25") if name == "Rot13" else "transparent")
        self.HillcipherButton.configure(fg_color=("gray75", "gray25") if name == "Hillcipher" else "transparent")
        self.eightButton.configure(fg_color=("gray75", "gray25") if name == "Substitution" else "transparent")
        self.VigenereButton.configure(fg_color=("gray75", "gray25") if name == "Vigenere" else "transparent")

        # show selected frame
        if name == "ceaser":
            self.ceaser.grid(row=0, column=1, sticky="nsew")
        else:
            self.ceaser.grid_forget()

        if name == "playFair":
            self.playFair.grid(row=0, column=1, sticky="nsew")
        else:
            self.playFair.grid_forget()

        if name == "RailFence":
            self.RailFence.grid(row=0, column=1, sticky="nsew")
        else:
            self.RailFence.grid_forget()

        if name == "Affine":
            self.Affine.grid(row=0, column=1, sticky="nsew")
        else:
            self.Affine.grid_forget()

        if name == "Transposition":
            self.Transposition.grid(row=0, column=1, sticky="nsew")
        else:
            self.Transposition.grid_forget()

        if name == "Rot13":
            self.Rot13.grid(row=0, column=1, sticky="nsew")
        else:
            self.Rot13.grid_forget()

        if name == "Hillcipher":
            self.Hillcipher.grid(row=0, column=1, sticky="nsew")
        else:
            self.Hillcipher.grid_forget()

        if name == "Substitution":
            self.Substitution.grid(row=0, column=1, sticky="nsew")
        else:
            self.Substitution.grid_forget()
        if name == "Vigenere":
            self.Vigenere.grid(row=0, column=1, sticky="nsew")
        else:
            self.Vigenere.grid_forget()
        if name == "tenthFrame":
            self.tenthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.tenthFrame.grid_forget()

        if name == "eleventhFrame":
            self.eleventhFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eleventhFrame.grid_forget()
        if name == "twelvethFrame":
            self.twelvethFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.twelvethFrame.grid_forget()

    # -----------------------------------------
    def ceaser_button_event(self):
        self.select_frame_by_name("ceaser")

    def playFair_button_event(self):
        self.select_frame_by_name("playFair")

    def RailFence_button_event(self):
        self.select_frame_by_name("RailFence")

    def Affine_button_event(self):
        self.select_frame_by_name("Affine")

    def Transposition_button_event(self):
        self.select_frame_by_name("Transposition")

    def Rot13_button_event(self):
        self.select_frame_by_name("Rot13")

    def Hillcipher_button_event(self):
        self.select_frame_by_name("Hillcipher")

    def Substitution_button_event(self):
        self.select_frame_by_name("Substitution")

    def Vigenere_button_event(self):
        self.select_frame_by_name("Vigenere")

    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")

    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")

    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def Hillcipher_button_event(self):
        self.select_frame_by_name("Hillcipher")

    def Substitution_button_event(self):
        self.select_frame_by_name("Substitution")

    def Vigenere_button_event(self):
        self.select_frame_by_name("Vigenere")

    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")

    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")

    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def ClearFields(self, frame):
        # Access attributes from frame_name object
        frame.decryptTextBox.delete(0, "end")
        frame.keyTextBox.delete(0, "end")
        frame.encryptTextBox.delete(0, "end")

    def create_gui_elements(self, frame_name, frame_label):
        frame_name.grid_columnconfigure(0, weight=1)
        frame_name.grid_rowconfigure(7, weight=1)

        Font = ("Georgia", 40, "bold")  # Assuming Font is defined somewhere
        rFont = ("Calibri", 20)
        Frame_label = customtkinter.CTkLabel(frame_name, text=frame_label, font=Font)
        Frame_label.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

        radio_var = customtkinter.IntVar(value=0)
        encryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=0,
                                                       text="Encryption", font=rFont)
        encryptionRadio.grid(row=1, column=0, pady=0, padx=0, sticky="s")
        decryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=1,
                                                       text="Decryption", font=rFont)
        decryptionRadio.grid(row=1, column=1, pady=0, padx=100, sticky="w")

        encryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Plain text", height=50, width=0,
                                                font=rFont)
        encryptTextBox.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        decryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Cipher text", height=50, width=0,
                                                font=rFont)
        decryptTextBox.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        keyTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Key", height=50, width=250, font=rFont)
        keyTextBox.grid(row=3, column=0, padx=(20, 20), pady=0, sticky="ns", columnspan=2)

        processButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,
                                                text="Encrypt",
                                                font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), anchor="ns")
        processButton.grid(row=4, column=0, sticky="s", pady=5, columnspan=2)
        clearButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,
                                              text="Clear",
                                              font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"), anchor="ns",
                                              command=lambda: self.ClearFields(frame_name))
        clearButton.grid(row=4, column=1, sticky="s", pady=5, padx=5, columnspan=2)

        selectFileButton = customtkinter.CTkButton(frame_name, text="Select File", width=300, height=40
                                                   )
        selectFileButton.grid(row=5, column=0, sticky="s", pady=5, columnspan=2)

        downloadFileButton = customtkinter.CTkButton(frame_name, text="Download File", width=300, height=40)
        downloadFileButton.grid(row=6, column=0, sticky="s", pady=5, columnspan=2)

        frame_name.encryptTextBox = encryptTextBox
        frame_name.Frame_label = Frame_label
        frame_name.encryptionRadio = encryptionRadio
        frame_name.decryptionRadio = decryptionRadio
        frame_name.decryptTextBox = decryptTextBox
        frame_name.keyTextBox = keyTextBox
        frame_name.processButton = processButton
        frame_name.selectFileButton = selectFileButton
        frame_name.downloadButton = downloadFileButton
        frame_name.radioVar = radio_var


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # Your additional code goes here


def main():
    app = App()
    app.mainloop()


import tkinter
from tkinter import filedialog, messagebox
import re
import numpy as np
import customtkinter
import os
from PIL import Image
import random
import math


class App(customtkinter.CTk):
    customtkinter.set_appearance_mode("Dark")

    def __init__(self):
        super().__init__()

        self.title("Home")
        self.geometry("900x500")
        Font = customtkinter.CTkFont(family="Georgia", size=40, weight="bold")
        customtkinter.set_default_color_theme("green")
        self.thirdFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.create_gui_elements(self.thirdFrame, "thirdFrame way")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        # self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
        #                                          dark_image=Image.open(os.path.join(image_path, "home_light.png")),
        #                                          size=(20, 20))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ICON (9).png")),
                                                 size=(26, 26))

        # --> Begin of navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)

        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Home page",
                                                             image=self.logo_image, compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.firstButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Ceaser",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.ceaser_button_event)
        self.firstButton.grid(row=1, column=0, sticky="ew", pady=5)
        self.secondButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Play Fair",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.playFair_button_event)

        self.secondButton.grid(row=1, column=1, sticky="ew", pady=5)
        self.RailFenceButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=10,
                                                       text="Rail Fence",
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),

                                                       image=self.logo_image, anchor="w",
                                                       command=self.RailFence_button_event)

        self.RailFenceButton.grid(row=2, column=0, sticky="ew", pady=5)
        self.fourthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Affine",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.Affine_button_event)

        self.fourthButton.grid(row=2, column=1, sticky="ew", pady=5)
        self.fifthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Transposition",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.Transposition_button_event)

        self.fifthButton.grid(row=3, column=0, sticky="ew", pady=5)
        self.Rot13Button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Rot 13",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.Rot13_button_event)
        self.Rot13Button.grid(row=3, column=1, sticky="ew", pady=5)
        self.HillcipherButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=10,
                                                        text="Hill Cipher",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),

                                                        image=self.logo_image, anchor="w",
                                                        command=self.Hillcipher_button_event)
        self.HillcipherButton.grid(row=4, column=0, sticky="ew", pady=5)
        self.eightButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Substitution",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.Substitution_button_event)
        self.eightButton.grid(row=4, column=1, sticky="ew", pady=5)
        self.VigenereButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10,
                                                      text="Vigenere",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.logo_image, anchor="w",
                                                      command=self.Vigenere_button_event)
        self.VigenereButton.grid(row=5, column=0, sticky="ns", pady=5, columnspan=2)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=0, pady=10, sticky="n", columnspan=2)
        self.playFairButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10,
                                                      text="Play Fair",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.logo_image, anchor="w")
        self.playFairButton.configure(command=self.playFairFunction)
        # ================> end of navigation <=================
        # ================> Frames Creation <===================
        self.ceaser = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.playFair = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.RailFence = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Affine = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Transposition = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Rot13 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Hillcipher = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Substitution = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Vigenere = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.tenthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eleventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.twelvethFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.create_gui_elements(self.ceaser, "Ceaser")
        self.create_gui_elements(self.playFair, "Play Fair")
        self.create_gui_elements(self.RailFence, "Rail Fence")
        self.create_gui_elements(self.Affine, "Affine")
        self.create_gui_elements(self.Rot13, "Rot13")
        self.create_gui_elements(self.Transposition, "Transposition")
        self.create_gui_elements(self.Hillcipher, "Hill Cipher")
        self.create_gui_elements(self.Substitution, "Substitution")
        self.create_gui_elements(self.Vigenere, "Vigenere")

        self.Rot13.keyTextBox.configure(state="readonly")
        # ==============> Edit process button name

        self.bind_update_process_button_text(self.ceaser)
        self.bind_update_process_button_text(self.playFair)
        self.bind_update_process_button_text(self.Affine)
        self.bind_update_process_button_text(self.Rot13)
        self.bind_update_process_button_text(self.Transposition)
        self.bind_update_process_button_text(self.RailFence)
        self.bind_update_process_button_text(self.Hillcipher)
        self.bind_update_process_button_text(self.Substitution)
        self.bind_update_process_button_text(self.Vigenere)

        # ================================================================>>
        self.ceaser.processButton.configure(command=self.ceaserprocess_button_click)
        self.playFair.processButton.configure(command=self.playFairFunction)
        self.playFairButton.configure(command=self.playFairFunction)
        self.Affine.processButton.configure(command=self.AffineFunction)
        self.Rot13.processButton.configure(command=self.Rot13Function)
        self.Transposition.processButton.configure(command=self.TranspositionFunction)
        self.RailFence.processButton.configure(command=self.RailFenceButtonClicked)
        self.Substitution.processButton.configure(command=self.SubstitutionFunction)
        self.Hillcipher.processButton.configure(command=self.HillcipherFunction)
        self.Vigenere.processButton.configure(command=self.VigenereFunction)
        # Select first frame as a default ============================================
        self.select_frame_by_name("ceaser")
        # ============================================================================
        self.ceaser.selectFileButton.configure(command=lambda: self.add_content(
            self.ceaser))  # self.playFair.selectFileButton.configure(command=self.download(self.playFair))
        self.Affine.selectFileButton.configure(command=lambda: self.add_content(self.Affine))
        self.Rot13.selectFileButton.configure(command=lambda: self.add_content(self.Rot13))
        self.Transposition.selectFileButton.configure(command=lambda: self.add_content(self.Transposition))
        self.RailFence.selectFileButton.configure(command=lambda: self.add_content(self.RailFence))
        self.Substitution.selectFileButton.configure(command=lambda: self.add_content(self.Substitution))
        self.Hillcipher.selectFileButton.configure(command=lambda: self.add_content(self.Hillcipher))
        self.Vigenere.selectFileButton.configure(command=lambda: self.add_content(self.Vigenere))
        self.playFair.selectFileButton.configure(command=lambda: self.add_content(self.playFair))
        # ============================================================================
        self.ceaser.downloadButton.configure(command=lambda: self.download(self.ceaser))
        self.Affine.downloadButton.configure(command=lambda: self.download(self.Affine))
        self.Rot13.downloadButton.configure(command=lambda: self.download(self.Rot13))
        self.Transposition.downloadButton.configure(command=lambda: self.download(self.Transposition))
        self.RailFence.downloadButton.configure(command=lambda: self.download(self.RailFence))
        self.Substitution.downloadButton.configure(command=lambda: self.download(self.Substitution))
        self.Hillcipher.downloadButton.configure(command=lambda: self.download(self.Hillcipher))
        self.Vigenere.downloadButton.configure(command=lambda: self.download(self.Vigenere))
        self.playFair.downloadButton.configure(command=lambda: self.download(self.playFair))

    # ===============================================================
    # ==> Functions
    def download(self, frameName):

        message = frameName.decryptTextBox.get()

        if message is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                                     title=f"Save {type} Message As")

            if file_path:
                # Write the encrypted message to the chosen file
                with open(file_path, "w") as file:
                    file.write(message)

                messagebox.showinfo("Download", "Your Encrypted Message is Downloaded Successfully.")
            else:
                messagebox.showinfo("Download", "Download Cancelled.")

    def VigenereFunction(self):
        # Get the ciphertext and key from the input fields
        self.Vigenere.decryptTextBox.delete(0, "end")
        PlainText = self.Vigenere.encryptTextBox.get()
        key = self.Vigenere.keyTextBox.get()

        # Store the indices of spaces in the plaintext and key
        space_indices_plain = [i for i, char in enumerate(PlainText) if char == ' ']
        space_indices_key = [i for i, char in enumerate(key) if char == ' ']

        # Remove spaces from the plaintext and key
        PlainText = PlainText.replace(' ', '')
        key = key.replace(' ', '')

        # Validate plaintext, ciphertext and key
        if not all(char.isalpha() for char in PlainText) or not all(char.isalpha() for char in key):
            messagebox.showerror("Error",
                                 "Invalid input. Please ensure the plaintext, ciphertext and key are alphabetic.")
            return

        # Validate key length
        if len(key) > len(PlainText):
            messagebox.showerror("Error",
                                 "Invalid key. The key length should be less than or equal to the plaintext or ciphertext length.")
            return

        rVar = self.Vigenere.radioVar.get()

        if rVar == 0:
            decryptedText = self.encryptionVigenereCipher(PlainText, key)
        else:
            try:
                decryptedText = self.decryptionVigenereCipher(PlainText, key)
            except ValueError:
                messagebox.showerror("Error", "Invalid ciphertext. It contains characters not present in the key.")
                return

        # Handle uppercase letters in the plaintext/ciphertext
        decryptedText = ''.join(
            [decryptedText[i].upper() if PlainText[i].isupper() else decryptedText[i] for i in range(len(PlainText))])

        # Insert the spaces back into the decrypted text and key
        for index in space_indices_plain:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]
        for index in space_indices_key:
            key = key[:index] + ' ' + key[index:]

        self.Vigenere.decryptTextBox.insert("end", decryptedText)

    def encryptionVigenereCipher(self, plainText, key):
        allLetters = "abcdefghijklmnopqrstuvwxyz"
        encryption = ""
        plainText = plainText.lower()
        key = key.lower()

        oldKey1 = len(plainText) // len(key)
        oldKey2 = len(plainText) / len(key)
        if oldKey2 > oldKey1:
            oldKey1 += 1

        key *= oldKey1

        j = 0
        for i in range(len(plainText)):
            if plainText[i] != ' ':
                numberOfLetterInMessage = allLetters.find(plainText[i])
                numberOfLetterInKey = allLetters.find(key[j])
                numberOfLetterInEncryption = (numberOfLetterInMessage + numberOfLetterInKey) % 26
                encryption += allLetters[numberOfLetterInEncryption]
                j += 1
            else:
                encryption += ' '
        return encryption

    def decryptionVigenereCipher(self, cipherText, key):
        allLetters = "abcdefghijklmnopqrstuvwxyz"
        decryption = ""
        cipherText = cipherText.lower()
        key = key.lower()

        oldKey1 = len(cipherText) // len(key)
        oldKey2 = len(cipherText) / len(key)
        if oldKey2 > oldKey1:
            oldKey1 += 1

        key *= oldKey1
        j = 0
        for i in range(len(cipherText)):
            if cipherText[i] != ' ':
                numberOfLetterInMessage = allLetters.find(cipherText[i])
                numberOfLetterInKey = allLetters.find(key[j])
                if (numberOfLetterInMessage - numberOfLetterInKey) < 0:
                    numberOfLetterInDecryption = (numberOfLetterInMessage - numberOfLetterInKey) + 26
                    decryption += allLetters[numberOfLetterInDecryption]
                else:
                    numberOfLetterInDecryption = (numberOfLetterInMessage - numberOfLetterInKey) % 26
                    decryption += allLetters[numberOfLetterInDecryption]
                j += 1
            else:
                decryption += ' '
        return decryption

    def HillcipherFunction(self):
        # Get the ciphertext and key from the input fields
        self.Hillcipher.decryptTextBox.delete(0, "end")
        PlainText = self.Hillcipher.encryptTextBox.get()
        key = self.Hillcipher.keyTextBox.get()

        # Store the indices of spaces
        space_indices = [i for i, char in enumerate(PlainText) if char == ' ']

        # Remove spaces from the plaintext
        PlainText = PlainText.replace(' ', '')

        # Validate plaintext and ciphertext
        if not all(char.isalpha() for char in PlainText):
            messagebox.showerror("Error",
                                 "Invalid plaintext. Please ensure the plaintext is alphabetic.")
            return

        # Validate plaintext length
        if len(PlainText) % 2 != 0:
            messagebox.showerror("Error",
                                 "Invalid plaintext. The length of the plaintext should be even.")
            return

        # Validate key
        if not ((len(key.split()) == 4 and all(i.isdigit() for i in key.split())) or (len(key) == 4 and key.isalpha())):
            messagebox.showerror("Error",
                                 "Invalid key. The key should be either four numbers separated by spaces or a string of length 4.")
            return

        rVar = self.Hillcipher.radioVar.get()

        if rVar == 0:
            decryptedText = self.encryptHill2x2(PlainText, key)
        else:
            decryptedText = self.decryptHill2x2(PlainText, key)

        # Insert the spaces back into the decrypted text
        for index in space_indices:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]

        self.Hillcipher.decryptTextBox.insert("end", decryptedText)

    def charToNum(self, char):
        return ord(char.lower()) - ord('a')

    def numToChar(self, num, is_upper):
        char = chr(num % 26 + ord('a'))
        if is_upper:
            return char.upper()
        else:
            return char

    def multiplyAndConvert(self, pair, keyMatrix):
        pairNums = np.array([[self.charToNum(char)] for char in pair])
        resultNums = np.dot(keyMatrix, pairNums).ravel() % 26
        return ''.join(self.numToChar(num, char.isupper()) for num, char in zip(resultNums, pair))

    def encryptHill2x2(self, text, keyMatrix):
        if keyMatrix.replace(' ', '').isdigit():
            # Split the string into a list of numbers
            numbers = list(map(int, keyMatrix.split()))
            # Arrange the numbers into a 2D numpy array
            keyMatrix = np.array(numbers).reshape(-1, 2)
        elif keyMatrix.isalpha():
            keyMatrix = self.key_matrix(keyMatrix)

        space_indices = [i for i, char in enumerate(text) if char == ' ']
        text = text.replace(' ', '')
        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        cipher = ''.join(self.multiplyAndConvert(pair, keyMatrix) for pair in pairs)
        for index in space_indices:
            cipher = cipher[:index] + ' ' + cipher[index:]
        return cipher

    # ----------------------------------------------------------------

    def key_matrix(self, key):
        key_values = [ord(char) - ord('a') for char in key]
        matrix = np.array([[key_values[0], key_values[1]], [key_values[2], key_values[3]]])
        if np.linalg.det(matrix) == 0:
            print("Invalid Key")
            exit()

        return matrix

    def inverse_matrix(self, matrix):
        det = int(round(np.linalg.det(matrix)))
        inv_det = pow(det, -1, 26)
        adjoint_matrix = np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])
        inverse = (inv_det * adjoint_matrix) % 26
        return inverse

    def decryptHill2x2(self, ciphertext, keyMatrix):
        if isinstance(keyMatrix, str):
            if keyMatrix.replace(' ', '').isdigit():
                # Split the string into a list of numbers
                numbers = list(map(int, keyMatrix.split()))
                # Arrange the numbers into a 2D numpy array
                keyMatrix = np.array(numbers).reshape(-1, 2)
            elif keyMatrix.isalpha():
                keyMatrix = self.key_matrix(keyMatrix)

        space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']
        ciphertext = ciphertext.replace(' ', '')
        inv_key = self.inverse_matrix(keyMatrix)
        ciphertext_values = [ord(char.lower()) - ord('a') for char in ciphertext]
        plaintext = ""
        for i in range(0, len(ciphertext_values), 2):
            block = np.array([[ciphertext_values[i]], [ciphertext_values[i + 1]]])
            decrypted_block = np.dot(inv_key, block) % 26
            for value, original_char in zip(decrypted_block, ciphertext[i:i + 2]):
                plaintext += self.numToChar(value[0], original_char.isupper())
        for index in space_indices:
            plaintext = plaintext[:index] + ' ' + plaintext[index:]
        return plaintext

    def add_content(self, frameName):
        # Ask the user to choose the file

        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")], title="Choose File")

        if file_path:
            # Open the selected file and read its content
            with open(file_path, "r") as file:
                file_content = file.read()

                # Insert the file content into the entry widget
                frameName.encryptTextBox.delete(0, "end")
                frameName.encryptTextBox.insert(0, file_content)

            messagebox.showinfo("File Loaded", "Content from the selected file has been loaded.")
        else:
            messagebox.showinfo("No File Selected", "No file selected. Operation cancelled.")

    def Substitutionencrypt(self, plaintext, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
        keyIndices = [alphabet.index(k.lower()) for k in plaintext]
        return ''.join(key[keyIndex] for keyIndex in keyIndices)

    def Substitutiondecrypt(self, cipher, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
        decryptedText = ''
        for char in cipher:
            if char.isupper():
                try:
                    keyIndex = key.upper().index(char)
                except ValueError:
                    messagebox.showerror("Error", "Invalid cipher. It contains characters not present in the key.")
                    return
                decryptedText += alphabet[keyIndex].upper()
            else:
                try:
                    keyIndex = key.lower().index(char)
                except ValueError:
                    messagebox.showerror("Error", "Invalid cipher. It contains characters not present in the key.")
                    return
                decryptedText += alphabet[keyIndex].lower()
        return decryptedText

    def Rot13Function(self):
        # Get the ciphertext and key from the input fields
        self.Rot13.keyTextBox.configure(state="readonly")
        self.Rot13.decryptTextBox.delete(0, "end")
        PlainText = self.Rot13.encryptTextBox.get()
        rVar = self.Rot13.radioVar.get()

        if rVar == 0:
            decryptedText = self.Rot13encrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", decryptedText)
        else:
            encryptedText = self.Rot13decrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", encryptedText)

    def SubstitutionFunction(self):
        # Get the ciphertext and key from the input fields
        self.Substitution.decryptTextBox.delete(0, "end")
        PlainText = self.Substitution.encryptTextBox.get()
        key = self.Substitution.keyTextBox.get()

        # Store the indices of spaces
        space_indices = [i for i, char in enumerate(PlainText) if char == ' ']

        # Remove spaces from the plaintext
        PlainText = PlainText.replace(' ', '')

        # Validate plaintext and key
        if not all(char.isalpha() for char in PlainText):
            messagebox.showerror("Error", "Invalid plaintext. Please ensure the plaintext is alphabetic.")
            return

        # Validate key
        if len(key) != 26 or len(set(key.lower())) != 26 or not all(char.isalpha() for char in key):
            messagebox.showerror("Error", "Invalid key. The key should be 26 distinct alphabetic characters.")
            return

        # Convert key to match case of plaintext
        if PlainText.isupper():
            key = key.upper()
        else:
            key = key.lower()

        rVar = self.Substitution.radioVar.get()

        if rVar == 0:
            decryptedText = self.Substitutionencrypt(PlainText, key)
        else:
            try:
                decryptedText = self.Substitutiondecrypt(PlainText, key)
            except ValueError:
                messagebox.showerror("Error", "Invalid ciphertext. It contains characters not present in the key.")
                return

        # Convert the corresponding letter in the decrypted text to uppercase if the letter in the original text is uppercase
        decryptedText = ''.join(
            [decryptedText[i].upper() if PlainText[i].isupper() else decryptedText[i] for i in range(len(PlainText))])

        # Insert the spaces back into the decrypted text
        for index in space_indices:
            decryptedText = decryptedText[:index] + ' ' + decryptedText[index:]

        self.Substitution.decryptTextBox.insert("end", decryptedText)

    def Rot13encrypt(self, Plaintext):
        translated = ''
        for char in Plaintext:
            if char.isalpha():
                if char.isupper():
                    translated += chr(((ord(char) - 65 + 13) % 26) + 65)
                elif char.islower():
                    translated += chr(((ord(char) - 97 + 13) % 26) + 97)
            else:
                translated += char
        return translated

    def Rot13decrypt(self, cipher_text):
        decrypted = ''
        for char in cipher_text:
            if char.isalpha():
                if char.isupper():
                    decrypted += chr(((ord(char) - 65 - 13) % 26) + 65)
                elif char.islower():
                    decrypted += chr(((ord(char) - 97 - 13) % 26) + 97)
            else:
                decrypted += char
        return decrypted

    def ceaserprocess_button_click(self):
        # Get the ciphertext and key from the input fields
        PTxt = self.ceaser.encryptTextBox.get()
        K = self.ceaser.keyTextBox.get()
        CTxt = self.ceaser.decryptTextBox.get()
        rVar = self.ceaser.radioVar.get()

        # Validate inputs

        # Perform decryption
        if rVar == 0:
            if not all(char.isalpha() or char.isspace() for char in PTxt) or not K.isdigit():
                messagebox.showerror("Error",
                                     "Invalid input. Please ensure the plaintext and ciphertext are alphabetic (spaces allowed) and the key is numeric.")
                return
            decryptedText = self.CeaserEncryption(PTxt, int(K))
            self.ceaser.decryptTextBox.insert("end", decryptedText)
        else:
            if not all(
                    char.isalpha() or char.isspace() for char in CTxt) or not K.isdigit():
                messagebox.showerror("Error",
                                     "Invalid input. Please ensure the plaintext and ciphertext are alphabetic (spaces allowed) and the key is numeric.")
                return
            encryptedText = self.CeaserDecryption(CTxt, int(K))
            self.ceaser.encryptTextBox.insert("end", encryptedText)

    def columnar_transposition_encrypt(self, msg, key):
        cipher = ""
        k_indx = 0

        # Add spaces after every key size - 1 characters
        msg = ' '.join(msg[i:i + int(key) - 1] for i in range(0, len(msg), int(key) - 1))

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))
        col = len(key)
        row = int(math.ceil(msg_len / col))
        fill_null = int((row * col) - msg_len)
        msg_lst.extend(' ' * fill_null)
        matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] for row in matrix])
            k_indx += 1

        return cipher

    def columnar_transposition_decrypt(self, cipher, key):
        k_indx = 0
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)
        col = len(key)
        row = int(math.ceil(msg_len / col))
        key_lst = sorted(list(key))
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            for j in range(row):
                if msg_indx < len(msg_lst) and curr_idx < len(dec_cipher[j]):
                    dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                    msg_indx += 1
            k_indx += 1

        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot handle repeating words.")

        null_count = msg.count(' ')

        if null_count > 0:
            msg = msg[: -null_count]

        # Remove the spaces added during encryption
        msg = msg.replace(' ', '')

        return msg

    def AffineFunction(self):  # function

        def ceaserprocess_button_click(self):
            # Get the ciphertext and key from the input fields
            PTxt = self.ceaser.encryptTextBox.get()
            K = self.ceaser.keyTextBox.get()
            CTxt = self.ceaser.decryptTextBox.get()
            rVar = self.ceaser.radioVar.get()
            # Perform decryption
            if rVar == 0:
                decryptedText = self.CeaserEncryption(PTxt, iznt(K))
                self.ceaser.decryptTextBox.insert("end", decryptedText)
            else:
                encryptedText = self.CeaserDecryption(CTxt, int(K))
                self.ceaser.encryptTextBox.insert("end", encryptedText)

    def AffineFunction(self):
        # Get the ciphertext and key from the input fields
        self.Affine.decryptTextBox.delete(0, "end")
        PTxt = self.Affine.encryptTextBox.get()
        k = self.Affine.keyTextBox.get()

        # Validate key
        if not re.match(r'^\d+,\d+$', k) or any(int(i) <= 0 for i in k.split(',')):
            messagebox.showerror("Error",
                                 "Invalid key. Please ensure the key is two numbers separated by a comma and both are greater than 0.")
            return

        k = [int(i) for i in k.split(',')]

        rVar = self.Affine.radioVar.get()

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return

            Text = self.encryptAffine(PTxt, k)
            self.Affine.decryptTextBox.insert("end", Text)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return

            Text = self.decryptAffine(PTxt, k)
            self.Affine.decryptTextBox.insert("end", Text)

    def TranspositionFunction(self):
        # Get the ciphertext and key from the input fields
        self.Transposition.decryptTextBox.delete(0, "end")
        PTxt = self.Transposition.encryptTextBox.get()
        k = self.Transposition.keyTextBox.get()

        # Validate key
        if not k.isdigit() or len(k) <= 1 or len(set(k)) != len(k) or any(int(i) < 1 for i in k):
            messagebox.showerror("Error",
                                 "Invalid key. Please ensure the key is a string of numbers with length greater than 1, each digit is greater than or equal to 1, and all digits are distinct.")
            return

        rVar = self.Transposition.radioVar.get()

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return

            Text = self.columnar_transposition_encrypt(PTxt, k)
            self.Transposition.decryptTextBox.insert("end", Text)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PTxt):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return

            Text = self.columnar_transposition_decrypt(PTxt, k)
            self.Transposition.decryptTextBox.insert("end", Text)

        # # Perform decryption
        # if rVar == 0:
        #     Text = self.encryptAffine(PTxt,k)
        #     self.Affine.decryptTextBox.insert("end", Text)
        # else:
        #     Text = self.decryptAffine(PTxt, k)
        #     self.Affine.decryptTextBox.insert("end", Text)

    def inverse(self, b):
        # T = T1 - (T2 * Q)
        # Q , A, B, r, T1, T2, T
        t1, t2 = 0, 1
        ans = 0
        a = 26
        while b != 0:
            q = int(a / b);
            r = a % b;
            t = t1 - (t2 * q)
            if r == 0:
                ans = t2
                break
            a, b = b, r
            t1, t2 = t2, t

        if ans < 0:
            return ans + 26
        else:
            return ans

    def decryptAffine(self, cipher, key):
        inv = self.inverse(key[0])
        decryptedText = ''
        for i in range(len(cipher)):
            if cipher[i] >= 'A' and cipher[i] <= 'Z':
                decryptedText += chr(((inv * ((ord(cipher[i]) - ord('A')) - key[1])) % 26) + ord('A'))
            elif cipher[i] >= 'a' and cipher[i] <= 'z':
                decryptedText += chr(((inv * ((ord(cipher[i]) - ord('a')) - key[1])) % 26) + ord('a'))
            else:
                decryptedText += ' '
        return decryptedText

    def encryptAffine(self, text, key):
        # c = (ax + b) mod 26
        encryptedText = ""
        for i in range(len(text)):
            if text[i] >= 'A' and text[i] <= 'Z':
                encryptedText += chr((((key[0] * (ord(text[i]) - ord('A'))) + key[1]) % 26) + ord('A'))
            elif text[i] >= 'a' and text[i] <= 'z':
                encryptedText += chr((((key[0] * (ord(text[i]) - ord('a'))) + key[1]) % 26) + ord('a'))
            else:
                encryptedText += ' '
        return encryptedText

    def bind_update_process_button_text(self, frame):
        frame.radioVar.trace("w", lambda *args, f=frame: self.update_process_button_text(f))

    def CeaserEncryption(self, plaintext, n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) + n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) + n - 97) % 26 + 97)
        self.ceaser.decryptTextBox.delete(0, "end")
        return ans

    def CeaserDecryption(self, plaintext, n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) - n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) - n - 97) % 26 + 97)
        self.ceaser.encryptTextBox.delete(0, "end")
        return ans

    # ==========================================================>
    def generateKeyMatrix(self, key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        keyMatrix = [[None] * 5 for _ in range(5)]
        keySet = set()
        for char in key + alphabet:
            if char not in keySet:
                row, col = divmod(len(keySet), 5)
                keyMatrix[row][col] = char
                keySet.add(char)
        return keyMatrix

    def prepareMessage(self, message):
        message = message.upper().replace(" ", "")
        preparedMessage = ""
        i = 0
        while i < len(message):
            if i == len(message) - 1:
                preparedMessage += message[i] + "X"
            elif message[i] == message[i + 1]:
                preparedMessage += message[i] + "X"
                i -= 1
            else:
                preparedMessage += message[i:i + 2]
            i += 2

        return preparedMessage

    def encryptMessage(self, keyMatrix, message):
        encryptedMessage = ""

        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)
            if rowA == rowB:
                encryptedMessage += keyMatrix[rowA][(colA + 1) % 5] + keyMatrix[rowB][(colB + 1) % 5]
            elif colA == colB:
                encryptedMessage += keyMatrix[(rowA + 1) % 5][colA] + keyMatrix[(rowB + 1) % 5][colB]
            else:
                encryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return encryptedMessage

    def findPosition(self, keyMatrix, char):
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j] == char:
                    return i, j

    def decryptMessage(self, keyMatrix, message):
        decryptedMessage = ""
        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)

            if rowA == rowB:
                decryptedMessage += keyMatrix[rowA][(colA - 1) % 5] + keyMatrix[rowB][(colB - 1) % 5]
            elif colA == colB:
                decryptedMessage += keyMatrix[(rowA - 1) % 5][colA] + keyMatrix[(rowB - 1) % 5][colB]
            else:
                decryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return decryptedMessage

    def playFairFunction(self):
        msg = self.playFair.encryptTextBox.get()
        ky = self.playFair.keyTextBox.get()
        rVar = self.playFair.radioVar.get()

        # Replace 'j' with 'i'
        msg = msg.replace("j", "i")
        cipher = msg  # Assign msg to cipher before replacing 'j' with 'i'
        cipher = cipher.replace("j", "i")
        ky = ky.replace("j", "i")

        # Perform operation
        if rVar == 0:
            if not msg.isalpha() or not ky.isalpha():
                messagebox.showerror("Error", "Invalid input or key. Please ensure the key and message are alphabetic.")
                return
            key = ky.upper().replace(" ", "")
            keyMatrix = self.generateKeyMatrix(key)

            # Prepare message
            msg = self.prepareMessage(msg)
            result = self.encryptMessage(keyMatrix, msg)

            # Convert result to the case of the original message
            result = result.upper() if msg.isupper() else result.lower()

            self.playFair.decryptTextBox.delete(0, tkinter.END)
            self.playFair.decryptTextBox.insert("end", result)
        elif rVar == 1:
            if not cipher.isalpha() or not ky.isalpha():
                messagebox.showerror("Error",
                                     "Invalid input or key. Please ensure the key and cipher text are alphabetic.")
                return
            key = ky.upper().replace(" ", "")
            keyMatrix = self.generateKeyMatrix(key)

            # Prepare message
            msg = self.prepareMessage(msg)
            result = self.decryptMessage(keyMatrix, cipher)

            # Convert result to the case of the original cipher
            result = result.upper() if cipher.isupper() else result.lower()

            self.playFair.encryptTextBox.delete(0, tkinter.END)
            self.playFair.encryptTextBox.insert("end", result)

        # return result

    # ==============================================================>
    def update_process_button_text(self, frame):
        # Get the value of the variable to determine which radio button is selected
        selected_value = frame.radioVar.get()

        if selected_value == 0:  # Encryption
            frame.processButton.configure(text="Encrypt")


        else:  # Decryption
            frame.processButton.configure(text="Decrypt")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # ________________________________________

    def RailFenceButtonClicked(self):
        # Get the ciphertext and key from the input fields
        self.RailFence.decryptTextBox.delete(0, "end")
        PlainText = self.RailFence.encryptTextBox.get()
        Key = self.RailFence.keyTextBox.get()
        rVar = self.RailFence.radioVar.get()

        # Validate key
        if not Key.isdigit() or int(Key) <= 1:
            messagebox.showerror("Error", "Invalid key. Please ensure the key is a positive number greater than 1.")
            return

        # Perform decryption
        if rVar == 0:
            # Validate plaintext
            if not all(char.isalpha() or char.isspace() for char in PlainText):
                messagebox.showerror("Error",
                                     "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
                return
            if int(Key) >= len(PlainText):
                decryptedText = PlainText
            else:
                decryptedText = self.rail_fence_encrypt(PlainText, int(Key))
            self.RailFence.decryptTextBox.insert("end", decryptedText)
        else:
            # Validate ciphertext
            if not all(char.isalpha() or char.isspace() for char in PlainText):
                messagebox.showerror("Error",
                                     "Invalid ciphertext. Please ensure the ciphertext is alphabetic (spaces allowed).")
                return
            if int(Key) >= len(PlainText):
                encryptedText = PlainText
            else:
                encryptedText = self.rail_fence_decrypt(PlainText, int(Key))
            # encryptedText = self.rail_fence_decrypt(PlainText, int(Key))
            self.RailFence.decryptTextBox.insert("end", encryptedText)

    def rail_fence_encrypt(self, plaintext, rails):
        rails = int(rails)
        fence = [[] for _ in range(rails)]  # Create a list of empty lists to represent the fence
        rail = 0
        direction = 1  # Direction of movement along the rails (down or up)
        space_indices = [i for i, char in enumerate(plaintext) if char == ' ']  # Store the indices of spaces

        # Fill the fence with characters from the plaintext
        for char in plaintext:
            if char == ' ':
                continue
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1  # Change direction when reaching the top or bottom rail

        # Flatten the fence and concatenate the characters
        encrypted_text = ''.join(char for rail in fence for char in rail)

        # Add the spaces back into the encrypted text
        for index in space_indices:
            encrypted_text = encrypted_text[:index] + ' ' + encrypted_text[index:]

        return encrypted_text

    def rail_fence_decrypt(self, ciphertext, rails):
        rails = int(rails)
        fence = [['' for _ in ciphertext] for _ in range(rails)]  # Create an empty fence matrix
        rail = 0
        direction = 1
        space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']  # Store the indices of spaces

        # Remove spaces from ciphertext
        ciphertext = ciphertext.replace(' ', '')

        # Fill the fence matrix with placeholders for characters
        for i in range(len(ciphertext)):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Fill the fence matrix with ciphertext characters
        index = 0
        for i in range(rails):
            for j in range(len(ciphertext)):
                if fence[i][j] == '*':
                    fence[i][j] = ciphertext[index]
                    index += 1

        # Read the characters from the fence matrix to retrieve the plaintext
        rail = 0
        direction = 1
        decrypted_text = ''
        for i in range(len(ciphertext)):
            decrypted_text += fence[rail][i]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Add the spaces back into the decrypted text
        for index in space_indices:
            decrypted_text = decrypted_text[:index] + ' ' + decrypted_text[index:]

        return decrypted_text

    # ---------------------------------------------
    def Rot13Function(self):
        # Set the key to a static number
        self.Rot13.keyTextBox.delete(0, "end")
        self.Rot13.keyTextBox.insert("end", "13")
        self.Rot13.keyTextBox.configure(state="readonly")

        self.Rot13.decryptTextBox.delete(0, "end")
        PlainText = self.Rot13.encryptTextBox.get()
        rVar = self.Rot13.radioVar.get()

        if not all(char.isalpha() or char.isspace() for char in PlainText):
            messagebox.showerror("Error",
                                 "Invalid plaintext. Please ensure the plaintext is alphabetic (spaces allowed).")
            return
        # Divide the function based on the value of rVar
        if rVar == 0:
            decryptedText = self.Rot13encrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", decryptedText)
        else:
            encryptedText = self.Rot13decrypt(PlainText)
            self.Rot13.decryptTextBox.insert("end", encryptedText)

    def select_frame_by_name(self, name):
        # set button color for selected button

        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "ceaser" else "transparent")
        self.secondButton.configure(fg_color=("gray75", "gray25") if name == "playFair" else "transparent")

        self.fourthButton.configure(fg_color=("gray75", "gray25") if name == "Affine" else "transparent")
        self.fifthButton.configure(fg_color=("gray75", "gray25") if name == "Transposition" else "transparent")
        self.RailFenceButton.configure(fg_color=("gray75", "gray25") if name == "RailFence" else "transparent")

        self.Rot13Button.configure(fg_color=("gray75", "gray25") if name == "Rot13" else "transparent")
        self.HillcipherButton.configure(fg_color=("gray75", "gray25") if name == "Hillcipher" else "transparent")
        self.eightButton.configure(fg_color=("gray75", "gray25") if name == "Substitution" else "transparent")
        self.VigenereButton.configure(fg_color=("gray75", "gray25") if name == "Vigenere" else "transparent")

        # show selected frame
        if name == "ceaser":
            self.ceaser.grid(row=0, column=1, sticky="nsew")
        else:
            self.ceaser.grid_forget()

        if name == "playFair":
            self.playFair.grid(row=0, column=1, sticky="nsew")
        else:
            self.playFair.grid_forget()

        if name == "RailFence":
            self.RailFence.grid(row=0, column=1, sticky="nsew")
        else:
            self.RailFence.grid_forget()

        if name == "Affine":
            self.Affine.grid(row=0, column=1, sticky="nsew")
        else:
            self.Affine.grid_forget()

        if name == "Transposition":
            self.Transposition.grid(row=0, column=1, sticky="nsew")
        else:
            self.Transposition.grid_forget()

        if name == "Rot13":
            self.Rot13.grid(row=0, column=1, sticky="nsew")
        else:
            self.Rot13.grid_forget()

        if name == "Hillcipher":
            self.Hillcipher.grid(row=0, column=1, sticky="nsew")
        else:
            self.Hillcipher.grid_forget()

        if name == "Substitution":
            self.Substitution.grid(row=0, column=1, sticky="nsew")
        else:
            self.Substitution.grid_forget()
        if name == "Vigenere":
            self.Vigenere.grid(row=0, column=1, sticky="nsew")
        else:
            self.Vigenere.grid_forget()
        if name == "tenthFrame":
            self.tenthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.tenthFrame.grid_forget()

        if name == "eleventhFrame":
            self.eleventhFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eleventhFrame.grid_forget()
        if name == "twelvethFrame":
            self.twelvethFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.twelvethFrame.grid_forget()

    # -----------------------------------------
    def ceaser_button_event(self):
        self.select_frame_by_name("ceaser")

    def playFair_button_event(self):
        self.select_frame_by_name("playFair")

    def RailFence_button_event(self):
        self.select_frame_by_name("RailFence")

    def Affine_button_event(self):
        self.select_frame_by_name("Affine")

    def Transposition_button_event(self):
        self.select_frame_by_name("Transposition")

    def Rot13_button_event(self):
        self.select_frame_by_name("Rot13")

    def Hillcipher_button_event(self):
        self.select_frame_by_name("Hillcipher")

    def Substitution_button_event(self):
        self.select_frame_by_name("Substitution")

    def Vigenere_button_event(self):
        self.select_frame_by_name("Vigenere")

    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")

    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")

    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def Hillcipher_button_event(self):
        self.select_frame_by_name("Hillcipher")

    def Substitution_button_event(self):
        self.select_frame_by_name("Substitution")

    def Vigenere_button_event(self):
        self.select_frame_by_name("Vigenere")

    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")

    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")

    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def ClearFields(self, frame):
        # Access attributes from frame_name object
        frame.decryptTextBox.delete(0, "end")
        frame.keyTextBox.delete(0, "end")
        frame.encryptTextBox.delete(0, "end")

    def create_gui_elements(self, frame_name, frame_label):
        frame_name.grid_columnconfigure(0, weight=1)
        frame_name.grid_rowconfigure(7, weight=1)

        Font = ("Georgia", 40, "bold")  # Assuming Font is defined somewhere
        rFont = ("Calibri", 20)
        Frame_label = customtkinter.CTkLabel(frame_name, text=frame_label, font=Font)
        Frame_label.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

        radio_var = customtkinter.IntVar(value=0)
        encryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=0,
                                                       text="Encryption", font=rFont)
        encryptionRadio.grid(row=1, column=0, pady=0, padx=0, sticky="s")
        decryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=1,
                                                       text="Decryption", font=rFont)
        decryptionRadio.grid(row=1, column=1, pady=0, padx=100, sticky="w")

        encryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Plain text", height=50, width=0,
                                                font=rFont)
        encryptTextBox.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        decryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Cipher text", height=50, width=0,
                                                font=rFont)
        decryptTextBox.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        keyTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Key", height=50, width=250, font=rFont)
        keyTextBox.grid(row=3, column=0, padx=(20, 20), pady=0, sticky="ns", columnspan=2)

        processButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,
                                                text="Encrypt",
                                                font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), anchor="ns")
        processButton.grid(row=4, column=0, sticky="s", pady=5, columnspan=2)
        clearButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,
                                              text="Clear",
                                              font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"), anchor="ns",
                                              command=lambda: self.ClearFields(frame_name))
        clearButton.grid(row=4, column=1, sticky="s", pady=5, padx=5, columnspan=2)

        selectFileButton = customtkinter.CTkButton(frame_name, text="Select File", width=300, height=40
                                                   )
        selectFileButton.grid(row=5, column=0, sticky="s", pady=5, columnspan=2)

        downloadFileButton = customtkinter.CTkButton(frame_name, text="Download File", width=300, height=40)
        downloadFileButton.grid(row=6, column=0, sticky="s", pady=5, columnspan=2)

        frame_name.encryptTextBox = encryptTextBox
        frame_name.Frame_label = Frame_label
        frame_name.encryptionRadio = encryptionRadio
        frame_name.decryptionRadio = decryptionRadio
        frame_name.decryptTextBox = decryptTextBox
        frame_name.keyTextBox = keyTextBox
        frame_name.processButton = processButton
        frame_name.selectFileButton = selectFileButton
        frame_name.downloadButton = downloadFileButton
        frame_name.radioVar = radio_var


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # Your additional code goes here


def main():
    app = App()
    app.mainloop()
v