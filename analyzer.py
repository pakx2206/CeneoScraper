import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*list(map(lambda x: x.split(".")[0], os.listdir("./opinions"))), sep="\n")


product_code = input("Podaj kod produktu: ")
opinions = pd.read_json(f"./opinions/{product_code}.json")
print(opinions)
opinions.score= opinions.score.map(lambda x: x.split("/")[0].replace(",",".")).astype(float)

stats = {   
    "opinions_count": len(opinions.index),
    "pros_count": opinions.pros.astype(bool).sum(),
    "cons_count": opinions.cons.astype(bool).sum(),
    "average_score": opinions.score.mean()
}
print(f'''Dla produktu o kodzie {product_code} pobranych zostało {stats["opinions_count"]} opinii. 
Dla {stats["pros_count"]} opinii podana została lista zalet produktu, a dla {stats["cons_count"]}
opinii lsita jego wad. Średnia ocena produktu wynosi {stats["average_score"]:.2f}.''')

if not os.path.exists("./plots/"):
    os.mkdir("./plots/")

score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
print(score)
score.plot.bar()
plt.savefig(f"./plots/{product_code}_score.png")
plt.close()
