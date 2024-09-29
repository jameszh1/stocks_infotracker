#converting to html file
import yfinance as yf
import webbrowser
import os

choice = input("Enter the stock which you want to know the current price of: ").upper()
stock = yf.Ticker(choice)
data = stock.history(period="1d")

html_file = data.to_html()
filename = f"{choice}_info.html"
with open(filename, "w") as file:
    file.write(
    f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>{choice} Stock Information</title>
    </head>
    """
    )
    file.write(f"<h1>{choice} Stock Information</h1>")
    file.write(html_file)

webbrowser.open(f"file://{os.path.realpath(filename)}")
print(f"A detailed report for stock {choice} has been created")
print(f"The current price of {choice} is ${data['Close'].iloc[0]}")
time.sleep(1)
os.remove(filename)

