
import pandas as pd

df = pd.DataFrame(data, columns=columns)
df.to_csv("out.csv", index=False)

