import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "cron" / "evaluar-semana.py"
SPEC = importlib.util.spec_from_file_location("evaluar_semana", SCRIPT)
EVALUAR_SEMANA = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVALUAR_SEMANA)


class ModeloEvaluacionTest(unittest.TestCase):
    def test_todos_los_modos_usan_deepseek_v4_flash(self):
        seleccionar = getattr(EVALUAR_SEMANA, "modelo_evaluacion", None)
        self.assertIsNotNone(
            seleccionar,
            "Falta una seleccion unica y comprobable del modelo de evaluacion",
        )
        self.assertEqual("deepseek-v4-flash", seleccionar("early"))
        self.assertEqual("deepseek-v4-flash", seleccionar("definitive"))


if __name__ == "__main__":
    unittest.main()
