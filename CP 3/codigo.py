from pathlib import Path
import  json
import csv

texto = Path("leads.json").read_text(encoding="utf-8")
leads = json.loads(texto)

unicos = {}
for lead in leads:
    chave = lead["email"].lower()
    unicos[chave] = lead

with open("export.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "stage"])
    w.writeheader()
    for lead in unicos.values():
        w.writerow({"name": lead["name"], "stage": lead["stage"]})

linhas = Path("export.csv").read_text(encoding="utf-8").splitlines()
print(len(linhas), linhas[1])