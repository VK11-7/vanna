import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from google.colab import auth
from google.auth import default
import gspread

# Authenticate user
auth.authenticate_user()

# Get credentials
creds, _ = default()

# Authorize gspread
gc = gspread.authorize(creds)

# Open the spreadsheet
worksheet = gc.open('Dainika almanac').sheet1

# Get all values from the worksheet
rows = worksheet.get_all_values()

# Create a DataFrame
df = pd.DataFrame.from_records(rows)

# Get today's date
today = datetime.today()

# Get tomorrow's date
tomorrow = today + timedelta(1)
date1 = tomorrow.strftime("%d/%m/%Y")

# Filter the DataFrame for tomorrow's date
res = df.loc[df[0] == date1]

# Streamlit app
st.title("Simply Ayurveda - Dainika Vaidya Almanac")

# Display the data
if not res.empty:
    Date = res[0].values[0]
    Weekday = res[1].values[0]
    Sunrise = res[2].values[0]
    Sunset = res[3].values[0]
    Moonrise = res[4].values[0]
    Moonset = res[5].values[0]
    Samvatsara = res[6].values[0]
    Ayana = res[7].values[0]
    Rtu = res[8].values[0]
    Masa = res[9].values[0]
    Kollamera = res[10].values[0]
    Paksha = res[11].values[0]
    Tithi = res[12].values[0]
    Vasara = res[13].values[0]
    Nakshatra = res[14].values[0]
    Sunsign = res[15].values[0]
    Moonsign = res[16].values[0]
    Brahmamuhurta = res[17].values[0]
    Pratahsandhya = res[18].values[0]
    Abhijitmuhurta = res[19].values[0]
    Saayamsandhya = res[20].values[0]
    Rahukalam = res[21].values[0]
    Yamaganda = res[22].values[0]
    Gulikaikaalam = res[23].values[0]
    Significance = res[24].values[0]
    Sudhakalainwomen = res[25].values[0]
    Sudhakalainmen = res[26].values[0]
    Vishakalainwomen = res[27].values[0]
    Vishakalainmen = res[28].values[0]
    Chakrabasedonvasara = res[29].values[0]
    Bodypartbasedonnakshatra = res[30].values[0]

    # Display the information
    st.markdown(f"## Suprabhatam")
    st.markdown(f"{Date} - {Weekday}")
    st.markdown(f"Sunrise: {Sunrise} am")
    st.markdown(f"Sunset: {Sunset} pm")
    st.markdown(f"Moonrise: {Moonrise} pm")
    st.markdown(f"Moonset: {Moonset} am")

    st.markdown(f"Samvatsara: {Samvatsara}")
    st.markdown(f"Ayana: {Ayana}")
    st.markdown(f"Rtu: {Rtu}")
    st.markdown(f"Masa: {Masa}")
    st.markdown(f"Kollamera: {Kollamera}")
    st.markdown(f"Paksha: {Paksha}")
    st.markdown(f"Tithi: {Tithi}")
    st.markdown(f"Vasara: {Vasara}")
    st.markdown(f"Nakshatra: {Nakshatra}")
    st.markdown(f"Sunsign: {Sunsign}")
    st.markdown(f"Moonsign: {Moonsign}")

    st.markdown(f"## Auspicious Hours")
    st.markdown(f"Brahma Muhurta: {Brahmamuhurta}")
    st.markdown(f"Pratah Sandhya: {Pratahsandhya}")
    st.markdown(f"Abhijit Muhurta: {Abhijitmuhurta}")
    st.markdown(f"Saayam Sandhya: {Saayamsandhya}")

    st.markdown(f"## Hours to Be Careful Around")
    st.markdown(f"Rahu Kalam: {Rahukalam}")
    st.markdown(f"Yama Gandha: {Yamaganda}")
    st.markdown(f"Gulikai Kaalam: {Gulikaikaalam}")

    st.markdown(f"## Significance")
    st.markdown(Significance)

    st.markdown(f"## Medicoastrological Significance")
    st.markdown(f"Sudhakala in Women: {Sudhakalainwomen}")
    st.markdown(f"Sudhakala in Men: {Sudhakalainmen}")
    st.markdown(f"Vishakala in Women: {Vishakalainwomen}")
    st.markdown(f"Vishakala in Men: {Vishakalainmen}")
    st.markdown(f"Chakra Based on Vasara: {Chakrabasedonvasara}")

    st.markdown(f"## Body of Kala Purusha According to Nakshatra")
    st.markdown(Bodypartbasedonnakshatra)

    st.markdown(
        f"Have we missed anything important? Message Simply Ayurveda on WhatsApp. [WhatsApp](https://wa.me/message/DTX6RK5L6HE3B1)"
    )
    st.markdown(
        f"Subscribe to our YouTube channel - [Simply Ayurveda](https://youtube.com/c/SimplyAyurveda)"
    )
else:
    st.warning("No data found for tomorrow's date.")
