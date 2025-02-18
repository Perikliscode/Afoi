from openai import OpenAI

client = OpenAI(api_key="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")

def prognosis(age,alcohol,diet,phys_act,smoking,gender,lastAppoint):
    promt="  What is the percentage of having cancer based on these life factors age:50,alcohol:everyday,diet:bad. What can i do to lower the chances(advice).Also give a random fact that increases cancer chacne and people often neglet"

    with open("BackEnd/AppointmentDoc.txt", "r") as file:
        file_contentAppoint = file.read()
    with open("BackEnd/data.txt", "w+") as file:
        file.write("User Cancer risk factors:\n")
        file.write("age="+str(age)+"\n")
        file.write("alcohol="+alcohol+" (none,little,regularly,everyday)\n")
        file.write("diet="+diet+" (excelent,okay,bad,very bad)\n")
        file.write("phys_act="+phys_act+" (everyday,regularly,little,none)\n")
        file.write("smoking="+smoking+" (none,little,regularly,everyday)\n")
        file.write("gender="+gender+"\n")
        file.write("Last appointment:"+str(lastAppoint))
        file.seek(0)
        file_contentData = file.read()

    promt=f"""
    You are a health assistant that helps users of an app and calculates an approximation on risk of cancer based on their given factors
    at the end  tell them an approximation of concerning using words
    tell them that they sould visit a doctor soon and the type of doctor they need.
    What can i do to lower the chances(advice).
    Based on the last appointment suggest an exact date when should the next one be.
    Also give a fact that increases cancer chance and people often neglet.
    Now, based on the folloing information given, please answer (Do not repeat the information the user gave)
    {file_contentData}
    {file_contentAppoint}
    In bullet points and multiline
    """

    response = client.chat.completions.create(messages=[{"role":"user","content":promt}],model="gpt-4o-mini",temperature=0.0,max_tokens=1000)

    response = response.choices[0].message.content

    return response