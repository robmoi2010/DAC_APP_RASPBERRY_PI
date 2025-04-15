import tkinter as tk
import DAC_VOLUME as volume

background = "lightblue"
main = tk.Tk()
main.title("ESS DAC")
main.geometry("300x300")

# home frame
home = tk.Frame(main, bg=background, padx=10, pady=10)
home.pack(padx=20, pady=20, fill="both", expand=True)
tk.Label(home, text="home").grid(row=0, column=0, sticky="w")

# dac filters frame
filters = tk.Frame(main, bg=background, padx=10, pady=10)
filters.pack(padx=20, pady=20, fill="both", expand=True)
tk.Label(filters, text="home").grid(row=0, column=0, sticky="w")
main.mainloop()


if __name__ == "__main__":
    main()
