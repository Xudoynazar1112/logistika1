from datetime import datetime, timedelta

import requests
import sqlite3
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from .forms import OrderForm, fields_name


def export_data_to_excel():
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')

    # Write a SQL query to fetch the data
    query = "SELECT * FROM logistika_web_order"

    # Execute the query and load the data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Define the file path for the Excel file
    file_path = 'media/report/data_export.xlsx'

    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

    print(f"Data successfully exported to {file_path}")


def send_telegram_message(text):
    # Call the function to export data to Excel
    export_data_to_excel()
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text, 'parse_mode': 'HTML'}
    response = requests.post(url, data=data)
    # print(response)
    return response


def send_report():
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    scheduled_date = datetime(2024, 8, 19)
    response = None
    print(scheduled_date)
    if scheduled_date.date() == datetime.now().date():
        url = f"https://api.telegram.org/bot{token}/sendDocument"
        file_path = 'media/report/data_export.xlsx'
        with open(file_path, 'rb') as file:
            files = {'document': file}
            data = {'chat_id': chat_id}
            response = requests.post(url, data=data, files=files)
            print("everything is ok")
    elif scheduled_date.date() >= datetime.now().date():
        pass
    elif scheduled_date.date() <= datetime.now().date():
        scheduled_date += timedelta(days=7)
        print(scheduled_date)
    return response


send_report()


def order(request):
    if request.method == 'POST':
        # print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form_data = form.save()
            msg_to_bot = f"New order:\n "
            for field, label in fields_name.items():
                value = getattr(form_data, field, None)
                if value:
                    msg_to_bot += f"<b>{label}</b>: <em>{value}</em>\n"
            send_telegram_message(msg_to_bot)
            return render(request, 'success.html', )
        else:
            print(form.errors)
    else:
        form = OrderForm()
    return render(request, 'form.html', {'form': form})

