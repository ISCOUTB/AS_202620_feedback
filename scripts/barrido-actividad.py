"""Barrido de actividad de los repositorios de los equipos, por protocolo git (sin API).

Uso:
    python scripts/barrido-actividad.py --cierre "2026-08-31T05:00:00Z" --desde "2026-08-24T05:00:00Z"

Por cada repositorio de EQUIPOS.md imprime el último commit anterior al cierre y los commits
nuevos desde el cierre anterior (con clon efímero que se borra al terminar), y guarda el volcado
en revisiones/<periodo>/_meta/actividad.txt (gitignored).
"""
import argparse
import io
import os
import re
import shutil
import subprocess
import tempfile

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def repos_de_equipos():
    s = io.open(os.path.join(KIT, "EQUIPOS.md"), encoding="utf-8").read()
    return sorted(set(re.findall(r"`(AS_202620_[A-Za-z0-9_-]+)`", s.split("## Estado")[0])))


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cierre", required=True, help="ISO del cierre de la semana en curso (UTC)")
    ap.add_argument("--desde", required=True, help="ISO del cierre de la semana anterior (UTC)")
    args = ap.parse_args()

    out = []
    for repo in repos_de_equipos():
        d = tempfile.mkdtemp()
        p = run(["git", "clone", "--filter=blob:none", "--no-checkout", "-q",
                 f"https://github.com/ISCOUTB/{repo}.git", d])
        if p.returncode != 0:
            line = f"{repo}\tNO VISIBLE O CLONE FALLIDO"
            print(line)
            out.append(line)
            shutil.rmtree(d, ignore_errors=True)
            continue
        last = run(["git", "-C", d, "log", "-1", "--format=%h %cI %s",
                    f"--until={args.cierre}"]).stdout.strip() or "(sin commits <= cierre)"
        new = run(["git", "-C", d, "log", "--format=%h %cI %s",
                   f"--after={args.desde}", "-5"]).stdout.strip().replace("\n", " | ") or "(sin commits nuevos)"
        line = f"{repo}\t{last}\t[{new}]"
        print(line)
        out.append(line)
        shutil.rmtree(d, ignore_errors=True)

    meta = os.path.join(KIT, "revisiones", "2026-2", "_meta")
    os.makedirs(meta, exist_ok=True)
    with io.open(os.path.join(meta, "actividad.txt"), "w", encoding="utf-8") as f:
        f.write(f"# barrido --cierre {args.cierre} --desde {args.desde}\n")
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
