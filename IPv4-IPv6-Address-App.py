import tkinter as tk
import requests
from tkinter import messagebox


def get_ip_info():
    try:
        
        api_url = 'https://ipinfo.io/120.28.70.150/json/' 
        response = requests.get(api_url)
        ip_info = response.json()

       
        ipv4_address = ip_info.get('ip', 'N/A')
        city = ip_info.get('city', 'N/A')
        region = ip_info.get('region', 'N/A')
        country = ip_info.get('country', 'N/A')
        isp = ip_info.get('org', 'N/A')

        
        result_text = f"IPv4 Address: {ipv4_address}\nCity: {city}\nRegion: {region}\nCountry: {country}\nISP: {isp}"
        result_label.config(text=result_text)

    except requests.exceptions.RequestException as e:
       
        messagebox.showerror("Error", f"Failed to retrieve IP information: {e}")


root = tk.Tk()
root.title("IP Address Info")


info_label = tk.Label(root, text="Click the button to get your IP Address information", font=("Arial", 12))
info_label.pack(pady=10)

get_ip_button = tk.Button(root, text="Get IP Info", command=get_ip_info, font=("Arial", 12), bg='lightblue')
get_ip_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)


root.geometry("400x300")
root.mainloop()
