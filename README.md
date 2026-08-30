# classic-test-project

`wangaiyang71-ux` 下的经典测试项目：用面向对象实现一个不可透支的银行账户和转账服务，并配上单元测试。适合用来演示 Cursor Automations 的「PR 打开后自动审查」。

## 运行测试

在项目根目录执行：

```powershell
python -m unittest discover -s tests -v
```

## 结构

- `classic_bank/account.py`：账户实体，负责存款、取款和流水
- `classic_bank/transfer_service.py`：转账服务，失败时回滚
- `classic_bank/transaction.py`：流水记录
- `tests/`：账户、转账、限额的单元测试
- `.github/workflows/tests.yml`：PR 和 `main` 上跑单元测试
- `.cursor/rules/classic-bank.mdc`：项目编码约定

默认分支是 `main`。开发请从 `main` 拉功能分支，不要直接改 `main`。
