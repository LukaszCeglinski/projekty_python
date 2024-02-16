import tkinter as tk
import math

def oblicz_odchylenie_standardowe(dane):
  """
  Funkcja oblicza odchylenie standardowe z listy danych.

  Argumenty:
    dane: Lista liczb.

  Zwraca:
    Odchylenie standardowe.
  """
  średnia = sum(dane) / len(dane)
  wariancja = sum([(x - średnia)**2 for x in dane]) / len(dane)
  odchylenie_standardowe = math.sqrt(wariancja)
  return odchylenie_standardowe

def main():
  """
  Funkcja główna programu.
  """
  # Utworzenie okna tkinter.
  okno = tk.Tk()
  okno.geometry("400x200")
  okno.title("Odchylenie standardowe")

  # Utworzenie etykiety dla wprowadzenia danych.
  etykieta_dane = tk.Label(text="Wprowadź dane (oddzielone przecinkami):")
  etykieta_dane.pack()

  # Utworzenie pola tekstowego dla wprowadzenia danych.
  pole_tekstowe_dane = tk.Entry()
  pole_tekstowe_dane.pack()

  # Utworzenie przycisku do obliczania odchylenia standardowego.
  przycisk_oblicz = tk.Button(text="Oblicz", command=lambda: oblicz())
  przycisk_oblicz.pack()

  # Utworzenie etykiety do wyświetlania wyniku.
  etykieta_wynik = tk.Label(text="Odchylenie standardowe:")
  etykieta_wynik.pack()

  # Funkcja obliczająca i wyświetlająca wynik.
  def oblicz():
    dane = [float(x) for x in pole_tekstowe_dane.get().split(",")]
    odchylenie_standardowe = oblicz_odchylenie_standardowe(dane)
    etykieta_wynik.config(text=f"Odchylenie standardowe: {odchylenie_standardowe}")

  # Uruchamianie pętli głównej tkinter.
  okno.mainloop()

if __name__ == "__main__":
  main()