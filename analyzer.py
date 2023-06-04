import os
import pandas as pd
print(*list(map(lambda x: x.split(".")[0], os.listdir("./opinions"))), sep="\n")


product_code = input("Podaj kod produktu: ")
opinions = pd.read_json(f"./opinions/{product_code}.json")
print(opinions)
opinions.score= opinions.score.map(lambda x: x.split("/")[0].replace(",",".")).astype(float)

stats = {   
    "opinions_count": len(opinions.index),
    "pros_count": opinions.pros.astype(bool).sum(),
    "cons_count": opinions.cons.astype(bool).sum(),
    "average": opinions.score.mean()
}
print(f'''Dla produktu o kodzie {product_code} pobranych zostało {stats["opinions_count"]} opinii. 
Dla {stats["pros_count"]} opinii podana została lista zalet produktu, a dla {stats["cons_count"]}
opinii lsita jego wad. Średnia ocena produktu wynosi {stats["average_score"]:.2f}.''')
