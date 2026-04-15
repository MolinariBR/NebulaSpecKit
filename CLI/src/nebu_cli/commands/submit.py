"""Implementation of `nebu submit`."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

def run(args) -> int:
    """Execute the submit command enforcing Nébula task rules."""
    print("🚀 Iniciando submission de task (Quality Gate + Tracker)")

    # 1. Tenta rodar o Quality Gate (se existir no projeto alvo)
    # Assumimos que a raiz possui as automações do Nebula em tools/
    script_path = Path("tools/analyze-consistency.sh")
    if script_path.exists():
        print(f"✅ Encontrado analisador de consistência em {script_path}. Validando...")
        gate_res = subprocess.run([str(script_path)])
        if gate_res.returncode != 0:
            print("❌ Falha no Quality Gate. Corrija o documento antes de submeter a task.")
            return 1
    else:
        print("⚠️ Script de Quality Gate não encontrado localmente (tools/analyze-consistency.sh). Pulando...")

    # 2. Stage de arquivos (adiciona . e Docs/)
    subprocess.run(["git", "add", "."])

    # 3. Commit
    commit_cmd = ["git", "commit", "-m", args.message]
    commit_res = subprocess.run(commit_cmd, capture_output=True, text=True)

    if commit_res.returncode != 0:
        print("ℹ️ Nada para comitar ou erro no hook do git.")
        print(commit_res.stdout)
        return commit_res.returncode

    # 4. Obter o Hash
    hash_res = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
    commit_hash = hash_res.stdout.strip()

    # 5. Registrar no Tasks.md
    tasks_file = Path("Docs/tasks.md")
    if tasks_file.exists():
        task_id_info = f" (Ref: {args.task_id})" if args.task_id else ""
        log_entry = f"\n- ✅ **{commit_hash}** - {args.message}{task_id_info}"
        
        with open(tasks_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        print(f"✅ Hash {commit_hash} registrado automaticamente em Docs/tasks.md!")
    else:
        print(f"⚠️ Docs/tasks.md não encontrado. Commit {commit_hash} gerado, mas o rastreamento foi ignorado.")

    print("🎉 Task concluída com sucesso e de acordo com as regras de Governança do Nébula!")
    return 0
