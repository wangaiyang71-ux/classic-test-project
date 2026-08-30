## 改动说明

- 

## 测试

- [ ] `python -m unittest discover -s tests -v` 已通过

## 审查关注点

- 金额是否使用 `Decimal`
- 限额是否来自 `classic_bank/constants.py`
- 转账失败是否回滚
