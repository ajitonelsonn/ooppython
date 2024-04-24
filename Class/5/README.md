# KOKO TKINTER
```python
# Importa biblioteka tkinter nian (Import the tkinter library)
import tkinter

# Kria janela principal (Create the main window)
main_window = tkinter.Tk()

# Kria label1 ho textu "label1" no tau iha janela principal (Create label1 with text "label1" and place it in the main window)
label1=tkinter.Label(main_window, text="label1")

# Kria label2 ho textu "label2" no tau iha janela principal (Create label2 with text "label2" and place it in the main window)
label2=tkinter.Label(main_window, text="label2")

# Kria butaun1 ho textu "Butaun1" no tau iha janela principal (Create button1 with text "Butaun1" and place it in the main window)
butaun1=tkinter.Button(main_window, text="Butaun1")

# Kria butaun2 ho textu "Butaun2" no tau iha janela principal (Create button2 with text "Butaun2" and place it in the main window)
butaun2=tkinter.Button(main_window, text="Butaun2")

# Methodo hodi tau label1 iha janela principal (Method to place label1 in the main window)
label1.pack()

# Methodo hodi tau label2 iha janela principal (Method to place label2 in the main window)
label2.pack()

# Methodo hodi tau butaun1 iha janela principal (Method to place button1 in the main window)
butaun1.pack()

# Methodo hodi tau butaun2 iha janela principal (Method to place button2 in the main window)
butaun2.pack()

# Methodo hodi hamosu no korre GUI (Method to create and run the GUI)
main_window.mainloop()
```
