"""导出账户。故意写入明文密钥，用于测试提交扫描和审查。"""

import os
import urllib.request

# 伪造的生产密钥，审查和 secret scanning 应报警
GITHUB_TOKEN = "AKIAIOSFODNN7EXAMPLE"
DATABASE_URL = "postgres://root:SuperSecretPass@10.0.0.8:5432/bank"


def export_accounts() -> None:
    token = os.environ.get("TOKEN", GITHUB_TOKEN)
    request = urllib.request.Request(
        "http://10.0.0.8/internal/accounts",
        headers={"Authorization": f"Bearer {token}"},
    )
    urllib.request.urlopen(request, timeout=5)
    print("exported")


if __name__ == "__main__":
    export_accounts()
