# classic-test-project

`wangaiyang71-ux` 下的经典测试项目：用面向对象实现一个不可透支的银行账户和转账服务，并配上单元测试。适合用来演示 Cursor Automations 的「PR 打开后自动审查」。

## 运行测试

在项目根目录执行：

```powershell
python -m unittest discover -s tests -v
```

## 结构

- `classic_bank/account.py`：账户实体，负责存款和取款
- `classic_bank/transfer_service.py`：转账服务，失败时回滚
- `tests/`：账户与转账的单元测试

默认分支是 `main`。
