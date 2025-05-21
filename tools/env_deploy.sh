#!/bin/bash
# tools/env_deploy.sh

# 部署测试环境
echo "正在部署测试环境..."
docker-compose -f docker/test-env.yml up -d

# 等待服务启动
sleep 30

# 初始化测试数据
echo "初始化基础数据..."
python3 -m tools.data_generator --count 1000

# 执行数据库迁移
echo "执行数据库迁移..."
alembic upgrade head