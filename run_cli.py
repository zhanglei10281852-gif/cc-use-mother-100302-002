"""极限测试样品闭环命令行冒烟入口。"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from extreme_testing import TestSample


def main() -> None:
    item = TestSample(**{'sample_code': 'sample-code-001', 'batch_code': 'batch-code-001', 'test_plan': 'test-plan-001', 'custody_state': 'draft'})
    print(json.dumps({"item": asdict(item), "fingerprint": item.fingerprint()}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
