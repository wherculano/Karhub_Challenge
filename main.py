import pandas as pd

# 0 = maker, 1 = model, 2 = year, 3 = version
# data_a = pd.read_excel("a_list_maker_model_standard_meli.xlsx", header=None)
# df_a = pd.DataFrame(data_a)


data_b = pd.read_excel("b_list_cp_application_complete.xlsx", usecols=["pasted"])
df_b = pd.DataFrame(data_b).sort_values(by=['pasted']).reset_index(drop=True).dropna()

new_df = {"MAKER": [], "MODEL": [], "YEAR": [], "TYPE": []}

for i in df_b['pasted']:
    info = i.split("$")
    for data in info:
        if len(data.strip().split()) > 2:
            YEAR_index = data.find('@#')
            YEAR = data[YEAR_index-4: YEAR_index]
            _TYPE = ''.join(data[YEAR_index+2:].split("@#"))
            MAKER = data.split(YEAR)[0].split()[0]
            MODEL = ''.join(data.split(YEAR)[0].split()[1:])
            if not YEAR.isnumeric():
                continue
            new_df['MAKER'].append(MAKER)
            new_df["MODEL"].append(MODEL)
            new_df["YEAR"].append(YEAR)
            new_df["TYPE"].append(_TYPE)
print("::: FIM :::")
pd.DataFrame(new_df).to_csv("karhub_challenge.xlsx", index=False)